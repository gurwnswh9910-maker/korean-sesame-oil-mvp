#!/usr/bin/env python3
"""Run the post-24h note dashboard gate with stale-snapshot protection."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from record_note_dashboard_snapshot import append_rows, parse_dashboard_text


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DASHBOARD_TEXT = ROOT / ".tmp" / "note_dashboard_current.txt"
DEFAULT_STATUS_JSON = ROOT / "experiments" / "post_24h_gate_status.json"
DEFAULT_SUMMARY_JSON = ROOT / "experiments" / "validation_signal_summary.json"
DEFAULT_MIN_AGGREGATION_AT = "2026-06-28T21:45:00+09:00"
SEOUL = ZoneInfo("Asia/Seoul")


def parse_dashboard_datetime(value: str) -> datetime | None:
    value = (value or "").strip()
    if not value:
        return None
    for fmt in ("%Y年%m月%d日 %H:%M", "%Y年%-m月%-d日 %H:%M"):
        try:
            return datetime.strptime(value, fmt).replace(tzinfo=SEOUL)
        except ValueError:
            continue
    return None


def parse_iso_datetime(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=SEOUL)
    return parsed


def run_command(command: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=check)


def export_dashboard_text(output: Path, *, wait_ms: int, refresh: bool) -> str:
    command = [
        "node",
        "scripts/export_note_dashboard_text.mjs",
        "--output",
        str(output),
        "--wait-ms",
        str(wait_ms),
    ]
    if refresh:
        command.append("--refresh")
    result = run_command(command)
    return result.stdout.strip()


def summarize_counts(rows: list[dict[str, str]]) -> dict[str, int]:
    return {
        "post_count": len(rows),
        "views": sum(int(row["views"]) for row in rows),
        "comments": sum(int(row["comments"]) for row in rows),
        "likes": sum(int(row["likes"]) for row in rows),
    }


def load_response_metrics(path: Path = DEFAULT_SUMMARY_JSON) -> dict[str, int]:
    defaults = {
        "total_respondents": 0,
        "online_public_responses": 0,
        "strong_problem_fit_responses": 0,
        "public_social_responses": 0,
        "form_or_github_responses": 0,
        "offline_interviews": 0,
        "sample_or_purchase_requests": 0,
    }
    if not path.exists():
        return defaults
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError:
        return defaults
    metrics = payload.get("metrics", {})
    for key in defaults:
        try:
            defaults[key] = int(metrics.get(key, 0))
        except (TypeError, ValueError):
            defaults[key] = 0
    return defaults


def gate_for_counts(counts: dict[str, int], response_metrics: dict[str, int] | None = None) -> str:
    response_metrics = response_metrics or {}
    if int(response_metrics.get("strong_problem_fit_responses", 0)) >= 5:
        return "problem_fit_candidate_import_label_gate"
    if counts["comments"] > 0 or int(response_metrics.get("total_respondents", 0)) > 0:
        return "review_responses_for_strong_fit"
    if counts["views"] < 30:
        return "distribution_failure_hold_6th_note"
    return "problem_language_or_cta_failure_consider_aromaloss_note"


def select_gate(
    counts: dict[str, int],
    response_metrics: dict[str, int],
    *,
    stale: bool,
    can_record: bool,
) -> str:
    has_strong_fit = int(response_metrics.get("strong_problem_fit_responses", 0)) >= 5
    has_any_response = int(response_metrics.get("total_respondents", 0)) > 0
    if has_strong_fit or has_any_response:
        return gate_for_counts(counts, response_metrics)
    if stale and not can_record:
        return "stale_dashboard_not_recorded"
    return gate_for_counts(counts, response_metrics)


def decision_for_gate(gate: str) -> dict[str, object]:
    decisions: dict[str, dict[str, object]] = {
        "stale_dashboard_not_recorded": {
            "interpretation": "dashboard aggregation is too old to use for the 24h gate",
            "next_action": "rerun after the note dashboard aggregation time is at or after the gate minimum",
            "allowed_actions": ["do_not_record_snapshot", "do_not_publish_6th_note"],
            "reference_files": ["mvp/post_24h_action_packet_20260628.md"],
        },
        "distribution_failure_hold_6th_note": {
            "interpretation": "note did not reach enough people, so the current evidence is distribution failure rather than message failure",
            "next_action": "hold the 6th note and choose exactly one post-gate external/offline lane",
            "allowed_actions": [
                "ask_user_for_x_or_threads_one_question_permission",
                "run_offline_shinokubo_or_korean_grocery_interviews_if_possible",
                "check_konest_rules_before_any_post",
            ],
            "reference_files": [
                "mvp/post_gate_external_channel_packet_20260628.md",
                "mvp/x_threads_posting_packet.md",
                "mvp/field_aroma_interview_script.md",
            ],
        },
        "problem_language_or_cta_failure_consider_aromaloss_note": {
            "interpretation": "note reached at least a minimal audience, but no one responded",
            "next_action": "consider publishing the 6th aroma-loss note only after pre-publish routing checks",
            "allowed_actions": [
                "verify_aroma_loss_quick_answer_and_field_aroma_production_urls",
                "publish_mvp_note_aromaloss_posting_packet_if_checks_pass",
                "add_live_6th_note_url_to_source_routing_after_publish",
            ],
            "reference_files": [
                "mvp/note_aromaloss_posting_packet.md",
                "mvp/post_24h_action_packet_20260628.md",
            ],
        },
        "review_responses_for_strong_fit": {
            "interpretation": "there is at least one comment, form, public reply, or interview signal to inspect before expanding channels",
            "next_action": "review original response sources and score them against strong problem-fit criteria",
            "allowed_actions": [
                "open_original_response_sources",
                "record_qualified_public_responses",
                "ask_follow_up_questions_for_missing_strong_fit_fields",
            ],
            "reference_files": [
                "scripts/record_public_social_response.py",
                "experiments/public_social_responses.csv",
                "검증/응답_데이터_상태.md",
            ],
        },
        "problem_fit_candidate_import_label_gate": {
            "interpretation": "strong problem-fit response threshold has been met",
            "next_action": "stop collecting lightweight traffic and move to import, labeling, unit economics, and sample-interview gates before any sale or reservation",
            "allowed_actions": [
                "audit_original_strong_responses",
                "run_import_label_unit_economics_gate",
                "plan_sample_interviews_without_payment_or_private_contact_collection",
            ],
            "reference_files": [
                "research/02_import_label_unit_economics_gate.md",
                "experiments/validation_signal_summary.md",
                "검증/응답_데이터_상태.md",
            ],
        },
    }
    return decisions.get(
        gate,
        {
            "interpretation": "unknown gate state",
            "next_action": "inspect experiments/post_24h_gate_status.json and the dashboard snapshot manually",
            "allowed_actions": ["manual_review"],
            "reference_files": ["mvp/post_24h_action_packet_20260628.md"],
        },
    )


def stamp_rows(rows: list[dict[str, str]], *, captured_at: str, aggregation_at: str) -> list[dict[str, str]]:
    stamped: list[dict[str, str]] = []
    for row in rows:
        stamped_row = dict(row)
        stamped_row["captured_at"] = captured_at
        stamped_row["aggregation_at"] = aggregation_at
        stamped.append(stamped_row)
    return stamped


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dashboard-text", type=Path, default=DEFAULT_DASHBOARD_TEXT)
    parser.add_argument("--export-dashboard", action="store_true", help="Export dashboard text from the logged-in CDP browser first.")
    parser.add_argument("--refresh-dashboard", action="store_true", help="Reload the dashboard before CDP export.")
    parser.add_argument("--wait-ms", type=int, default=1500, help="Wait after opening/reloading before export.")
    parser.add_argument("--record", action="store_true", help="Append rows to note_dashboard_snapshots.csv when aggregation is fresh enough.")
    parser.add_argument("--min-aggregation-at", default=DEFAULT_MIN_AGGREGATION_AT)
    parser.add_argument("--allow-stale", action="store_true", help="Allow recording even if aggregation_at is older than the minimum.")
    parser.add_argument("--skip-downstream", action="store_true", help="Skip follow-up/waitlist/validation summary refresh.")
    parser.add_argument("--status-json", type=Path, default=DEFAULT_STATUS_JSON)
    parser.add_argument("--summary-json", type=Path, default=DEFAULT_SUMMARY_JSON)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    captured_at = datetime.now(SEOUL).isoformat(timespec="seconds")
    export_output = ""
    if args.export_dashboard:
        export_output = export_dashboard_text(args.dashboard_text, wait_ms=args.wait_ms, refresh=args.refresh_dashboard)

    text = args.dashboard_text.read_text(encoding="utf-8-sig")
    aggregation_at, parsed_rows = parse_dashboard_text(text, fill_missing_zero=True)
    counts = summarize_counts(parsed_rows)
    aggregation_dt = parse_dashboard_datetime(aggregation_at)
    min_dt = parse_iso_datetime(args.min_aggregation_at)
    stale = aggregation_dt is None or aggregation_dt < min_dt
    can_record = args.record and (args.allow_stale or not stale)
    stamped_rows = stamp_rows(parsed_rows, captured_at=captured_at, aggregation_at=aggregation_at)

    if can_record:
        append_rows(stamped_rows)

    downstream: dict[str, str] = {}
    if can_record and not args.skip_downstream:
        for name, command in {
            "followups": [sys.executable, "scripts/check_note_comment_followups.py", "--write"],
            "waitlist": [sys.executable, "scripts/summarize_waitlist.py"],
            "summary": [sys.executable, "scripts/summarize_validation_signals.py"],
        }.items():
            result = run_command(command)
            downstream[name] = result.stdout.strip()

    response_metrics = load_response_metrics(args.summary_json)
    gate = select_gate(counts, response_metrics, stale=stale, can_record=can_record)
    decision = decision_for_gate(gate)
    status = {
        "captured_at": captured_at,
        "dashboard_text": str(args.dashboard_text),
        "exported": bool(args.export_dashboard),
        "export_output": export_output,
        "aggregation_at": aggregation_at,
        "min_aggregation_at": args.min_aggregation_at,
        "stale": stale,
        "record_requested": bool(args.record),
        "recorded": bool(can_record),
        "gate": gate,
        "decision": decision,
        "counts": counts,
        "response_metrics": response_metrics,
        "downstream": downstream,
    }
    args.status_json.parent.mkdir(parents=True, exist_ok=True)
    args.status_json.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        f"post_24h_gate captured_at={captured_at} aggregation_at={aggregation_at or 'n/a'} "
        f"stale={stale} recorded={can_record} gate={status['gate']} "
        f"views={counts['views']} comments={counts['comments']} likes={counts['likes']} "
        f"respondents={response_metrics['total_respondents']} strong={response_metrics['strong_problem_fit_responses']} "
        f"next_action={decision['next_action']}"
    )
    if args.record and stale and not args.allow_stale:
        print("Refusing to record stale dashboard aggregation; rerun later or pass --allow-stale intentionally.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

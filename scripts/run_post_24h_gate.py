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


def gate_for_counts(counts: dict[str, int]) -> str:
    if counts["comments"] > 0:
        return "review_comments_for_strong_fit"
    if counts["views"] < 30:
        return "distribution_failure_hold_6th_note"
    return "problem_language_or_cta_failure_consider_aromaloss_note"


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
        "gate": gate_for_counts(counts) if can_record or not stale else "stale_dashboard_not_recorded",
        "counts": counts,
        "downstream": downstream,
    }
    args.status_json.parent.mkdir(parents=True, exist_ok=True)
    args.status_json.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        f"post_24h_gate captured_at={captured_at} aggregation_at={aggregation_at or 'n/a'} "
        f"stale={stale} recorded={can_record} gate={status['gate']} "
        f"views={counts['views']} comments={counts['comments']} likes={counts['likes']}"
    )
    if args.record and stale and not args.allow_stale:
        print("Refusing to record stale dashboard aggregation; rerun later or pass --allow-stale intentionally.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

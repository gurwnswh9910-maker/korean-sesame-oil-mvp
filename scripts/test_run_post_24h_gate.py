#!/usr/bin/env python3
"""Lightweight assertions for post-24h gate helpers."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from run_post_24h_gate import (
    decision_for_gate,
    gate_for_counts,
    load_response_metrics,
    parse_dashboard_datetime,
    parse_iso_datetime,
    select_gate,
    summarize_counts,
)


def test_parse_dashboard_datetime() -> None:
    parsed = parse_dashboard_datetime("2026年6月28日 21:45")
    assert parsed is not None
    assert parsed.isoformat() == "2026-06-28T21:45:00+09:00"
    assert parse_dashboard_datetime("") is None


def test_parse_iso_datetime() -> None:
    assert parse_iso_datetime("2026-06-28T21:45:00+09:00").isoformat() == "2026-06-28T21:45:00+09:00"
    assert parse_iso_datetime("2026-06-28T21:45:00").isoformat() == "2026-06-28T21:45:00+09:00"


def test_gate_for_counts() -> None:
    assert gate_for_counts({"views": 5, "comments": 0, "likes": 0, "post_count": 5}) == "distribution_failure_hold_6th_note"
    assert gate_for_counts({"views": 30, "comments": 0, "likes": 0, "post_count": 5}) == "problem_language_or_cta_failure_consider_aromaloss_note"
    assert gate_for_counts({"views": 5, "comments": 1, "likes": 0, "post_count": 5}) == "review_responses_for_strong_fit"
    assert (
        gate_for_counts(
            {"views": 5, "comments": 0, "likes": 0, "post_count": 5},
            {"total_respondents": 1, "strong_problem_fit_responses": 0},
        )
        == "review_responses_for_strong_fit"
    )
    assert (
        gate_for_counts(
            {"views": 5, "comments": 0, "likes": 0, "post_count": 5},
            {"total_respondents": 5, "strong_problem_fit_responses": 5},
        )
        == "problem_fit_candidate_import_label_gate"
    )


def test_decision_for_gate() -> None:
    stale = decision_for_gate("stale_dashboard_not_recorded")
    assert stale["next_action"] == "rerun after the note dashboard aggregation time is at or after the gate minimum"
    assert "do_not_publish_6th_note" in stale["allowed_actions"]

    distribution = decision_for_gate("distribution_failure_hold_6th_note")
    assert distribution["next_action"] == "hold the 6th note and choose exactly one post-gate external/offline lane"
    assert "mvp/post_gate_external_channel_packet_20260628.md" in distribution["reference_files"]

    message = decision_for_gate("problem_language_or_cta_failure_consider_aromaloss_note")
    assert "publish_mvp_note_aromaloss_posting_packet_if_checks_pass" in message["allowed_actions"]

    comments = decision_for_gate("review_responses_for_strong_fit")
    assert "검증/응답_데이터_상태.md" in comments["reference_files"]

    strong = decision_for_gate("problem_fit_candidate_import_label_gate")
    assert "run_import_label_unit_economics_gate" in strong["allowed_actions"]


def test_select_gate() -> None:
    counts = {"views": 5, "comments": 0, "likes": 0, "post_count": 5}
    assert select_gate(counts, {}, stale=True, can_record=False) == "stale_dashboard_not_recorded"
    assert (
        select_gate(
            counts,
            {"total_respondents": 1, "strong_problem_fit_responses": 0},
            stale=True,
            can_record=False,
        )
        == "review_responses_for_strong_fit"
    )
    assert (
        select_gate(
            counts,
            {"total_respondents": 5, "strong_problem_fit_responses": 5},
            stale=True,
            can_record=False,
        )
        == "problem_fit_candidate_import_label_gate"
    )


def test_load_response_metrics() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "summary.json"
        path.write_text(
            json.dumps(
                {
                    "metrics": {
                        "total_respondents": 2,
                        "online_public_responses": 1,
                        "strong_problem_fit_responses": 0,
                        "public_social_responses": 1,
                        "form_or_github_responses": 0,
                        "offline_interviews": 1,
                        "sample_or_purchase_requests": 1,
                    }
                }
            ),
            encoding="utf-8",
        )
        metrics = load_response_metrics(path)
        assert metrics["total_respondents"] == 2
        assert metrics["public_social_responses"] == 1
        assert metrics["offline_interviews"] == 1
    assert load_response_metrics(Path("does-not-exist.json"))["total_respondents"] == 0


def test_summarize_counts() -> None:
    rows = [
        {"views": "1", "comments": "0", "likes": "2"},
        {"views": "3", "comments": "1", "likes": "0"},
    ]
    assert summarize_counts(rows) == {"post_count": 2, "views": 4, "comments": 1, "likes": 2}


def main() -> int:
    test_parse_dashboard_datetime()
    test_parse_iso_datetime()
    test_gate_for_counts()
    test_decision_for_gate()
    test_select_gate()
    test_load_response_metrics()
    test_summarize_counts()
    print("run_post_24h_gate tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

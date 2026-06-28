#!/usr/bin/env python3
"""Lightweight assertions for post-24h gate helpers."""

from __future__ import annotations

from run_post_24h_gate import gate_for_counts, parse_dashboard_datetime, parse_iso_datetime, summarize_counts


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
    assert gate_for_counts({"views": 5, "comments": 1, "likes": 0, "post_count": 5}) == "review_comments_for_strong_fit"


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
    test_summarize_counts()
    print("run_post_24h_gate tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

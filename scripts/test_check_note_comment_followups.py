#!/usr/bin/env python3
"""Lightweight assertions for note comment follow-up checks."""

from __future__ import annotations

from check_note_comment_followups import check_followups, parse_posted_comment_count, posted_rows, status_for


def test_parse_posted_count() -> None:
    assert parse_posted_comment_count("Public API: comments=1 likes=14") == 1
    assert parse_posted_comment_count("before comments=1; after comments=2") == 2
    assert parse_posted_comment_count("no count") is None


def test_posted_rows_filter() -> None:
    rows = [
        {"source": "note_comment_a", "action_status": "posted_pending_reply", "url": "https://note.com/u/n/n77fa3f5a7fe9"},
        {"source": "note_comment_b", "action_status": "ready_not_posted", "url": "https://note.com/u/n/n77fa3f5a7fe9"},
        {"source": "other", "action_status": "posted_pending_reply", "url": "https://note.com/u/n/n77fa3f5a7fe9"},
    ]
    assert len(posted_rows(rows)) == 1


def test_status_for() -> None:
    assert status_for(1, 1, True)[0] == "no_new_comment"
    assert status_for(1, 2, True)[0] == "new_comment_signal"
    assert status_for(2, 1, True)[0] == "count_dropped"
    assert status_for(None, 1, True)[0] == "missing_posted_baseline"
    assert status_for(1, None, True)[0] == "missing_current_count"
    assert status_for(1, 1, False)[0] == "api_error"


def test_check_followups_with_fake_fetcher() -> None:
    rows = [
        {
            "source": "note_comment_a",
            "url": "https://note.com/user/n/n77fa3f5a7fe9",
            "action_status": "posted_pending_reply",
            "evidence": "Posted. Public API: comments=1 likes=4.",
        }
    ]

    def fake_fetcher(source: str, key: str, url: str) -> dict[str, object]:
        assert source == "note_comment_a"
        assert key == "n77fa3f5a7fe9"
        assert url == "https://note.com/user/n/n77fa3f5a7fe9"
        return {"ok": True, "name": "Title", "comment_count": 2}

    checked = check_followups(rows, checked_at="2026-06-28T17:00:00+09:00", fetcher=fake_fetcher)
    assert checked[0]["status"] == "new_comment_signal"
    assert checked[0]["delta"] == "1"
    assert checked[0]["posted_comment_count"] == "1"
    assert checked[0]["current_comment_count"] == "2"


def main() -> int:
    test_parse_posted_count()
    test_posted_rows_filter()
    test_status_for()
    test_check_followups_with_fake_fetcher()
    print("check_note_comment_followups tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

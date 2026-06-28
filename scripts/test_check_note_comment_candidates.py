#!/usr/bin/env python3
"""Lightweight assertions for note comment candidate readiness checks."""

from __future__ import annotations

from check_note_comment_candidates import check_candidates, comment_candidate_rows, readiness


def test_candidate_filter() -> None:
    rows = [
        {"channel": "note external comment candidate", "source": "note_comment_a", "post_url": "https://note.com/u/n/n77fa3f5a7fe9"},
        {"channel": "note kfood", "source": "note_kfood", "post_url": "https://note.com/u/n/n77fa3f5a7fe9"},
        {"channel": "note external comment candidate", "source": "other", "post_url": "https://note.com/u/n/n77fa3f5a7fe9"},
    ]
    assert len(comment_candidate_rows(rows)) == 1


def test_readiness_states() -> None:
    assert readiness({"posted": "yes"}, {"ok": True, "status": "published", "can_comment": True}) == "posted"
    assert readiness({"posted": "no"}, {"ok": False}) == "api_error"
    assert readiness({"posted": "no"}, {"ok": True, "status": "draft", "can_comment": True}) == "not_published"
    assert readiness({"posted": "no"}, {"ok": True, "status": "published", "can_comment": False}) == "not_commentable"
    assert readiness({"posted": "no"}, {"ok": True, "status": "published", "can_comment": True}) == "ready_not_posted"


def test_check_candidates_with_fake_fetcher() -> None:
    rows = [
        {
            "channel": "note external comment candidate",
            "source": "note_comment_a",
            "post_url": "https://note.com/user/n/n77fa3f5a7fe9",
            "posted": "no",
            "notes": "candidate note",
        }
    ]

    def fake_fetcher(source: str, key: str, url: str) -> dict[str, object]:
        assert source == "note_comment_a"
        assert key == "n77fa3f5a7fe9"
        assert url == "https://note.com/user/n/n77fa3f5a7fe9"
        return {
            "ok": True,
            "name": "Title",
            "status": "published",
            "can_comment": True,
            "comment_count": 2,
            "like_count": 5,
            "published_at": "2026-01-01T00:00:00+09:00",
        }

    checked = check_candidates(rows, checked_at="2026-06-28T15:15:00+09:00", fetcher=fake_fetcher)
    assert checked == [
        {
            "checked_at": "2026-06-28T15:15:00+09:00",
            "source": "note_comment_a",
            "url": "https://note.com/user/n/n77fa3f5a7fe9",
            "key": "n77fa3f5a7fe9",
            "title": "Title",
            "published_at": "2026-01-01T00:00:00+09:00",
            "status": "published",
            "can_comment": "True",
            "comment_count": "2",
            "like_count": "5",
            "posted": "no",
            "readiness": "ready_not_posted",
            "note": "candidate note",
        }
    ]


def main() -> int:
    test_candidate_filter()
    test_readiness_states()
    test_check_candidates_with_fake_fetcher()
    print("check_note_comment_candidates tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

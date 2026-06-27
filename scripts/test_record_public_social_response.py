#!/usr/bin/env python3
"""Lightweight assertions for public social response recording."""

from __future__ import annotations

import tempfile
from pathlib import Path

from record_public_social_response import append_response, read_rows


def sample_row(url: str = "https://x.com/example/status/1") -> dict[str, str]:
    return {
        "captured_at": "2026-06-27T21:35:00+09:00",
        "platform": "X",
        "source": "x_threads_travel",
        "response_url": url,
        "response_text": "100ml 1,480円なら試したい。新大久保でごま油を買ったことがある。",
        "recent_purchase": "新大久保で購入",
        "aroma_memory": "ある",
        "single_price_reaction": "試したい",
        "bundle_price_reaction": "",
        "sample_or_purchase_signal": "少量なら買いたい",
        "notes": "test row",
    }


def test_append_and_reject_duplicate() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "public_social_responses.csv"
        append_response(path, sample_row())
        rows = read_rows(path)
        assert len(rows) == 1
        assert rows[0]["source"] == "x_threads_travel"
        try:
            append_response(path, sample_row())
        except ValueError as exc:
            assert "duplicate response_url" in str(exc)
        else:
            raise AssertionError("duplicate URL was accepted")


def test_reject_bad_url() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "public_social_responses.csv"
        try:
            append_response(path, sample_row("not-a-url"))
        except ValueError as exc:
            assert "absolute http(s) URL" in str(exc)
        else:
            raise AssertionError("invalid URL was accepted")


def main() -> int:
    test_append_and_reject_duplicate()
    test_reject_bad_url()
    print("record_public_social_response tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

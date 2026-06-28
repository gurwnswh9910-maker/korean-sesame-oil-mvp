#!/usr/bin/env python3
"""Lightweight assertions for note public API helper parsing."""

from __future__ import annotations

from check_note_public_api import extract_note_key, parse_note_spec


def test_extract_key_from_plain_key() -> None:
    assert extract_note_key("n77fa3f5a7fe9") == "n77fa3f5a7fe9"


def test_extract_key_from_note_url() -> None:
    assert extract_note_key("https://note.com/example/n/n77fa3f5a7fe9?foo=bar") == "n77fa3f5a7fe9"


def test_parse_labeled_spec() -> None:
    source, key, display_url = parse_note_spec("candidate=https://note.com/example/n/n77fa3f5a7fe9")
    assert source == "candidate"
    assert key == "n77fa3f5a7fe9"
    assert display_url == "https://note.com/example/n/n77fa3f5a7fe9"


def main() -> int:
    test_extract_key_from_plain_key()
    test_extract_key_from_note_url()
    test_parse_labeled_spec()
    print("check_note_public_api parsing tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

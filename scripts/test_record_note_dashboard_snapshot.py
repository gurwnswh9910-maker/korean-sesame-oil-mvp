#!/usr/bin/env python3
"""Lightweight assertions for note dashboard snapshot parsing."""

from __future__ import annotations

from record_note_dashboard_snapshot import parse_dashboard_aggregation_at, parse_dashboard_text, parse_note_spec


def test_parse_note_spec() -> None:
    row = parse_note_spec("note_kfood=5,0,1,manual check")
    assert row["source"] == "note_kfood"
    assert row["views"] == "5"
    assert row["comments"] == "0"
    assert row["likes"] == "1"
    assert row["notes"] == "manual check"


def test_parse_dashboard_aggregation_at() -> None:
    text = "アクセス状況\n最新集計時刻 2026年6月28日 21:45\n記事"
    assert parse_dashboard_aggregation_at(text) == "2026年6月28日 21:45"


def test_parse_dashboard_text_partial() -> None:
    text = (
        "最新集計時刻 2026年6月28日 21:45\n"
        "韓国旅行で覚えた「しぼりたてごま油の香り」は、日本の家でも使いたいですか？\n"
        "\t5\t0\t0\n"
    )
    aggregation_at, rows = parse_dashboard_text(text)
    assert aggregation_at == "2026年6月28日 21:45"
    assert len(rows) == 1
    assert rows[0]["source"] == "note_kfood"
    assert rows[0]["views"] == "5"


def test_parse_dashboard_text_fill_missing_zero() -> None:
    text = (
        "最新集計時刻 2026年6月28日 21:45\n"
        "韓国旅行で買ったごま油、家で使い切れていますか？\n"
        "\t2\t1\t0\n"
    )
    _, rows = parse_dashboard_text(text, fill_missing_zero=True)
    by_source = {row["source"]: row for row in rows}
    assert len(rows) == 5
    assert by_source["note_content_travel"]["views"] == "2"
    assert by_source["note_content_travel"]["comments"] == "1"
    assert by_source["note_kfood"]["views"] == "0"
    assert by_source["note_kfood"]["notes"] == "not_present_in_dashboard_text_treated_as_zero"


def main() -> int:
    test_parse_note_spec()
    test_parse_dashboard_aggregation_at()
    test_parse_dashboard_text_partial()
    test_parse_dashboard_text_fill_missing_zero()
    print("record_note_dashboard_snapshot tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

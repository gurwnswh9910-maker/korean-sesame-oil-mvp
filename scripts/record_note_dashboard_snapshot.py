#!/usr/bin/env python3
"""Append note dashboard view/comment/like snapshots for the MVP validation gate."""

from __future__ import annotations

import argparse
import csv
import re
from datetime import datetime
from pathlib import Path


OUTPUT_CSV = Path("experiments") / "note_dashboard_snapshots.csv"
FIELDNAMES = ["captured_at", "aggregation_at", "source", "post_url", "views", "comments", "likes", "notes"]
NOTE_URLS = {
    "note_kfood": "https://note.com/dreamy_viola8978/n/n77fa3f5a7fe9",
    "note_content_travel": "https://note.com/dreamy_viola8978/n/n3f3af286cf6d",
    "note_content_shinokubo": "https://note.com/dreamy_viola8978/n/n700b325ba824",
    "note_content_homecook": "https://note.com/dreamy_viola8978/n/n08bad3dce2a9",
    "note_content_homecook_ricebowl": "https://note.com/dreamy_viola8978/n/nbb21605544ca",
}
NOTE_TITLES = {
    "note_kfood": "韓国旅行で覚えた「しぼりたてごま油の香り」は、日本の家でも使いたいですか？",
    "note_content_travel": "韓国旅行で買ったごま油、家で使い切れていますか？",
    "note_content_shinokubo": "新大久保で韓国ごま油、いつもどれを買っていますか？",
    "note_content_homecook": "ビビンバとナムル、最後のごま油の香りは足りていますか？",
    "note_content_homecook_ricebowl": "韓国のりご飯とTKG、ごま油を最後に少し足しますか？",
}


def parse_note_spec(spec: str) -> dict[str, str]:
    """Parse source=views,comments,likes[,notes]."""
    if "=" not in spec:
        raise ValueError(f"Invalid --note spec, expected source=views,comments,likes: {spec}")
    source, payload = spec.split("=", 1)
    source = source.strip()
    parts = [part.strip() for part in payload.split(",", 3)]
    if len(parts) < 3:
        raise ValueError(f"Invalid --note counts, expected views,comments,likes: {spec}")
    views, comments, likes = (parse_nonnegative_int(value, spec) for value in parts[:3])
    notes = parts[3] if len(parts) >= 4 else ""
    return {
        "source": source,
        "post_url": NOTE_URLS.get(source, ""),
        "views": str(views),
        "comments": str(comments),
        "likes": str(likes),
        "notes": notes,
    }


def parse_nonnegative_int(value: str, spec: str) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise ValueError(f"Invalid integer in --note spec {spec!r}: {value!r}") from exc
    if parsed < 0:
        raise ValueError(f"Counts must be nonnegative in --note spec: {spec}")
    return parsed


def parse_dashboard_aggregation_at(text: str) -> str:
    match = re.search(r"最新集計時刻\s*([^\n\r]+)", text)
    return match.group(1).strip() if match else ""


def parse_dashboard_text(text: str, *, fill_missing_zero: bool = False) -> tuple[str, list[dict[str, str]]]:
    aggregation_at = parse_dashboard_aggregation_at(text)
    rows: list[dict[str, str]] = []
    for source, title in NOTE_TITLES.items():
        pattern = re.compile(re.escape(title) + r"\s+(\d+)\s+(\d+)\s+(\d+)")
        match = pattern.search(text)
        if match:
            views, comments, likes = match.groups()
            rows.append(
                {
                    "source": source,
                    "post_url": NOTE_URLS[source],
                    "views": views,
                    "comments": comments,
                    "likes": likes,
                    "notes": "parsed_from_dashboard_text",
                }
            )
        elif fill_missing_zero:
            rows.append(
                {
                    "source": source,
                    "post_url": NOTE_URLS[source],
                    "views": "0",
                    "comments": "0",
                    "likes": "0",
                    "notes": "not_present_in_dashboard_text_treated_as_zero",
                }
            )
    return aggregation_at, rows


def append_rows(rows: list[dict[str, str]]) -> None:
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    write_header = not OUTPUT_CSV.exists() or OUTPUT_CSV.stat().st_size == 0
    with OUTPUT_CSV.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--captured-at", default=datetime.now().astimezone().isoformat(timespec="seconds"))
    parser.add_argument("--aggregation-at", default="", help="Latest aggregation timestamp shown in note dashboard.")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print totals without writing CSV rows.")
    parser.add_argument(
        "--from-dashboard-text",
        type=Path,
        help="Parse note dashboard body text copied or exported from the logged-in dashboard.",
    )
    parser.add_argument(
        "--fill-missing-zero",
        action="store_true",
        help="When parsing dashboard text, write known project notes not present in the text as 0,0,0.",
    )
    parser.add_argument(
        "--note",
        action="append",
        default=[],
        help="One note row as source=views,comments,likes[,free notes]. Repeat for each post.",
    )
    args = parser.parse_args()

    if not args.note and not args.from_dashboard_text:
        parser.error("Provide at least one --note or --from-dashboard-text.")

    rows = []
    aggregation_at = args.aggregation_at
    if args.from_dashboard_text:
        text = args.from_dashboard_text.read_text(encoding="utf-8-sig")
        parsed_aggregation_at, parsed_rows = parse_dashboard_text(text, fill_missing_zero=args.fill_missing_zero)
        if parsed_aggregation_at and not aggregation_at:
            aggregation_at = parsed_aggregation_at
        rows.extend(parsed_rows)
    for spec in args.note:
        rows.append(parse_note_spec(spec))
    if not rows:
        parser.error("No note rows could be parsed.")
    for row in rows:
        row["captured_at"] = args.captured_at
        row["aggregation_at"] = aggregation_at

    if not args.dry_run:
        append_rows(rows)
    total_views = sum(int(row["views"]) for row in rows)
    total_comments = sum(int(row["comments"]) for row in rows)
    total_likes = sum(int(row["likes"]) for row in rows)
    action = "Validated" if args.dry_run else "Recorded"
    print(
        f"{action} {len(rows)} note dashboard rows at {args.captured_at}: "
        f"aggregation_at={aggregation_at or 'n/a'}, "
        f"views={total_views}, comments={total_comments}, likes={total_likes}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

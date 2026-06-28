#!/usr/bin/env python3
"""Append note dashboard view/comment/like snapshots for the MVP validation gate."""

from __future__ import annotations

import argparse
import csv
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
        "--note",
        action="append",
        required=True,
        help="One note row as source=views,comments,likes[,free notes]. Repeat for each post.",
    )
    args = parser.parse_args()

    rows = []
    for spec in args.note:
        row = parse_note_spec(spec)
        row["captured_at"] = args.captured_at
        row["aggregation_at"] = args.aggregation_at
        rows.append(row)

    if not args.dry_run:
        append_rows(rows)
    total_views = sum(int(row["views"]) for row in rows)
    total_comments = sum(int(row["comments"]) for row in rows)
    total_likes = sum(int(row["likes"]) for row in rows)
    action = "Validated" if args.dry_run else "Recorded"
    print(
        f"{action} {len(rows)} note dashboard rows at {args.captured_at}: "
        f"views={total_views}, comments={total_comments}, likes={total_likes}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

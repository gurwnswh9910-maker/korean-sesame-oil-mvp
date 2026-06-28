#!/usr/bin/env python3
"""Check note comment candidate readiness from the channel posting log."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Callable, Iterable

from check_note_public_api import extract_note_key, fetch_note, now_local


CHANNEL_LOG = Path("experiments/channel_posting_log.csv")
STATUS_CSV = Path("experiments/note_comment_candidate_status.csv")

OUTPUT_FIELDS = [
    "checked_at",
    "source",
    "url",
    "key",
    "title",
    "published_at",
    "status",
    "can_comment",
    "comment_count",
    "like_count",
    "posted",
    "readiness",
    "note",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return [{key: (value or "").strip() for key, value in row.items()} for row in csv.DictReader(handle)]


def comment_candidate_rows(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    return [
        row
        for row in rows
        if row.get("channel") == "note external comment candidate"
        and row.get("source", "").startswith("note_comment_")
        and (row.get("post_url") or row.get("url_to_post"))
    ]


def candidate_url(row: dict[str, str]) -> str:
    return row.get("post_url") or row.get("url_to_post") or ""


def readiness(row: dict[str, str], note: dict[str, object]) -> str:
    if row.get("posted", "").lower() == "yes":
        return "posted"
    if not note.get("ok"):
        return "api_error"
    if note.get("status") != "published":
        return "not_published"
    if note.get("can_comment") is not True:
        return "not_commentable"
    return "ready_not_posted"


def check_candidates(
    rows: Iterable[dict[str, str]],
    *,
    checked_at: str,
    fetcher: Callable[[str, str, str], dict[str, object]] = fetch_note,
) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for row in comment_candidate_rows(rows):
        source = row["source"]
        url = candidate_url(row)
        try:
            key = extract_note_key(url)
            note = fetcher(source, key, url)
        except ValueError as exc:
            key = ""
            note = {"ok": False, "error": str(exc)}
        state = readiness(row, note)
        results.append(
            {
                "checked_at": checked_at,
                "source": source,
                "url": url,
                "key": key,
                "title": str(note.get("name") or ""),
                "published_at": str(note.get("published_at") or ""),
                "status": str(note.get("status") or ("ERROR" if not note.get("ok") else "")),
                "can_comment": str(note.get("can_comment") if note.get("ok") else ""),
                "comment_count": str(note.get("comment_count") if note.get("ok") else ""),
                "like_count": str(note.get("like_count") if note.get("ok") else ""),
                "posted": row.get("posted", ""),
                "readiness": state,
                "note": row.get("notes", "") if state == "ready_not_posted" else str(note.get("error") or row.get("notes", "")),
            }
        )
    return results


def write_status(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def print_table(rows: list[dict[str, str]]) -> None:
    print("source\treadiness\tcomments\tlikes\tcan_comment\ttitle")
    for row in rows:
        print(
            f"{row['source']}\t{row['readiness']}\t{row['comment_count']}\t"
            f"{row['like_count']}\t{row['can_comment']}\t{row['title']}"
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=CHANNEL_LOG, help="channel_posting_log.csv path.")
    parser.add_argument("--output", type=Path, default=STATUS_CSV, help="Output CSV path used with --write.")
    parser.add_argument("--write", action="store_true", help="Write the candidate status CSV.")
    parser.add_argument("--json", action="store_true", help="Emit JSON rows instead of a table.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    rows = check_candidates(read_csv(args.input), checked_at=now_local())
    if args.write:
        write_status(args.output, rows)
    if args.json:
        for row in rows:
            print(json.dumps(row, ensure_ascii=False, sort_keys=True))
    else:
        print_table(rows)
        ready = sum(1 for row in rows if row["readiness"] == "ready_not_posted")
        print(f"\nchecked={len(rows)} ready_not_posted={ready} wrote={args.output if args.write else 'no'}")
    return 0 if all(row["readiness"] in {"ready_not_posted", "posted"} for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())

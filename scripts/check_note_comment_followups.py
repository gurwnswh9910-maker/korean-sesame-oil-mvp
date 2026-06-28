#!/usr/bin/env python3
"""Check whether posted note comments have new reply/comment signals."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Callable, Iterable

from check_note_public_api import extract_note_key, fetch_note, now_local


QUEUE_CSV = Path("experiments/note_comment_execution_queue.csv")
OUTPUT_CSV = Path("experiments/note_comment_followup_status.csv")

OUTPUT_FIELDS = [
    "checked_at",
    "source",
    "url",
    "key",
    "posted_comment_count",
    "current_comment_count",
    "delta",
    "status",
    "title",
    "note",
]

COMMENT_COUNT_RE = re.compile(r"comments\s*[=:]\s*(\d+)", re.IGNORECASE)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return [{key: (value or "").strip() for key, value in row.items()} for row in csv.DictReader(handle)]


def posted_rows(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    return [
        row
        for row in rows
        if row.get("source", "").startswith("note_comment_")
        and row.get("action_status") == "posted_pending_reply"
        and row.get("url")
    ]


def parse_posted_comment_count(evidence: str) -> int | None:
    matches = COMMENT_COUNT_RE.findall(evidence or "")
    if not matches:
        return None
    return int(matches[-1])


def status_for(posted_count: int | None, current_count: int | None, ok: bool) -> tuple[str, str]:
    if not ok:
        return "api_error", ""
    if posted_count is None:
        return "missing_posted_baseline", ""
    if current_count is None:
        return "missing_current_count", ""
    delta = current_count - posted_count
    if delta > 0:
        return "new_comment_signal", f"current comment_count is {delta} above the post-check baseline; inspect original note page before recording as response"
    if delta == 0:
        return "no_new_comment", "no count increase after our posted comment"
    return "count_dropped", "current comment_count is below the post-check baseline; recheck note page manually"


def check_followups(
    rows: Iterable[dict[str, str]],
    *,
    checked_at: str,
    fetcher: Callable[[str, str, str], dict[str, object]] = fetch_note,
) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for row in posted_rows(rows):
        source = row["source"]
        url = row["url"]
        posted_count = parse_posted_comment_count(row.get("evidence", ""))
        key = extract_note_key(url)
        note = fetcher(source, key, url)
        current_raw = note.get("comment_count") if note.get("ok") else None
        current_count = int(current_raw) if isinstance(current_raw, int) else None
        state, detail = status_for(posted_count, current_count, bool(note.get("ok")))
        delta = "" if posted_count is None or current_count is None else str(current_count - posted_count)
        results.append(
            {
                "checked_at": checked_at,
                "source": source,
                "url": url,
                "key": key,
                "posted_comment_count": "" if posted_count is None else str(posted_count),
                "current_comment_count": "" if current_count is None else str(current_count),
                "delta": delta,
                "status": state,
                "title": str(note.get("name") or ""),
                "note": detail or str(note.get("error") or ""),
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
    print("source\tstatus\tposted\tcurrent\tdelta\ttitle")
    for row in rows:
        print(
            f"{row['source']}\t{row['status']}\t{row['posted_comment_count']}\t"
            f"{row['current_comment_count']}\t{row['delta']}\t{row['title']}"
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=QUEUE_CSV, help="note_comment_execution_queue.csv path.")
    parser.add_argument("--output", type=Path, default=OUTPUT_CSV, help="Output CSV path used with --write.")
    parser.add_argument("--write", action="store_true", help="Write the follow-up status CSV.")
    parser.add_argument("--json", action="store_true", help="Emit JSON rows instead of a table.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    rows = check_followups(read_csv(args.input), checked_at=now_local())
    if args.write:
        write_status(args.output, rows)
    if args.json:
        for row in rows:
            print(json.dumps(row, ensure_ascii=False, sort_keys=True))
    else:
        print_table(rows)
        signals = sum(1 for row in rows if row["status"] == "new_comment_signal")
        print(f"\nchecked={len(rows)} new_comment_signal={signals} wrote={args.output if args.write else 'no'}")
    return 0 if all(row["status"] in {"no_new_comment", "new_comment_signal"} for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())

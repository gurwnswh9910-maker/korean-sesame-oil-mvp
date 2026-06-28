"""Check public note status/comment/like counts for the MVP posts."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone


NOTE_KEYS = {
    "note_kfood": "n77fa3f5a7fe9",
    "note_content_travel": "n3f3af286cf6d",
    "note_content_shinokubo": "n700b325ba824",
    "note_content_homecook": "n08bad3dce2a9",
    "note_content_homecook_ricebowl": "nbb21605544ca",
}


def now_local() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def fetch_note(source: str, key: str) -> dict[str, object]:
    url = f"https://note.com/api/v3/notes/{key}"
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return {
            "source": source,
            "key": key,
            "url": f"https://note.com/dreamy_viola8978/n/{key}",
            "ok": False,
            "error": str(exc),
        }

    data = payload.get("data", {})
    return {
        "source": source,
        "key": key,
        "url": f"https://note.com/dreamy_viola8978/n/{key}",
        "ok": True,
        "status": data.get("status"),
        "name": data.get("name"),
        "like_count": data.get("like_count"),
        "comment_count": data.get("comment_count"),
        "price": data.get("price"),
        "can_comment": data.get("can_comment"),
        "published_at": data.get("publish_at") or data.get("published_at"),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit JSON lines instead of a table.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    rows = [fetch_note(source, key) for source, key in NOTE_KEYS.items()]
    if args.json:
        for row in rows:
            print(json.dumps({"checked_at": now_local(), **row}, ensure_ascii=False, sort_keys=True))
    else:
        print("source\tstatus\tcomments\tlikes\tcan_comment\tpublished_at")
        for row in rows:
            if not row.get("ok"):
                print(f"{row['source']}\tERROR\t\t\t\t{row.get('error', '')}")
                continue
            print(
                f"{row['source']}\t{row.get('status')}\t{row.get('comment_count')}\t"
                f"{row.get('like_count')}\t{row.get('can_comment')}\t{row.get('published_at')}"
            )
    return 0 if all(row.get("ok") for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

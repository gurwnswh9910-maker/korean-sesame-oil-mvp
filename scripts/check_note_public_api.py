"""Check public note status/comment/like counts for note posts."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


NOTE_KEYS = {
    "note_kfood": "n77fa3f5a7fe9",
    "note_content_travel": "n3f3af286cf6d",
    "note_content_shinokubo": "n700b325ba824",
    "note_content_homecook": "n08bad3dce2a9",
    "note_content_homecook_ricebowl": "nbb21605544ca",
    "note_content_aromaloss": "n363650c8697f",
}

NOTE_KEY_RE = re.compile(r"^n[0-9a-f]{12,}$", re.IGNORECASE)


def now_local() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def extract_note_key(value: str) -> str:
    value = value.strip()
    if NOTE_KEY_RE.fullmatch(value):
        return value
    parsed = urllib.parse.urlparse(value)
    path_parts = [part for part in parsed.path.split("/") if part]
    for index, part in enumerate(path_parts):
        if part == "n" and index + 1 < len(path_parts) and NOTE_KEY_RE.fullmatch(path_parts[index + 1]):
            return path_parts[index + 1]
    raise ValueError(f"Could not parse note key from {value!r}")


def parse_note_spec(spec: str) -> tuple[str, str, str]:
    if "=" in spec:
        source, value = spec.split("=", 1)
        source = source.strip()
        if not source:
            raise ValueError(f"Missing source name in {spec!r}")
    else:
        value = spec.strip()
        source = extract_note_key(value)
    key = extract_note_key(value)
    display_url = value if value.startswith(("http://", "https://")) else f"https://note.com/n/{key}"
    return source, key, display_url


def fetch_note(source: str, key: str, display_url: str | None = None) -> dict[str, object]:
    url = f"https://note.com/api/v3/notes/{key}"
    display_url = display_url or f"https://note.com/dreamy_viola8978/n/{key}"
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
            "url": display_url,
            "ok": False,
            "error": str(exc),
        }

    data = payload.get("data", {})
    return {
        "source": source,
        "key": key,
        "url": display_url,
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
    parser.add_argument(
        "--note",
        action="append",
        default=[],
        metavar="SOURCE=URL_OR_KEY",
        help="Check an arbitrary note URL/key. Repeat to check several notes. Defaults to MVP posts when omitted.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        note_specs = [parse_note_spec(spec) for spec in args.note] if args.note else [
            (source, key, f"https://note.com/dreamy_viola8978/n/{key}") for source, key in NOTE_KEYS.items()
        ]
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    rows = [fetch_note(source, key, display_url) for source, key, display_url in note_specs]
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

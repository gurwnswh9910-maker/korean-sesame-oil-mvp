#!/usr/bin/env python3
"""Append a real public social response URL to the validation CSV."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


DEFAULT_CSV = Path("experiments/public_social_responses.csv")
FIELDNAMES = [
    "captured_at",
    "platform",
    "source",
    "response_url",
    "response_text",
    "recent_purchase",
    "brand_or_store",
    "volume_or_price",
    "use_up_period",
    "aroma_memory",
    "substitute_comparison",
    "needed_proof",
    "single_price_reaction",
    "bundle_price_reaction",
    "sample_or_purchase_signal",
    "notes",
]


def now_local_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def validate_url(url: str) -> str:
    parsed = urlparse(url.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("response_url must be an absolute http(s) URL")
    return url.strip()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return [{key: (value or "").strip() for key, value in row.items()} for row in csv.DictReader(handle)]


def append_response(path: Path, row: dict[str, str], *, dry_run: bool = False) -> dict[str, str]:
    response_url = validate_url(row["response_url"])
    row["response_url"] = response_url
    row["captured_at"] = row.get("captured_at") or now_local_iso()

    rows = read_rows(path)
    existing_urls = {existing.get("response_url", "").strip() for existing in rows}
    if response_url in existing_urls:
        raise ValueError(f"duplicate response_url: {response_url}")

    clean_row = {field: (row.get(field) or "").strip() for field in FIELDNAMES}
    if not clean_row["response_text"]:
        raise ValueError("response_text is required")
    if not clean_row["source"]:
        raise ValueError("source is required")

    if dry_run:
        return clean_row

    path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow(clean_row)
    return clean_row


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="Target public social response CSV")
    parser.add_argument("--platform", required=True, help="Platform name, for example X or Threads")
    parser.add_argument("--source", required=True, help="Tracking source, for example x_threads_travel")
    parser.add_argument("--url", required=True, help="Public response URL")
    parser.add_argument("--text", required=True, help="Response text or faithful summary")
    parser.add_argument("--recent-purchase", default="", help="Recent purchase/search signal")
    parser.add_argument("--brand-store", default="", help="Brand, store, market, or candidate product")
    parser.add_argument("--volume-price", default="", help="Bottle volume and/or remembered price")
    parser.add_argument("--use-up-period", default="", help="How long one bottle takes to use up")
    parser.add_argument("--aroma-memory", default="", help="Aroma-memory signal")
    parser.add_argument("--substitute-comparison", default="", help="Whether current Kadoya/Kuki/Ottogi/Kim-san substitutes are enough")
    parser.add_argument("--needed-proof", default="", help="Needed proof such as manufacturing date, pressed date, tasting, dark bottle, or repurchase convenience")
    parser.add_argument("--single-price", default="", help="100ml 1,480 yen reaction")
    parser.add_argument("--bundle-price", default="", help="3-bottle 3,980 yen reaction")
    parser.add_argument("--sample-signal", default="", help="Sample, purchase, or stock-notice signal")
    parser.add_argument("--notes", default="", help="Internal notes, no private contact info")
    parser.add_argument("--captured-at", default="", help="ISO timestamp override")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print row without writing")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    row = {
        "captured_at": args.captured_at,
        "platform": args.platform,
        "source": args.source,
        "response_url": args.url,
        "response_text": args.text,
        "recent_purchase": args.recent_purchase,
        "brand_or_store": args.brand_store,
        "volume_or_price": args.volume_price,
        "use_up_period": args.use_up_period,
        "aroma_memory": args.aroma_memory,
        "substitute_comparison": args.substitute_comparison,
        "needed_proof": args.needed_proof,
        "single_price_reaction": args.single_price,
        "bundle_price_reaction": args.bundle_price,
        "sample_or_purchase_signal": args.sample_signal,
        "notes": args.notes,
    }
    written = append_response(args.csv, row, dry_run=args.dry_run)
    if args.dry_run:
        print("dry-run ok:", written)
    else:
        print(f"appended public social response: {written['response_url']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

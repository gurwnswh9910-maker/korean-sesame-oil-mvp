#!/usr/bin/env python3
"""Summarize GitHub Issue Form responses for the sesame oil MVP."""

from __future__ import annotations

import csv
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


REPO = os.environ.get("GITHUB_REPOSITORY", "gurwnswh9910-maker/korean-sesame-oil-mvp")
TOKEN = os.environ.get("GITHUB_TOKEN")
OUT_DIR = Path("experiments")
CSV_PATH = OUT_DIR / "waitlist_responses.csv"
SUMMARY_PATH = OUT_DIR / "waitlist_summary.md"

FIELDS = {
    "このページをどこで知りましたか": "source_self_reported",
    "韓国旅行や韓国料理店で、印象に残ったごま油の香りはありますか": "experience",
    "最近6か月以内に買ったごま油のブランド/購入場所": "recent_purchase",
    "主に使いたい料理": "dishes",
    "100ml 1,480円なら入荷案内を受け取りたいですか": "single_price",
    "3本 3,980円なら誰かと分けたいですか": "bundle_price",
    "価格・容量・香りについてのコメント": "comment",
}


def parse_source_from_title(title: str) -> str:
    match = re.search(r"\[src:([a-z0-9_-]{1,40})\]", title.lower())
    return match.group(1) if match else ""


def request_json(url: str) -> object:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "sesame-oil-mvp-validator",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API error {exc.code}: {detail}") from exc


def fetch_waitlist_issues() -> list[dict]:
    issues: list[dict] = []
    page = 1
    while True:
        url = (
            f"https://api.github.com/repos/{REPO}/issues"
            f"?state=all&labels=waitlist&per_page=100&page={page}"
        )
        batch = request_json(url)
        if not isinstance(batch, list):
            raise RuntimeError(f"Unexpected GitHub response: {batch!r}")
        if not batch:
            return issues
        issues.extend(item for item in batch if "pull_request" not in item)
        page += 1


def clean_value(value: str) -> str:
    value = value.strip()
    value = re.sub(r"<!--.*?-->", "", value, flags=re.DOTALL).strip()
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value


def parse_issue_body(body: str | None) -> dict[str, str]:
    parsed = {key: "" for key in FIELDS.values()}
    if not body:
        return parsed

    matches = list(re.finditer(r"^###\s+(.+?)\s*$", body, flags=re.MULTILINE))
    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        if heading in FIELDS:
            parsed[FIELDS[heading]] = clean_value(body[start:end])
    return parsed


def summarize(rows: list[dict[str, str]]) -> str:
    total = len(rows)
    yes_single = sum(1 for row in rows if row["single_price"] == "はい")
    yes_bundle = sum(1 for row in rows if row["bundle_price"] == "はい")
    has_experience = sum(1 for row in rows if row["experience"] == "ある")
    latest = max((row["created_at"] for row in rows), default="")
    generated_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    source_counts: dict[str, int] = {}
    for row in rows:
        source = row.get("source_title") or row.get("source_self_reported") or "untracked"
        source_counts[source] = source_counts.get(source, 0) + 1

    def pct(count: int) -> str:
        return "n/a" if total == 0 else f"{count / total:.0%}"

    lines = [
        "# Waitlist Response Summary",
        "",
        f"Generated at: {generated_at}",
        f"Repository: https://github.com/{REPO}",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Total waitlist issues | {total} |",
        f"| Korean sesame oil aroma experience = ある | {has_experience} ({pct(has_experience)}) |",
        f"| 100ml 1,480円 = はい | {yes_single} ({pct(yes_single)}) |",
        f"| 3本 3,980円 = はい | {yes_bundle} ({pct(yes_bundle)}) |",
        f"| Latest response | {latest or 'n/a'} |",
        "",
        "## Source Breakdown",
        "",
        "| Source | Responses |",
        "|---|---:|",
    ]
    if source_counts:
        for source, count in sorted(source_counts.items(), key=lambda item: (-item[1], item[0])):
            lines.append(f"| {source} | {count} |")
    else:
        lines.append("| n/a | 0 |")
    lines.extend([
        "",
        "## Interpretation",
        "",
    ])
    if total == 0:
        lines.append("No external validation responses have been collected yet.")
    else:
        lines.append(
            "Use this as behavioral evidence only when responses come from real outreach channels, "
            "not from internal test submissions."
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    issues = fetch_waitlist_issues()
    rows: list[dict[str, str]] = []
    for issue in issues:
        parsed = parse_issue_body(issue.get("body"))
        row = {
            "number": str(issue["number"]),
            "title": issue.get("title") or "",
            "source_title": parse_source_from_title(issue.get("title") or ""),
            "state": issue.get("state") or "",
            "created_at": issue.get("created_at") or "",
            "updated_at": issue.get("updated_at") or "",
            "url": issue.get("html_url") or "",
            **parsed,
        }
        rows.append(row)

    rows.sort(key=lambda row: int(row["number"]))
    fieldnames = [
        "number",
        "title",
        "source_title",
        "state",
        "created_at",
        "updated_at",
        "url",
        "source_self_reported",
        "experience",
        "recent_purchase",
        "dishes",
        "single_price",
        "bundle_price",
        "comment",
    ]
    with CSV_PATH.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    SUMMARY_PATH.write_text(summarize(rows), encoding="utf-8")
    print(f"Wrote {CSV_PATH} and {SUMMARY_PATH} from {len(rows)} waitlist issues.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

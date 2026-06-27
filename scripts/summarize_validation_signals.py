#!/usr/bin/env python3
"""Summarize all current validation signals for the sesame oil MVP."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


EXP_DIR = Path("experiments")
WAITLIST_CSV = EXP_DIR / "waitlist_responses.csv"
NOTION_EXPORT_CSV = EXP_DIR / "notion_submissions_export.csv"
FIELD_INTERVIEW_CSV = EXP_DIR / "field_interview_log.csv"
PUBLIC_SOCIAL_CSV = EXP_DIR / "public_social_responses.csv"
CHANNEL_LOG_CSV = EXP_DIR / "channel_posting_log.csv"
SUMMARY_MD = EXP_DIR / "validation_signal_summary.md"
SUMMARY_JSON = EXP_DIR / "validation_signal_summary.json"


YES_WORDS = ("はい", "ある", "試したい", "買いたい", "入荷", "知らせて", "yes", "y")
MAYBE_WORDS = ("迷う", "条件", "サンプル", "試食", "maybe")
NO_WORDS = ("いいえ", "ない", "興味なし", "高い", "no", "n")
NEGATIVE_PURCHASE_WORDS = ("買っていない", "覚えていない", "なし", "ない", "未購入")
SAMPLE_WORDS = ("サンプル", "試食", "少量", "買いたい", "購入", "入荷", "知らせて")


@dataclass
class Respondent:
    channel: str
    source: str
    recent_purchase: bool
    aroma_memory: bool
    single_price_mentioned: bool
    single_price_positive: bool
    bundle_price_mentioned: bool
    bundle_price_positive: bool
    sample_or_purchase_signal: bool


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows: list[dict[str, str]] = []
        for row in csv.DictReader(handle):
            clean_row: dict[str, str] = {}
            for key, value in row.items():
                if key is None:
                    if isinstance(value, list):
                        clean_row["__extra__"] = " ".join(part for part in value if part).strip()
                    continue
                if isinstance(value, list):
                    value = " ".join(part for part in value if part)
                clean_row[key] = (value or "").strip()
            rows.append(clean_row)
        return rows


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def contains_any(text: str, words: Iterable[str]) -> bool:
    lowered = text.lower()
    return any(word.lower() in lowered for word in words)


def positive(text: str) -> bool:
    text = normalize(text)
    if not text:
        return False
    if contains_any(text, NO_WORDS) and not contains_any(text, YES_WORDS + MAYBE_WORDS):
        return False
    return contains_any(text, YES_WORDS + MAYBE_WORDS)


def mentioned(text: str) -> bool:
    return bool(normalize(text))


def has_recent_purchase(text: str) -> bool:
    text = normalize(text)
    if not text:
        return False
    if contains_any(text, NEGATIVE_PURCHASE_WORDS):
        return False
    return True


def parse_source_from_title(title: str) -> str:
    match = re.search(r"\[src:([a-z0-9_-]{1,40})\]", title.lower())
    return match.group(1) if match else ""


def split_submission(text: str) -> dict[str, str]:
    """Parse the one-line Notion submission template into loose key/value fields."""
    fields: dict[str, str] = {}
    for part in re.split(r"\s*/\s*", text):
        if ":" in part:
            key, value = part.split(":", 1)
        elif "：" in part:
            key, value = part.split("：", 1)
        else:
            continue
        fields[key.strip()] = value.strip()
    return fields


def first_present(row: dict[str, str], names: Iterable[str]) -> str:
    lowered = {key.lower(): value for key, value in row.items()}
    for name in names:
        if name in row and row[name]:
            return row[name]
        value = lowered.get(name.lower())
        if value:
            return value
    return ""


def notion_respondents() -> list[Respondent]:
    rows = read_csv(NOTION_EXPORT_CSV)
    respondents: list[Respondent] = []
    for row in rows:
        raw = first_present(row, ("Submission", "submission", "回答", "Name", "名前"))
        fields = split_submission(raw)
        source = (
            first_present(row, ("Source", "source", "流入元"))
            or fields.get("流入元")
            or "notion_untracked"
        )
        recent = first_present(row, ("Recent sesame oil purchase", "recent_purchase", "最近買ったごま油")) or fields.get("最近買ったごま油", "")
        aroma = first_present(row, ("Aroma memory", "experience", "香り経験")) or fields.get("香り経験", "")
        single = first_present(row, ("100ml 1,480円", "single_price", "Price reaction")) or fields.get("100ml 1,480円", "")
        bundle = first_present(row, ("3本 3,980円", "bundle_price")) or fields.get("3本 3,980円", "")
        comment = first_present(row, ("Comment", "comment", "Notes", "コメント")) or fields.get("コメント", "")
        joined = " ".join([raw, comment, recent, aroma, single, bundle])
        if not joined.strip():
            continue
        respondents.append(
            Respondent(
                channel="notion",
                source=source,
                recent_purchase=has_recent_purchase(recent),
                aroma_memory=positive(aroma),
                single_price_mentioned=mentioned(single),
                single_price_positive=positive(single),
                bundle_price_mentioned=mentioned(bundle),
                bundle_price_positive=positive(bundle),
                sample_or_purchase_signal=contains_any(joined, SAMPLE_WORDS),
            )
        )
    return respondents


def github_respondents() -> list[Respondent]:
    respondents: list[Respondent] = []
    for row in read_csv(WAITLIST_CSV):
        source = row.get("source_title") or parse_source_from_title(row.get("title", "")) or row.get("source_self_reported") or "github_untracked"
        joined = " ".join(row.values())
        if not joined.strip():
            continue
        respondents.append(
            Respondent(
                channel="github",
                source=source,
                recent_purchase=has_recent_purchase(row.get("recent_purchase", "")),
                aroma_memory=positive(row.get("experience", "")),
                single_price_mentioned=mentioned(row.get("single_price", "")),
                single_price_positive=positive(row.get("single_price", "")),
                bundle_price_mentioned=mentioned(row.get("bundle_price", "")),
                bundle_price_positive=positive(row.get("bundle_price", "")),
                sample_or_purchase_signal=contains_any(joined, SAMPLE_WORDS),
            )
        )
    return respondents


def field_respondents() -> list[Respondent]:
    respondents: list[Respondent] = []
    for row in read_csv(FIELD_INTERVIEW_CSV):
        joined = " ".join(row.values())
        if (
            row.get("location", "").lower() == "example"
            or row.get("person_id", "").lower() == "p01"
            or "replace this row" in joined.lower()
        ):
            continue
        if not joined.strip():
            continue
        respondents.append(
            Respondent(
                channel="offline",
                source=row.get("source") or "offline_untracked",
                recent_purchase=has_recent_purchase(row.get("recent_purchase", "")),
                aroma_memory=positive(row.get("aroma_memory", "")),
                single_price_mentioned=mentioned(row.get("single_price_reaction", "")),
                single_price_positive=positive(row.get("single_price_reaction", "")),
                bundle_price_mentioned=mentioned(row.get("bundle_price_reaction", "")),
                bundle_price_positive=positive(row.get("bundle_price_reaction", "")),
                sample_or_purchase_signal=contains_any(joined, SAMPLE_WORDS),
            )
        )
    return respondents


def public_social_respondents() -> list[Respondent]:
    respondents: list[Respondent] = []
    for row in read_csv(PUBLIC_SOCIAL_CSV):
        joined = " ".join(row.values())
        if not joined.strip():
            continue
        if row.get("response_url", "").lower() == "example":
            continue
        text = row.get("response_text", "")
        source = row.get("source") or row.get("platform") or "social_untracked"
        respondents.append(
            Respondent(
                channel="social",
                source=source,
                recent_purchase=has_recent_purchase(row.get("recent_purchase", "") or text),
                aroma_memory=positive(row.get("aroma_memory", "") or text),
                single_price_mentioned=mentioned(row.get("single_price_reaction", "") or text),
                single_price_positive=positive(row.get("single_price_reaction", "") or text),
                bundle_price_mentioned=mentioned(row.get("bundle_price_reaction", "") or text),
                bundle_price_positive=positive(row.get("bundle_price_reaction", "") or text),
                sample_or_purchase_signal=contains_any(joined, SAMPLE_WORDS),
            )
        )
    return respondents


def channel_status() -> dict[str, int]:
    rows = read_csv(CHANNEL_LOG_CSV)
    return {
        "rows": len(rows),
        "posted_yes": sum(1 for row in rows if row.get("posted", "").lower() == "yes"),
        "ready_or_pending": sum(1 for row in rows if "ready" in row.get("status", "").lower() or "pending" in row.get("status", "").lower()),
        "held_or_excluded": sum(1 for row in rows if "hold" in row.get("status", "").lower() or "do_not" in row.get("status", "").lower()),
    }


def count_true(respondents: list[Respondent], attr: str) -> int:
    return sum(1 for respondent in respondents if getattr(respondent, attr))


def decision(metrics: dict[str, int]) -> tuple[str, list[str]]:
    reasons: list[str] = []
    if metrics["online_public_responses"] >= 30:
        reasons.append("Online public responses reached 30+.")
    if metrics["purchase_conversation_signals"] >= 10:
        reasons.append("Purchase-context signals reached 10+.")
    if metrics["offline_interviews"] >= 10 and metrics["offline_recent_purchase"] >= 3:
        reasons.append("Offline interviews reached 10 with 3+ concrete recent buyers/searchers.")
    if metrics["sample_or_purchase_requests"] >= 5:
        reasons.append("Sample or purchase signals reached 5+.")
    if reasons:
        return "ready_for_manual_go_pivot_review", reasons
    return "insufficient_external_evidence", ["External response threshold has not been met."]


def percent(numerator: int, denominator: int) -> str:
    if denominator <= 0:
        return "n/a"
    return f"{numerator / denominator:.0%}"


def recommendation(metrics: dict[str, int], verdict: str) -> tuple[str, list[str]]:
    if verdict == "insufficient_external_evidence":
        return "collect_more_evidence", [
            "Do not make a Go/Pivot/Stop decision before at least one completion threshold is met.",
        ]

    single_price_rate = (
        metrics["single_price_positive"] / metrics["single_price_responses"]
        if metrics["single_price_responses"]
        else 0
    )
    purchase_or_sample = metrics["purchase_conversation_signals"] + metrics["sample_or_purchase_requests"]
    support: list[str] = []

    if single_price_rate >= 0.30 and purchase_or_sample >= 10:
        support.append("Price-positive share is at least 30% and purchase-context signals are 10+.")
        if metrics["aroma_memory_positive"] >= 5:
            support.append("Aroma-memory signal is present in 5+ responses.")
        return "candidate_go_small_batch", support

    if metrics["single_price_responses"] >= 10 and single_price_rate < 0.30:
        return "candidate_pivot_price_or_bundle", [
            "100ml price-positive share is below 30% among 10+ price-bearing responses.",
            "Test smaller trial size, bundle/gift framing, or lower landed-cost path before sourcing inventory.",
        ]

    if metrics["online_public_responses"] >= 30 and purchase_or_sample < 5:
        return "candidate_stop_or_resegment", [
            "Online response volume is 30+ but purchase/sample signals are below 5.",
            "Re-segment toward existing Shin-Okubo/Korean-grocery buyers or stop this wedge.",
        ]

    return "manual_review_needed", [
        "A threshold was met, but the current signal mix is not decisive enough for automatic Go/Pivot/Stop.",
    ]


def render_summary(respondents: list[Respondent], metrics: dict[str, int], status: dict[str, int], verdict: str, reasons: list[str], rec: str, rec_reasons: list[str]) -> str:
    generated_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    source_counts = Counter(respondent.source or "untracked" for respondent in respondents)
    channel_counts = Counter(respondent.channel for respondent in respondents)

    lines = [
        "# Validation Signal Summary",
        "",
        f"Generated at: {generated_at}",
        "",
        f"Verdict: `{verdict}`",
        "",
        "## Threshold Evidence",
        "",
        "| Metric | Current | Threshold |",
        "|---|---:|---:|",
        f"| Online public responses | {metrics['online_public_responses']} | 30 |",
        f"| Purchase-context signals | {metrics['purchase_conversation_signals']} | 10 |",
        f"| Offline interviews | {metrics['offline_interviews']} | 10 |",
        f"| Offline recent purchase/search signals | {metrics['offline_recent_purchase']} | 3 |",
        f"| Sample or purchase requests | {metrics['sample_or_purchase_requests']} | 5 |",
        "",
        "## Supporting Metrics",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Total respondents | {metrics['total_respondents']} |",
        f"| Notion + GitHub responses | {metrics['form_or_github_responses']} |",
        f"| Public social responses | {metrics['public_social_responses']} |",
        f"| Aroma memory positive | {metrics['aroma_memory_positive']} |",
        f"| 100ml price-bearing responses | {metrics['single_price_responses']} |",
        f"| 100ml price positive or conditional | {metrics['single_price_positive']} |",
        f"| 100ml price positive share | {percent(metrics['single_price_positive'], metrics['single_price_responses'])} |",
        f"| 3-bottle price-bearing responses | {metrics['bundle_price_responses']} |",
        f"| 3-bottle price positive or conditional | {metrics['bundle_price_positive']} |",
        f"| 3-bottle price positive share | {percent(metrics['bundle_price_positive'], metrics['bundle_price_responses'])} |",
        f"| Channel rows tracked | {status['rows']} |",
        f"| Posted/public rows | {status['posted_yes']} |",
        f"| Ready or pending rows | {status['ready_or_pending']} |",
        f"| Held or excluded rows | {status['held_or_excluded']} |",
        "",
        "## Source Breakdown",
        "",
        "| Source | Responses |",
        "|---|---:|",
    ]
    if source_counts:
        for source, count in source_counts.most_common():
            lines.append(f"| {source} | {count} |")
    else:
        lines.append("| n/a | 0 |")

    lines.extend(["", "## Channel Breakdown", "", "| Channel | Responses |", "|---|---:|"])
    if channel_counts:
        for channel, count in channel_counts.most_common():
            lines.append(f"| {channel} | {count} |")
    else:
        lines.append("| n/a | 0 |")

    lines.extend(["", "## Interpretation", ""])
    for reason in reasons:
        lines.append(f"- {reason}")
    lines.extend(["", "## Go/Pivot/Stop Recommendation", "", f"`{rec}`", ""])
    for reason in rec_reasons:
        lines.append(f"- {reason}")
    if verdict == "insufficient_external_evidence":
        lines.append("- Keep the goal active until real external responses or interviews meet one completion threshold.")
    else:
        lines.append("- Review response quality manually before making a Go/Pivot/Stop decision.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    EXP_DIR.mkdir(parents=True, exist_ok=True)
    respondents = notion_respondents() + github_respondents() + public_social_respondents() + field_respondents()
    metrics = {
        "total_respondents": len(respondents),
        "form_or_github_responses": sum(1 for respondent in respondents if respondent.channel in {"notion", "github"}),
        "public_social_responses": sum(1 for respondent in respondents if respondent.channel == "social"),
        "online_public_responses": sum(1 for respondent in respondents if respondent.channel in {"notion", "github", "social"}),
        "purchase_conversation_signals": sum(1 for respondent in respondents if respondent.recent_purchase or respondent.sample_or_purchase_signal),
        "offline_interviews": sum(1 for respondent in respondents if respondent.channel == "offline"),
        "offline_recent_purchase": sum(1 for respondent in respondents if respondent.channel == "offline" and respondent.recent_purchase),
        "sample_or_purchase_requests": count_true(respondents, "sample_or_purchase_signal"),
        "aroma_memory_positive": count_true(respondents, "aroma_memory"),
        "single_price_responses": count_true(respondents, "single_price_mentioned"),
        "single_price_positive": count_true(respondents, "single_price_positive"),
        "bundle_price_responses": count_true(respondents, "bundle_price_mentioned"),
        "bundle_price_positive": count_true(respondents, "bundle_price_positive"),
    }
    status = channel_status()
    verdict, reasons = decision(metrics)
    rec, rec_reasons = recommendation(metrics, verdict)
    payload = {
        "generated_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "verdict": verdict,
        "reasons": reasons,
        "recommendation": rec,
        "recommendation_reasons": rec_reasons,
        "metrics": metrics,
        "channel_status": status,
    }
    SUMMARY_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    SUMMARY_MD.write_text(render_summary(respondents, metrics, status, verdict, reasons, rec, rec_reasons), encoding="utf-8")
    print(f"Wrote {SUMMARY_MD} and {SUMMARY_JSON}. Verdict: {verdict}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

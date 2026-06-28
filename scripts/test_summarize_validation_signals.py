#!/usr/bin/env python3
"""Lightweight assertions for validation-signal recommendation rules."""

from __future__ import annotations

from summarize_validation_signals import has_recent_purchase, recommendation, split_submission


def base_metrics() -> dict[str, int]:
    return {
        "online_public_responses": 0,
        "purchase_conversation_signals": 0,
        "sample_or_purchase_requests": 0,
        "single_price_responses": 0,
        "single_price_positive": 0,
        "aroma_memory_positive": 0,
    }


def test_collect_more_evidence() -> None:
    rec, reasons = recommendation(base_metrics(), "insufficient_external_evidence")
    assert rec == "collect_more_evidence"
    assert reasons


def test_candidate_go_small_batch() -> None:
    metrics = base_metrics()
    metrics.update(
        {
            "purchase_conversation_signals": 10,
            "sample_or_purchase_requests": 5,
            "single_price_responses": 10,
            "single_price_positive": 3,
            "aroma_memory_positive": 5,
        }
    )
    rec, reasons = recommendation(metrics, "ready_for_manual_go_pivot_review")
    assert rec == "candidate_go_small_batch"
    assert any("30%" in reason for reason in reasons)


def test_candidate_pivot_price() -> None:
    metrics = base_metrics()
    metrics.update(
        {
            "purchase_conversation_signals": 10,
            "sample_or_purchase_requests": 0,
            "single_price_responses": 10,
            "single_price_positive": 2,
        }
    )
    rec, reasons = recommendation(metrics, "ready_for_manual_go_pivot_review")
    assert rec == "candidate_pivot_price_or_bundle"
    assert any("below 30%" in reason for reason in reasons)


def test_candidate_stop_or_resegment() -> None:
    metrics = base_metrics()
    metrics.update({"online_public_responses": 30, "single_price_responses": 3, "single_price_positive": 1})
    rec, reasons = recommendation(metrics, "ready_for_manual_go_pivot_review")
    assert rec == "candidate_stop_or_resegment"
    assert any("below 5" in reason for reason in reasons)


def test_shelfcheck_submission_fields_parse() -> None:
    fields = split_submission(
        "流入元: content_shelfcheck / 最後に買ったまたは見た場所: 棚で見ている / "
        "候補のブランドや店名: 韓国スーパーの棚 / 残りが少ない時の香り: 途中で弱くなる"
    )
    assert fields["最後に買ったまたは見た場所"] == "棚で見ている"
    assert has_recent_purchase(fields["最後に買ったまたは見た場所"])


def main() -> int:
    test_collect_more_evidence()
    test_candidate_go_small_batch()
    test_candidate_pivot_price()
    test_candidate_stop_or_resegment()
    test_shelfcheck_submission_fields_parse()
    print("summarize_validation_signals recommendation tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

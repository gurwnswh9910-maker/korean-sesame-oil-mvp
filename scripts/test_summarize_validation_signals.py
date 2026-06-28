#!/usr/bin/env python3
"""Lightweight assertions for validation-signal recommendation rules."""

from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

import summarize_validation_signals
from summarize_validation_signals import (
    finishing_oil_use,
    has_recent_purchase,
    note_dashboard_snapshot,
    problem_fit_score,
    recommendation,
    split_submission,
    substitute_gap,
    use_up_burden,
)


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
        "候補のブランドや店名: 韓国スーパーの棚 / 1本を使い切る期間: 半年以上 / "
        "5g・110ml・しぼりたて候補で十分か: 香り・鮮度が不安 / 残りが少ない時の香り: 途中で弱くなる"
    )
    assert fields["最後に買ったまたは見た場所"] == "棚で見ている"
    assert fields["1本を使い切る期間"] == "半年以上"
    assert use_up_burden(fields["1本を使い切る期間"])
    assert substitute_gap(fields["5g・110ml・しぼりたて候補で十分か"])
    assert has_recent_purchase(fields["最後に買ったまたは見た場所"])


def test_finishing_oil_use_signal() -> None:
    fields = split_submission(
        "流入元: content_aromaloss / 主な使い方: 最後に香りを足す / "
        "香りが一番よかった使い方: 冷奴に最後だけ"
    )
    assert fields["主な使い方"] == "最後に香りを足す"
    assert finishing_oil_use(" ".join(fields.values()))
    assert not finishing_oil_use("主な使い方: 炒める時に使う")


def test_problem_fit_score_strong_response() -> None:
    joined = (
        "流入元: content_shelfcheck / 最後に買ったまたは見た場所: 新大久保の韓国スーパー / "
        "候補のブランドや店名: オットゥギ 110ml / 候補の容量や価格: 110ml 518円 / "
        "1本を使い切る期間: 半年以上 / 残りが少ない時の香り: 香りが弱くなる / "
        "5g・110ml・しぼりたて候補で十分か: 5gパックより何度も使う料理向きで、かどやや九鬼より韓国料理の最後の香りが足りない / "
        "買い直す条件: 製造日と搾った日、遮光瓶が見えるなら / 100ml 1,480円: 迷うが条件次第"
    )
    score = problem_fit_score(
        purchase="新大久保の韓国スーパー",
        brand_or_store="オットゥギ",
        volume_or_price="110ml 518円",
        useup="半年以上",
        aroma="香りが弱くなる",
        substitute="5gパックより何度も使う料理向きで、かどやや九鬼より韓国料理の最後の香りが足りない",
        evidence="製造日と搾った日、遮光瓶",
        price_reaction="迷うが条件次第",
        joined=joined,
    )
    assert score >= 5


def test_problem_fit_score_weak_interest() -> None:
    score = problem_fit_score(
        purchase="",
        brand_or_store="",
        volume_or_price="",
        useup="",
        aroma="韓国料理が好き",
        substitute="",
        evidence="",
        price_reaction="",
        joined="小瓶がかわいい。韓国式なら良さそう。",
    )
    assert score < 5


def test_note_dashboard_snapshot_gate() -> None:
    original = summarize_validation_signals.NOTE_DASHBOARD_CSV
    with TemporaryDirectory() as tmpdir:
        snapshot = Path(tmpdir) / "note_dashboard_snapshots.csv"
        snapshot.write_text(
            "captured_at,aggregation_at,source,post_url,views,comments,likes,notes\n"
            "2026-06-28T21:50:00+09:00,2026年6月28日 21:45,note_kfood,,20,0,0,\n"
            "2026-06-28T21:50:00+09:00,2026年6月28日 21:45,note_content_travel,,15,0,0,\n",
            encoding="utf-8",
        )
        summarize_validation_signals.NOTE_DASHBOARD_CSV = snapshot
        try:
            dashboard = note_dashboard_snapshot()
        finally:
            summarize_validation_signals.NOTE_DASHBOARD_CSV = original
    assert dashboard["available"]
    assert dashboard["views"] == 35
    assert dashboard["gate"] == "problem_language_or_cta_failure_consider_aromaloss_note"


def test_note_dashboard_snapshot_distribution_failure() -> None:
    original = summarize_validation_signals.NOTE_DASHBOARD_CSV
    with TemporaryDirectory() as tmpdir:
        snapshot = Path(tmpdir) / "note_dashboard_snapshots.csv"
        snapshot.write_text(
            "captured_at,aggregation_at,source,post_url,views,comments,likes,notes\n"
            "2026-06-28T21:50:00+09:00,2026年6月28日 21:45,note_kfood,,5,0,0,\n",
            encoding="utf-8",
        )
        summarize_validation_signals.NOTE_DASHBOARD_CSV = snapshot
        try:
            dashboard = note_dashboard_snapshot()
        finally:
            summarize_validation_signals.NOTE_DASHBOARD_CSV = original
    assert dashboard["views"] == 5
    assert dashboard["gate"] == "distribution_failure_hold_6th_note"


def main() -> int:
    test_collect_more_evidence()
    test_candidate_go_small_batch()
    test_candidate_pivot_price()
    test_candidate_stop_or_resegment()
    test_shelfcheck_submission_fields_parse()
    test_finishing_oil_use_signal()
    test_problem_fit_score_strong_response()
    test_problem_fit_score_weak_interest()
    test_note_dashboard_snapshot_gate()
    test_note_dashboard_snapshot_distribution_failure()
    print("summarize_validation_signals recommendation tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

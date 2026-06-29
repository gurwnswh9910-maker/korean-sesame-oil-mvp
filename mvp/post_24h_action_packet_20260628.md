# post-24h 실행 패킷

작성 시각: 2026-06-28T12:05+09:00
최근 갱신: 2026-06-29T23:31+09:00

## 목적

2026-06-28T21:50+09:00 note 24h 체크 이후, 감으로 다음 글을 올리지 않기 위한 실행 패킷이다.

## 0. 실제 24h gate 결과

2026-06-28T21:56+09:00에 fresh note dashboard snapshot을 기록했다.

- Dashboard aggregation at: `2026年6月28日 21:46`
- note 1~5 total: views 36, comments 0, スキ 0
- 글별 views/comments/スキ: note 1 `10/0/0`, note 2 `7/0/0`, note 3 `7/0/0`, note 4 `6/0/0`, note 5 `6/0/0`
- 실제 응답자: 0
- Strong problem-fit responses: 0
- Gate: `problem_language_or_cta_failure_consider_aromaloss_note`

해석: 유통 실패 기준인 views < 30은 피했지만, 실제 답변은 0이라 제품 검증 성공이 아니다. 다음 조치는 X/Threads 자동 게시가 아니라 6차 향 손실 note 후보의 pre-publish routing 확인이다. 게시 후보를 보려면 `/aroma-loss-goma`, `/quick-answer`, `/field-aroma` production 경로와 `note_content_aromaloss` source 라우팅을 먼저 확인한다.

2026-06-29T23:31+09:00 실행 결과:

- 6차 note 게시 완료: `https://note.com/dreamy_viola8978/n/n363650c8697f`
- source: `note_content_aromaloss`
- 게시 전 production route/pre-publish check 통과.
- 게시 후 public API는 `published`, `can_comment=true`, 댓글 0, スキ 0.
- `/answer-note`와 `/quick-answer`의 `note_content_aromaloss` source routing은 6차 note URL로 갱신한다.
- 게시 직후 실제 응답 데이터는 0명이다. 이후 판단은 새 댓글/폼/공개 답글/오프라인 원본 응답으로만 한다.

## 1. 먼저 확인할 것

```powershell
$env:PYTHONUTF8='1'; $env:PYTHONIOENCODING='utf-8'; python .\scripts\summarize_validation_signals.py
gh issue list --state all --limit 20 --json number,title,state,labels,url,createdAt,updatedAt
```

note는 대시보드와 API를 함께 본다.

- 대시보드: 글별 views, comments, スキ, 최신 집계 시각
- API: `like_count`, `comment_count`, `status`
- Notion: export 또는 UI 원본 행. SQL query는 현재 Business/Notion AI 제한으로 막힐 수 있음
- 공개 검색: exact hashtag, Vercel URL, note title

대시보드 값을 확인한 뒤 아래처럼 snapshot을 기록한다. 실제 숫자를 넣기 전에는 `--dry-run`으로만 확인한다.

```powershell
$env:PYTHONUTF8='1'; $env:PYTHONIOENCODING='utf-8'; python .\scripts\record_note_dashboard_snapshot.py --dry-run --aggregation-at "2026年6月28日 21:45" --note "note_kfood=5,0,0" --note "note_content_travel=0,0,0" --note "note_content_shinokubo=0,0,0" --note "note_content_homecook=0,0,0" --note "note_content_homecook_ricebowl=0,0,0"
```

숫자가 맞으면 `--dry-run`을 빼고 기록한다. 기록 후 `scripts/summarize_validation_signals.py`를 재실행하면 `Note Dashboard Snapshot` 섹션과 `24h action gate`가 갱신된다.

2026-06-28T17:02+09:00부터는 CDP로 대시보드 본문 텍스트를 파일로 저장한 뒤 자동 파싱할 수도 있다.

```powershell
node .\scripts\export_note_dashboard_text.mjs --output .\.tmp\note_dashboard_current.txt --wait-ms 1000
$env:PYTHONUTF8='1'; $env:PYTHONIOENCODING='utf-8'; python .\scripts\record_note_dashboard_snapshot.py --dry-run --from-dashboard-text .\.tmp\note_dashboard_current.txt --fill-missing-zero
```

더 안전한 한 번 실행 경로:

```powershell
$env:PYTHONUTF8='1'; $env:PYTHONIOENCODING='utf-8'; python .\scripts\run_post_24h_gate.py --export-dashboard --refresh-dashboard
```

위 명령은 기본적으로 기록하지 않고 `experiments/post_24h_gate_status.json`만 갱신한다. `stale=false`와 숫자를 확인한 뒤 실제 기록은 아래처럼 한다.

```powershell
$env:PYTHONUTF8='1'; $env:PYTHONIOENCODING='utf-8'; python .\scripts\run_post_24h_gate.py --export-dashboard --refresh-dashboard --record
```

주의:

- `export_note_dashboard_text.mjs`는 로그인된 Edge/Chrome CDP 포트 `9222`의 `https://note.com/sitesettings/stats` 탭에서 `document.body.innerText`를 저장한다.
- `--from-dashboard-text`는 `最新集計時刻`과 프로젝트 note 제목 5개를 읽어 rows를 만든다.
- 대시보드에 안 보이는 프로젝트 note는 `--fill-missing-zero`를 붙였을 때만 0으로 기록한다.
- 집계시각이 24h 체크 기준보다 오래된 값이면 기록하지 않는다. 2026-06-28T17:08+09:00 `run_post_24h_gate.py --record` 검증에서는 `最新集計時刻 2026年6月28日 01:31`, views 5, comments 0, likes 0이라 `stale_dashboard_not_recorded`로 기록을 거절했다.
- 2026-06-28T17:32+09:00부터 `experiments/post_24h_gate_status.json`에는 `decision` 블록도 들어간다. 콘솔 출력에도 `next_action=...`가 붙는다. 따라서 21:50 이후에는 `gate`와 `decision.next_action`을 함께 보고, stale이면 기록/게시하지 않는다.
- 2026-06-28T17:41+09:00부터 `run_post_24h_gate.py`는 `experiments/validation_signal_summary.json`의 `response_metrics`도 함께 읽는다. 대시보드 집계가 stale이어도 실제 폼/공개 답글/오프라인 응답이 있으면 `review_responses_for_strong_fit`로 보내고, `strong_problem_fit_responses >= 5`이면 수입/표시/단가 gate로 보낸다. stale 판정은 조회수 기반 의사결정만 막는다.

## 2. 판정 게이트

| 결과 | 판정 | 실행 |
|---|---|---|
| 합산 views < 30, 댓글/폼 0 | 유통 실패 | 6차 note 게시 보류. `mvp/post_gate_external_channel_packet_20260628.md` 기준으로 X/Threads URL 없는 공개 질문 1회, 오프라인 인터뷰, 또는 Konest 규칙 확인 중 1개만 선택한다. |
| 합산 views >= 30, 댓글/폼 0 | 문제 언어 또는 CTA 실패 | 2026-06-29T23:31+09:00 6차 note 향 손실/향 타이밍 글을 게시했다. 이후에는 새 글을 더 늘리기보다 note 6 URL routing, 댓글/폼/공개 답글/오프라인 원본 응답, 대시보드 지표를 확인한다. |
| 댓글/폼/공개 답글/오프라인 1~4건 | 질적 탐색 | 원본 응답을 열어 strong 기준으로 수동 판정. 모자란 문항을 기록하고 추가 질문. |
| strong 응답 5건 이상 | 문제 fit 후보 | 결제/예약 전 수입/표시/단가 gate로 이동. |

## 3. 6차 note 게시 전 조건 기록

아래 조건은 2026-06-29T23:31+09:00 게시 전에 사용한 체크리스트다. 현재 6차 note는 게시 완료됐으므로, 새 판단에는 이 조건을 반복 적용하지 말고 게시 후 확인 항목과 실제 응답 데이터를 본다.

1. 24h 체크가 끝났다.
2. note 1~5가 적어도 일부 타겟에게 도달했다.
3. 응답 0 또는 약한 응답의 원인이 `상품이 너무 넓음`으로 보인다.
4. 게시 전에는 `/answer-note?src=note_content_aromaloss`와 `/quick-answer?src=note_content_aromaloss`가 6차 note URL 없이 note 댓글 CTA를 숨기는 상태였다.
5. 게시 후 실제 note URL을 source routing에 추가할 시간이 있었다.

게시 직전 문안 점검:

- `大きいごま油、使い切る前に香りが弱くなりますか？`만 묻지 않는다.
- 실제 게시 제목은 `ごま油、炒めるより最後に香らせていますか？`다.
- `5gの使い切りパック`, `110mlの安い韓国ごま油`, `100ml前後の搾りたてごま油` 중 무엇을 고르는지 묻는다.
- `香りが一番よかった使い方`를 물어, 단순 용량 문제가 아니라 향이 살아 있는 타이밍 문제인지 본다.
- 100ml 긍정은 향, 사용 기간, 제조일/압착일, 시식, 차광병, 재구매 편의 중 하나 이상의 이유가 있어야 강하게 본다.

## 4. 6차 note 게시 후 즉시 할 일

1. note URL 기록
2. `docs/answer-note.html`, `docs/quick-answer.html`, `mvp/answer-note.html`, `mvp/quick-answer.html`의 `note_content_aromaloss` 라우팅에 6차 note URL 추가
3. Vercel production 배포
4. mobile 390px에서 `/answer-note?src=note_content_aromaloss`, `/quick-answer?src=note_content_aromaloss`, `/aroma-loss-goma?src=note_content_aromaloss` 확인
5. `experiments/channel_posting_log.csv`, `experiments/live_validation_log.csv`, `검증/게시_배포_기록.md`, `검증/응답_데이터_상태.md`, `검증/검증_원장.md` 갱신

## 5. 게시하지 않는 경우

유통 실패로 판정되면 아래 중 하나만 선택한다.

- X/Threads 단일 게시 권한을 사용자에게 받아 `mvp/x_threads_posting_packet.md`의 URL 없는 공개 질문 사용
- 오프라인 실행자가 있을 때 `mvp/field_aroma_interview_script.md`와 `field-aroma` QR 사용. 실제 기록은 `experiments/field_interview_log.csv`의 `aroma_timing`에 향이 좋았던 요리/타이밍을 남긴다.
- Konest는 `mvp/post_gate_external_channel_packet_20260628.md` 기준으로 규칙 확인 또는 운영자 문의 후, 링크 없는 여행 경험 질문만 검토한다.
- 사용 가능한 외부 채널이 없으면 새 게시가 아니라 메시지/응답 경로만 더 다듬고 목표는 active로 둔다

## 6. strong 응답 판정

아래 8개 중 5개 이상이면 strong으로 본다.

1. 구매처/탐색처
2. 브랜드/店名
3. 용량/가격
4. 1병 사용 기간
5. 향 저하/큰 병 부담
6. 기존 대체재와 비교
7. 필요한 증거
8. 100ml 1,480円 반응

이 기준은 `scripts/summarize_validation_signals.py`가 `Strong problem-fit responses`와 `Highest problem-fit score`로 자동 집계한다. 24h 체크 후에는 먼저 `experiments/validation_signal_summary.md`의 두 지표를 확인한다.

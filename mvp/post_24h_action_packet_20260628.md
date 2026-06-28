# post-24h 실행 패킷

작성 시각: 2026-06-28T12:05+09:00

## 목적

2026-06-28T21:50+09:00 note 24h 체크 이후, 감으로 다음 글을 올리지 않기 위한 실행 패킷이다.

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

## 2. 판정 게이트

| 결과 | 판정 | 실행 |
|---|---|---|
| 합산 views < 30, 댓글/폼 0 | 유통 실패 | 6차 note 게시 보류. X/Threads 권한 또는 오프라인 실행 가능성 없이는 게시 수를 늘리지 않는다. |
| 합산 views >= 30, 댓글/폼 0 | 문제 언어 또는 CTA 실패 | 6차 note 향 손실 글 게시 후보. 게시 전 `/aroma-loss-goma`, `/quick-answer` production 검증. |
| 댓글/폼 1~4건 | 질적 탐색 | strong 기준으로 수동 판정. 모자란 문항을 기록하고 추가 질문. |
| strong 응답 5건 이상 | 문제 fit 후보 | 결제/예약 전 수입/표시/단가 gate로 이동. |

## 3. 6차 note 게시 조건

아래가 모두 true일 때만 `mvp/note_aromaloss_posting_packet.md`를 게시한다.

1. 24h 체크가 끝났다.
2. note 1~5가 적어도 일부 타겟에게 도달했다.
3. 응답 0 또는 약한 응답의 원인이 `상품이 너무 넓음`으로 보인다.
4. `/answer-note?src=note_content_aromaloss`와 `/quick-answer?src=note_content_aromaloss`가 6차 note URL 없이도 note 댓글 CTA를 숨기는 상태다.
5. 게시 후 실제 note URL을 source routing에 추가할 시간이 있다.

## 4. 6차 note 게시 후 즉시 할 일

1. note URL 기록
2. `docs/answer-note.html`, `docs/quick-answer.html`, `mvp/answer-note.html`, `mvp/quick-answer.html`의 `note_content_aromaloss` 라우팅에 6차 note URL 추가
3. Vercel production 배포
4. mobile 390px에서 `/answer-note?src=note_content_aromaloss`, `/quick-answer?src=note_content_aromaloss`, `/aroma-loss-goma?src=note_content_aromaloss` 확인
5. `experiments/channel_posting_log.csv`, `experiments/live_validation_log.csv`, `검증/게시_배포_기록.md`, `검증/응답_데이터_상태.md`, `검증/검증_원장.md` 갱신

## 5. 게시하지 않는 경우

유통 실패로 판정되면 아래 중 하나만 선택한다.

- X/Threads 단일 게시 권한을 사용자에게 받아 `mvp/x_threads_posting_packet.md` 사용
- 오프라인 실행자가 있을 때 `mvp/field_aroma_interview_script.md`와 `field-aroma` QR 사용
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

# 검증 폴더 작업 원칙

## 역할

이 폴더는 참기름 MVP의 감사 가능한 절차기억이다. 다음 세션이 "어디까지 했고, 왜 그렇게 판단했고, 어떤 URL과 데이터로 확인했는지"를 재검증할 수 있어야 한다.

## 최근 적대적 검증 포인터

- 2026-06-27T22:56+09:00 적대적 검증 루프: `검증/적대적_검증_루프_20260627.md`
- 2026-06-27T22:56+09:00 내용 적대적 검증: `검증/내용_적대적_검증_20260627.md`
- `/answer-note`는 2026-06-27T22:56+09:00 기준 Vercel production에서 200, no redirect, mobile answer hub로 확인됐다.
- 제품 외 콘텐츠/타겟 밀집 검증: `검증/제품외_콘텐츠_타겟밀집_검증법_20260627.md`
- 참기름 판매 목표 아래의 욕구/문제 가설: `검증/욕구_문제_가설_20260627.md`
- 글쓰기 레퍼런스 수집과 AI티 검수: `검증/글쓰기_레퍼런스_수집_AI티_검수_원칙_20260628.md`
- note 댓글 관찰/접촉 패킷: `검증/note_댓글_관찰_접촉_패킷_20260628.md`

## 반드시 지킬 것

- 숨은 사고과정 원문을 적지 않는다. 대신 재검증 가능한 판단 근거, 출처, 관찰값, 명령, URL, 파일 경로를 적는다.
- `검증/검증_원장.md`는 현재 truth snapshot이다. 오래된 실험 로그와 다르면 원장을 우선하되, 원장도 원자료 링크로 검증한다.
- 외부 게시나 계정 작업은 게시 URL, 계정/채널, 시각, 권한 근거, 원문 파일, 설정값, 다음 측정 시각을 남긴다.
- 소비자-facing 링크는 기본적으로 Vercel clean URL을 사용한다.
- 제품 외 콘텐츠로 타겟을 검증할 때는 `https://korean-sesame-oil-mvp.vercel.app/korea-trip-goma`를 사용하고, `content_travel`, `content_shinokubo`, `content_homecook` source를 분리한다.
- 신오쿠보/한국식품점 대체재 전환 검증은 `https://korean-sesame-oil-mvp.vercel.app/shinokubo-goma`를 사용한다. 이 검증은 `신오쿠보를 좋아한다`가 아니라 구매처, 브랜드/店名, 용량·가격, 향 보존 불만, 제조일/강한 향/100ml小瓶/구입 편의 전환 조건이 있는 응답을 강한 신호로 센다.
- 집밥 한국요리/마지막 향 검증은 `https://korean-sesame-oil-mvp.vercel.app/homecook-goma`를 사용한다. 이 검증은 `韓国料理が好き`가 아니라 최근 만든 요리, 현재 참기름 구매처/브랜드, 용량·가격, 마지막 향 부족 또는 충분한 이유, 바꿀 조건이 있는 응답을 강한 신호로 센다.
- 밥친구/한국김/TKG 같은 `밥 한 그릇 5분 완성` 축은 홈쿡 검증의 하위 문제로 본다. 강한 신호는 반복 사용 빈도, 현재 참기름 단품 구매처, 소량/향 보존/가격 전환 조건이 함께 있을 때만 센다.
- note/콘텐츠 무응답이 이어질 때는 게시 수를 늘리기보다 `개봉 후 향 손실/큰 병 부담`, `기존 대체재 선택 피로`, `밥 한 그릇 5분 향미`를 비교한다. 최신 정리는 `검증/무응답_학습_및_다음검증_20260628.md`를 본다.
- 고의도 채널 KPI와 24h 이후 실행 게이트는 `검증/고의도_채널_KPI_및_다음실험_20260628.md`와 `mvp/post_24h_action_packet_20260628.md`를 본다. note 1~5 합산 views가 30 미만이고 응답 0이면 유통 실패로 보고 6차 note를 바로 게시하지 않는다.
- note dashboard views/comments/スキ는 `scripts/record_note_dashboard_snapshot.py`로 `experiments/note_dashboard_snapshots.csv`에 기록한다. 먼저 `--dry-run`으로 숫자 파싱을 확인한 뒤 실제 기록하고, `scripts/summarize_validation_signals.py`를 재실행한다.
- note 공개 상태/댓글/スキ는 `scripts/check_note_public_api.py`로 확인한다. 이 스크립트는 조회수를 주지 않으므로 24h gate의 views는 note 대시보드 snapshot으로만 기록한다.
- 개봉 후 향 손실/큰 병 부담 검증은 `https://korean-sesame-oil-mvp.vercel.app/aroma-loss-goma`와 source `content_aromaloss`를 사용한다. note 원고는 `mvp/note_aromaloss_posting_packet.md`에 준비됐지만 24h 재확인 전 live note 게시하지 않는다.
- 매대 앞 선택 피로/신선도 증거 검증은 `https://korean-sesame-oil-mvp.vercel.app/shelf-check`와 짧은 경로 `https://korean-sesame-oil-mvp.vercel.app/shelf`를 사용한다. source는 `content_shelfcheck`다. 이 검증은 `한국식이면 좋다`가 아니라 실제로 본 후보 상품, 용량·가격, 안 사는 이유, 제조일/압착/마지막 향 보존/재구매 편의 같은 전환 증거가 있는 응답을 강한 신호로 센다.
- `참기름 팔기` 목표를 더 작은 욕구/문제로 다시 해석할 때는 `검증/참기름_팔기_욕구_세분화_20260628.md`와 `research/08_micro_jtbd_and_competing_solutions_20260628.md`를 먼저 본다. 현재 보정은 `사용량-향 보존 불일치`, `대체재 선택 피로`, `搾りたて 체험 욕구`, `신오쿠보 밖 재구매 불편`, `요리 마지막 향`, `선물/나눔`에 더해 `Kadoya 5g使い切りパック보다 100ml가 나은 이유`를 묻는 것이다. `5g pack은 편하지만 여러 번 쓰는 한국요리에는 부족하다`, `Ottogi 110ml는 싸지만 제조일/향 신뢰가 약하다`, `신오쿠보 搾りたて는 좋지만 평소 재구매가 불편하다`처럼 대체재별로 남는 이유가 없는 호감 반응은 강한 수요로 세지 않는다.
- 기존 대체재/가격 기준은 `research/07_existing_substitute_price_map_20260628.md`를 본다. Ottogi 110ml 506~518円, Kuki 600g 1,046円, Kim-san 계열 搾りたて 100~120ml 1,500円대 대체재를 알고도 남는 이유가 없는 100ml 1,480円 긍정은 약한 신호로 둔다.
- 향 손실/큰 병 부담의 고의도 오프라인 검증은 `https://korean-sesame-oil-mvp.vercel.app/field-aroma`와 source `offline_aromaloss`를 사용한다. QR은 `https://korean-sesame-oil-mvp.vercel.app/quick-answer?src=offline_aromaloss`로 바로 보낸다. 실제 인터뷰 원본은 `experiments/field_interview_log.csv`에 기록되기 전까지 응답으로 세지 않는다. 2026-06-28T13:55+09:00부터 오프라인 질문은 `향이 가장 좋았던 요리/타이밍`, `5g・110ml・しぼりたて 후보로 충분한지`, `100ml 병이 더 맞는 이유`를 함께 묻는다.
- note/모바일 유입에서는 QR을 CTA로 쓰지 않는다. `https://korean-sesame-oil-mvp.vercel.app/answer-note` 모바일 응답 허브, note 댓글 템플릿, 탭 가능한 `/share` 링크를 우선한다.
- 구조화 응답이 필요하면 `https://korean-sesame-oil-mvp.vercel.app/quick-answer`를 사용한다. 이 페이지는 다문항 선택을 Notion 1줄 `Submission`으로 변환하는 보조 MVP이며, 응답 데이터 자체는 Notion/export/note 댓글/공개 답글 원본으로만 센다.
- 2026-06-28T13:04+09:00 기준 `/quick-answer`, `/aroma-loss-goma`, `/shelf-check`, `/shelf`는 `1本を使い切る期間`과 `5g・110ml・しぼりたて候補で十分か`를 묻는다. 집계 요약은 `Use-up or aroma-retention burden signals`, `Existing-substitute gap signals`를 supporting metric으로 표시한다.
- 2026-06-28T12:13+09:00 기준 집계 요약은 `Strong problem-fit responses`와 `Highest problem-fit score`도 표시한다. 강한 응답은 8개 기준 중 5개 이상을 포함해야 하며, 기준은 `scripts/summarize_validation_signals.py`와 `검증/고의도_채널_KPI_및_다음실험_20260628.md`를 본다.
- `/answer-note`와 `/quick-answer`는 note source별 댓글 URL을 다르게 써야 한다. `note_content_travel` -> `n3f3af286cf6d`, `note_content_shinokubo` -> `n700b325ba824`, `note_content_homecook` -> `n08bad3dce2a9`, `note_content_homecook_ricebowl` -> `nbb21605544ca`.
- GitHub Pages, GitHub Issue, 저장소 파일은 운영/감사용으로 유지한다. 일본 소비자에게 "참기름을 사거나 응답하는 곳"처럼 앞세우지 않는다.
- note는 사용자가 이 프로젝트에 한해 자유 게시/수정/댓글을 허용했다. 2026-06-28T14:20+09:00 기준 외부 공개 글 관찰도 허용됐다. X, Threads, Konest, 다른 커뮤니티는 별도 계정/명시 허용 전 게시·댓글·DM을 하지 않는다.
- note 댓글 실험은 `검증/note_댓글_관찰_접촉_패킷_20260628.md`를 기준으로 한다. 댓글은 하루 3개 이하, 링크 없이, 글 맥락에 맞는 질문만 허용한다. 인앱 브라우저가 note 로그아웃 상태이거나 CDP 포트가 없으면 댓글을 게시한 것으로 기록하지 말고 `ready_not_posted`로 둔다. 후보 상태는 `scripts/check_note_comment_candidates.py --write`로 `experiments/note_comment_candidate_status.csv`에 재기록한다.
- note/Vercel/커뮤니티 등 소비자-facing 글을 새로 쓰거나 크게 고칠 때는 유사한 일본어 글을 먼저 수집한다. 참고할 것은 문장 복사가 아니라 글 형태, 감정 흐름, 문체, 구조, CTA 거리감이다. 게시 전에는 기존에 쓴 글과 새 초안을 다시 읽고 AI티가 나는지 적대적으로 검수해 필요하면 수정한다.
- 실제 검증 신호는 공개 답글 URL, Notion export, GitHub waitlist issue, 오프라인 인터뷰 기록처럼 원본이 남는 데이터만 센다.
- 공개 답글은 `scripts/record_public_social_response.py`로 기록한다. strong 판정을 위해 `--brand-store`, `--volume-price`, `--use-up-period`, `--substitute-comparison`, `--needed-proof`를 가능한 한 채운다.
- 오프라인 인터뷰는 `experiments/field_interview_log.csv`에 1명 1행으로 기록하고, 새 컬럼 `aroma_timing`에는 `冷奴に最後だけ`, `ナムルを作った日`, `韓国のりご飯に少し`처럼 향이 제일 좋았던 사용 장면을 적는다.
- 조회수, 좋아요, 스키, 공유는 채널 품질 지표로만 기록하고, 구매/수요 응답으로 세지 않는다.

## 현재 canonical 공개면

- Vercel landing: `https://korean-sesame-oil-mvp.vercel.app/`
- Vercel content MVP: `https://korean-sesame-oil-mvp.vercel.app/korea-trip-goma`
- Vercel Shin-Okubo content MVP: `https://korean-sesame-oil-mvp.vercel.app/shinokubo-goma`
- Vercel home-cooking content MVP: `https://korean-sesame-oil-mvp.vercel.app/homecook-goma`
- Vercel aroma-retention MVP: `https://korean-sesame-oil-mvp.vercel.app/aroma-loss-goma`
- Vercel shelf-choice MVP: `https://korean-sesame-oil-mvp.vercel.app/shelf-check`
- Vercel shelf-choice short URL: `https://korean-sesame-oil-mvp.vercel.app/shelf`
- Vercel aroma-retention offline QR page: `https://korean-sesame-oil-mvp.vercel.app/field-aroma`
- Vercel article: `https://korean-sesame-oil-mvp.vercel.app/note`
- Vercel answer memo: `https://korean-sesame-oil-mvp.vercel.app/share?src=note_kfood`
- Vercel note/mobile answer entry: `https://korean-sesame-oil-mvp.vercel.app/answer-note`
- Vercel structured quick answer: `https://korean-sesame-oil-mvp.vercel.app/quick-answer`
- Vercel offline page: `https://korean-sesame-oil-mvp.vercel.app/field`
- note post 1: `https://note.com/dreamy_viola8978/n/n77fa3f5a7fe9`
- note post 2 content: `https://note.com/dreamy_viola8978/n/n3f3af286cf6d`
- note post 3 Shin-Okubo: `https://note.com/dreamy_viola8978/n/n700b325ba824`
- note post 4 home-cooking: `https://note.com/dreamy_viola8978/n/n08bad3dce2a9`
- note post 5 rice-bowl/TKG: `https://note.com/dreamy_viola8978/n/nbb21605544ca`
- Primary form: `https://www.notion.so/forms/38c5da6ea39c8149beb3000c9ab0ea98`

## 갱신할 파일

- 현재 상태: `검증/검증_원장.md`
- 출처: `검증/출처_목록.md`
- 게시/배포: `검증/게시_배포_기록.md`
- 판단 변경: `검증/판단_로그.md`
- 데이터 상태: `검증/응답_데이터_상태.md`
- 원본 CSV 로그: `experiments/channel_posting_log.csv`, `experiments/live_validation_log.csv`

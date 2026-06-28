# 참기름 프로젝트 작업 원칙

## 먼저 읽을 파일

이 저장소에서 일본 한국식 방앗간 참기름 MVP 검증을 이어갈 때는 먼저 아래 순서로 읽는다.

1. `검증/AGENTS.md`
2. `검증/검증_원장.md`
3. `검증/게시_배포_기록.md`
4. `검증/응답_데이터_상태.md`
5. `experiments/validation_signal_summary.md`

최근 적대적 검증 루프는 `검증/적대적_검증_루프_20260627.md`와 `검증/내용_적대적_검증_20260627.md`에 있다. 기존 작업자는 이어가기 전에 이 파일들의 결론과 stale checklist 지적을 먼저 확인한다. `/answer-note`는 2026-06-27T22:56+09:00 기준 Vercel production 200 확인 완료 상태다.

제품 외 콘텐츠와 타겟 심리 검증은 `검증/제품외_콘텐츠_타겟밀집_검증법_20260627.md`와 `검증/욕구_문제_가설_20260627.md`를 함께 본다. 현재 방향은 `참기름을 살 사람`을 직접 찾기보다, 한국여행/신오쿠보/집밥 K-food/밥 한 그릇 맥락에서 최근 구매처, 향 불만, 대체재 전환 조건을 먼저 캐는 것이다.

소비자-facing 글을 새로 쓰거나 크게 고칠 때는 `검증/글쓰기_레퍼런스_수집_AI티_검수_원칙_20260628.md`를 먼저 본다. 유사한 일본어 글을 수집해 글 형태, 감정 흐름, 문체, 구조, CTA 거리감을 참고하고, 게시 전에는 기존 글과 새 초안을 다시 읽어 AI티가 나는지 적대적으로 검수한다.

note 댓글/외부 공개글 관찰로 응답 씨앗을 만들 때는 `검증/note_댓글_관찰_접촉_패킷_20260628.md`와 `검증/note_댓글_실행_큐_20260628.md`를 함께 본다. 2026-06-28T14:20+09:00 기준 사용자는 이 프로젝트에 한해 note 게시/수정/댓글을 Codex에게 허용했고, 외부 공개 글 관찰도 허용했다. 단, note 외부 채널의 실제 게시/댓글/DM은 별도 계정과 명시 허용 없이는 하지 않는다.

## 현재 운영 기준

- 소비자에게 공유할 기본 URL은 Vercel clean URL이다: `https://korean-sesame-oil-mvp.vercel.app/`
- 제품 외 콘텐츠형 검증 URL은 `https://korean-sesame-oil-mvp.vercel.app/korea-trip-goma`다.
- 신오쿠보/한국식품점 대체재 전환 검증 URL은 `https://korean-sesame-oil-mvp.vercel.app/shinokubo-goma`다.
- 집밥 한국요리/마지막 향 검증 URL은 `https://korean-sesame-oil-mvp.vercel.app/homecook-goma`다.
- 개봉 후 향 손실/큰 병 부담 검증 URL은 `https://korean-sesame-oil-mvp.vercel.app/aroma-loss-goma`다.
- 매대 앞 선택 피로/신선도 증거 검증 URL은 `https://korean-sesame-oil-mvp.vercel.app/shelf-check`이고, 짧은 공유 경로는 `https://korean-sesame-oil-mvp.vercel.app/shelf`다. `content_shelfcheck` 응답은 실제로 본 후보 상품, 용량·가격, 안 사는 이유, 제조일/압착/마지막 향 보존 같은 전환 증거가 있어야 강한 신호로 센다.
- 향 손실/큰 병 부담 오프라인 인터뷰 QR 페이지는 `https://korean-sesame-oil-mvp.vercel.app/field-aroma`다. QR 타겟은 `https://korean-sesame-oil-mvp.vercel.app/quick-answer?src=offline_aromaloss`이며, 실제 인터뷰 원본이 생기기 전에는 응답 데이터로 세지 않는다. 2026-06-28T13:55+09:00부터 이 경로는 `향이 가장 좋았던 요리/타이밍`과 `5g・110ml・しぼりたて 후보로 충분한지`도 묻는다.
- note/모바일 유입의 기본 응답 링크는 `https://korean-sesame-oil-mvp.vercel.app/answer-note`다. 이 링크는 모바일 응답 허브이며 note 댓글, Notion Form, 복사용 메모를 선택하게 한다. QR은 오프라인 종이/대면 인터뷰에서만 쓴다.
- 구조화 응답 생성기는 `https://korean-sesame-oil-mvp.vercel.app/quick-answer`다. Notion이 1줄 Submission만 받는 한, 최근 구매처 또는 현재 보고 있는 후보/요리/향 보존/전환 조건을 고르게 한 뒤 1줄 메모로 복사하게 한다.
- 2026-06-28T13:04+09:00 기준 `/quick-answer`, `/aroma-loss-goma`, `/shelf-check`, `/shelf`는 `1本を使い切る期間`과 `5g・110ml・しぼりたて候補で十分か`를 묻는다. 집계 요약도 `Use-up or aroma-retention burden signals`, `Existing-substitute gap signals`를 supporting metric으로 표시한다.
- 2026-06-28T12:13+09:00 기준 `scripts/summarize_validation_signals.py`는 `Strong problem-fit responses`와 `Highest problem-fit score`를 표시한다. 8개 기준 중 5개 이상인 응답만 strong으로 본다.
- 기존 대체재/가격 지도는 `research/07_existing_substitute_price_map_20260628.md`를 본다. Ottogi 110ml 506~518円, Kuki 600g 1,046円, 신오쿠보 Kim-san 계열 搾りたて 100~120ml 1,500円대와 비교해 남는 이유가 있어야 100ml 1,480円 가설을 강하게 본다.
- `/answer-note`와 `/quick-answer`의 note 댓글 버튼은 source별 게시물로 라우팅한다. `note_content_travel`은 note 2차, `note_content_shinokubo`는 note 3차, `note_content_homecook`은 note 4차, `note_content_homecook_ricebowl`은 note 5차로 보내야 한다.
- note 게시물은 5개다. 1차 제품/입하 안내형은 `https://note.com/dreamy_viola8978/n/n77fa3f5a7fe9`, 2차 여행/사용 콘텐츠형은 `https://note.com/dreamy_viola8978/n/n3f3af286cf6d`, 3차 신오쿠보/한국식품점 대체재 체크형은 `https://note.com/dreamy_viola8978/n/n700b325ba824`, 4차 홈쿡/마지막 향 체크형은 `https://note.com/dreamy_viola8978/n/n08bad3dce2a9`, 5차 한국김/TKG 밥 한 그릇 체크형은 `https://note.com/dreamy_viola8978/n/nbb21605544ca`다.
- 6차 후보인 개봉 후 향 손실/큰 병 부담 note 원고는 `mvp/note_aromaloss_posting_packet.md`에 `ready_not_published`로 준비돼 있다. 24h 재확인 전에는 live note 게시하지 않는다.
- 24h 이후 실행 게이트는 `mvp/post_24h_action_packet_20260628.md`와 `검증/고의도_채널_KPI_및_다음실험_20260628.md`를 본다. note 1~5 합산 views가 30 미만이고 응답 0이면 유통 실패로 보고 6차 note를 바로 게시하지 않는다.
- note dashboard snapshot은 `scripts/record_note_dashboard_snapshot.py`로 `experiments/note_dashboard_snapshots.csv`에 기록한다. 먼저 `--dry-run`으로 확인하고 실제 기록 후 재집계한다.
- note 공개 상태/댓글/スキ는 `scripts/check_note_public_api.py`로 확인한다. 이 스크립트는 조회수를 주지 않으므로 24h gate의 views는 대시보드 snapshot으로만 기록한다.
- 매대 앞 선택 피로/신선도 증거 보강은 `research/06_shelf_choice_freshness_proof_20260628.md`를 본다. 이 축은 소량병 자체보다 제조일, 압착, 차광/보관, 마지막 향 보존, 재구매 편의가 실제 전환 이유인지 묻는다.
- `참기름 팔기`를 더 구체적인 욕구/문제로 해석할 때는 `검증/참기름_팔기_욕구_세분화_20260628.md`와 `research/08_micro_jtbd_and_competing_solutions_20260628.md`를 먼저 본다. 최신 보정은 `사용량-향 보존 불일치`, `대체재 선택 피로`, `搾りたて 체험 욕구`, `신오쿠보 밖 재구매 불편`, `요리 마지막 향`, `선물/나눔`에 더해 `Kadoya 5g使い切りパック보다 100ml가 나은 이유`까지 묻는 것이다. `5g pack은 편하지만 여러 번 쓰는 한국요리에는 부족하다`, `Ottogi 110ml는 싸지만 제조일/향 신뢰가 약하다`, `신오쿠보 搾りたて는 좋지만 평소 재구매가 불편하다`처럼 대체재별로 남는 이유가 있는 응답만 강하게 본다.
- 2026-06-28T15:55+09:00 기준 새 핵심 검증축은 `한국식 방앗간 참기름을 炒め油가 아니라 仕上げの香味油로 이해할 수 있는가`다. 먼저 `검증/향미오일_포지셔닝_가설_20260628.md`를 보고, `/quick-answer`, `/aroma-loss-goma`, `/field-aroma`, 오프라인 PDF, note 댓글 실행 큐, 6차 note 후보가 이 질문을 앞에 두는지 확인한다. 실제 finishing 사용 장면, 기존 브랜드/용량·가격 비교, 제조일/搾った日/향 비교 증거, 조건부 가격 반응이 함께 있는 응답만 강하게 본다.
- GitHub Pages와 GitHub Issue Form은 검증 기록, 자동 집계, 내부 fallback으로만 본다. 일본 소비자-facing 구매/응답 화면으로 앞세우지 않는다.
- note 계정은 이 프로젝트에 한해 Codex가 자유롭게 게시/수정할 수 있다고 사용자가 허용했다. 단, note 외부 채널인 X, Threads, Konest 등은 별도 명시 허용 전 게시하지 않는다.
- note 댓글 실험은 `검증/note_댓글_관찰_접촉_패킷_20260628.md`와 `검증/note_댓글_실행_큐_20260628.md` 기준으로 하루 3개 이하, 링크 없이, 글 맥락에 맞는 질문만 남긴다. 2026-06-28T15:27+09:00 기준 실행 1순위는 Ottogi 110ml 대체재 후보, 2순위는 신오쿠보 구매 맥락 후보다. `scripts/check_note_comment_candidates.py --write`는 `experiments/note_comment_candidate_status.csv`에 후보 6개를 모두 `ready_not_posted`로 기록했다. 새 계정은 필요 없고, 필요한 것은 로그인된 note 조작 표면이다.
- 식품 결제, 예약금, 배송지, 전화번호, 이메일 등 개인정보 수집은 수입/표시/단가 gate 통과 전 하지 않는다.
- note/Vercel/커뮤니티 글은 레퍼런스 없이 바로 쓰지 않는다. 필요 시 기존 게시글과 원고 패킷을 다시 읽고, 너무 반듯한 기획서 말투, 광고 카피 느낌, 과한 검증 용어 반복, 구체 장면 부족, 반례 선택지 부재를 수정한다.
- 검증 완료는 실제 응답 데이터로만 판단한다. 조회수, 스키, 좋아요, 공유는 보조 신호이며 응답 수로 세지 않는다. 신오쿠보 검증에서는 `신오쿠보를 좋아한다`가 아니라 실제 구매처/브랜드/용량·가격/불만/전환 조건이 있는 응답만 강한 신호로 본다. 홈쿡 검증에서는 `韓国料理が好き`가 아니라 최근 만든 요리, 현재 참기름, 향 불만 또는 충분한 이유, 바꿀 조건이 있는 응답만 강한 신호로 본다. 밥친구/한국김/TKG 축은 `맛있어 보임`이 아니라 반복 사용 빈도와 참기름 단품 구매/재구매 조건이 있어야 강한 신호로 본다.
- 공개 답글은 `scripts/record_public_social_response.py`로 기록하며, strong 판정을 위해 브랜드/店名, 용량·가격, 1병 사용 기간, 기존 대체재 비교, 필요한 증거 컬럼을 가능한 한 채운다. 오프라인 응답은 `experiments/field_interview_log.csv`의 `aroma_timing`에도 마지막으로 향이 좋았던 사용 장면을 남긴다.

## 기록 규칙

- 외부 게시, 배포, 폼 변경, 브라우저 계정 작업을 하면 `검증/게시_배포_기록.md`와 `experiments/live_validation_log.csv`에 함께 남긴다.
- 판단이 바뀌면 `검증/검증_원장.md`의 현재 상태와 `검증/판단_로그.md`를 갱신한다.
- 새 응답은 원본 URL 또는 원본 export 파일 경로를 남긴 뒤 `experiments/public_social_responses.csv`, `experiments/notion_submissions_export_template.csv`, `experiments/field_interview_log.csv` 중 맞는 파일에 기록한다.
- 한국어/일본어 파일은 UTF-8로 저장한다.

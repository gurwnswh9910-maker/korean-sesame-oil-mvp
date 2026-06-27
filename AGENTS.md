# 참기름 프로젝트 작업 원칙

## 먼저 읽을 파일

이 저장소에서 일본 한국식 방앗간 참기름 MVP 검증을 이어갈 때는 먼저 아래 순서로 읽는다.

1. `검증/AGENTS.md`
2. `검증/검증_원장.md`
3. `검증/게시_배포_기록.md`
4. `검증/응답_데이터_상태.md`
5. `experiments/validation_signal_summary.md`

최근 적대적 검증 루프는 `검증/적대적_검증_루프_20260627.md`와 `검증/내용_적대적_검증_20260627.md`에 있다. 기존 작업자는 이어가기 전에 이 파일들의 결론과 stale checklist 지적을 먼저 확인한다. `/answer-note`는 2026-06-27T22:56+09:00 기준 Vercel production 200 확인 완료 상태다.

제품 외 콘텐츠와 타겟 심리 검증은 `검증/제품외_콘텐츠_타겟밀집_검증법_20260627.md`와 `검증/욕구_문제_가설_20260627.md`를 함께 본다. 현재 방향은 `참기름을 살 사람`을 직접 찾기보다, 한국여행/신오쿠보/집밥 K-food 맥락에서 최근 구매처, 향 불만, 대체재 전환 조건을 먼저 캐는 것이다.

## 현재 운영 기준

- 소비자에게 공유할 기본 URL은 Vercel clean URL이다: `https://korean-sesame-oil-mvp.vercel.app/`
- 제품 외 콘텐츠형 검증 URL은 `https://korean-sesame-oil-mvp.vercel.app/korea-trip-goma`다.
- note/모바일 유입의 기본 응답 링크는 `https://korean-sesame-oil-mvp.vercel.app/answer-note`다. 이 링크는 모바일 응답 허브이며 note 댓글, Notion Form, 복사용 메모를 선택하게 한다. QR은 오프라인 종이/대면 인터뷰에서만 쓴다.
- GitHub Pages와 GitHub Issue Form은 검증 기록, 자동 집계, 내부 fallback으로만 본다. 일본 소비자-facing 구매/응답 화면으로 앞세우지 않는다.
- note 계정은 이 프로젝트에 한해 Codex가 자유롭게 게시/수정할 수 있다고 사용자가 허용했다. 단, note 외부 채널인 X, Threads, Konest 등은 별도 명시 허용 전 게시하지 않는다.
- 식품 결제, 예약금, 배송지, 전화번호, 이메일 등 개인정보 수집은 수입/표시/단가 gate 통과 전 하지 않는다.
- 검증 완료는 실제 응답 데이터로만 판단한다. 조회수, 스키, 좋아요, 공유는 보조 신호이며 응답 수로 세지 않는다.

## 기록 규칙

- 외부 게시, 배포, 폼 변경, 브라우저 계정 작업을 하면 `검증/게시_배포_기록.md`와 `experiments/live_validation_log.csv`에 함께 남긴다.
- 판단이 바뀌면 `검증/검증_원장.md`의 현재 상태와 `검증/판단_로그.md`를 갱신한다.
- 새 응답은 원본 URL 또는 원본 export 파일 경로를 남긴 뒤 `experiments/public_social_responses.csv`, `experiments/notion_submissions_export_template.csv`, `experiments/field_interview_log.csv` 중 맞는 파일에 기록한다.
- 한국어/일본어 파일은 UTF-8로 저장한다.

# 검증 폴더 작업 원칙

## 역할

이 폴더는 참기름 MVP의 감사 가능한 절차기억이다. 다음 세션이 "어디까지 했고, 왜 그렇게 판단했고, 어떤 URL과 데이터로 확인했는지"를 재검증할 수 있어야 한다.

## 최근 적대적 검증 포인터

- 2026-06-27T22:56+09:00 적대적 검증 루프: `검증/적대적_검증_루프_20260627.md`
- 2026-06-27T22:56+09:00 내용 적대적 검증: `검증/내용_적대적_검증_20260627.md`
- `/answer-note`는 2026-06-27T22:56+09:00 기준 Vercel production에서 200, no redirect, mobile answer hub로 확인됐다.
- 제품 외 콘텐츠/타겟 밀집 검증: `검증/제품외_콘텐츠_타겟밀집_검증법_20260627.md`
- 참기름 판매 목표 아래의 욕구/문제 가설: `검증/욕구_문제_가설_20260627.md`

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
- 개봉 후 향 손실/큰 병 부담 검증은 `https://korean-sesame-oil-mvp.vercel.app/aroma-loss-goma`와 source `content_aromaloss`를 사용한다. note 원고는 `mvp/note_aromaloss_posting_packet.md`에 준비됐지만 24h 재확인 전 live note 게시하지 않는다.
- note/모바일 유입에서는 QR을 CTA로 쓰지 않는다. `https://korean-sesame-oil-mvp.vercel.app/answer-note` 모바일 응답 허브, note 댓글 템플릿, 탭 가능한 `/share` 링크를 우선한다.
- 구조화 응답이 필요하면 `https://korean-sesame-oil-mvp.vercel.app/quick-answer`를 사용한다. 이 페이지는 다문항 선택을 Notion 1줄 `Submission`으로 변환하는 보조 MVP이며, 응답 데이터 자체는 Notion/export/note 댓글/공개 답글 원본으로만 센다.
- `/answer-note`와 `/quick-answer`는 note source별 댓글 URL을 다르게 써야 한다. `note_content_travel` -> `n3f3af286cf6d`, `note_content_shinokubo` -> `n700b325ba824`, `note_content_homecook` -> `n08bad3dce2a9`, `note_content_homecook_ricebowl` -> `nbb21605544ca`.
- GitHub Pages, GitHub Issue, 저장소 파일은 운영/감사용으로 유지한다. 일본 소비자에게 "참기름을 사거나 응답하는 곳"처럼 앞세우지 않는다.
- note는 사용자가 이 프로젝트에 한해 자유 게시를 허용했다. X, Threads, Konest, 다른 커뮤니티는 별도 허용 전 게시하지 않는다.
- 실제 검증 신호는 공개 답글 URL, Notion export, GitHub waitlist issue, 오프라인 인터뷰 기록처럼 원본이 남는 데이터만 센다.
- 조회수, 좋아요, 스키, 공유는 채널 품질 지표로만 기록하고, 구매/수요 응답으로 세지 않는다.

## 현재 canonical 공개면

- Vercel landing: `https://korean-sesame-oil-mvp.vercel.app/`
- Vercel content MVP: `https://korean-sesame-oil-mvp.vercel.app/korea-trip-goma`
- Vercel Shin-Okubo content MVP: `https://korean-sesame-oil-mvp.vercel.app/shinokubo-goma`
- Vercel home-cooking content MVP: `https://korean-sesame-oil-mvp.vercel.app/homecook-goma`
- Vercel aroma-retention MVP: `https://korean-sesame-oil-mvp.vercel.app/aroma-loss-goma`
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

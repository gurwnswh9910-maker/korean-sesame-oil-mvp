# 검증 폴더 작업 원칙

## 역할

이 폴더는 참기름 MVP의 감사 가능한 절차기억이다. 다음 세션이 "어디까지 했고, 왜 그렇게 판단했고, 어떤 URL과 데이터로 확인했는지"를 재검증할 수 있어야 한다.

## 최근 적대적 검증 포인터

- 2026-06-27T22:39+09:00 적대적 검증 루프: `검증/적대적_검증_루프_20260627.md`
- 2026-06-27T22:50+09:00 내용 적대적 검증: `검증/내용_적대적_검증_20260627.md`
- 주의: 로컬에는 `/answer-note` 모바일 허브 전환 변경이 있으나, 2026-06-27T22:45+09:00 live 확인 기준 배포 URL은 아직 Notion Form redirect였다. 다음 작업자는 배포 반영 여부를 먼저 확인한다.

## 반드시 지킬 것

- 숨은 사고과정 원문을 적지 않는다. 대신 재검증 가능한 판단 근거, 출처, 관찰값, 명령, URL, 파일 경로를 적는다.
- `검증/검증_원장.md`는 현재 truth snapshot이다. 오래된 실험 로그와 다르면 원장을 우선하되, 원장도 원자료 링크로 검증한다.
- 외부 게시나 계정 작업은 게시 URL, 계정/채널, 시각, 권한 근거, 원문 파일, 설정값, 다음 측정 시각을 남긴다.
- 소비자-facing 링크는 기본적으로 Vercel clean URL을 사용한다.
- note/모바일 유입에서는 QR을 CTA로 쓰지 않는다. `https://korean-sesame-oil-mvp.vercel.app/answer-note`는 live/로컬 반영 상태를 확인한 뒤 쓰고, note 댓글 템플릿과 탭 가능한 `/share` 링크를 우선한다.
- GitHub Pages, GitHub Issue, 저장소 파일은 운영/감사용으로 유지한다. 일본 소비자에게 "참기름을 사거나 응답하는 곳"처럼 앞세우지 않는다.
- note는 사용자가 이 프로젝트에 한해 자유 게시를 허용했다. X, Threads, Konest, 다른 커뮤니티는 별도 허용 전 게시하지 않는다.
- 실제 검증 신호는 공개 답글 URL, Notion export, GitHub waitlist issue, 오프라인 인터뷰 기록처럼 원본이 남는 데이터만 센다.
- 조회수, 좋아요, 스키, 공유는 채널 품질 지표로만 기록하고, 구매/수요 응답으로 세지 않는다.

## 현재 canonical 공개면

- Vercel landing: `https://korean-sesame-oil-mvp.vercel.app/`
- Vercel article: `https://korean-sesame-oil-mvp.vercel.app/note`
- Vercel answer memo: `https://korean-sesame-oil-mvp.vercel.app/share?src=note_kfood`
- Vercel note/mobile answer entry: `https://korean-sesame-oil-mvp.vercel.app/answer-note`
- Vercel offline page: `https://korean-sesame-oil-mvp.vercel.app/field`
- note post: `https://note.com/dreamy_viola8978/n/n77fa3f5a7fe9`
- Primary form: `https://www.notion.so/forms/38c5da6ea39c8149beb3000c9ab0ea98`

## 갱신할 파일

- 현재 상태: `검증/검증_원장.md`
- 출처: `검증/출처_목록.md`
- 게시/배포: `검증/게시_배포_기록.md`
- 판단 변경: `검증/판단_로그.md`
- 데이터 상태: `검증/응답_데이터_상태.md`
- 원본 CSV 로그: `experiments/channel_posting_log.csv`, `experiments/live_validation_log.csv`

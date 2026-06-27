# 일본 한국식 방앗간 참기름 MVP 검증

이 저장소는 일본에서 한국식 방앗간 참기름이 팔릴지 검증하기 위한 1차 리서치, 핵심가설, MVP 랜딩, 게시 문안, 측정 템플릿을 모은 작업 폴더다.

## 결론

1차 결론은 `조건부 진행`이다. 일본 참기름 시장은 이미 크고 성장 중이며, 일본 내 K-food/한국여행 경험에서 "갓 짠 한국 참기름의 향"이라는 구체적 차별 신호가 있다. 다만 실제 판매 전에는 일본 식품 수입신고, 일본어 라벨, 원재료/알레르겐/원산지/보존 표시, 신선도 물류를 먼저 해결해야 한다.

## 핵심 산출물

- `research/01_research_brief.md`: 1차 리서치와 2차 핵심가설
- `research/hypothesis_scorecard.csv`: 가설 점수표
- `mvp/index.html`: 일본어 MVP 랜딩 페이지 초안
- `mvp/posting_copy.md`: 일본어 게시/아웃리치 문안
- `mvp/outreach_targets.md`: 1차 수동 게시 채널
- `mvp/validation_plan.md`: 2주 검증 계획과 KPI
- Notion Form: 로그인 마찰을 낮춘 1차 입하 안내/검증 폼
- `experiments/measurement_sheet_template.csv`: 실험 기록 템플릿
- `experiments/notion_form_status.md`: Notion Form 공개 설정과 한계
- `experiments/validation_tracker_issue_body.md`: 공개 GitHub 검증 트래커 본문
- `experiments/waitlist_responses.csv`: GitHub Issue Form 응답 자동 집계 CSV
- `experiments/waitlist_summary.md`: 응답 요약 자동 집계

## 공개 MVP

- Landing: https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/
- Primary validation form: https://www.notion.so/forms/38c5da6ea39c81bb879b000c55b872eb
- Public GitHub fallback: https://github.com/gurwnswh9910-maker/korean-sesame-oil-mvp/issues/new?template=waitlist.yml
- Validation tracker: https://github.com/gurwnswh9910-maker/korean-sesame-oil-mvp/issues/1

Notion Form은 일반 소비자용 1차 CTA다. 이메일, 주소, 전화번호 같은 개인정보는 받지 않는다.
GitHub Issue Form은 로그인 가능한 사용자의 공개 검증 신호만 받는 fallback으로 유지한다.

응답 집계는 `.github/workflows/summarize-waitlist.yml`가 `waitlist` 이슈를 읽어 자동 갱신한다.
채널별 게시에는 `?src=x_threads_travel`처럼 source 파라미터를 붙인다. 랜딩은 Notion Form URL에 source를 넘기고, GitHub fallback은 Issue 제목의 `[src:...]`에 넣어 집계한다.

## 실행 원칙

- MVP는 결제 의향이 아니라 행동으로 검증한다.
- 첫 검증은 광고보다 수동 게시/수동 대화로 한다.
- 판매 확정 표현은 규제 확인 전 사용하지 않는다.
- 공개 게시 전에는 CTA 폼 URL, 연락처, 배송 가능성, 가격/배송비 조건을 확정한다.

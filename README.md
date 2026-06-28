# 일본 한국식 방앗간 참기름 MVP 검증

이 저장소는 일본에서 한국식 방앗간 참기름이 팔릴지 검증하기 위한 1차 리서치, 핵심가설, MVP 랜딩, 게시 문안, 측정 템플릿을 모은 작업 폴더다.

## 결론

1차 결론은 `조건부 진행`이다. 일본 참기름 시장은 이미 크고 성장 중이며, 일본 내 K-food/한국여행 경험에서 "갓 짠 한국 참기름의 향"이라는 구체적 차별 신호가 있다. 다만 실제 판매 전에는 일본 식품 수입신고, 일본어 라벨, 원재료/알레르겐/원산지/보존 표시, 신선도 물류를 먼저 해결해야 한다.

## 핵심 산출물

- `research/01_research_brief.md`: 1차 리서치와 2차 핵심가설
- `research/02_import_label_unit_economics_gate.md`: 일본 수입·표시·원가 gate
- `research/03_live_signal_update_20260627.md`: 현재 웹 신호와 가설 보정
- `research/04_public_discovery_and_benchmark_20260627.md`: MVP 응답 발견 여부와 주변 가격/대체재 벤치마크
- `research/05_aroma_retention_review_language_20260628.md`: 개봉 후 향 손실/큰 병 부담 언어 검증
- `research/06_shelf_choice_freshness_proof_20260628.md`: 매대 앞 선택 피로/신선도 증거 검증
- `research/07_existing_substitute_price_map_20260628.md`: Kadoya/Kuki/Ottogi/Kim-san 기존 대체재와 가격 기준 지도
- `검증/참기름_팔기_욕구_세분화_20260628.md`: `참기름 팔기`를 사용량-향 보존, 대체재 선택 피로, 搾りたて 체험, 재구매 불편 등으로 세분화한 최신 KB
- `research/hypothesis_scorecard.csv`: 가설 점수표
- `mvp/index.html`: 일본어 MVP 랜딩 페이지 초안
- `mvp/korea-trip-goma.html`: 제품 외 콘텐츠형 타겟 밀집 검증 페이지
- `mvp/share_note.html`: 일본어 커뮤니티/노트 공유용 설명 페이지
- `mvp/note_article.html`: note/Vercel용 공개 설명 기사
- `mvp/field_interview.html`: 오프라인 QR 인터뷰용 페이지
- `mvp/field_interview_script.md`: 오프라인 10명 인터뷰 스크립트
- `mvp/runbook_first_traffic.md`: 첫 외부 트래픽 실행 런북
- `mvp/channel_rules_and_permission_gate.md`: 외부 게시 채널 규칙과 계정 권한 게이트
- `mvp/note_article_draft.md`: note 첫 게시용 일본어 원고
- `output/pdf/field_interview_flyer.pdf`: 인쇄용 A4 QR 플라이어
- `mvp/posting_copy.md`: 일본어 게시/아웃리치 문안
- `mvp/outreach_targets.md`: 1차 수동 게시 채널
- `mvp/validation_plan.md`: 2주 검증 계획과 KPI
- Notion Form: 로그인 마찰을 낮춘 1차 입하 안내/검증 폼
- `experiments/channel_posting_log.csv`: 채널별 게시 URL과 반응 기록판
- `experiments/completion_audit.md`: goal 완료 조건별 증거 감사
- `experiments/field_interview_log.csv`: 오프라인 10명 인터뷰 기록표
- `experiments/measurement_sheet_template.csv`: 실험 기록 템플릿
- `experiments/unit_economics_template.csv`: 100ml/3병 세트 단가 gate 템플릿
- `experiments/notion_form_status.md`: Notion Form 공개 설정과 한계
- `experiments/validation_tracker_issue_body.md`: 공개 GitHub 검증 트래커 본문
- `experiments/waitlist_responses.csv`: GitHub Issue Form 응답 자동 집계 CSV
- `experiments/waitlist_summary.md`: 응답 요약 자동 집계
- `experiments/notion_submissions_export_template.csv`: Notion 1줄 응답 export용 템플릿
- `experiments/public_social_responses.csv`: X 등 공개 응답 URL 수동 수집 CSV
- `experiments/public_social_responses_template.csv`: X 등 공개 응답 URL 수동 수집 템플릿
- `experiments/public_discovery_log.csv`: 직접 MVP 응답 검색과 주변 시장 신호 발견 로그
- `experiments/validation_signal_summary.md`: Notion/GitHub/오프라인 신호 통합 판정 요약
- `experiments/validation_signal_summary.json`: 통합 판정 요약의 기계 판독용 JSON
- `scripts/record_public_social_response.py`: X/Threads 공개 응답 URL을 중복 없이 CSV에 기록하는 helper
- `scripts/summarize_validation_signals.py`: 검증 신호 통합 집계 스크립트

## 공개 MVP

- Landing: https://korean-sesame-oil-mvp.vercel.app/
- Content MVP: https://korean-sesame-oil-mvp.vercel.app/korea-trip-goma
- Shin-Okubo substitute check: https://korean-sesame-oil-mvp.vercel.app/shinokubo-goma
- Home-cooking last aroma check: https://korean-sesame-oil-mvp.vercel.app/homecook-goma
- Aroma-loss check: https://korean-sesame-oil-mvp.vercel.app/aroma-loss-goma
- Shelf-choice check: https://korean-sesame-oil-mvp.vercel.app/shelf-check
- Shelf-choice short URL: https://korean-sesame-oil-mvp.vercel.app/shelf
- Share note: https://korean-sesame-oil-mvp.vercel.app/share
- Short answer link for note/mobile: https://korean-sesame-oil-mvp.vercel.app/answer-note
- Structured quick answer: https://korean-sesame-oil-mvp.vercel.app/quick-answer
- Public article: https://korean-sesame-oil-mvp.vercel.app/note
- Field interview QR: https://korean-sesame-oil-mvp.vercel.app/field
- Aroma-loss field QR: https://korean-sesame-oil-mvp.vercel.app/field-aroma
- Printable flyer PDF: https://korean-sesame-oil-mvp.vercel.app/field-flyer
- note posts: 1차 https://note.com/dreamy_viola8978/n/n77fa3f5a7fe9 / 2차 https://note.com/dreamy_viola8978/n/n3f3af286cf6d / 3차 https://note.com/dreamy_viola8978/n/n700b325ba824 / 4차 https://note.com/dreamy_viola8978/n/n08bad3dce2a9 / 5차 https://note.com/dreamy_viola8978/n/nbb21605544ca
- Primary validation form: https://www.notion.so/forms/38c5da6ea39c8149beb3000c9ab0ea98
- Public GitHub fallback: https://github.com/gurwnswh9910-maker/korean-sesame-oil-mvp/issues/new?template=waitlist.yml
- Validation tracker: https://github.com/gurwnswh9910-maker/korean-sesame-oil-mvp/issues/1

Notion Form은 일반 소비자용 1차 CTA다. 현재 도구로 만든 폼은 1줄 응답 방식이며, 이메일, 주소, 전화번호 같은 개인정보는 받지 않는다.
GitHub Issue Form은 로그인 가능한 사용자의 공개 검증 신호만 받는 내부 fallback으로 유지한다. 소비자에게 공유하는 기본 URL은 Vercel clean URL이다.

응답 집계는 `.github/workflows/summarize-waitlist.yml`가 `waitlist` 이슈를 읽고, `scripts/summarize_validation_signals.py`로 Notion export, GitHub fallback, X 공개 응답 URL 수동 수집, 오프라인 인터뷰를 합쳐 자동 갱신한다. 워크플로는 매일 실행되고, 응답 입력 CSV나 채널 로그가 push될 때도 다시 실행된다. 통합 요약은 임계값 충족 여부와 함께 `collect_more_evidence`, `candidate_go_small_batch`, `candidate_pivot_price_or_bundle`, `candidate_stop_or_resegment` 같은 Go/Pivot/Stop 추천을 낸다.
채널별 게시에는 `?src=x_threads_travel`처럼 source 파라미터를 붙인다. 랜딩은 Notion Form URL에 source를 넘기고, GitHub fallback은 Issue 제목의 `[src:...]`에 넣어 집계한다.

공개 X/Threads 답글 URL은 아래처럼 기록한다.

```powershell
$env:PYTHONUTF8='1'; $env:PYTHONIOENCODING='utf-8'; python .\scripts\record_public_social_response.py --platform X --source x_threads_travel --url "https://x.com/{user}/status/{id}" --text "{공개 답글 요약}" --recent-purchase "{최근 구매/탐색}" --aroma-memory "{향 기억}" --single-price "{100ml 가격 반응}" --sample-signal "{샘플/구매 신호}"
```

## 실행 원칙

- MVP는 결제 의향이 아니라 행동으로 검증한다.
- 첫 검증은 광고보다 수동 게시/수동 대화로 한다.
- 판매 확정 표현은 규제 확인 전 사용하지 않는다.
- 공개 게시 전에는 CTA 폼 URL, 연락처, 배송 가능성, 가격/배송비 조건을 확정한다.

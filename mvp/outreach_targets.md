# 1차 수동 게시 채널

작성일: 2026-06-27

## 목적

GitHub Pages로 공개한 MVP에 실제 일본어 트래픽을 넣고, Notion Form 또는 댓글/DM으로 행동 신호를 모은다.

Landing: https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/
Share note: https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/share_note.html
Public article: https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/note_article.html
Primary Form: https://www.notion.so/forms/38c5da6ea39c8149beb3000c9ab0ea98

채널별 링크는 `?src=`를 붙인다. 랜딩은 1줄 응답 메모의 `流入元` 값을 source로 바꾸고, Notion Form URL에도 source를 넘긴다. GitHub fallback은 이 값을 Issue 제목의 `[src:...]`에 넣어 집계한다.

## 우선순위

2026-06-27 현재 웹 신호 업데이트(`../research/03_live_signal_update_20260627.md`) 기준, 신오쿠보/한국식품점은 단순 유입 채널이 아니라 기존 대체재 인지와 가격 비교를 확인하는 벤치마크 채널로도 본다.

| 순위 | 채널 | 이유 | 게시 문안 |
|---:|---|---|---|
| 1 | GitHub Pages article / note `#韓国料理` 태그 | note 계정 게시 전에도 `note_article.html`은 즉시 공유 가능하다. note 계정이 준비되면 같은 원고를 자기 글로 발행하고 조회/댓글/스키를 확인한다. | `note_article.html`, `note_article_draft.md`, `?src=article_github` / `?src=note_kfood` |
| 2 | X/Threads 해시태그 `#韓国料理`, `#韓国旅行`, `#新大久保`, `#韓国購入品`, `#ごま油`, `#おうち韓国` | 한국여행/신오쿠보/홈쿡 맥락을 가장 빠르게 수동 테스트할 수 있다. 반복 게시 없이 1~2개만 수동 게시한다. | `posting_copy.md` A 또는 B, `?src=x_threads_travel` / `?src=x_threads_homecook` |
| 3 | Konest 커뮤니티 | 한국여행 정보 탐색자가 있어 "한국에서 먹은 향을 일본에서 다시 사고 싶은가"를 묻기 좋다. 다만 규칙 확인/운영자 문의 전에는 보류한다. | `posting_copy.md` A, `?src=konest` |
| 4 | Tunagate 한국요리/신오쿠보 모임 | 이용규약상 영업, 권유, 선전 목적 이용과 외부 서비스 유도가 금지되어 플랫폼 내 게시에는 맞지 않는다. | 게시 제외. 오프라인에서 자연스럽게 대화가 생긴 경우에만 질문 |
| 5 | 신오쿠보 식재료점/한국식품점 수동 인터뷰 | 구매 직전/직후 고객에게 현재 대체재, 가격 저항, 제조일/향 보존 신뢰를 물을 수 있다. 온라인보다 샘플 판매 단가 검증에 강하다. | 인터뷰 질문 7개, `?src=offline_shinokubo` |

## 24시간 실행 루프

1. 첫날에는 note 1개만 게시한다. 24시간 반응이 0이면 X/Threads 1개를 추가한다.
2. 게시 URL을 `experiments/channel_posting_log.csv`에 기록한다.
3. 댓글/DM은 바로 판매하지 말고 최근 구매 행동을 묻는다.
4. 긍정 댓글은 Notion Form으로 이동시키고, 1줄 응답 메모를 붙여넣도록 안내한다. 더 긴 대화는 댓글/DM에서 최근 구매 행동을 묻는다.
5. Notion Form 제출이 막히거나 source 추적이 약하면 Google Forms/Tally로 CTA를 교체한다.
6. 외부 계정 게시 전에는 `channel_rules_and_permission_gate.md`의 권한 확인을 통과한다.

## 주의

- 커뮤니티 규칙상 판매/홍보 금지인 곳에는 게시하지 않는다.
- "정식 판매", "즉시 배송", "효능" 표현을 쓰지 않는다.
- 개인 연락처는 공개 댓글/Issue로 받지 않는다.
- 실제 결제는 일본 수입/표시 요건 확인 전에는 받지 않는다.

## 참고한 공개 신호

- note `#韓国料理` 태그: https://note.com/hashtag/%E9%9F%93%E5%9B%BD%E6%96%99%E7%90%86
- Tunagate 한국요리/신오쿠보 모임 검색 결과: https://tunagate.com/eatings/all/497
- Konest 커뮤니티 한국여행/맛집 게시판 예시: https://comm.konest.com/topic/558065
- Threads 한국 구매품/참기름 게시 신호: https://www.threads.com/@kankoku.gohan/post/DIqy_2dyVwy
- 현재 외부 신호 업데이트: `../research/03_live_signal_update_20260627.md`
- 채널 규칙/권한 게이트: `channel_rules_and_permission_gate.md`

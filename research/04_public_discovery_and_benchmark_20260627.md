# 공개 발견/벤치마크 업데이트

작성일: 2026-06-27

## 목적

MVP 공개 후 현재 웹에서 우리 MVP 자체의 응답/공유가 발견되는지 확인하고, 동시에 한국식 갓 짠 참기름의 일본어 주변 신호를 가격/대체재 벤치마크로 분리한다.

## 직접 MVP 응답 발견 여부

2026-06-27 기준 아래 검색어로 확인했다.

- `"韓国ごま油検証"`
- `"gurwnswh9910-maker.github.io/korean-sesame-oil-mvp"`
- `"韓国旅行で覚えた" "しぼりたてごま油"`
- `"韓国式しぼりたてごま油" "入荷前"`

결과: 우리 MVP에 대한 실제 공개 응답, 공유, 댓글 URL은 발견되지 않았다. 따라서 이 검색은 `0 external responses` 판정을 바꾸지 않는다.

## 새로 확인한 주변 신호

| 신호 | 내용 | MVP 해석 |
|---|---|---|
| 한국 여행 구매 행동 | 일본어 여행/생활 콘텐츠에서 서울 중부시장/제유소에서 참기름을 사는 경험과 강한 향, 선물/소분 수요가 반복적으로 보인다. | H1 `한국 여행에서 기억한 향 재현`은 계속 유효하다. |
| 일본 내 대체재 | 오사카 코리아타운/이쿠노 쪽에서 갓 짠 참기름을 현지에서 살 수 있다는 콘텐츠가 보인다. | "일본에 없다"가 아니라 기존 대체재와 비교한 전환 이유를 물어야 한다. |
| 가격 기준 | 여행지 구매품은 병당 수천 엔대, 일본 내 대체재는 더 낮은 가격대 신호도 있다. | 100ml 1,480엔은 무조건 비싸다/싸다로 판단하지 말고, 용량/제조일/향 보존/재구매 편의와 묶어 검증한다. |
| 콘텐츠 채널 | note, Ameblo, LEE, Konest, Threads류의 한국여행/한국요리 콘텐츠에서 관련 이야기가 발견된다. | 첫 유입은 넓은 식품 광고보다 한국여행 회상, 코리아타운 구매, K-food 홈쿡 문맥이 맞다. |

## 가설 보정

### H1 유지

`韓国旅行で覚えた香りを家で再現したいか`는 여전히 가장 강한 메시지다. 여행 콘텐츠의 실제 구매/선물 이야기는 설문 찬성보다 강한 주변 행동 신호다.

### H4 강화

일본 내에서 이미 살 수 있는 한국식 또는 갓 짠 참기름이 보이므로, MVP의 진짜 질문은 아래처럼 바뀐다.

- 기존 제품보다 제조일/향 보존이 선명하면 바꿀 이유가 생기는가
- 100ml처럼 빨리 쓰는 소량이 더 좋은가
- 한 번 산 뒤 다시 사기 쉬운 온라인/정기 입하가 가치인가
- 오사카/신오쿠보/한국식품점에서 직접 사는 것보다 배송/예약이 나은 순간이 있는가

## 다음 수집 루프

1. 직접 MVP 응답은 `experiments/public_social_responses.csv`, `experiments/waitlist_responses.csv`, Notion export, 오프라인 인터뷰만 증거로 센다.
2. 주변 시장 신호는 `experiments/public_discovery_log.csv`에 별도로 기록한다.
3. 외부 계정 댓글/DM/게시를 할 때는 게시 권한과 계정 리스크를 먼저 확인한다. 제3자 글에 답글을 다는 것은 별도 확인 전에는 하지 않는다.
4. 오프라인 질문에는 신오쿠보뿐 아니라 오사카 코리아타운/이쿠노, 서울 중부시장/여행 구매 경험도 포함한다.

## 참고 소스

- LEE, Korea travel sesame oil gift signal: https://lee.hpplus.jp/100nintai/3150695/
- Ameblo, Seoul Central Market sesame oil purchase signal: https://ameblo.jp/himekuma39/entry-12904791684.html
- Ameblo, Osaka Korea Town freshly pressed sesame oil benchmark: https://ameblo.jp/1208miyako/entry-12906656092.html
- note, Korean sesame oil trend/story signal: https://note.com/yugimama/n/n4466b7278d59
- Konest, Korean sesame oil news surface: https://www.konest.com/contents/news_detail.html?id=57722

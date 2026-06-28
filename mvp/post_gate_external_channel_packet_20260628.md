# post-gate 외부 채널 실행 패킷

작성 시각: 2026-06-28T17:27+09:00
상태: `ready_for_post_21_50_gate`, note 외부 실제 게시/댓글은 별도 허용 전 금지

## 목적

2026-06-28T21:50+09:00 note dashboard gate 이후 `views < 30, 응답 0`으로 유통 실패가 확인될 때, 6차 note를 추가로 올리는 대신 어떤 채널을 쓸지 즉시 결정하기 위한 패킷이다.

현재 핵심 가설은 `한국식 방앗간 참기름을 仕上げの香味油로 이해하고, 5g・110ml・しぼりたて 대체재와 비교해 남는 이유가 있는가`다. 따라서 외부 채널에서도 `100ml 1,480円 살래요?`보다 아래 질문을 먼저 던진다.

```text
ごま油を炒め油ではなく、料理の最後に香りを足す油として使うことがありますか？
```

## 게이트별 실행

| 21:50 결과 | 해석 | 실행 |
|---|---|---|
| note 1~5 views < 30, 응답 0 | 유통 실패 | 6차 note 보류. 아래 외부 채널 중 1개만 선택한다. |
| note 1~5 views >= 30, 응답 0 | 문제 언어/CTA 실패 | `mvp/note_aromaloss_posting_packet.md` 게시 후보. |
| 댓글/폼 1건 이상 | 질적 탐색 | 외부 채널 확장보다 응답 원본을 strong 기준으로 판정하고 추가 질문한다. |

## 채널 후보

| 우선순위 | 채널 | 왜 고의도인가 | 실행 권한/계정 | 권장 실행 |
|---:|---|---|---|---|
| 1 | X/Threads 공개 질문 | 링크 없이도 공개 답글을 받을 수 있고, note보다 발견성이 높을 수 있다. | 사용자 명시 허용 필요. 계정은 사용자 기존 계정 또는 새 프로젝트 계정 중 선택 필요. | `mvp/x_threads_posting_packet.md`의 URL 없는 1순위 문안 1회만 게시. |
| 2 | 오프라인 신오쿠보/한국식품점 인터뷰 | 실제 대체재를 보는 사람에게 가격/브랜드/사용량을 바로 물을 수 있다. | 물리 실행자 필요. 계정 불필요. | `mvp/field_aroma_interview_script.md`, `/field-aroma`, `/quick-answer?src=offline_aromaloss` 사용. |
| 3 | Konest 한국여행 커뮤니티/리뷰 맥락 | 한국 시장/제유소/搾りたてごま油 후기와 배송/액체 반입 질문이 이미 많다. | 별도 계정과 커뮤니티 규칙 확인 필요. 홍보성 게시 금지. | 즉시 게시 금지. 규칙 확인 또는 운영자 문의 후, 링크 없는 여행 경험 질문만 검토. |
| 4 | Instagram/Lemon8/Threads 신오쿠보 리뷰 맥락 | Kim-san 계열처럼 搾りたて/시식/소프트크림/한국김 콘텐츠가 시각적으로 퍼진다. | 계정 필요. 이미지/영상 자산 없으면 약함. 댓글 홍보 금지. | 관찰/레퍼런스 우선. 게시하려면 실제 제품/현장 이미지 확보 뒤 별도 패킷. |
| 5 | Cookpad/레시피 댓글 | 나물/冷奴/TKG 같은 finishing use 장면은 많다. | 계정 필요. 레시피 댓글 홍보 리스크 높음. | 직접 게시 제외. 문체/요리 장면 레퍼런스로만 사용. |

## X/Threads 계정 판단

새 전용 계정이 반드시 필요한 것은 아니다.

| 계정 선택 | 장점 | 리스크 | 추천 |
|---|---|---|---|
| 사용자 기존 공개 계정 | 봇처럼 덜 보이고 답글 신뢰가 높다. | 사용자 개인 정체성과 프로젝트가 섞인다. | 사용자가 원하면 1회 질문에 가장 적합. |
| 새 프로젝트 계정 | 프로젝트와 개인 계정을 분리할 수 있다. | 빈 계정이면 더 봇처럼 보이고 도달이 낮을 수 있다. | 바로 게시보다 프로필/고정글/관찰 후 사용. |
| Codex 전용 자동 계정 | 운영 분리가 쉽다. | 자동화/스팸 인상, 인증/지문 리스크가 크다. | 현재 비추천. |

따라서 21:50에 유통 실패가 확정되면, 사용자에게 필요한 권한은 `X 또는 Threads 중 어느 공개 계정으로 URL 없는 질문 1회를 올릴지` 하나다. 새 계정을 만들기보다, 먼저 기존 신뢰 계정 1회 질문 또는 오프라인 인터뷰가 더 낫다.

## Konest용 질문 후보

게시 전 규칙 확인/허용이 필요하다. 허용되더라도 링크, 판매, 가격, 입하 안내를 빼고 여행 경험 질문으로만 둔다.

```text
韓国の市場や製油所で搾りたてのごま油を買ったことがある方に質問です。

日本に帰ってから、家で最後まで香りよく使い切れましたか？
それとも、量が多い・香りが弱くなる・また買いにくいなどで困ったことがありますか？

今後の聞き取りの参考に、買った場所、瓶の大きさ、使った料理だけ教えていただけるとうれしいです。
販売や予約の案内ではありません。
```

응답으로 세는 조건:

- 한국에서 산 장소나 시장/제유소 이름이 있다.
- 일본 집에서 실제로 쓴 요리와 사용 기간이 있다.
- 다시 사고 싶은데 어려운 이유 또는 기존 대체재로 충분한 이유가 있다.

## 기록 규칙

- X/Threads/Konest/Instagram/Lemon8 등 note 외부 실제 게시 전에는 사용자 명시 허용을 받는다.
- 공개 답글만 `scripts/record_public_social_response.py`로 기록한다.
- DM, 연락처, 배송지, 결제, 예약금은 받지 않는다.
- 단순 좋아요/조회/저장은 응답으로 세지 않는다.
- 외부 게시 후에는 `experiments/channel_posting_log.csv`, `experiments/live_validation_log.csv`, `검증/게시_배포_기록.md`, `검증/응답_데이터_상태.md`를 갱신한다.

## 출처/관찰

- Konest 커뮤니티 `美味しいごま油`: https://comm.konest.com/m/board/detail.html?no=651964
- Konest `忠北製油所`: https://www.konest.com/contents/shop_mise_detail.html?id=38989
- Konest 커뮤니티 `長年続く老舗のごま油屋さん`: https://comm.konest.com/m/board/detail.html?no=658572
- Konest 뉴스 `搾りたての香りが日本人を魅了`: https://www.konest.com/contents/news_detail.html?id=57722
- Konest 커뮤니티 `水物、ごま油の発送ルール`: https://comm.konest.com/m/board/detail.html?no=634674
- Konest 커뮤니티 규칙: https://www.konest.com/contents/member_security2_4.html
- Kim-san Instagram account: https://www.instagram.com/kims_nori_sesamioil/
- Kim-san Lemon8 review: https://www.lemon8-app.com/%40himekagami/7635247589920178709?region=jp
- Kim-san Tabelog review/listing: https://tabelog.com/tokyo/A1304/A130401/13322659/
- Threads Shin-Okubo sesame oil post: https://www.threads.com/@egg._.life.gumi/post/DX4WVTyCQzy/

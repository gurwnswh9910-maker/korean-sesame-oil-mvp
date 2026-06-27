# note 게시 패킷: 큰 병/개봉 후 향 손실 체크

상태: ready_not_published
작성 시각: 2026-06-28T02:52+09:00
게시 권한: note 계정은 이 프로젝트에 한해 Codex 자유 게시 허용. 다만 5개 note 직후 연속 게시로 보일 수 있어 24h 집계 재확인 뒤 게시 여부를 결정한다.

## 게시 목적

`참기름을 사고 싶나요?`보다 더 구체적으로, 큰 병을 다 쓰기 전에 향이 약해지는 문제가 실제로 있는지 확인한다.

강한 응답은 아래를 포함해야 한다.

- 지금 쓰는 참기름의 구매처 또는 브랜드
- 병 용량/가격
- 개봉 후 사용 기간 또는 잔량
- 향이 약해졌는지, 마지막까지 충분했는지
- 100ml小瓶/제조일/차광병/가격 중 전환 조건

## 공개 링크

Vercel page:

https://korean-sesame-oil-mvp.vercel.app/aroma-loss-goma?src=note_content_aromaloss

구조화 응답:

https://korean-sesame-oil-mvp.vercel.app/quick-answer?src=note_content_aromaloss

## 제목 후보

大きいごま油、使い切る前に香りが弱くなりますか？

## 태그 후보

#ごま油 #韓国料理 #おうちごはん #自炊 #韓国食品

## 본문 후보

ごま油は、開けたての香りがいちばん印象に残ります。

でも、家で使う量が少ないと、大きい瓶を使い切る前に香りが弱くなることはありますか。

これは商品を売るための案内ではなく、正式販売前の小さな需要確認です。

知りたいのは、韓国式か日本式かより先に、今のごま油を最後まで香りよく使えているかです。

たとえば、

- 300gくらいの瓶をなかなか使い切れない
- 開けたては香るけれど途中で弱くなる
- 冷奴、ナムル、ビビンバ、韓国のりご飯に少しだけ使う
- 100mlくらいなら新鮮なうちに使い切れそう

逆に、大きい瓶で十分なら、それも知りたいです。

住所、電話番号、メールアドレスはいりません。
覚えている範囲で大丈夫です。

30秒のメモはこちらです。

https://korean-sesame-oil-mvp.vercel.app/aroma-loss-goma?src=note_content_aromaloss

質問に沿って答える場合はこちらです。

https://korean-sesame-oil-mvp.vercel.app/quick-answer?src=note_content_aromaloss

特に知りたいのは、今使っているごま油の容量、開封してからどのくらいか、そして小瓶なら買い直す理由になるかです。

#ごま油 #韓国料理 #おうちごはん #自炊 #韓国食品

## 수요로 세지 않는 것

- `小瓶がかわいい`만 있음
- 향 취향만 있고 현재 병/구매처/용량이 없음
- note 조회수, 스키, 공유만 있음

## 게시 전 확인

- 24h note 집계에서 1~5차 반응을 재확인한다.
- `/aroma-loss-goma?src=note_content_aromaloss`가 production 200인지 확인한다.
- `/quick-answer?src=note_content_aromaloss`가 source와 `開封後どのくらい` 필드를 유지하는지 확인한다.
- 게시 후에는 source별 note 댓글 라우팅에 6차 note URL을 추가한다.

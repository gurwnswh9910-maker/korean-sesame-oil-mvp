# X/Threads 단일 게시 패킷

작성일: 2026-06-27
최근 갱신: 2026-06-28T17:27+09:00
상태: note 24시간 반응 확인 후, 별도 계정 게시 권한 대기

## 사용 조건

note 게시 후 24시간 반응이 0이고, 사용자가 X 또는 Threads 계정으로 단일 게시를 명시 허용할 때만 사용한다. 반복 게시, 대량 댓글, DM 발송은 하지 않는다.

2026-06-28T17:27+09:00 보정: note 조회가 낮아 `유통 실패`로 보이는 경우에는 링크 포함 판매/검증글보다, 먼저 공개 답글을 받는 낮은 마찰 질문이 낫다. 따라서 1순위는 URL 없는 질문글로 바꾼다. URL은 사용자가 묻거나, 공개 답글이 생긴 뒤 구조화 메모가 필요할 때만 보낸다.

## 1순위 게시문: 링크 없는 공개 질문

source: `x_threads_finishing_question`

```text
家で韓国料理を作る方に聞きたいです。

ごま油を炒め油というより、最後に香りを足す油として使うことはありますか？

かどや、九鬼、オットゥギ、新大久保のしぼりたてで十分かも知りたいです。

よければ返信で、
・今使っているごま油
・1本を使い切る期間
・最後に使う料理
だけ教えてください。

販売ではなく、正式販売前の聞き取りです。
```

강한 신호로 세는 답글:

- 브랜드/구매처/용량/가격 중 하나 이상이 있다.
- `最後にかける`, `仕上げ`, `和える`, `たれ` 같은 finishing use가 있다.
- Kadoya/Kuki/Ottogi/신오쿠보 搾りたて 중 무엇으로 충분하거나 부족한지 비교한다.
- 100ml나 제조일/搾った日/차광병/시식 같은 조건이 나온다.

## 2순위 대안: 링크 포함 답변 유도

source: `x_threads_aromaloss`

1순위 게시 후 실제 답글이 생겼거나, 사용자가 링크 포함 게시를 별도로 허용할 때만 사용한다.

```text
ごま油を最後の香りに使う方へ、30秒だけメモできるページを作りました。

知りたいのは「買いたいですか？」より、
今のごま油を何ヶ月で使い切るか、
5gパック・110ml小瓶・新大久保のしぼりたてで十分か、
製造日や搾った日が見えたら比べたいかです。

https://korean-sesame-oil-mvp.vercel.app/quick-answer?src=x_threads_aromaloss
```

## 기존 broad travel 문안 보류

아래 문안은 한국여행 기억에는 맞지만, 지금의 핵심 가설인 `仕上げの香味油`, `5g・110ml・しぼりたて 후보와의 비교`, `1本を使い切る期間`이 약하다. 따라서 2026-06-28T17:27+09:00 기준 보류한다.

```text
家でビビンバ、キンパ、ナムルを作る人向けに、韓国式の香りが強いごま油を少量で届けられるか試しています。

日本のスーパーで買えるごま油とは少し違う、「韓国の食堂っぽい香り」を重視したタイプです。

100ml 1,480円前後なら試したいか、率直に教えてください。

https://korean-sesame-oil-mvp.vercel.app/?src=x_threads_homecook
```

## 게시 직전 확인 문구

아래 내용을 공개 X/Threads 계정에 단일 게시해도 되는지 사용자에게 확인한다.

```text
이 글을 X/Threads 공개 계정에 1회 게시해도 될까요?

- 판매/결제/배송 약속 없음
- 개인 연락처 수집 없음
- 반복 댓글/DM 없음
- 1순위는 URL 없는 공개 질문
- 게시 후 공개 URL과 실제 답글만 기록
```

## 게시 후 기록

1. 게시 URL을 `experiments/channel_posting_log.csv`의 `X/Threads finishing question` 행 `post_url`에 넣는다. 행이 없으면 새로 추가한다.
2. `posted=yes`, `status=public_pending_traffic`로 바꾼다.
3. 24시간 뒤 `visits`, `form_submits`, `replies`를 기록한다.
4. 공개 답글 중 실제 수요 답변만 `experiments/public_social_responses.csv`에 넣는다. 단순 좋아요, 조회, 공유는 응답으로 세지 않는다.
5. 입력 CSV를 push하면 GitHub Actions가 `experiments/validation_signal_summary.md/json`을 갱신한다.

공개 답글 URL 기록 명령:

```powershell
$env:PYTHONUTF8='1'; $env:PYTHONIOENCODING='utf-8'; python .\scripts\record_public_social_response.py --platform X --source x_threads_finishing_question --url "https://x.com/{user}/status/{id}" --text "{公開返信の要約}" --recent-purchase "{最近買った/見た場所}" --brand-store "{ブランド/店名}" --volume-price "{容量/価格}" --use-up-period "{1本を使い切る期間}" --aroma-memory "{香り経験/香り低下}" --substitute-comparison "{5g・110ml・しぼりたて候補で十分か}" --needed-proof "{製造日/搾った日/試食/遮光瓶など}" --single-price "{100ml 1,480円の反応}" --sample-signal "{少量/購入/入荷案内の希望}"
```

## 공개 응답 검색어

- `#韓国ごま油検証`
- `korean-sesame-oil-mvp.vercel.app`
- `x_threads_finishing_question`

# X/Threads 단일 게시 패킷

작성일: 2026-06-27
상태: 계정 게시 권한 대기

## 사용 조건

note 이메일 인증이 지연되고, 사용자가 X 또는 Threads 계정으로 단일 게시를 명시 허용할 때만 사용한다. 반복 게시, 대량 댓글, DM 발송, URL shortener 사용은 하지 않는다.

## 1순위 게시문

source: `x_threads_travel`

길이: 220자. X 단일 게시 제한 안에 들어간다.

```text
韓国の市場でしぼりたてのごま油を買ったことがある方に聞きたいです。

あのふたを開けた瞬間の香りを、日本の家でも使えるように、少量ボトルで入荷できるか検証しています。

100ml 1,480円前後なら試したいか、30秒だけ教えてください。正式販売前なので個人情報は不要です。

https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/?src=x_threads_travel
```

## 2순위 대안

source: `x_threads_homecook`

1순위 게시 후 반응이 없고, 사용자가 두 번째 게시를 따로 허용할 때만 사용한다.

```text
家でビビンバ、キンパ、ナムルを作る人向けに、韓国式の香りが強いごま油を少量で届けられるか試しています。

日本のスーパーで買えるごま油とは少し違う、「韓国の食堂っぽい香り」を重視したタイプです。

100ml 1,480円前後なら試したいか、率直に教えてください。

https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/?src=x_threads_homecook
```

## 게시 직전 확인 문구

아래 내용을 공개 X/Threads 계정에 단일 게시해도 되는지 사용자에게 확인한다.

```text
이 글을 X/Threads 공개 계정에 1회 게시해도 될까요?

- 판매/결제/배송 약속 없음
- 개인 연락처 수집 없음
- 반복 댓글/DM 없음
- 게시 후 공개 URL만 기록
```

## 게시 후 기록

1. 게시 URL을 `experiments/channel_posting_log.csv`의 `X/Threads travel` 행 `post_url`에 넣는다.
2. `posted=yes`, `status=public_pending_traffic`로 바꾼다.
3. 24시간 뒤 `visits`, `form_submits`, `replies`를 기록한다.
4. 공개 답글 중 실제 수요 답변만 `experiments/public_social_responses.csv`에 넣는다. 단순 좋아요, 조회, 공유는 응답으로 세지 않는다.
5. 입력 CSV를 push하면 GitHub Actions가 `experiments/validation_signal_summary.md/json`을 갱신한다.

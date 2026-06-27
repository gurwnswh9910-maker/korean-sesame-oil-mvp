# 첫 외부 트래픽 실행 런북

목적: 공개 MVP에 실제 일본어 트래픽을 넣고, `좋아요`가 아니라 과거 구매 행동/가격 반응/입하 관심 신호를 기록한다.

## 준비물

- Landing: `https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/`
- Share note: `https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/share_note.html`
- Field QR page: `https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/field_interview.html`
- Printable flyer: `https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/field_interview_flyer.pdf`
- Primary form: `https://www.notion.so/forms/38c5da6ea39c8149beb3000c9ab0ea98`

## 오늘 할 일 60분 버전

현재 우선 메시지: `韓国旅行や新大久保で、搾りたてのごま油の香りを覚えている人`을 먼저 찾는다. 넓은 주부층보다 과거 경험과 대체재 인지가 있는 사람을 먼저 검증한다.

### 1. X/Threads 짧은 게시 2개

게시 A source: `x_threads_travel`

```text
韓国の市場でしぼりたてのごま油を買ったことがある方に聞きたいです。

あのふたを開けた瞬間の香りを、日本の家でも使えるように、少量ボトルで入荷できるか検証しています。

100ml 1,480円前後なら試したいか、30秒だけ教えてください。正式販売前なので個人情報は不要です。

https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/?src=x_threads_travel
```

게시 B source: `x_threads_homecook`

```text
家でビビンバ、キンパ、ナムルを作る人向けに、韓国式の香りが強いごま油を少量で届けられるか試しています。

日本のスーパーで買えるごま油とは少し違う、「韓国の食堂っぽい香り」を重視したタイプです。

100ml 1,480円前後なら試したいか、率直に教えてください。

https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/?src=x_threads_homecook
```

### 2. note/Konest 설명형 게시 1개

source: `note_kfood` 또는 `konest`

```text
韓国旅行や新大久保で、ふたを開けた瞬間に「香りが違う」と感じたごま油はありますか。

日本にもおいしいごま油はたくさんありますが、韓国の市場や食堂で記憶に残る、仕上げに一滴たらしたときの香りを少量で再現したい人がいるかを調べています。

正式販売ではなく、入荷前の需要検証です。仮に100ml 1,480円、3本 3,980円くらいならどう感じるかを知りたいです。

個人情報は不要です。最後に買ったごま油、使いたい料理、価格感だけ30秒で教えてください。

https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/share_note.html?src=note_kfood
```

### 3. 오프라인 3명만 묻기

사용 링크: `https://gurwnswh9910-maker.github.io/korean-sesame-oil-mvp/field_interview.html`

질문:

1. 最近6か月以内にごま油を買いましたか。どこで、どのブランドでしたか。
2. 韓国旅行や韓国料理店で、ごま油の香りが印象に残ったことはありますか。
3. 100ml 1,480円なら試したいですか。

## 기록

- 온라인 게시 후 `experiments/channel_posting_log.csv`의 `posted`, `post_url`, `visits`, `form_submits`, `replies`를 업데이트한다.
- 오프라인 대화는 `experiments/field_interview_log.csv`에 1명 1행으로 기록한다.
- Notion 응답은 Notion UI/export로 확인한다.
- GitHub fallback 응답은 `experiments/waitlist_summary.md` 또는 GitHub Issues에서 확인한다.

## 1차 판정

- 24시간 안에 댓글/폼/오프라인 대화 합산 5건 이상이면 같은 메시지를 더 넓힌다.
- 10명 중 3명 이상이 최근 구매 행동을 말하면 H2 첫 고객 세그먼트를 유지한다.
- 신오쿠보/한국식품점에서 이미 대체재를 본 사람이 많으면 `한국산` 대신 `제조일/향 보존/소량/재구매 편의` 비교로 메시지를 바꾼다.
- 가격 반응이 약하면 100ml 단품보다 3병 세트/선물용 또는 生使い 요리 완성도 메시지로 피벗한다.

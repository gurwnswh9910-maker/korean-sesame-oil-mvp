# 첫 외부 트래픽 실행 런북

목적: 공개 MVP에 실제 일본어 트래픽을 넣고, `좋아요`가 아니라 과거 구매 행동/가격 반응/입하 관심 신호를 기록한다.

## 준비물

- Landing: `https://korean-sesame-oil-mvp.vercel.app/`
- Content MVP: `https://korean-sesame-oil-mvp.vercel.app/korea-trip-goma`
- Share note: `https://korean-sesame-oil-mvp.vercel.app/share`
- Mobile note answer hub: `https://korean-sesame-oil-mvp.vercel.app/answer-note`
- Public article: `https://korean-sesame-oil-mvp.vercel.app/note`
- Field QR page: `https://korean-sesame-oil-mvp.vercel.app/field`
- Printable flyer: `https://korean-sesame-oil-mvp.vercel.app/field-flyer`
- Primary form: `https://www.notion.so/forms/38c5da6ea39c8149beb3000c9ab0ea98`
- Channel rules gate: `mvp/channel_rules_and_permission_gate.md`
- First note draft: `mvp/note_article_draft.md`

## 오늘 할 일 60분 버전

현재 우선 메시지: `韓国旅行や新大久保で、搾りたてのごま油の香りを覚えている人`을 먼저 찾는다. 넓은 주부층보다 과거 경험과 대체재 인지가 있는 사람을 먼저 검증한다.

현재 우선 문제: `참기름을 사고 싶은가`가 아니라 마지막 구매 장소, 향이 끝까지 남았는지, 일본에서 다시 살 조건이다. 자세한 가설은 `검증/욕구_문제_가설_20260627.md`를 본다.

### 1. note 설명형 게시 1개

게시 source: `note_kfood`

note는 2026-06-27T21:46+09:00에 게시 완료했다.

```text
https://note.com/dreamy_viola8978/n/n77fa3f5a7fe9
```

2026-06-27T22:10+09:00에 모바일 CTA도 수정했다. note 본문은 QR이 아니라 `/answer-note` 탭 링크, `/share?src=note_kfood` 응답 메모, note 댓글 템플릿을 사용한다.

2026-06-27T22:40+09:00에는 `/answer-note`를 Notion direct redirect에서 모바일 응답 허브로 바꿨다. 사용자는 같은 링크 안에서 note 댓글, Notion 폼, 복사용 메모, 상세 설명을 선택할 수 있다.

두 번째 note를 낸다면 `mvp/note_content_posting_packet.md`의 콘텐츠형 글을 쓴다. 이 글의 링크는 `https://korean-sesame-oil-mvp.vercel.app/korea-trip-goma?src=note_content_travel`이며 제품 가격보다 여행/신오쿠보 구매 경험을 먼저 묻는다.

### 2. X/Threads 짧은 게시 1개

기본 순서는 note 게시 후 24시간 반응이 0일 때만 추가한다. 단, note 이메일 인증이 지연되고 사용자가 X/Threads 단일 게시를 명시 허용하면 이 경로를 먼저 써도 된다. 동일 문안 반복, 댓글 대량 발송, DM 발송은 하지 않는다. 실제 게시 절차는 `mvp/x_threads_posting_packet.md`를 따른다.

게시 A source: `x_threads_travel`

```text
韓国の市場でしぼりたてのごま油を買ったことがある方に聞きたいです。

あのふたを開けた瞬間の香りを、日本の家でも使えるように、少量ボトルで入荷できるか検証しています。

100ml 1,480円前後なら試したいか、30秒だけ教えてください。正式販売前なので個人情報は不要です。

https://korean-sesame-oil-mvp.vercel.app/korea-trip-goma?src=x_threads_travel
#韓国ごま油検証
```

대안 게시 source: `x_threads_homecook`

```text
家でビビンバ、キンパ、ナムルを作る人向けに、韓国式の香りが強いごま油を少量で届けられるか試しています。

日本のスーパーで買えるごま油とは少し違う、「韓国の食堂っぽい香り」を重視したタイプです。

100ml 1,480円前後なら試したいか、率直に教えてください。

https://korean-sesame-oil-mvp.vercel.app/?src=x_threads_homecook
```

### 3. Konest 보류

Konest는 규칙 확인 또는 운영자 문의 전까지 게시하지 않는다.

### 4. 오프라인 3명만 묻기

사용 링크: `https://korean-sesame-oil-mvp.vercel.app/field`

질문:

1. 最近6か月以内にごま油を買いましたか。どこで、どのブランドでしたか。
2. 韓国旅行や韓国料理店で、ごま油の香りが印象に残ったことはありますか。
3. 新大久保や韓国食材店で、韓国式のごま油を見たことや買ったことはありますか。
4. 100ml 1,480円なら試したいですか。

## 기록

- 온라인 게시 후 `experiments/channel_posting_log.csv`의 `posted`, `post_url`, `visits`, `form_submits`, `replies`를 업데이트한다.
- note 게시 후 24h/72h 전체뷰, 댓글, 스키를 기록한다.
- Vercel article은 `article` source로 Notion 응답을 기록한다. GitHub fallback은 내부용으로만 본다.
- X 공개 응답은 해시태그 `#韓国ごま油検証`이 붙은 실제 응답 URL만 `experiments/public_social_responses.csv`에 기록한다. 단순 공유는 응답으로 세지 않는다.
- 오프라인 대화는 `experiments/field_interview_log.csv`에 1명 1행으로 기록한다.
- Notion 응답은 Notion UI/export로 확인한다.
- GitHub fallback 응답은 `experiments/waitlist_summary.md` 또는 GitHub Issues에서 확인한다.
- 공개 X 응답은 검색/수동 확인 후 `experiments/public_social_responses.csv`로 옮긴다.
- Notion export, 공개 X 응답 CSV, 오프라인 인터뷰 CSV, 채널 로그 CSV를 push하면 GitHub Actions가 `experiments/validation_signal_summary.md/json`을 다시 만든다. summary 파일만 bot이 커밋하는 push는 입력 path가 아니므로 반복 실행되지 않는다.

## 1차 판정

- 24시간 안에 댓글/폼/오프라인 대화 합산 5건 이상이면 같은 메시지를 더 넓힌다.
- note 24시간 전체뷰가 30 미만이면 메시지 판단보다 유입 부족으로 본다.
- 10명 중 3명 이상이 최근 구매 행동을 말하면 H2 첫 고객 세그먼트를 유지한다.
- 콘텐츠형 검증에서 강한 응답은 최근 구매처, 브랜드/매장, 용량/가격, 바꿀 조건 또는 불만 중 3개 이상을 포함해야 한다.
- 신오쿠보/한국식품점에서 이미 대체재를 본 사람이 많으면 `한국산` 대신 `제조일/향 보존/소량/재구매 편의` 비교로 메시지를 바꾼다.
- 신오쿠보나 한국식품점에서 이미 한국식 참기름을 사는 사람은 부정 신호가 아니라 전환 이유 검증 대상이다. 기존 구매처, 제조일 인지, 향 보존, 100ml 소량 선호를 따로 기록한다.
- 가격 반응이 약하면 100ml 단품보다 3병 세트/선물용 또는 生使い 요리 완성도 메시지로 피벗한다.

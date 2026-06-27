# 모바일 CTA 검증 메모

최근 갱신: 2026-06-27T22:40:00+09:00

## 결론

note 유입은 기본적으로 스마트폰으로 본다고 가정한다. 스마트폰에서 QR을 찍으라고 하면 사용자가 다른 기기를 가져와야 하므로 전환이 떨어진다.

## 채널별 CTA 원칙

| 채널 | 기본 CTA | 보조 CTA | QR 사용 |
|---|---|---|---|
| note 모바일 | 탭 가능한 모바일 응답 허브 `/answer-note` | note 댓글 응답, Notion 폼, 복사용 메모 | 사용하지 않음 |
| note PC | 탭 가능한 모바일 응답 허브 `/answer-note` | `/share?src=note_kfood` 응답 메모 | 사용하지 않음 |
| X/Threads | 본문 링크 또는 프로필/답글 링크 | 공개 답글 템플릿 | 사용하지 않음 |
| 오프라인 플라이어 | QR + 짧은 URL 병기 | 대면 질문지 | 사용 |
| 대면 인터뷰 | QR 또는 interviewer가 직접 링크 전송 | 수기 기록 | 상황별 사용 |

## 추가한 경로

- 모바일 응답 허브: `https://korean-sesame-oil-mvp.vercel.app/answer-note`
- 응답 메모: `https://korean-sesame-oil-mvp.vercel.app/share?src=note_kfood`
- 상세 설명: `https://korean-sesame-oil-mvp.vercel.app/note`

## note 본문 권장 CTA

```text
スマホで読んでいる方は、QRではなくこのままリンクをタップしてください。

30秒回答ページ:
https://korean-sesame-oil-mvp.vercel.app/answer-note

フォームが面倒な場合は、このnoteのコメントでも大丈夫です。
香り経験:
最近買ったごま油:
使いたい料理:
100ml 1,480円:
コメント:
```

## 판정

QR은 오프라인 플라이어와 대면 인터뷰에서는 유효하다. note, X, Threads처럼 사용자가 이미 스마트폰 화면 안에 있는 채널에서는 QR을 CTA로 쓰지 않는다.

## 2026-06-27T22:40 보완

`/answer-note`는 Notion Form으로 바로 보내는 redirect가 아니라 모바일 응답 허브로 바꾼다. 이유는 note 앱/모바일 브라우저에서 외부 폼으로 바로 전환하면 이탈이 생길 수 있기 때문이다. 허브에는 아래 선택지를 둔다.

- note 댓글로 답하기
- 익명 Notion Form으로 답하기
- 응답 메모 복사
- 상세 설명 보기

배포 검증:

- 첫 Vercel 배포 후 rewrite만으로는 `/answer-note`가 404였으므로 `docs/answer-note.html`을 직접 추가했다.
- 재배포 후 `https://korean-sesame-oil-mvp.vercel.app/answer-note?src=note_kfood`는 status 200, final URL 유지.
- Playwright production check: 390px mobile과 1280px desktop 모두 overflow count 0.

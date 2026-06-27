# 모바일 CTA 검증 메모

최근 갱신: 2026-06-27T22:10:00+09:00

## 결론

note 유입은 기본적으로 스마트폰으로 본다고 가정한다. 스마트폰에서 QR을 찍으라고 하면 사용자가 다른 기기를 가져와야 하므로 전환이 떨어진다.

## 채널별 CTA 원칙

| 채널 | 기본 CTA | 보조 CTA | QR 사용 |
|---|---|---|---|
| note 모바일 | 탭 가능한 짧은 링크 `/answer-note` | note 댓글 응답 | 사용하지 않음 |
| note PC | 탭 가능한 짧은 링크 `/answer-note` | `/share?src=note_kfood` 응답 메모 | 사용하지 않음 |
| X/Threads | 본문 링크 또는 프로필/답글 링크 | 공개 답글 템플릿 | 사용하지 않음 |
| 오프라인 플라이어 | QR + 짧은 URL 병기 | 대면 질문지 | 사용 |
| 대면 인터뷰 | QR 또는 interviewer가 직접 링크 전송 | 수기 기록 | 상황별 사용 |

## 추가한 경로

- 짧은 응답 링크: `https://korean-sesame-oil-mvp.vercel.app/answer-note`
- 응답 메모: `https://korean-sesame-oil-mvp.vercel.app/share?src=note_kfood`
- 상세 설명: `https://korean-sesame-oil-mvp.vercel.app/note`

## note 본문 권장 CTA

```text
スマホで読んでいる方は、QRではなくこのままリンクをタップしてください。

回答フォーム:
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

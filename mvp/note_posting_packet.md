# note 게시 패킷

작성일: 2026-06-27
상태: note 공개 완료, 24h/72h 반응 측정 대기

## 현재 상태

2026-06-27T21:46+09:00 기준 note 게시가 완료되었다.

공개 URL:

```text
https://note.com/dreamy_viola8978/n/n77fa3f5a7fe9
```

2026-06-27T21:40+09:00 기준 이메일 인증은 완료되었다. Edge CDP로 note draft `n77fa3f5a7fe9`를 열어 제목/본문을 입력하고 초안을 저장했다. 공개 설정은 무료 글, 댓글 허용, 자동 번역 off, AI 학습 대가 환원 프로그램 off, 아래 5개 핵심 태그 적용 상태였다.

```text
#韓国料理 #新大久保 #韓国旅行 #ごま油 #おうち韓国
```

사용자가 `note 계정 니꺼니까 note에 한해서 너가 자유롭게 게시해`라고 명시 허용한 뒤 `投稿する`를 눌렀다. 이후 canonical URL은 Edge CDP에서 확인했다.

note 본문은 2026-06-27T22:10+09:00에 모바일 CTA 기준으로 갱신했다. 공개 글에는 기존 GitHub Pages 링크가 남아 있지 않고, 아래 링크와 댓글 응답 템플릿이 들어 있다.

```text
https://korean-sesame-oil-mvp.vercel.app/answer-note
https://korean-sesame-oil-mvp.vercel.app/share?src=note_kfood
https://korean-sesame-oil-mvp.vercel.app/note
```

남은 작업은 24h/72h 반응을 기록하는 것이다.

## 인증 재전송 위치

2026-06-27T21:03+09:00 기준 note 홈 `https://note.com/` 하단 배너에 인증 메일 재전송 버튼이 보인다. 버튼 문구는 아래와 같다.

```text
メールを再送信
```

이 버튼은 계정에 인증 메일을 다시 보내는 실제 계정 액션이므로 Codex가 임의로 누르지 않는다. 사용자가 직접 버튼을 누른 뒤, 메일함에서 최신 인증 메일 링크를 열어야 한다.

note 공식 도움말 기준 인증 URL은 2시간 유효하고, 여러 번 재전송한 경우 마지막에 받은 인증 메일의 URL을 사용해야 한다.

참고: https://www.help-note.com/hc/ja/articles/360011357753-%E7%99%BB%E9%8C%B2%E3%83%A1%E3%83%BC%E3%83%AB%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9%E3%82%92%E8%AA%8D%E8%A8%BC%E3%81%99%E3%82%8B

## 게시 절차 기록

1. 공개 설정 화면에서 final `投稿する` 버튼이 보이는지 확인했다.
2. 사용자에게 note 한정 자유 게시 허용을 받았다.
3. 허용 후 `投稿する`를 눌렀다.
4. 게시 완료 후 URL을 캡처했다.
5. 제목은 아래 문구다.

```text
韓国旅行で覚えた「しぼりたてごま油の香り」は、日本の家でも使いたいですか？
```

6. 본문은 `mvp/note_article_draft.md`의 `## 本文` 아래 내용을 사용했다.
7. 태그 후보는 아래 5개를 적용했다.

```text
#韓国料理 #新大久保 #韓国旅行 #ごま油 #おうち韓国
```

8. 게시 URL과 게시 시각은 `experiments/channel_posting_log.csv`에 기록했다. 24h/72h 전체뷰, 댓글, 스키, Notion 응답 수는 아직 측정 전이다.

## 게시 후 판정

- 24시간 내 댓글/스키/응답이 1건 이상이면 댓글 내용 기준으로 대체재 인지와 가격 저항을 추가 질문한다.
- 24시간 내 반응이 0이면 `mvp/runbook_first_traffic.md` 기준으로 X/Threads travel 글 1개만 추가한다.
- 어떤 경우에도 정식 수입, 식품 표시, 단가 확인 전 결제나 배송 약속은 하지 않는다.

# 외부 게시 채널 규칙과 권한 게이트

작성일: 2026-06-27
최근 갱신: 2026-06-29T23:35:42+09:00

## 목적

공개 MVP에 실제 일본어 트래픽을 넣되, 커뮤니티 규칙 위반이나 계정 리스크를 만들지 않는다. 이 문서는 게시 전 채널별 실행 가능성과 필요한 권한을 정리한다.

## 채널별 판단

| 채널 | 현재 판단 | 이유 | 실행 방식 |
|---|---|---|---|
| note | 1순위, 6개 게시 완료, 댓글 후보 운영 중 | 자기 글로 수요 검증 취지를 설명할 수 있고, note 공식 도움말 기준 대시보드에서 글별 조회/댓글/스키를 확인할 수 있다. 사용자는 이 프로젝트에 한해 note 게시/수정/댓글을 허용했다. 1차 제품/입하, 2차 여행/사용, 3차 신오쿠보, 4차 홈쿡, 5차 한국김/TKG, 6차 향 손실/仕上げの香味油 글은 게시 완료. 6차 note URL은 `https://note.com/dreamy_viola8978/n/n363650c8697f`이고, 게시 직후 댓글/스키/폼/공개 응답은 0이라 수요 증거로 세지 않는다. 관련 note 글 댓글 후보는 `검증/note_댓글_관찰_접촉_패킷_20260628.md`에 준비됐다. | note 1~6의 조회, 댓글, 스키, 폼 응답을 기록한다. 댓글은 하루 3개 이하, 링크 없이, 맥락형 질문만 한다. 2026-06-28T14:53+09:00 현재 새 전용 계정은 필요 없고, 실제 댓글 실행에는 로그인된 note 브라우저 표면만 필요하다. |
| X/Threads | 2순위 | 한국여행/신오쿠보/K-food 해시태그 유입을 빠르게 볼 수 있다. 단, X는 비정상적 반복/대량 활동과 오해성 링크를 제한하므로 1개 수동 질문만 한다. | 사용자가 명시 허용하면 `mvp/x_threads_posting_packet.md`의 URL 없는 공개 질문 1회만 사용. 동일문 반복 금지, URL shortener 금지, 댓글/DM 대량 발송 금지 |
| Konest | 보류 | 한국 시장/제유소/搾りたてごま油 여행 후기와 액체 반입/배송 질문이 있어 타겟 밀도는 높다. 다만 커뮤니티 규칙 확인이 필요하고 홍보/상업 목적처럼 보이면 삭제/제재 리스크가 있다. | `mvp/post_gate_external_channel_packet_20260628.md` 기준으로 규칙 확인 또는 운영자 문의 후, 링크 없는 여행 경험 질문만 검토 |
| Tunagate | 게시 제외 | 이용규약상 영업, 권유, 선전 목적 이용과 외부 서비스 유도를 금지한다. | 플랫폼 내 게시 금지. 별도 오프라인 대화가 자연스럽게 생기는 경우에만 개인 정보 없이 질문 |
| 신오쿠보/한국식품점 현장 | 1순위 오프라인 | 대체재 인지와 가격 저항을 바로 확인할 수 있다. | `mvp/field_interview_script.md`와 QR 플라이어 사용 |

## 게시 전 권한 확인

외부 계정으로 실제 게시하기 전에는 아래가 필요하다. 2026-06-28T14:20+09:00 사용자는 외부 공개 글 관찰은 허용했지만, note 외부 플랫폼의 실제 게시/댓글/DM은 별도 계정과 명시 허용 없이는 하지 않는다.

1. 사용할 계정: note, X, Threads 중 어떤 계정인지. 현재 필수 전용 계정은 없고, note 계정만으로 우선 실행한다. 현재 부족한 것은 새 계정이 아니라 Codex가 조작 가능한 로그인된 note 브라우저 표면이다.
2. 게시 허용 범위: 단일 글, 2개 글, 댓글 답변, DM 답변 가능 여부
3. 문안 변경 허용 여부: 의미는 유지하되 계정 톤에 맞게 약간 바꿔도 되는지
4. 응답 기록 방식: 댓글/DM 원문을 저장할지, 익명 요약만 기록할지
5. 금지선: 판매 확정, 결제 유도, 개인 연락처 수집, 반복 댓글, 커뮤니티 규칙 우회는 하지 않음

## 첫 실행 순서

1. note 1~6차 게시물의 전체뷰, 댓글, 스키와 Notion 응답 수를 기록
2. note 댓글이 있으면 note 댓글 템플릿 또는 `/answer-note`로 응답 신호를 정리
3. 반응이 0이면 6차 note를 추가 수요 증거로 세지 말고, 새 댓글/폼/공개 답글/오프라인 원본 응답이 생겼는지 먼저 확인한다. 외부 채널은 `mvp/post_gate_external_channel_packet_20260628.md` 기준으로 한 번에 1개만 선택하고, X/Threads는 사용자가 별도 허용할 때만 URL 없는 공개 질문 1회를 추가한다.
4. 댓글이 달리면 판매하지 말고 최근 구매처/대체재/가격 반응만 묻는다
5. 응답 5건 전에는 채널을 넓히지 않는다

## 참고한 공개 규칙/도움말

- note dashboard help: https://www.help-note.com/hc/ja/articles/360010324194-%E3%83%80%E3%83%83%E3%82%B7%E3%83%A5%E3%83%9C%E3%83%BC%E3%83%89%E3%81%A7%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E7%8A%B6%E6%B3%81%E3%82%92%E3%81%BF%E3%82%8B
- note terms: https://terms.help-note.com/hc/ja/articles/44943817565465-note-%E3%81%94%E5%88%A9%E7%94%A8%E8%A6%8F%E7%B4%84
- X authenticity and platform manipulation policy: https://help.x.com/en/rules-and-policies/authenticity
- X link blocking/spam guidance: https://help.x.com/en/safety-and-security/phishing-spam-and-malware-links
- Tunagate rules: https://tunagate.com/article/rules
- Konest community rules: https://www.konest.com/contents/member_security2_4.html
- post-gate 외부 채널 패킷: `mvp/post_gate_external_channel_packet_20260628.md`

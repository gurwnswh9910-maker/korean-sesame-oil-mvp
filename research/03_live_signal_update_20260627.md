# 현재 외부 신호 업데이트

작성일: 2026-06-27

최신 보정: 2026-06-27T23:17+09:00 현재 이 문서의 `note 계정 게시 상태` 행은 과거 상태다. 이후 note 이메일 인증과 게시가 완료되었고, 공개 note URL은 `https://note.com/dreamy_viola8978/n/n77fa3f5a7fe9`다. 현재 소비자-facing canonical은 Vercel이며, 제품 외 콘텐츠 MVP는 `https://korean-sesame-oil-mvp.vercel.app/korea-trip-goma`다. 최신 truth는 `검증/검증_원장.md`와 `검증/욕구_문제_가설_20260627.md`를 우선한다.

## 목적

기존 리서치와 MVP 공개 이후, 현재 웹에서 보이는 한국식 방앗간/갓 짠 참기름 관련 신호가 2차 가설을 강화하는지 확인한다. 이 문서는 실제 MVP 응답이 아니라, 게시 전 메시지와 인터뷰 질문을 조정하기 위한 보조 리서치다.

## 확인한 신호

| 신호 | 내용 | 해석 |
|---|---|---|
| 한국 참기름 수출 증가 | 연합뉴스 영문 기사는 2026년 1~4월 한국 참기름 수출액이 614만 달러로 전년 동기 대비 37% 증가했고, 중량은 657톤으로 47.6% 증가했다고 보도했다. | 한국 참기름이 해외에서 커지는 흐름은 확인된다. 다만 일본 단독 수요 증명은 아니므로 MVP 응답으로 검증해야 한다. |
| 일본 관광객/주부 반응 | Record China는 2026년 6월 한국 갓 짠 참기름이 일본 관광객과 주부 사이에서 화제가 되고, SNS 언급과 한국 방앗간 방문 수요가 있다는 취지로 보도했다. | H1의 `한국 여행에서 맡은 향 재현` 메시지를 더 우선해도 된다. |
| FOODEX 2026 B2B 신호 | FOODEX JAPAN 2026 웹가이드에는 한국산 참기름/들기름 관련 출품사가 확인된다. | 일본 시장을 보는 공급자/B2B 관심은 있다. 하지만 소비자 수요와 차별성은 별도로 검증해야 한다. |
| 신오쿠보 경쟁/벤치마크 | 웹 검색 결과상 신오쿠보의 한국식 참기름 관련 매장/계정 신호가 보인다. 일부 SNS/Instagram 출처는 직접 열람 제한이 있어 독립 검증이 필요하다. | 일본에 대체재가 없다는 식으로 말하면 안 된다. 오프라인 인터뷰에서는 이미 신오쿠보나 한국식품점에서 본 적이 있는지 묻는다. |
| Notion 구조화 폼 재시도 | 새 Notion DB와 Form view, 추가 다문항 테스트 view를 만들었지만, MCP fetch 기준 공개 폼 질문은 여전히 `Submission` 1개만 노출됐다. | 랜딩 CTA는 기존 1줄 템플릿 방식을 유지한다. 다문항 폼이 필요하면 Google Forms/Tally 같은 별도 폼 도구로 전환한다. |
| note 계정 게시 상태 | 브라우저에서 `https://note.com/notes/new` 접근 시 note 로그인 페이지로 리다이렉트됐다. | 계정 게시는 아직 실행하지 않는다. 현재 외부 공유 표면은 GitHub Pages article이다. |

## 가설 조정

### H1 보강: 여행 기억 기반 향 재현

현재 신호는 `한국산 참기름`보다 `한국 여행/시장/방앗간에서 맡은 갓 짠 향`을 더 강한 wedge로 지지한다. 게시문 첫 문장은 가격보다 경험 회상 질문으로 시작하는 편이 낫다.

### H2 보강: 첫 고객은 신오쿠보/한국여행 경험자

첫 트래픽은 넓은 주부층보다 아래 순서로 좁힌다.

1. 한국 여행에서 방앗간/시장 참기름을 사거나 먹어본 사람
2. 신오쿠보/한국식품점에서 한국 식재료를 사는 사람
3. 집에서 비빔밥, 나물, 김밥을 자주 만드는 사람

### H3 유지: 판매 전 규제/단가 gate

수요 신호가 강해져도 결제/배송을 받기 전에는 수입신고, 일본어 표시, 알레르겐/원산지/유통기한, 보관 조건, 샘플 단가를 먼저 확인한다.

### H4 추가: 대체재 인지 가설

신오쿠보나 한국식품점에서 이미 유사 참기름을 봤거나 살 수 있는 고객은 단순 입하 알림보다 `제조일`, `향 보존`, `소량`, `가격`, `재구매 편의`를 비교한다. MVP 메시지는 "일본에 없다"가 아니라 "이미 살 수 있는 제품과 비교해도 바꿀 이유가 있는가"를 묻는 쪽으로 좁힌다.

검증 질문:

- 新大久保や韓国食材店で、韓国式のごま油を見たことがありますか。
- その商品と比べて、製造日や香りの強さが分かるなら試したいですか。
- 100ml 1,480円なら、既存のごま油から替える理由がありますか。

## 실행 반영

- `mvp/field_interview_script.md`에 신오쿠보/한국식품점 대체재 질문을 추가한다.
- `mvp/outreach_targets.md`에는 신오쿠보를 단순 유입 채널이 아니라 경쟁/벤치마크 확인 채널로 표시한다.
- `mvp/runbook_first_traffic.md`는 첫 게시 후 실제 계정 URL과 반응 수가 기록되기 전까지 `검증 완료`로 보지 않는다.
- `mvp/index.html`, `mvp/share_note.html`, `mvp/note_article.html`에는 기존 신오쿠보/한국식품점 대체재 대비 전환 이유 질문을 명시한다.

## 참고 소스

- Yonhap, S. Korea's sesame oil exports jump 37 pct in Jan-April: https://en.yna.co.kr/view/AEN20260602002900320
- Record China, Korean freshly pressed sesame oil topic among Japanese tourists/consumers: https://www.recordchina.co.jp/b978218-s39-c30-d0195.html
- FOODEX JAPAN 2026 web guide, Korean sesame oil exhibitor signal: https://www.jma-tradeshow.com/foodex/webguide_jp/company.php?no=2201
- OILLO Japan Instagram search-result signal, direct fetch throttled: https://www.instagram.com/oillo_japan/

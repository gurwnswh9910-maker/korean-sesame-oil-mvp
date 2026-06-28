# CTA 폼 스펙

## 목적

랜딩 방문자가 실제로 `입하 안내`, `선예약 관심`, `가격 수용`, `과거 구매 행동`을 남기게 만드는 최소 폼이다.

## 현재 게시용 도구

현재 공개 MVP는 Vercel + Notion Form으로 게시한다. GitHub Pages와 GitHub Issue Form은 로그인 가능한 사용자의 내부 fallback으로만 남긴다.

- Landing: `https://korean-sesame-oil-mvp.vercel.app/`
- note/mobile answer hub: `https://korean-sesame-oil-mvp.vercel.app/answer-note`
- Structured quick answer: `https://korean-sesame-oil-mvp.vercel.app/quick-answer`
- Primary Form: `https://www.notion.so/forms/38c5da6ea39c8149beb3000c9ab0ea98`
- GitHub fallback: `https://github.com/gurwnswh9910-maker/korean-sesame-oil-mvp/issues/new?template=waitlist.yml`
- 개인정보 보호: 이메일, 주소, 전화번호를 받지 않는다.
- 검증 신호: 과거 구매 행동, 가격 수용, 사용 요리, note 댓글/폼 제출/공개 답글/후속 대화
- Notion 데이터베이스: `韓国式しぼりたてごま油 MVP 検証`
- 도구 한계: Notion MCP로 생성한 공개 Form은 현재 `Submission` 1줄 입력만 노출된다. `/quick-answer`에서 다문항처럼 선택하게 한 뒤 1줄 제출문을 자동 생성하고, `/answer-note`와 랜딩에서 이 경로로 보낸다. 폼이 부담스러운 사람은 note 댓글로 답하게 한다.
- note 댓글 CTA는 source별로 분리한다. `note_kfood`는 1차 note `https://note.com/dreamy_viola8978/n/n77fa3f5a7fe9`, `note_content_travel`은 2차 note `https://note.com/dreamy_viola8978/n/n3f3af286cf6d`, `note_content_shinokubo`는 3차 note `https://note.com/dreamy_viola8978/n/n700b325ba824`, `note_content_homecook`은 4차 note `https://note.com/dreamy_viola8978/n/n08bad3dce2a9`, `note_content_homecook_ricebowl`은 5차 note `https://note.com/dreamy_viola8978/n/nbb21605544ca`로 보낸다.

## 대체 권장 도구

1. 연락처 수집이 필요해지면 Google Forms 또는 Tally로 전환
2. 응답 저장은 Google Sheets 또는 Notion database export
3. 개인정보 문구는 일본어로 명시
4. 결제/배송 전환 전에는 수입/식품표시 확인을 별도 gate로 둔다

## 일본어 폼 제목

韓国式しぼりたてごま油 入荷案内

## 일본어 설명

正式販売前の需要検証フォームです。食品として販売する場合は、日本の輸入・食品表示条件を確認したうえで、少量入荷できる場合のみご案内します。

## 질문

| 필수 | 필드 | 형식 |
|---|---|---|
| 예 | Submission | 1-line text: `流入元 / 香り経験 / 最近買ったごま油 / 使いたい料理 / 100ml価格 / 3本価格 / コメント` |

## `/quick-answer` 구조화 메모 생성 질문

Notion 저장은 여전히 `Submission` 1줄이지만, 사용자는 아래 필드를 누르면 1줄 제출문을 자동으로 받는다.

| 필수 | 필드 | 형식 |
|---|---|---|
| 예 | 主な使い方 | radio: 最後に香りを足す / 炒める時に使う / 和える・たれに使う / あまり意識しない |
| 예 | 最後に買ったまたは見た場所 | radio: 棚で見ている / 韓国旅行 / 新大久保 / 韓国スーパー / ネット / 日本のスーパー / その他 |
| 아니오 | ブランドや店名 | text |
| 아니오 | 容量と価格 | text |
| 아니오 | 開封してからの期間 | text |
| 예 | 1本を使い切る期間 | text: 1〜2か月 / 3〜4か月 / 半年以上 / 使い切れない / 覚えていない |
| 예 | 使いたい料理 | checkbox: ビビンバ / ナムル / キンパ / 卵かけご飯 / ラーメン / 冷奴 / 焼肉 / その他 |
| 예 | 香りは最後まで残ったか | radio: 最後まで残った / 途中で弱くなった / 覚えていない |
| 예 | 5g・110ml・しぼりたて候補で十分か | radio: 5gパックで十分 / 110ml小瓶で十分 / 香り・鮮度が不安 / 使い切れない / 選び方が分からない / 100ml前後なら比べたい / 覚えていない |
| 예 | 日本で買い直すなら決め手 | checkbox: 製造日 / 搾った日 / 試食 / 仕上げで残る香り / 100ml小瓶 / 遮光瓶 / 1〜2か月で使い切れる / 買い直しやすさ / 価格 / その他 |
| 예 | 100ml 1,480円 | radio: はい / 迷う / いいえ |
| 아니오 | コメント | paragraph |

## 이상적인 다문항 폼으로 전환할 때의 질문

| 필수 | 필드 | 형식 |
|---|---|---|
| 예 | 最近6か月以内に買ったごま油のブランド/購入場所 | short text |
| 예 | 韓国旅行や韓国料理店で、印象に残ったごま油の香りはありますか | multiple choice: ある / ない / 覚えていない |
| 예 | 主に使いたい料理 | checkbox: ビビンバ / ナムル / キンパ / 卵かけご飯 / ラーメン / 冷奴 / 焼肉 / その他 |
| 예 | 100ml 1,480円なら入荷案内を受け取りたいですか | multiple choice: はい / 迷う / いいえ |
| 예 | 3本 3,980円なら誰かと分けたいですか | multiple choice: はい / 迷う / いいえ |
| 아니오 | 価格や容量へのコメント | paragraph |
| 아니오 | このページをどこで知りましたか / 流入元 | short text |

## 개인정보 문구 초안

ご入力いただいた情報は、韓国式ごま油の入荷案内と需要検証の目的でのみ使用します。正式販売前の検証であり、購入義務はありません。
このフォームでは住所・電話番号・メールアドレスなどの個人情報は集めません。

## 게시 가능 조건

- CTA가 실제 수집 경로로 연결됨
- 폼 응답 저장 위치 확인
- 판매 확정/효능/즉시 배송 표현 제거
- 수입·식품表示 확인 전 결제 받지 않음

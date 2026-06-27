# Notion Form 상태

확인 시각: 2026-06-27T17:10:00+09:00

## 공개 URL

- Primary Form: https://www.notion.so/forms/38c5da6ea39c8149beb3000c9ab0ea98
- Previous Form: https://www.notion.so/forms/38c5da6ea39c81bb879b000c55b872eb
- Database: https://app.notion.com/p/77a3c095b2414c56ace2d5d190c34642
- Data source: `collection://55cebd14-105e-40a3-9296-b0b3adc4a52f`
- Primary form view: `view://38c5da6e-a39c-8149-beb3-000c9ab0ea98`
- Previous form view: `view://38c5da6e-a39c-81bb-879b-000c55b872eb`

## 현재 설정

- `FORM OPEN`
- `FORM ANONYMOUS true`
- `FORM PERMISSIONS none`
- 노출 질문: `Submission` 1줄 입력
- 수집 포맷: 랜딩에서 `流入元 / 香り経験 / 最近買ったごま油 / 使いたい料理 / 100ml価格 / 3本価格 / コメント` 템플릿을 복사하게 한다.
- 한계: Notion MCP의 `SHOW` 설정으로는 공개 Form 질문이 여러 개로 늘어나지 않았다.

## 검증 결과

- `https://www.notion.so/forms/38c5da6ea39c8149beb3000c9ab0ea98` HTTP 200
- page-not-found marker 없음
- form marker 있음
- database fetch 기준 새 form view도 `questions=[Submission]`만 노출
- Notion data source SQL query는 Business plan/Notion AI 요구로 차단됨

## 운영 메모

- 랜딩의 1차 CTA는 Notion Form이다.
- GitHub Issue Form은 로그인 가능한 사용자용 공개 fallback이다.
- Notion 응답 수는 Notion UI 또는 export로 확인한다.
- 채널별 `?src=`는 랜딩의 1줄 응답 메모에 반영된다.

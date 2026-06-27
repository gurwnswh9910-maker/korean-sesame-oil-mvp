# Notion Form 상태

확인 시각: 2026-06-27T17:10:00+09:00

## 공개 URL

- Form: https://www.notion.so/forms/38c5da6ea39c81bb879b000c55b872eb
- Database: https://app.notion.com/p/77a3c095b2414c56ace2d5d190c34642
- Data source: `collection://55cebd14-105e-40a3-9296-b0b3adc4a52f`
- Form view: `view://38c5da6e-a39c-81bb-879b-000c55b872eb`

## 현재 설정

- `FORM OPEN`
- `FORM ANONYMOUS true`
- `FORM PERMISSIONS none`
- 표시 필드: `Submission`, `韓国ごま油の香り経験`, `最近6か月以内に買ったごま油`, `使いたい料理`, `100ml 1,480円`, `3本 3,980円`, `コメント`, `流入元`

## 검증 결과

- `https://www.notion.so/forms/38c5da6ea39c81bb879b000c55b872eb` HTTP 200
- page-not-found marker 없음
- form marker 있음
- Notion data source SQL query는 Business plan/Notion AI 요구로 차단됨

## 운영 메모

- 랜딩의 1차 CTA는 Notion Form이다.
- GitHub Issue Form은 로그인 가능한 사용자용 공개 fallback이다.
- Notion 응답 수는 Notion UI 또는 export로 확인한다.
- 채널별 `?src=`는 Notion Form URL에 붙지만, Notion이 자동 prefill하지 않으면 응답자의 `流入元` 입력으로 대조한다.

## 목적

일본 한국식 방앗간 참기름 MVP 공개 검증을 2주간 추적한다.

## 공개 URL

- Landing: https://korean-sesame-oil-mvp.vercel.app/
- Short note/mobile answer: https://korean-sesame-oil-mvp.vercel.app/answer-note
- Structured quick answer: https://korean-sesame-oil-mvp.vercel.app/quick-answer
- Product-external content MVP: https://korean-sesame-oil-mvp.vercel.app/korea-trip-goma
- Shin-Okubo substitute-check content MVP: https://korean-sesame-oil-mvp.vercel.app/shinokubo-goma
- Home-cooking last-aroma content MVP: https://korean-sesame-oil-mvp.vercel.app/homecook-goma
- Aroma-retention / big-bottle burden content MVP: https://korean-sesame-oil-mvp.vercel.app/aroma-loss-goma
- Shelf-choice / freshness-proof content MVP: https://korean-sesame-oil-mvp.vercel.app/shelf-check
- Shelf-choice short URL: https://korean-sesame-oil-mvp.vercel.app/shelf
- Aroma-retention offline field page: https://korean-sesame-oil-mvp.vercel.app/field-aroma
- Aroma-retention offline field flyer: https://korean-sesame-oil-mvp.vercel.app/field-aroma-flyer
- Primary Notion Form: https://www.notion.so/forms/38c5da6ea39c8149beb3000c9ab0ea98
- Public article: https://korean-sesame-oil-mvp.vercel.app/note
- note post: https://note.com/dreamy_viola8978/n/n77fa3f5a7fe9
- note content post: https://note.com/dreamy_viola8978/n/n3f3af286cf6d
- note Shin-Okubo post: https://note.com/dreamy_viola8978/n/n700b325ba824
- note home-cooking post: https://note.com/dreamy_viola8978/n/n08bad3dce2a9
- note rice-bowl/TKG post: https://note.com/dreamy_viola8978/n/nbb21605544ca
- Public GitHub fallback: https://github.com/gurwnswh9910-maker/korean-sesame-oil-mvp/issues/new?template=waitlist.yml

## 현재 상태

- 1차 리서치: 조건부 진행
- 2차 핵심가설: 한국 여행/방앗간/식당에서 기억한 향을 일본 집밥에 재현하려는 K-food 홈쿡러가 첫 wedge
- 현재 웹 신호 업데이트: `research/03_live_signal_update_20260627.md`; 한국 여행/신오쿠보 향 기억 가설은 보강, 신오쿠보/한국식품점 대체재 인지 가설은 추가
- 공개 발견/벤치마크 업데이트: `research/04_public_discovery_and_benchmark_20260627.md`; exact MVP URL/hashtag search found 0 direct responses, while Korea travel and Osaka Korea Town content strengthen travel-memory and substitute-awareness tests
- MVP: Vercel canonical live; GitHub Pages retained as internal fallback
- Primary CTA: Notion Form live, anonymous/open/no-permission submission setting applied
- Notion Form question shape: current tool-created form exposes `Submission` as a single 1-line answer; landing page provides a copyable answer template to capture source, aroma experience, recent purchase, dishes, price acceptance, and comments.
- GitHub waitlist issues: 0
- Notion response count: Notion UI/export로 확인 필요; MCP SQL query는 Business plan 요구로 차단됨
- Regulatory/unit economics gate: 수요 검증 후 결제 전 `research/02_import_label_unit_economics_gate.md`와 `experiments/unit_economics_template.csv`를 통과해야 함
- Completion audit: `experiments/completion_audit.md`
- First traffic runbook: `mvp/runbook_first_traffic.md`
- Field interview update: 신오쿠보/한국식품점에서 이미 한국식 참기름을 봤거나 산 적이 있는지 묻고, 있으면 제조일/향 보존/소량/재구매 편의가 전환 이유인지 확인
- Channel rules gate: `mvp/channel_rules_and_permission_gate.md`; first account-side post should be note, X/Threads only one manual follow-up post, Konest held for rule check, Tunagate excluded for platform posting
- First note draft: `mvp/note_article_draft.md`
- Vercel article: `docs/note.html` / `docs/note_article.html`; source `article`
- note account-side post: published 2026-06-27T21:46+09:00 at `https://note.com/dreamy_viola8978/n/n77fa3f5a7fe9`; updated 2026-06-27T22:10+09:00 for mobile CTA with `/answer-note`, `/share?src=note_kfood`, and a note comment template
- note product-external content post: published 2026-06-27T23:38+09:00 at `https://note.com/dreamy_viola8978/n/n3f3af286cf6d`; source `note_content_travel`; asks last purchase place, aroma retention, and switching conditions before direct purchase intent
- `/answer-note` mobile answer hub: changed from Notion direct redirect to a Vercel page with note comment, Notion form, copyable memo, and detail-page choices to reduce mobile dropoff
- `/quick-answer` structured answer composer: added to turn multi-question choices into a single Notion-compatible `Submission`, reducing friction from the 1-line Notion form while preserving purchase-context fields
- Product-external content MVP: `/korea-trip-goma` added to test target density through Korea travel/Shin-Okubo/home-cooking content before asking direct purchase intent
- Shin-Okubo substitute-check MVP: `/shinokubo-goma` added to test whether people who already buy or browse Korean sesame oil in Shin-Okubo/Korean supermarkets have a switching reason around store/brand, volume/price, aroma retention, manufacturing date, 100ml small bottle, or repurchase convenience
- Home-cooking last-aroma MVP: `/homecook-goma` added to test whether people making bibimbap/namul/kimbap/TKG/ramen/cold tofu/Korean seaweed rice have a last-aroma or aroma-retention problem strong enough to switch sesame oil
- Aroma-retention MVP: `/aroma-loss-goma` added to test whether large bottles lose aroma before use-up and whether opened duration, remaining-bottle aroma, 100ml small bottle, manufacturing date, or light-blocking bottle create a stronger switching reason
- Shelf-choice MVP: `/shelf-check` and short route `/shelf` added to test whether people looking at existing Korean sesame oil or aroma-heavy Japanese sesame oil candidates need manufacturing-date/fresh-pressing/aroma-retention proof before switching
- Offline aroma-retention field kit: `/field-aroma` and QR target `/quick-answer?src=offline_aromaloss` added for high-intent Shin-Okubo/Korean supermarket interviews; this is not counted until real rows are entered in `experiments/field_interview_log.csv`
- Need/problem frame: `검증/욕구_문제_가설_20260627.md`; strong content response requires recent purchase place, brand/store, volume/price, usage dish, aroma-retention experience, and a switching condition or complaint
- `/answer-note` deployment check: first rewrite-only deploy returned 404, fixed by adding `docs/answer-note.html`; final production uses file-based clean URL without the underscore duplicate/rewrite, returns 200 with title `30秒回答 | 韓国式しぼりたてごま油`, no redirect, and mobile/desktop Playwright overflow count 0
- Article response controls: direct Notion form links, copyable 1-line answer memo, X share intent, LINE share link, and URL copy button
- X public answer path: MVP pages include `Xで公開回答` intent links with hashtag `#韓国ごま油検証`; only real answer URLs recorded in `experiments/public_social_responses.csv` count as responses
- note account-side posting: live and mobile-first; public note has no GitHub Pages links, auto translation off, AI training compensation off, comments on, and tags `#韓国旅行 #韓国料理 #新大久保 #ごま油 #おうち韓国`
- note Shin-Okubo posting: published 2026-06-28T01:04:46+09:00 at `https://note.com/dreamy_viola8978/n/n700b325ba824`; source `note_content_shinokubo`; free, comments on, auto translation disabled, AI learning reward excluded, tags `#韓国料理 #新大久保 #ごま油 #韓国食品 #おうち韓国`
- note home-cooking posting: published 2026-06-28T01:49:44+09:00 at `https://note.com/dreamy_viola8978/n/n08bad3dce2a9`; source `note_content_homecook`; free, comments on, auto translation disabled, AI learning reward excluded, tags `#韓国料理 #ビビンバ #ナムル #ごま油 #おうち韓国`
- note rice-bowl/TKG posting: published 2026-06-28T02:20:24+09:00 at `https://note.com/dreamy_viola8978/n/nbb21605544ca`; source `note_content_homecook_ricebowl`; free, comments on, auto translation disabled, AI learning reward excluded, tags `#卵かけご飯 #韓国海苔 #ごま油 #おうちごはん #韓国料理`
- note dashboard precheck: 2026-06-27T22:30+09:00 dashboard shows 0 views / 0 comments / 0 スキ, but latest aggregation is 2026-06-27 21:45, before the 21:46 publish time, so this is not counted as post-publish zero response
- current response check: GitHub waitlist label issues `[]`, local public/social and field files have no real rows, Notion export absent, Notion data-source search found no response rows, and exact `/answer-note` URL web search found no public response/share
- 24h follow-up automation: Codex heartbeat `note-24h` scheduled for 2026-06-28T21:50+09:00
- Validation signal summary: `experiments/validation_signal_summary.md`, generated by `scripts/summarize_validation_signals.py`; current verdict `insufficient_external_evidence`, total respondents `0`
- Automation: `.github/workflows/summarize-waitlist.yml` runs daily, on waitlist issues, manually, and on push to response input CSVs/channel log to refresh validation summaries
- Latest deploy: 2026-06-28T00:08+09:00 added `/quick-answer`; production inspect `https://vercel.com/gurwnswh9910-makers-projects/korean-sesame-oil-mvp/ASmFY1pCzn4aNWcheknGJiEBkPvz`; browser mobile390 verified source propagation, note route mapping, memo generation, overflow count 0
- 2026-06-28T00:32+09:00 update: `/korea-trip-goma?src=note_content_travel` now has a first-screen `/quick-answer` CTA; production inspect `https://vercel.com/gurwnswh9910-makers-projects/korean-sesame-oil-mvp/FojaxfiyMfUzn9YorE2KJxJMajsR`; latest response recheck still found 0 real responses
- 2026-06-28T01:05+09:00 update: `/shinokubo-goma` deployed and note Shin-Okubo post published at `https://note.com/dreamy_viola8978/n/n700b325ba824`; public HTTP/API checks passed; real response count remains 0 until Notion rows, note comments, public answer URLs, GitHub issues, or field interviews appear
- 2026-06-28T01:55+09:00 update: `/homecook-goma` deployed/refined with Korean seaweed rice/TKG sub-wedge and note home-cooking post published at `https://note.com/dreamy_viola8978/n/n08bad3dce2a9`; public HTTP/API/browser checks passed; real response count remains 0 until Notion rows, note comments, public answer URLs, GitHub issues, or field interviews appear
- 2026-06-28T02:12+09:00 update: note dashboard/API early check shows 5 total views, 0 comments, 0 likes, 0 waitlist issues, and no Notion submission rows found via available search. `/answer-note` and `/quick-answer` note comment routing now sends `note_content_travel` to note 2, `note_content_shinokubo` to note 3, and `note_content_homecook` to note 4; `/homecook-goma?src=note_content_homecook` now shows a note comment CTA.
- 2026-06-28T02:20+09:00 update: note rice-bowl/TKG post published at `https://note.com/dreamy_viola8978/n/nbb21605544ca` with source `note_content_homecook_ricebowl`; this tests lighter daily scenes such as Korean seaweed rice and TKG before counting any demand evidence.
- 2026-06-28T02:27+09:00 update: rice-bowl/TKG source routing corrected and redeployed; `/quick-answer`, `/answer-note`, and `/homecook-goma` with `src=note_content_homecook_ricebowl` all send the note comment CTA back to note 5 `https://note.com/dreamy_viola8978/n/nbb21605544ca`; real response count remains 0.
- 2026-06-28T02:39+09:00 update: post-publish recheck still found 0 real responses. GitHub waitlist is empty, local social/interview files have no real rows, Notion export is absent, note API shows all five posts published with like_count/comment_count 0, note profile lists all five posts, and note dashboard still shows latest aggregation 2026-06-28 01:31 with only note 1 at 5 views / 0 comments / 0 likes. Next problem priority is open-after-aroma loss / big-bottle burden before adding more note posts.
- 2026-06-28T02:57+09:00 update: `/aroma-loss-goma` deployed for open-after-aroma loss / big-bottle burden with source `content_aromaloss`; `/quick-answer` now captures `開封後どのくらい`; production inspect `https://vercel.com/gurwnswh9910-makers-projects/korean-sesame-oil-mvp/8YMa5hWcnStVF1siPwCpuLAKWs42`; mobile390 browser checks passed for `/aroma-loss-goma`, `/quick-answer`, and landing source/link/overflow behavior. `mvp/note_aromaloss_posting_packet.md` is ready_not_published until 24h recheck; real response count remains 0.
- 2026-06-28T03:07+09:00 update: response recheck still found 0 real responses; note API for all five posts remains like_count/comment_count 0. Added `research/05_aroma_retention_review_language_20260628.md`; aroma-loss language is supported by official storage guidance and consumer Q&A, but cheap 110ml Korean substitutes mean 100ml 1,480 yen needs manufacturing-date/fresh-pressing/aroma-retention proof, not small size alone.
- 2026-06-28T10:42+09:00 update: added and deployed the offline aroma-retention field kit at `/field-aroma`, flyer `/field-aroma-flyer`, and QR target `/quick-answer?src=offline_aromaloss`; QR decode, PDF inspection, and production HTTP checks passed. Validation summary still reports total respondents 0, channel rows 17, posted/public rows 13.
- 2026-06-28T11:02+09:00 update: added and deployed `/shelf-check` and `/shelf` for shelf-choice/freshness-proof validation with source `content_shelfcheck`; `/quick-answer` now accepts `最後に買ったまたは見た場所`; production HTTP and Chrome mobile checks passed. This is not demand evidence until real responses mention candidate product/store, volume-price, hesitation reason, switching proof, and price reaction. Validation summary remains total respondents 0, channel rows 18, posted/public rows 14.

## 성공 기준

- 방문자 300명 이상에서 CTA 클릭률 3% 이상
- 2주 내 관심 신호 30건 또는 구매 전제 대화 10건
- 가격 포함 회신 중 30% 이상이 긍정
- 인터뷰/댓글 중 최근 한국식 참기름 구매 또는 탐색 경험 30% 이상

## 중단/피벗 기준

- 300명 이상 노출 후 CTA 클릭률 1% 미만
- 가격 제시 후 대부분 이탈
- 수입/라벨/배송 단가 때문에 100ml 소비자가가 2,000엔 이상으로 상승
- 수입신고, 일본어 표시, 알레르겐/보존/기한, 수입자/표시책임자 경로가 불명확함

## 일일 기록 형식

```csv
date,channel,post_url,message_variant,visits,cta_clicks,form_submits,reply_count,interviews_done,price_accepted_count,sample_purchase_requests,notes
```

## 운영 메모

Notion Form과 GitHub fallback 모두 주소, 전화번호, 이메일을 받지 않는다. 정식 수입/표시 확인 전 결제는 받지 않는다.

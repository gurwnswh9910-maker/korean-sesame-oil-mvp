# 일본 수입·표시·원가 Gate

작성일: 2026-06-27

## 결론

수요 검증은 계속하되, 실제 판매형 MVP로 넘어가기 전에는 `수입신고 + 일본어 표시 + 알레르겐/원재료/보존/기한 + 샘플 단가` gate를 통과해야 한다. 특히 참기름은 향을 팔수록 제조일, 산패관리, 차광/보관 조건이 상품 신뢰의 일부가 된다.

## 공식 확인 사항

| 항목 | 확인 내용 | MVP 판단 |
|---|---|---|
| 식품 수입신고 | MHLW는 판매 또는 영업 목적 식품 수입 시 Food Sanitation Act Article 27에 따른 import notification이 필요하고, 신고 전 수입 식품을 판매/영업에 사용할 수 없다고 안내한다. | 결제/판매 전 수입자와 검역소 절차 확인 필수 |
| 우편/소량 수입 | MHLW는 우편으로 들어온 식품도 판매/영업 목적이면 수입신고 대상이라고 설명한다. 개인 사용은 면제될 수 있으나, 판매 목적은 양과 방식이 작아도 별도 취급하면 안 된다. | 10~30병 샘플도 판매 목적이면 개인 반입처럼 처리하지 않는다 |
| 일본어 식품 표시 | CAA 식품표시 자료는 포장 가공식품에 명칭, 원재료, 알레르겐 등 표시 항목이 필요하다고 설명한다. | 한국어 라벨 그대로 판매하지 않는다 |
| 알레르겐 | CAA의 2026년 알레르기 표시 안내는 표시 대상 알레르겐이 의무 표시와 권장 표시로 나뉘며, 2026년 개정 정보를 공지한다. 참깨/ごま는 표시 실무에서 반드시 확인해야 할 핵심 항목이다. | `ごま` 표시와 제조라인 교차접촉을 라벨 체크리스트에 넣는다 |
| 세번/관세 후보 | Japan Customs 2024 tariff schedule에는 `1515.50 Sesame oil and its fractions`가 있고, 세분은 산가 0.6 초과/이하로 나뉜다. NACCS 품목코드도 `1515.50-100`과 `1515.50-200`을 둔다. | 산가/성분서가 없으면 HS/세율 판단이 흐려진다 |
| 수입 모니터링 | MHLW FY2026 plan은 일본의 상업 목적 식품 수입 신고가 대규모로 관리되고, 위반 사례/검사가 존재한다고 설명한다. | “작게 들여오면 괜찮다”가 아니라 검역소/수입자 확인을 전제로 둔다 |

## 판매형 MVP로 넘어가기 전 필수 자료

1. 한국 공급자 정보: 제조자, 제조장 주소, 사업자 정보, HACCP/위생 관련 보유 자료
2. 제품 사양서: 원재료명, 원산지, 제조공정, 산가 또는 품질 규격, 유통기한, 보관 조건
3. 포장 정보: 용량, 용기 재질, 차광 여부, 누유 테스트, 병/캡/실링 사양
4. 일본어 라벨 초안: 명칭, 원재료, 내용량,賞味期限, 보존방법, 원산국명, 수입자, 알레르겐, 영양성분
5. 수입자/표시 책임자: 일본 내 수입 신고와 표시 책임을 맡을 주체
6. 배송 조건: 한국 내 픽업, 국제 운송, 일본 내 배송, 파손/누유/고온 대응
7. 단가표: 100ml 1병과 3병 세트 각각의 landed cost와 contribution margin

## Go / Pivot / Stop Gate

| Gate | Go | Pivot | Stop |
|---|---|---|---|
| 수입 절차 | 수입자/검역소 경로와 필요 서류가 명확하다 | 서류는 가능하지만 MOQ/대행비가 커서 선예약 수량을 늘려야 한다 | 판매 목적 수입 경로가 불명확하거나 샘플 판매도 막힌다 |
| 라벨 | 일본어 표시 초안과 알레르겐/보관/기한 정보가 준비된다 | 라벨 비용 때문에 100ml 단가가 상승한다 | 표시 책임자를 확보하지 못한다 |
| 단가 | 100ml 1,480엔에서 변동비 후 contribution margin 30% 이상 | 1,480엔은 어렵고 3병 세트/선물 세트만 가능하다 | 100ml 소비자가 2,000엔 이상이어야 손익이 맞는다 |
| 신선도 | 제조일/유통기한/차광/보관 설명이 신뢰를 만든다 | 냉장/단기 유통을 전제로 소량 드롭만 가능하다 | 산패/누유/고온 리스크를 통제할 방법이 없다 |

## 다음 실행

- `experiments/unit_economics_template.csv`에 실제 공급가, 물류비, 라벨/포장비, 수입대행비를 채운다.
- 10명 인터뷰에서 `100ml 1,480엔`, `3本 3,980円`, `2,000円超え` 반응을 분리한다.
- 실제 결제는 수입/표시 gate 통과 전에는 받지 않는다.

## 참고 소스

- MHLW Import Procedure under Food Sanitation Act: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/shokuhin/yunyu_kanshi/kanshi/index_00004.html
- CAA Japan's Food Labelling System: https://www.caa.go.jp/en/policy/food_labeling/assets/food_labeling_cms204_240425_01.pdf
- CAA Food Allergen Labelling Information: https://www.caa.go.jp/policies/policy/food_labeling/food_sanitation/allergy/
- CAA 2026 allergen labelling guide PDF: https://www.caa.go.jp/policies/policy/food_labeling/food_sanitation/allergy/assets/food_labeling_cms204_260401_02.pdf
- Japan Customs Tariff Schedule Chapter 15: https://www.customs.go.jp/english/tariff/2024_04_01/data/e_15.htm
- Japan Customs NACCS code list 2024: https://www.customs.go.jp/tariff/2024_04_01/naccscode202404_2.html
- MHLW Imported Foods Monitoring and Guidance Plan FY2026: https://www.mhlw.go.jp/content/001711310.pdf

---
schema_version: '1.0'
number: 14
technical_id: layered-atmospheric-depth-control
title_ko: 대기 원근을 보존하는 층별 풍경 깊이 조절
summary_ko: 풍경을 전경·피사체·원경·하늘 층으로 나누고 국소 대비와 대기 효과를 절제해 조절하여 자연스러운 깊이를 만든다.
version: 1.0.0
status: active
supported_tools:
- generate_ai
confidence: 0.87
raw_scenario_ids:
- raw-20260802-landscapemask01
- raw-20260803-fogdepth01
- raw-20260804-localdehaze01
- raw-20260805-churchlight01
source_urls:
- https://fstoppers.com/lightroom/how-add-real-depth-lightroom-without-overediting-900105
- https://fstoppers.com/lightroom/simple-lightroom-steps-make-subject-pop-722610
- https://fstoppers.com/photoshop/photoshop-2026s-dehaze-tool-more-powerful-think-901680
- https://www.adobe.com/learn/lightroom-cc/web/ai-masking-for-landscape-photos
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 대기 원근을 보존하는 층별 풍경 깊이 조절

풍경을 전경·피사체·원경·하늘 층으로 나누고 국소 대비와 대기 효과를 절제해 조절하여 자연스러운 깊이를 만든다.

## 적용 조건

- 안개·박무·설경·다층 풍경에서 전경과 원경이 평평하게 겹쳐 깊이가 약한 경우에 적용한다.
- 원경의 정의를 일부 회복하면서 대기 원근과 자연스러운 층을 보존해야 하는 경우에 적용한다.

## 기술 절차

1. 기본 노출과 노이즈를 먼저 정리한다.
2. 하늘·원경·주요 피사체·전경을 깊이 층으로 구분한다.
3. 전체 대기감은 보존하면서 필요한 원경 또는 피사체 층에만 대비·Dehaze·색을 절제해 더한다.
4. 주변과 프레임 가장자리는 필요할 때만 감광하고 기존 빛 방향에 맞는 밝은 유도 영역을 만든다.
5. 각 층의 경계가 자연스럽고 안개·눈·하늘의 연속성이 유지되는지 확인한다.

## 파라미터 가이드

- 노출·Dehaze·Vibrance 수치가 없는 근거는 층이 구분되되 효과가 먼저 보이지 않는 정성 범위로 사용한다.
- 안개 풍경에서는 Clarity와 Dehaze를 전역으로 낮춰 부드러움을 유지한 뒤 필요한 원경에만 선택적으로 정의를 더한다.
- 방향성 밝기와 감광은 하이라이트·암부 클리핑이 없는 범위에서 조절한다.

## 판단 근거

- 안개 풍경, 국소 Dehaze, 풍경 자동 마스크, 평평한 설경 건축 사례가 층별 선택과 절제된 명암 배치로 깊이를 만드는 원리를 독립적으로 보여 준다.
- 풍경 편집에서 결과 영향과 재사용성이 높고 Generate AI lighting-weather로 실행 가능하다.

## 주의사항

- 원경 전체에 강한 Dehaze를 적용하면 안개와 대기 원근이 사라진다.
- 경계별 밝기 차이를 과장하면 halo와 인공적인 빛 띠가 생긴다.
- 평평한 설경에서 하이라이트를 올릴 때 클리핑을 확인한다.

## 충돌 및 예외

- 몽환적 스타일이 최종 의도라면 원경 정의를 강하게 복원하지 말고 부드러운 대기 층을 우선한다.

## raw 근거

- raw-20260803-fogdepth01
- raw-20260804-localdehaze01
- raw-20260802-landscapemask01
- raw-20260805-churchlight01

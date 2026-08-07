---
schema_version: '1.0'
number: 2
technical_id: natural-subject-background-separation
title_ko: 피사체·배경 독립 톤 조정으로 자연스러운 분리 만들기
summary_ko: 피사체와 배경을 독립적으로 밝기 조정하고 기존 광원에 맞는 방향성을 더해 전역 보정 없이 자연스러운 시각적 분리를 만든다.
version: 1.0.0
status: active
supported_tools:
- generate_ai
confidence: 0.93
raw_scenario_ids:
- raw-20260802-vintageback01
- raw-20260803-subjectlight01
- raw-20260804-radiallight01
- raw-20260805-churchlight01
- raw-20260807-adobeperson01
- raw-20260807-portraitsplit01
- raw-20260807-subjectpop01
source_urls:
- https://fstoppers.com/education/how-edit-portrait-skin-tones-lightroom-902830
- https://fstoppers.com/education/how-make-your-subject-pop-using-lightroom-and-photoshop-902810
- https://fstoppers.com/lightroom/simple-lightroom-steps-make-subject-pop-722610
- https://www.adobe.com/learn/lightroom-cc/web/dodge-burn-radial-gradient
- https://www.adobe.com/learn/lightroom-cc/web/masking-basics-lightroom-web
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 피사체·배경 독립 톤 조정으로 자연스러운 분리 만들기

피사체와 배경을 독립적으로 밝기 조정하고 기존 광원에 맞는 방향성을 더해 전역 보정 없이 자연스러운 시각적 분리를 만든다.

## 적용 조건

- 인물·야생동물·건축물의 밝기와 배경 밝기가 비슷해 피사체 분리가 약한 사진에 적용한다.
- 전체 노출 조정으로는 피사체와 배경을 동시에 적절히 맞출 수 없는 장면에 적용한다.

## 기술 절차

1. 이미지 전체의 기본 노출을 먼저 정리한다.
2. 피사체와 배경을 의미적으로 분리해 각각 독립 조정 영역으로 취급한다.
3. 저노출 피사체는 밝히고 산만하거나 밝은 배경은 절제해 낮춘다.
4. 필요하면 한쪽에서 들어오는 듯한 방향성 빛을 추가하되 피사체 형태와 기존 광원에 맞춘다.
5. 확대 화면에서 경계를 확인한 뒤 전체 화면에서 분리 효과가 자연스러운지 전후 비교한다.

## 파라미터 가이드

- 피사체는 하이라이트와 피부·털 디테일이 남는 범위에서 밝히고, 배경은 주의가 덜 가는 정도로만 낮춘다.
- 수치가 제시되지 않은 근거는 정성 방향으로만 사용하고 고정 EV 값을 만들지 않는다.
- 경계에 띠가 보이면 밝기 차이를 줄이거나 선택 범위를 수정한다.

## 판단 근거

- 서로 다른 출처의 인물·야생동물·풍경 사례에서 피사체와 배경의 상반된 국소 톤 조정이 반복된다.
- 전역 보정으로 해결하기 어려운 분리 문제를 직접 해결하고 결과 영향과 재사용성이 크다.
- Generate AI의 identity-preserve 또는 lighting-weather 편집으로 실행할 수 있다.

## 주의사항

- 피사체를 과도하게 밝히고 배경을 과도하게 어둡게 하면 오려 붙인 듯한 경계와 halo가 생긴다.
- 머리카락·털·의상 가장자리의 누락과 과선택을 확대해 확인한다.
- 원래 광원 방향과 모순되는 밝기 분포를 만들지 않는다.

## 충돌 및 예외

- 몽환적이거나 저대비가 의도된 사진에서는 분리를 강하게 만들기보다 원래 분위기를 보존해야 한다.

## raw 근거

- raw-20260802-vintageback01
- raw-20260803-subjectlight01
- raw-20260807-subjectpop01
- raw-20260807-adobeperson01
- raw-20260807-portraitsplit01
- raw-20260804-radiallight01
- raw-20260805-churchlight01

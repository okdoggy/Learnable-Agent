---
schema_version: '1.0'
number: 4
technical_id: semantic-mask-composition-and-edge-check
title_ko: 의미 마스크 합성과 경계 검증으로 국소 편집 정밀화
summary_ko: 의미 선택과 그라디언트 방향을 합성하고 Add·Subtract·Intersect 및 경계 검사를 거쳐 자동 선택의 번짐과 halo를 방지한다.
version: 1.0.0
status: active
supported_tools:
- generate_ai
confidence: 0.94
raw_scenario_ids:
- raw-20260802-skygradient01
- raw-20260805-brushcontrol01
- raw-20260805-intersectlight01
- raw-20260807-adobesky01
- raw-20260807-objectexposure01
- raw-20260807-subjectpop01
source_urls:
- https://fstoppers.com/education/how-make-your-subject-pop-using-lightroom-and-photoshop-902810
- https://fstoppers.com/lightroom/intersect-masks-control-youre-missing-lightroom-721432
- https://www.adobe.com/learn/lightroom-cc/web/advanced-lightroom-masking
- https://www.adobe.com/learn/lightroom-cc/web/masking-basics-lightroom-web
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 의미 마스크 합성과 경계 검증으로 국소 편집 정밀화

의미 선택과 그라디언트 방향을 합성하고 Add·Subtract·Intersect 및 경계 검사를 거쳐 자동 선택의 번짐과 halo를 방지한다.

## 적용 조건

- AI 자동 선택이 산 능선·머리카락·바위·건축 경계에서 너무 넓거나 좁게 잡힌 경우에 적용한다.
- 그라디언트의 방향성과 피사체·하늘·객체 의미 선택을 함께 사용해야 하는 국소 조명 편집에 적용한다.

## 기술 절차

1. 피사체·하늘·배경·객체 중 편집 목적에 맞는 기본 의미 영역을 선택한다.
2. 방향성이 필요하면 Linear 또는 Radial 형태와 의미 영역의 교집합을 만든다.
3. 과선택은 제외하고 누락은 추가한다.
4. 산 능선·머리카락·털·건축 경계를 확대해 halo와 띠를 확인한다.
5. 조정 효과를 끄고 켜며 선택 오류와 보정 강도를 각각 분리해 검증한다.

## 파라미터 가이드

- 먼저 넓은 의미 선택을 만들고 Add·Subtract·Intersect로 필요한 영역만 남긴다.
- 경계 보정량은 halo가 보이지 않는 최소 수준으로 유지한다.
- Flow는 반복 획의 누적 속도, Density는 최대 적용량으로 구분해 사용한다는 근거를 따른다.

## 판단 근거

- Adobe 공식 사례와 Fstoppers 사례에서 의미 선택과 기하학적 마스크의 합성, Add·Subtract·Intersect, 경계 검사가 반복된다.
- 자동 선택 실패를 조기에 발견해 국소 보정의 가장 흔한 아티팩트를 예방한다.
- Generate AI 정밀 편집 프롬프트에서 적용 영역·보호 영역·경계 조건을 명시하는 방식으로 직접 재사용할 수 있다.

## 주의사항

- 자동 선택 결과를 검사하지 않고 강한 조정을 적용하면 halo와 어두운 띠가 생긴다.
- 부드러운 대기 경계에 단단한 선택을 강제하면 깊이감이 손상된다.
- 브러시 보정만 반복해 의미 선택의 구조를 잃지 않도록 한다.

## 충돌 및 예외

- 단단한 수평선에는 경계 정렬이 유효하지만 안개나 털처럼 본래 부드러운 경계에는 더 넓은 전이와 낮은 강도가 필요하다.

## raw 근거

- raw-20260802-skygradient01
- raw-20260805-intersectlight01
- raw-20260807-objectexposure01
- raw-20260807-adobesky01
- raw-20260805-brushcontrol01
- raw-20260807-subjectpop01

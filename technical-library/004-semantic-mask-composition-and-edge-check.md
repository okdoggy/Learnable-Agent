---
schema_version: '1.0'
number: 4
technical_id: semantic-mask-composition-and-edge-check
title_ko: 의미 마스크 합성과 경계 검증으로 국소 편집 정밀화
summary_ko: 의미 선택과 공간 마스크를 합성하고 Add·Subtract·Intersect, 오버레이 검사, Edge·Feather 조정으로 자동 선택의 누락·번짐·딱딱한 seam과
  halo를 줄인다.
version: 1.0.3
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
- raw-20260808-dodgeburnplan01
- raw-20260808-waterintersect01
- raw-20260809-maskrefine01
- raw-20260810-maskedge
source_urls:
- https://fstoppers.com/education/how-make-your-subject-pop-using-lightroom-and-photoshop-902810
- https://fstoppers.com/education/lightrooms-intersect-mask-tool-can-solve-edits-youve-been-doing-hard-way-903413
- https://fstoppers.com/education/two-new-sliders-make-every-lightroom-mask-look-more-natural-903883
- https://fstoppers.com/lightroom/intersect-masks-control-youre-missing-lightroom-721432
- https://helpx.adobe.com/lightroom/desktop/edit-photos/masking.html
- https://www.adobe.com/learn/lightroom-cc/web/advanced-lightroom-masking
- https://www.adobe.com/learn/lightroom-cc/web/masking-basics-lightroom-web
reviewed_at: '2026-08-10'
created_by: hermes-llm
---

# 의미 마스크 합성과 경계 검증으로 국소 편집 정밀화

의미 선택과 공간 마스크를 합성하고 Add·Subtract·Intersect, 오버레이 검사, Edge·Feather 조정으로 자동 선택의 누락·번짐·딱딱한 seam과 halo를 줄인다.

## 적용 조건

- AI 자동 선택이 산 능선·나뭇가지·털·머리카락·바위·건축·물 경계에서 너무 넓거나 좁게 잡힌 경우에 적용한다.
- 그라디언트의 공간 범위와 피사체·하늘·배경·객체·물 같은 의미 영역을 함께 제한해야 하는 국소 편집에 적용한다.
- 실제 톤·밝기 조정에서 딱딱한 seam이나 halo가 드러나는 복잡한 경계에 적용한다.

## 기술 절차

1. 편집 목적에 맞는 기본 의미 영역을 선택한다.
2. 오버레이 표시를 바꿔 누락과 넘침을 검사한다.
3. 방향성이나 공간 범위가 필요하면 Linear 또는 Radial Gradient와 의미 영역의 교집합만 남긴다.
4. 과선택은 Subtract로 제외하고 누락은 Add로 보완한다.
5. 실제 보정 강도를 적용해 경계 문제를 드러낸 뒤 선택이 부족하면 Edge를 확장 방향으로, 번지면 수축 방향으로 조정한다.
6. 딱딱한 전환은 Feather로 완화하고 최종 강도에서 확대해 halo·띠·질감 번짐을 확인한다.

## 파라미터 가이드

- Mask Feather의 원문 조절 범위는 0~100이며, 범위 전체를 임의로 쓰지 말고 seam이 사라지는 최소량만 사용한다.
- Mask Edge의 시작 위치는 0이며 선택 수축은 왼쪽, 확장은 오른쪽 방향이다.
- Flow는 반복 획의 누적 속도, Density는 최대 적용량으로 구분한다.
- 고정 수치가 없는 국소 조정은 주변 영역이 변하지 않고 목표가 자연스럽게 읽히는 범위에서 정성적으로 결정한다.

## 판단 근거

- Adobe 공식 사례와 여러 Fstoppers 사례에서 의미 선택, 기하학적 마스크 합성, Add·Subtract·Intersect, 경계 검사가 반복된다.
- 새 근거는 실제 보정을 먼저 적용한 상태에서 Edge로 선택 범위를 교정하고 Feather로 전환을 부드럽게 하는 절차를 보강한다.
- 자동 선택 실패와 국소 조명 번짐을 예방하며 Generate AI 정밀 편집의 적용·보호 영역 명세로 직접 재사용할 수 있다.

## 주의사항

- 자동 선택 결과를 검사하지 않고 강한 조정을 적용하면 halo, 어두운 띠, 주변 질감 과장이 생길 수 있다.
- 안개·털·물보라처럼 본래 부드러운 경계에 단단한 선택을 강제하지 않는다.
- Edge 확장은 인접 영역 침범을 만들 수 있으므로 나뭇가지·털·수평선을 확대 검사한다.
- Brush·Linear Gradient·Radial Gradient는 자체 feather 제어가 있으므로 AI 의미 마스크용 Edge·Feather 절차와 혼동하지 않는다.

## 충돌 및 예외

- 단단한 수평선·건축 경계에는 정밀 정렬이 유효하지만 부드러운 대기 경계에는 넓은 전이와 낮은 강도가 필요하다.
- 의미 영역 전체를 균일하게 보정할 때는 불필요한 공간 교차를 추가하지 않는다.

## raw 근거

- raw-20260802-skygradient01
- raw-20260805-intersectlight01
- raw-20260807-objectexposure01
- raw-20260807-adobesky01
- raw-20260805-brushcontrol01
- raw-20260807-subjectpop01
- raw-20260808-waterintersect01
- raw-20260808-dodgeburnplan01
- raw-20260809-maskrefine01
- raw-20260810-maskedge

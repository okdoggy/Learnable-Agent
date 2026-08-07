---
schema_version: '1.0'
scenario_id: raw-20260804-radiallight01
title_ko: Radial Gradient 복제와 반전으로 인물 주변의 빛 분포 재구성
status: validated
source:
  type: official
  publisher: Adobe Lightroom Learn
  author: unknown
  url: https://www.adobe.com/learn/lightroom-cc/web/dodge-burn-radial-gradient
  published_at: '2026-06-11'
  accessed_at: '2026-08-04T00:00:40Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: environmental-portrait
  condition:
  - uneven-lighting
  - dark-subject
  - bright-distraction
  intent:
  - local-dodge-and-burn
  - guide-attention
  - recover-shadow-detail
method:
  steps:
  - tool: Radial Gradient
    parameter: 어두운 얼굴이나 나무 위에 타원을 배치하고 Invert
    value: null
    unit: null
    reported_as: qualitative
  - tool: Exposure and Temperature
    parameter: 선택 내부의 Exposure와 Temperature를 올려 밝고 따뜻하게 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Radial Gradient Duplicate
    parameter: 기존 그라디언트를 복제해 다른 어두운 영역으로 이동·회전·크기 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Radial Gradient
    parameter: 밝고 산만한 자동차와 도로의 Exposure를 낮춤
    value: null
    unit: null
    reported_as: qualitative
  - tool: Mask overlay
    parameter: 파란 핀에 마우스를 올려 빨간 오버레이 확인
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 각 영역에 독립적인 Radial Gradient를 사용하면 전체 노출을 바꾸지 않고 어두운 피사체는 밝히고 밝은 방해물은 눌러 시선을 재배치할 수 있다.
- 기존 그라디언트를 복제하면 여러 영역에 비슷한 빛의 색과 성격을 빠르게 유지할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 222387557d80b8b3baf079728735cb40e36dd1f7a78266ad8ff2579aa31a18eb
  collected_at: '2026-08-04T00:00:40Z'
---

# Radial Gradient 복제와 반전으로 인물 주변의 빛 분포 재구성

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

환경 인물에서 얼굴과 주변 나무가 너무 어둡고 자동차나 도로가 지나치게 밝아 시선이 분산될 때, 전체 노출을 바꾸지 않고 국소적으로 닷지 앤 번을 적용한다.

## 촬영/작업 순서

1. 얼굴 위에 Radial Gradient 타원을 배치하고 위치와 크기를 맞춘 뒤 Invert로 타원 내부를 선택한다.
2. Exposure와 Temperature를 올려 얼굴을 밝고 따뜻하게 만들고 세부를 드러낸다.
3. 그라디언트를 복제해 어두운 나무로 이동한 뒤 크기와 회전을 맞추고 필요하면 Exposure, Shadows, Whites, Blacks를 추가 조정한다.
4. 자동차와 도로처럼 밝고 산만한 영역에 별도 Radial Gradient를 만들고 Exposure를 낮춘다.
5. 각 파란 핀의 빨간 마스크 오버레이를 확인해 보정이 의도한 영역에만 적용되는지 검토한다.

## 추천 시작값 / 조작값

- Radial Gradient / 어두운 얼굴이나 나무 위에 타원을 배치하고 Invert: 원문 정성 표현(수치 추정 없음)
- Exposure and Temperature / 선택 내부의 Exposure와 Temperature를 올려 밝고 따뜻하게 조정: 원문 정성 표현(수치 추정 없음)
- Radial Gradient Duplicate / 기존 그라디언트를 복제해 다른 어두운 영역으로 이동·회전·크기 조정: 원문 정성 표현(수치 추정 없음)
- Radial Gradient / 밝고 산만한 자동차와 도로의 Exposure를 낮춤: 원문 정성 표현(수치 추정 없음)
- Mask overlay / 파란 핀에 마우스를 올려 빨간 오버레이 확인: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 밝히는 마스크와 어둡게 하는 마스크를 분리해 각각 위치·크기·회전·반전을 조정한다.
- 같은 광색이 필요한 어두운 영역은 기존 그라디언트를 복제해 일관성을 유지한다.
- 마스크를 숨긴 전체 화면에서 시선이 인물로 모이고 국소 보정 경계가 보이지 않는지 확인한다.

## 주의할 점

- Radial Gradient는 기본적으로 타원 바깥쪽에 적용되므로 내부를 밝힐 때 Invert 상태를 확인한다.
- 너무 작은 타원이나 부드럽지 않은 배치는 얼굴 주변에 인공적인 빛 얼룩을 만들 수 있다.
- 복제한 마스크도 대상의 밝기 차이에 맞게 Exposure를 다시 조정해야 한다.

## 확실성과 근거

- 각 영역에 독립적인 Radial Gradient를 사용하면 전체 노출을 바꾸지 않고 어두운 피사체는 밝히고 밝은 방해물은 눌러 시선을 재배치할 수 있다.
- 기존 그라디언트를 복제하면 여러 영역에 비슷한 빛의 색과 성격을 빠르게 유지할 수 있다.

Adobe 튜토리얼이 얼굴 내부 반전 마스크의 밝기·온도 보정, 나무로의 그라디언트 복제, 자동차와 도로의 감광, 마스크 오버레이 확인을 직접 설명한다. 정확한 슬라이더 수치는 제시하지 않았다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/dodge-burn-radial-gradient
- 접근일: 2026-08-04

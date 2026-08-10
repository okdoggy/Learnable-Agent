---
schema_version: '1.0'
scenario_id: raw-20260808-localdenoise01
title_ko: 미세 질감 피사체와 부드러운 배경에 서로 다른 RAW 노이즈 엔진 적용
status: validated
source:
  type: magazine
  publisher: PetaPixel
  author: Michael Bonocore
  url: https://petapixel.com/2026/04/09/dxo-pureraw-6-the-ultimate-beginners-guide/
  published_at: '2026-04-09'
  accessed_at: '2026-08-08T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: DxO PureRAW 6
scenario:
  subject: wildlife
  condition:
  - high-iso
  - fine-texture-subject
  - smooth-background
  intent:
  - region-specific-denoise
  - detail-preservation
  - artifact-control
method:
  steps:
  - tool: DxO PureRAW 6
    parameter: 전체 사진의 일반 목적 노이즈 제거 엔진
    value: DeepPRIME 3
    unit: null
    reported_as: exact
  - tool: DxO PureRAW 6 Local Adjustments
    parameter: 깃털·털·직물처럼 미세 질감이 중요한 국소 영역의 엔진
    value: DeepPRIME XD3
    unit: null
    reported_as: exact
  - tool: DxO PureRAW 6 Local Adjustments
    parameter: 부드럽게 흐려진 배경의 국소 영역 엔진
    value: DeepPRIME 3
    unit: null
    reported_as: exact
  - tool: Preview zoom
    parameter: 결과의 질감과 아티팩트를 검사한다
    value: 100
    unit: percent
    reported_as: exact
rationale_ko:
- 미세 질감 영역에만 XD3를 쓰면 깃털·털의 세부 복원 이점을 얻으면서 매끈한 배경의 아티팩트와 처리 시간을 줄일 수 있다.
- DeepPRIME 3는 일반 장면과 부드러운 표면의 기반 처리로 두고, 추가 미세 대비가 실제로 필요한 영역만 분리하는 것이 효율적이다.
collection:
  collector_version: 1.0.0
  content_sha256: df05ee82dec68bdcfa1761c7ff196cbae87152d6dd5422376d8dbc42a0e27073
  collected_at: '2026-08-08T00:00:00Z'
---

# 미세 질감 피사체와 부드러운 배경에 서로 다른 RAW 노이즈 엔진 적용

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

고감도 야생동물 사진에서 새 깃털이나 털은 최대한 복원하면서, 부드러운 아웃포커스 배경에는 불필요한 미세 대비와 아티팩트를 만들고 싶지 않을 때 사용한다.

## 촬영/작업 순서

1. PureRAW 6의 Process with Preview로 원본 RAW를 연다.
2. 일반 처리의 시작 엔진은 DeepPRIME 3로 둔다.
3. Local Adjustments로 깃털·털 같은 미세 질감 피사체를 칠하고 그 영역에 DeepPRIME XD3를 지정한다.
4. 부드러운 배경은 DeepPRIME 3로 유지한다.
5. 100% 확대 전후 비교로 세부 복원과 매끈한 영역의 아티팩트를 확인한다.

## 추천 시작값 / 조작값

- DxO PureRAW 6 / 전체 사진의 일반 목적 노이즈 제거 엔진: DeepPRIME 3
- DxO PureRAW 6 Local Adjustments / 깃털·털·직물처럼 미세 질감이 중요한 국소 영역의 엔진: DeepPRIME XD3
- DxO PureRAW 6 Local Adjustments / 부드럽게 흐려진 배경의 국소 영역 엔진: DeepPRIME 3
- Preview zoom / 결과의 질감과 아티팩트를 검사한다: 100 percent

## 보정 루틴

- Process with Preview에서 전체 사진을 DeepPRIME 3로 시작한다.
- Local Adjustments에서 새의 깃털이나 털처럼 미세 질감이 중요한 부분을 수동 마스킹한다.
- 질감 마스크에는 DeepPRIME XD3를 지정하고, 부드러운 배경에는 DeepPRIME 3를 유지한다.
- 전후 미리보기와 100% 확대에서 깃털 복원, 배경 매끄러움, 경계 아티팩트를 비교한 뒤 처리한다.

## 주의할 점

- DeepPRIME XD3는 처리 시간이 약 두 배이며 매끈한 표면에서 아티팩트를 만들 수 있으므로 세부 영역에만 제한한다.
- Local mask는 preset에 저장되지 않으므로 여러 파일에 복잡한 마스크를 자동 재사용할 수 없다.
- 배경에서 XD3와 DeepPRIME 3의 차이가 보이지 않으면 불필요한 고강도 처리를 피한다.
- 후원 기사에 제시된 제품 워크플로이므로 다른 RAW 프로세서와 비교한 독립적 우월성까지 의미하지 않는다.

## 확실성과 근거

- 미세 질감 영역에만 XD3를 쓰면 깃털·털의 세부 복원 이점을 얻으면서 매끈한 배경의 아티팩트와 처리 시간을 줄일 수 있다.
- DeepPRIME 3는 일반 장면과 부드러운 표면의 기반 처리로 두고, 추가 미세 대비가 실제로 필요한 영역만 분리하는 것이 효율적이다.

PetaPixel의 DxO 후원 초보자 가이드가 새 깃털에는 DeepPRIME XD3, 부드러운 아웃포커스 배경에는 DeepPRIME 3를 Local Blend로 나누는 예를 직접 제시한다. 엔진별 용도와 XD3의 처리 시간·매끈한 영역 아티팩트 위험도 원문에 명시되어 있다.

## 출처

- 원문 URL: https://petapixel.com/2026/04/09/dxo-pureraw-6-the-ultimate-beginners-guide/
- 접근일: 2026-08-08

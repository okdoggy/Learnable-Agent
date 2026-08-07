---
schema_version: '1.0'
scenario_id: raw-20260805-clonestamp01
title_ko: Clone Stamp 재샘플링으로 구조적 방해물 제거
status: validated
source:
  type: official
  publisher: Adobe Photoshop Learn
  author: Dani Beaumont; Seán Duggan; Gabriela Iancu
  url: https://www.adobe.com/learn/photoshop/web/remove-objects-from-your-photos
  published_at: '2025-12-17'
  accessed_at: '2026-08-05T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Photoshop on the web
scenario:
  subject: photo-structural-distraction
  condition:
  - exact-pixel-reconstruction
  - structured-distraction
  intent:
  - remove-structured-object
  - preserve-boundary
method:
  steps:
  - tool: Photoshop Clone Stamp
    parameter: 빈 Retouching 레이어에서 Current and below 또는 All layers로 샘플
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Clone Stamp Source
    parameter: Alt 또는 Option 클릭으로 대상과 맞는 소스 픽셀 지정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Clone Stamp
    parameter: 제거할 요소보다 약간 넓은 브러시로 짧게 복제
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Clone Stamp Source
    parameter: 보존할 디테일에 접근하거나 반복 패턴이 보이면 다른 위치를 재샘플
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Clone Stamp는 혼합 대신 소스 픽셀을 그대로 복사하므로 구조를 정확히 재구성해야 하는 그림자나 선형 디테일 제거에 적합하다.
- 여러 소스를 사용해 반복을 깨면 복제 사실이 눈에 띄는 것을 줄일 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 715f5828c3c83d8faaf8217dd80c993674e918a5e58dd38438d3595d0ace39a8
  collected_at: '2026-08-05T00:00:00Z'
---

# Clone Stamp 재샘플링으로 구조적 방해물 제거

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

자동 혼합보다 주변 구조를 그대로 복사해야 자연스러운 무거운 그림자나 선형 방해물을 제거할 때 사용한다.

## 촬영/작업 순서

1. 사진 위에 빈 Retouching 레이어를 만든다.
2. 대상과 방향·질감이 맞는 인접 영역을 샘플한다.
3. 방해물 위를 짧은 구간으로 복제한다.
4. 보존할 디테일에 가까워지면 멈추고 새 소스를 고른다.
5. 반복 무늬가 보이면 다른 소스를 사용해 반복 부분을 다시 덮는다.

## 추천 시작값 / 조작값

- Photoshop Clone Stamp / 빈 Retouching 레이어에서 Current and below 또는 All layers로 샘플: 원문 정성 표현(수치 추정 없음)
- Photoshop Clone Stamp Source / Alt 또는 Option 클릭으로 대상과 맞는 소스 픽셀 지정: 원문 정성 표현(수치 추정 없음)
- Photoshop Clone Stamp / 제거할 요소보다 약간 넓은 브러시로 짧게 복제: 원문 정성 표현(수치 추정 없음)
- Photoshop Clone Stamp Source / 보존할 디테일에 접근하거나 반복 패턴이 보이면 다른 위치를 재샘플: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 짧은 구간을 복제할 때마다 소스 십자와 대상의 구조를 함께 본다.
- 같은 질감이 반복되면 다른 위치를 샘플해 반복 부분 위를 다시 칠한다.
- 중요한 경계 앞에서 멈추고 그 경계와 맞는 새 소스를 지정한다.

## 주의할 점

- Clone Stamp는 픽셀을 정확히 복사하므로 반복 무늬가 쉽게 드러난다.
- 보존해야 할 경계에 가까워지면 기존 소스를 계속 사용하지 않는다.
- 소스와 대상의 원근·조명·질감 방향이 다르면 복제 흔적이 생긴다.

## 확실성과 근거

- Clone Stamp는 혼합 대신 소스 픽셀을 그대로 복사하므로 구조를 정확히 재구성해야 하는 그림자나 선형 디테일 제거에 적합하다.
- 여러 소스를 사용해 반복을 깨면 복제 사실이 눈에 띄는 것을 줄일 수 있다.

Adobe 공식 튜토리얼이 빈 보정 레이어, 아래 레이어 샘플, Alt/Option 소스 지정, 반복 무늬 감시와 재샘플링을 직접 설명한다. 정확한 브러시 크기는 제시되지 않았다.

## 출처

- 원문 URL: https://www.adobe.com/learn/photoshop/web/remove-objects-from-your-photos
- 접근일: 2026-08-05

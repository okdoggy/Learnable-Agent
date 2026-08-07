---
schema_version: '1.0'
scenario_id: raw-20260805-healbrush01
title_ko: Healing Brush의 재샘플링으로 큰 표면 결함 복원
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
  subject: photo-surface-defect
  condition:
  - larger-surface-flaw
  - controlled-source-needed
  intent:
  - repair-surface
  - nondestructive-retouch
method:
  steps:
  - tool: Photoshop Healing Brush
    parameter: 빈 Retouching 레이어에서 Current and below 또는 All layers를 사용
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Healing Brush Source
    parameter: Alt 또는 Option 클릭으로 온전하고 유사한 질감의 소스 지정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Healing Brush
    parameter: 결함 위를 여러 획으로 덮고 큰 영역은 소스를 반복해 다시 지정
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Healing Brush는 편집자가 지정한 소스의 디테일을 대상 영역의 색과 밝기에 섞으므로 자동 소스가 부적절한 큰 결함을 더 통제해 고칠 수 있다.
- 서로 다른 소스를 반복해 사용하면 한 질감의 복제 흔적이 두드러지는 위험을 줄인다.
collection:
  collector_version: 1.0.0
  content_sha256: e1788d8504a4a46649261e881e8e8260a43559eb401150e39bc24a7310ce2546
  collected_at: '2026-08-05T00:00:00Z'
---

# Healing Brush의 재샘플링으로 큰 표면 결함 복원

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

벽의 벗겨짐이나 진흙 자국처럼 Spot Healing의 자동 소스로는 자연스럽게 고치기 어려운 더 큰 표면 결함을 복원할 때 사용한다.

## 촬영/작업 순서

1. 빈 Retouching 레이어를 만들고 아래 레이어 샘플링을 허용한다.
2. 결함과 질감·방향이 맞는 온전한 영역을 직접 샘플한다.
3. 결함 위를 여러 획으로 나누어 칠한다.
4. 복원 면적이 넓어지면 다른 온전한 지점을 다시 샘플한다.
5. 톤과 질감의 연결, 반복 무늬를 확대해 확인한다.

## 추천 시작값 / 조작값

- Photoshop Healing Brush / 빈 Retouching 레이어에서 Current and below 또는 All layers를 사용: 원문 정성 표현(수치 추정 없음)
- Photoshop Healing Brush Source / Alt 또는 Option 클릭으로 온전하고 유사한 질감의 소스 지정: 원문 정성 표현(수치 추정 없음)
- Photoshop Healing Brush / 결함 위를 여러 획으로 덮고 큰 영역은 소스를 반복해 다시 지정: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 몇 번의 획마다 소스와 결과의 질감 방향을 다시 확인한다.
- 톤과 밝기는 섞이더라도 구조적 무늬가 반복되는지 확대해 검사한다.
- 큰 결함은 한 번에 덮지 않고 여러 소스를 다시 샘플해 나누어 복원한다.

## 주의할 점

- 한 소스에서 너무 넓은 결함을 모두 덮으면 반복되거나 늘어난 질감이 보일 수 있다.
- 복원 대상과 명암·재질이 맞지 않는 소스를 선택하지 않는다.
- 원본 레이어에 직접 칠하지 않는다.

## 확실성과 근거

- Healing Brush는 편집자가 지정한 소스의 디테일을 대상 영역의 색과 밝기에 섞으므로 자동 소스가 부적절한 큰 결함을 더 통제해 고칠 수 있다.
- 서로 다른 소스를 반복해 사용하면 한 질감의 복제 흔적이 두드러지는 위험을 줄인다.

Adobe 공식 튜토리얼이 Healing Brush의 직접 소스 지정, Current and below 또는 All layers, Alt/Option 샘플, 여러 획과 재샘플링을 직접 설명한다. 크기와 획 수는 이미지에 따라 달라 수치화하지 않았다.

## 출처

- 원문 URL: https://www.adobe.com/learn/photoshop/web/remove-objects-from-your-photos
- 접근일: 2026-08-05

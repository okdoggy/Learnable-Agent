---
schema_version: '1.0'
scenario_id: raw-20260809-maskrefine01
title_ko: Lightroom AI 마스크를 오버레이와 Add·Subtract로 정밀하게 다듬기
status: validated
source:
  type: official
  publisher: Adobe
  author: Adobe Lightroom Help
  url: https://helpx.adobe.com/lightroom/desktop/edit-photos/masking.html
  published_at: '2026-08-07'
  accessed_at: '2026-08-09T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: general-photograph
  condition:
  - complex-edge
  - local-adjustment
  - ai-selection
  intent:
  - precise-mask
  - protect-unselected-area
  - organized-edit
method:
  steps:
  - tool: Lightroom AI Masking
    parameter: 사진에 맞는 Subject·Sky·Background·Landscape·Objects·People 중 하나로 기본 선택 생성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Mask Overlay
    parameter: 빨간 오버레이 또는 흑백·검정·흰색 배경 표시로 선택 경계 검사
    value: null
    unit: null
    reported_as: qualitative
  - tool: Mask Add and Subtract
    parameter: 누락 영역은 추가하고 넘친 영역은 제거
    value: null
    unit: null
    reported_as: qualitative
  - tool: Intersect with Mask
    parameter: 다른 선택과 공통인 영역만 남김
    value: null
    unit: null
    reported_as: qualitative
  - tool: Local adjustment sliders
    parameter: 정제된 영역에만 노출·명암·색·디테일 보정 적용
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 전역 보정 대신 피사체·하늘·배경 등 필요한 영역만 선택하면 나머지 사진을 유지하면서 밝기와 색을 조절할 수 있다.
- AI 선택을 오버레이로 검사하고 수동 도구로 정제하면 복잡한 경계의 누락과 넘침을 줄일 수 있다.
- Intersect는 밝기나 색 같은 두 조건이 겹치는 부분에만 보정을 제한할 때 유용하다.
collection:
  collector_version: 1.0.0
  content_sha256: 6415ab68d9d51f865f361b596806e4f7a9f6e2aa0740b62adbf41262a57410a9
  collected_at: '2026-08-09T00:00:00Z'
---

# Lightroom AI 마스크를 오버레이와 Add·Subtract로 정밀하게 다듬기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

피사체, 하늘, 배경 또는 특정 물체만 국소 보정하려는데 자동 선택의 가장자리 누락과 넘침 때문에 원치 않는 영역까지 바뀔 때 사용한다.

## 촬영/작업 순서

1. Masking 패널에서 대상에 맞는 AI 선택으로 기본 마스크를 만든다.
2. 오버레이 표시 방식을 바꿔가며 경계를 검사한다.
3. Add와 Subtract를 브러시·그라데이션·범위 도구와 결합해 선택을 정제한다.
4. 필요하면 Intersect로 밝기나 색 조건이 겹치는 영역만 남긴다.
5. 마스크 이름을 바꾸고 선택 영역에만 필요한 국소 보정을 적용한다.

## 추천 시작값 / 조작값

- Lightroom AI Masking / 사진에 맞는 Subject·Sky·Background·Landscape·Objects·People 중 하나로 기본 선택 생성: 원문 정성 표현(수치 추정 없음)
- Mask Overlay / 빨간 오버레이 또는 흑백·검정·흰색 배경 표시로 선택 경계 검사: 원문 정성 표현(수치 추정 없음)
- Mask Add and Subtract / 누락 영역은 추가하고 넘친 영역은 제거: 원문 정성 표현(수치 추정 없음)
- Intersect with Mask / 다른 선택과 공통인 영역만 남김: 원문 정성 표현(수치 추정 없음)
- Local adjustment sliders / 정제된 영역에만 노출·명암·색·디테일 보정 적용: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 기본 빨간 오버레이와 흑백·검정·흰색 배경 표시 모드를 번갈아 보며 누락과 넘침을 찾는다.
- Add로 빠진 영역을 포함하고 Subtract로 잘못 선택된 영역을 제거한다.
- 두 조건을 동시에 만족해야 하는 보정은 Intersect로 범위를 제한한다.
- 마스크를 의미 있는 이름으로 바꾸고 Exposure·Highlights·Shadows·Temperature 등 필요한 항목만 조정한다.
- 보정 전후를 비교해 경계 후광, 색 번짐, 열린 그림자의 노이즈를 검사한다.

## 주의할 점

- AI 선택 결과를 그대로 신뢰하지 말고 머리카락, 산 능선, 건축물 가장자리처럼 복잡한 경계를 검사한다.
- 마스크 안에서 Shadows를 올리면 휘도 노이즈가 드러날 수 있으므로 필요하면 국소 Noise Reduction을 함께 검토한다.
- Clarity는 국소 대비를 높여 가장자리와 피부를 거칠게 만들 수 있고, 음의 Sharpness는 디테일을 흐릴 수 있다.
- 서로 다른 보정 목적은 마스크를 분리하고 이름을 붙여 관리한다.

## 확실성과 근거

- 전역 보정 대신 피사체·하늘·배경 등 필요한 영역만 선택하면 나머지 사진을 유지하면서 밝기와 색을 조절할 수 있다.
- AI 선택을 오버레이로 검사하고 수동 도구로 정제하면 복잡한 경계의 누락과 넘침을 줄일 수 있다.
- Intersect는 밝기나 색 같은 두 조건이 겹치는 부분에만 보정을 제한할 때 유용하다.

Adobe 공식 도움말이 Subject·Sky·Background 등 AI 선택 후 빨간 오버레이를 검사하고 Add·Subtract·Intersect로 정제한 뒤 국소 슬라이더를 적용하는 절차를 직접 설명한다. 특정 사진에 맞는 슬라이더 수치는 제공하지 않아 정성적 시작법만 기록했다.

## 출처

- 원문 URL: https://helpx.adobe.com/lightroom/desktop/edit-photos/masking.html
- 접근일: 2026-08-09

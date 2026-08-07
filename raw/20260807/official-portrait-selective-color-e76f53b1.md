---
schema_version: '1.0'
scenario_id: raw-20260807-fashionbw01
title_ko: 인물은 컬러로 유지하고 배경만 어둡게 흑백 처리
status: validated
source:
  type: official
  publisher: Adobe Learn
  author: Seán Duggan
  url: https://www.adobe.com/learn/lightroom-cc/web/edit-part-photo-lightroom-cc
  published_at: '2025-12-18'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: portrait
  condition:
  - fashion-portrait
  - color-background
  - subject-separation
  intent:
  - selective-color
  - direct-attention
  - background-darkening
method:
  steps:
  - tool: Lightroom Masking > Subject
    parameter: AI가 모델을 선택하도록 Subject 마스크 생성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Subject mask > Exposure
    parameter: 모델이 밝아질 때까지 Exposure 증가
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Subject mask > Shadows
    parameter: 머리카락 세부가 드러날 정도로 Shadows 소폭 증가
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Masking > Background
    parameter: AI가 모델 이외 영역을 선택하도록 Background 마스크 생성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Background mask > Exposure
    parameter: 주변을 어둡게 할 정도로 Exposure 감소
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Background mask > Saturation
    parameter: Background만 흑백이 되도록 Saturation 슬라이더를 완전히 왼쪽으로 이동
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 인물은 밝히고 배경은 어둡게 해 명도 대비를 만들면 모델이 주변에서 더 뚜렷하게 분리된다.
- 배경의 채도만 제거하면 모델의 컬러를 보존하면서 배경의 색 경쟁을 줄일 수 있다.
- 마스크 Eye와 오버레이 비교는 선택 오류와 과도한 효과를 발견하는 데 도움이 된다.
collection:
  collector_version: 1.0.0
  content_sha256: e76f53b199d6ce4be1df5020c68a478706e3ae1ee5acf106271ac0bff163ca16
  collected_at: '2026-08-07T00:00:00Z'
---

# 인물은 컬러로 유지하고 배경만 어둡게 흑백 처리

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

컬러 패션 사진에서 모델의 색은 보존하면서 주변 배경의 색과 밝기를 억제해 시선을 인물에 집중시키고 싶을 때 사용하는 선택 보정이다.

## 촬영/작업 순서

1. Masking 패널에서 Subject를 선택하고 빨간 오버레이와 마스크 썸네일로 모델 선택 범위를 확인한다.
2. Subject 마스크의 Exposure를 올리고 Shadows를 조금 올려 모델과 머리카락의 어두운 디테일을 살린다.
3. 별도의 Background 마스크를 만든 뒤 선택 범위가 모델을 침범하지 않는지 확인한다.
4. Background의 Exposure를 낮추고 Saturation을 완전히 왼쪽으로 이동해 배경만 흑백으로 만든다.
5. 각 마스크의 Eye와 전체 Masks Eye를 사용해 개별 효과와 누적 전후를 비교한다.

## 추천 시작값 / 조작값

- Lightroom Masking > Subject / AI가 모델을 선택하도록 Subject 마스크 생성: 원문 정성 표현(수치 추정 없음)
- Lightroom Subject mask > Exposure / 모델이 밝아질 때까지 Exposure 증가: 원문 정성 표현(수치 추정 없음)
- Lightroom Subject mask > Shadows / 머리카락 세부가 드러날 정도로 Shadows 소폭 증가: 원문 정성 표현(수치 추정 없음)
- Lightroom Masking > Background / AI가 모델 이외 영역을 선택하도록 Background 마스크 생성: 원문 정성 표현(수치 추정 없음)
- Lightroom Background mask > Exposure / 주변을 어둡게 할 정도로 Exposure 감소: 원문 정성 표현(수치 추정 없음)
- Lightroom Background mask > Saturation / Background만 흑백이 되도록 Saturation 슬라이더를 완전히 왼쪽으로 이동: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- Subject 마스크의 흰색·검은색 썸네일과 오버레이를 먼저 점검한 후 밝기 보정을 적용한다.
- Background 마스크에서도 같은 방식으로 경계를 확인하고, 모델에 배경 보정이 번지면 Add 또는 Subtract로 선택을 다듬는다.
- 전체 마스크 전후 비교에서 인물 분리가 충분한지 확인하고 과도한 배경 감광이나 부자연스러운 경계는 되돌린다.

## 주의할 점

- AI 마스크가 항상 완전하지 않으므로 오버레이를 확인하고 필요하면 Add 또는 Subtract로 수정한다.
- 배경을 어둡게 하고 완전히 탈색하는 조합은 강한 효과이므로 인물 가장자리의 색 번짐과 부자연스러운 분리를 확인한다.
- 원문은 Exposure와 Shadows의 정확한 수치를 제시하지 않았으므로 정성적 조정으로만 기록한다.

## 확실성과 근거

- 인물은 밝히고 배경은 어둡게 해 명도 대비를 만들면 모델이 주변에서 더 뚜렷하게 분리된다.
- 배경의 채도만 제거하면 모델의 컬러를 보존하면서 배경의 색 경쟁을 줄일 수 있다.
- 마스크 Eye와 오버레이 비교는 선택 오류와 과도한 효과를 발견하는 데 도움이 된다.

Adobe Learn 튜토리얼이 Subject 밝기·머리카락 Shadows 보강과 Background 감광·완전 탈색 순서를 직접 설명한다. 정확한 Exposure 및 Shadows 값은 제공되지 않았으며, 경계 수정과 과도한 적용 확인은 원문의 마스크 점검 및 Add/Subtract 권고를 실무 루틴으로 정리한 것이다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/edit-part-photo-lightroom-cc
- 접근일: 2026-08-07

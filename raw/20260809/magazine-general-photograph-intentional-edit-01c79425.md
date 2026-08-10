---
schema_version: '1.0'
scenario_id: raw-20260809-fivepassedit
title_ko: 감정을 먼저 정하고 5단계로 진행하는 Lightroom 보정 루틴
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke; instruction by Sean Dalton
  url: https://fstoppers.com/education/stop-guessing-lightroom-and-start-editing-plan-901827
  published_at: '2026-04-24'
  accessed_at: '2026-08-09T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: general-photograph
  condition:
  - raw-edit
  - inconsistent-results
  - preset-mismatch
  intent:
  - intentional-edit
  - consistent-workflow
  - mood-control
method:
  steps:
  - tool: Creative intent
    parameter: 보정 전에 사진이 전달할 감정과 방향을 문장으로 결정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Crop and preparation
    parameter: 구도와 기본 상태를 먼저 준비
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Blacks and Whites
    parameter: 검정을 낮추고 흰색을 높여 명암 분리
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Tone Curve S-curve
    parameter: 명암 분리를 보강하는 완만한 형태
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Color Grading
    parameter: 중간톤과 하이라이트에는 따뜻한 색, 그림자에는 푸른색을 배치
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom final tuning
    parameter: 디테일·효과 적용 후 전체 결과를 미세조정
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 도구나 프리셋부터 시험하는 대신 감정을 먼저 정하면 각 조정의 필요성을 판단할 기준이 생긴다.
- 준비, 빛, 색, 디테일·효과, 미세조정의 고정된 순서는 임의로 슬라이더를 오가는 작업을 줄이고 문제 원인을 추적하기 쉽게 한다.
collection:
  collector_version: 1.0.0
  content_sha256: 01c7942570c88d6699b20d52acc51112b9b2f43b40d76e5735d928b249906423
  collected_at: '2026-08-09T00:00:00Z'
---

# 감정을 먼저 정하고 5단계로 진행하는 Lightroom 보정 루틴

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

프리셋과 슬라이더를 무작위로 시험해 결과가 일관되지 않거나, 무엇이 잘못됐는지 진단하기 어려울 때 사용하는 계획형 Lightroom 작업 순서다.

## 촬영/작업 순서

1. 사진을 열기 전에 최종 결과가 전달할 감정을 정한다.
2. 크롭과 기본 준비로 프레임을 정리한다.
3. Blacks·Whites와 Tone Curve로 빛과 대비를 설계한다.
4. Color Grading으로 의도에 맞는 톤 영역별 색을 배치한다.
5. 디테일과 효과를 적용한다.
6. 전체를 다시 보며 강도와 일관성을 미세조정한다.

## 추천 시작값 / 조작값

- Creative intent / 보정 전에 사진이 전달할 감정과 방향을 문장으로 결정: 원문 정성 표현(수치 추정 없음)
- Lightroom Crop and preparation / 구도와 기본 상태를 먼저 준비: 원문 정성 표현(수치 추정 없음)
- Lightroom Blacks and Whites / 검정을 낮추고 흰색을 높여 명암 분리: 원문 정성 표현(수치 추정 없음)
- Lightroom Tone Curve S-curve / 명암 분리를 보강하는 완만한 형태: 원문 정성 표현(수치 추정 없음)
- Lightroom Color Grading / 중간톤과 하이라이트에는 따뜻한 색, 그림자에는 푸른색을 배치: 원문 정성 표현(수치 추정 없음)
- Lightroom final tuning / 디테일·효과 적용 후 전체 결과를 미세조정: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 각 단계가 시작 전 정한 감정과 방향을 지원하는지 확인하고, 목적 없는 조정은 제거한다.
- 빛 단계에서는 히스토그램과 화면을 함께 보며 Blacks·Whites 및 S 커브가 필요한 분리만 만드는지 확인한다.
- 색 단계에서는 단순한 전역 온도 상승 대신 톤 영역별 따뜻함과 차가움을 배치한다.
- 디테일과 효과를 적용한 뒤 마지막 미세조정에서 전체 일관성과 클리핑을 다시 검사한다.

## 주의할 점

- 사진의 원래 팔레트와 빛이 받쳐주지 않는 스타일을 억지로 적용하지 않는다.
- 모든 사진에 같은 프리셋을 강제하면 장소와 피사체에 맞지 않는 색과 대비가 생길 수 있다.
- S 커브와 Blacks·Whites 조정은 의도한 감정을 지원하는 범위에서만 사용하며 클리핑을 확인한다.

## 확실성과 근거

- 도구나 프리셋부터 시험하는 대신 감정을 먼저 정하면 각 조정의 필요성을 판단할 기준이 생긴다.
- 준비, 빛, 색, 디테일·효과, 미세조정의 고정된 순서는 임의로 슬라이더를 오가는 작업을 줄이고 문제 원인을 추적하기 쉽게 한다.

Sean Dalton이 보정 전에 감정을 정하고 준비-빛-색-디테일·효과-미세조정의 5단계로 진행한다고 직접 제시했다. 예시의 Blacks·Whites, S 커브, 따뜻한 중간톤·하이라이트와 푸른 그림자는 정성적으로만 설명되어 수치를 추정하지 않았다.

## 출처

- 원문 URL: https://fstoppers.com/education/stop-guessing-lightroom-and-start-editing-plan-901827
- 접근일: 2026-08-09

---
schema_version: '1.0'
scenario_id: raw-20260809-complementgrade
title_ko: Lightroom 톤 영역에 보색을 나눠 배치하고 휴식 후 비교하기
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke; method by Sean Dalton
  url: https://fstoppers.com/education/how-color-grade-photos-lightroom-using-complementary-colors-902459
  published_at: '2026-05-19'
  accessed_at: '2026-08-09T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: general-photograph
  condition:
  - creative-color
  - color-fatigue
  - flat-color-depth
  intent:
  - complementary-color-grade
  - add-depth
  - compare-variants
method:
  steps:
  - tool: Lightroom White Balance
    parameter: Color Grading 전에 Temperature와 Tint로 기본 화이트 밸런스를 설정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Color Grading blue-orange
    parameter: 그림자에 푸른색, 밝은 영역에 따뜻한 주황색을 절제해 배치
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Color Grading green-red
    parameter: 대안으로 그림자와 밝은 영역에 녹색·붉은색 관계를 약하게 시험
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Snapshot
    parameter: 서로 다른 그레이딩 변형을 보존
    value: null
    unit: null
    reported_as: qualitative
  - tool: Visual rest
    parameter: 색 적응을 풀기 위한 최소 휴식 시간
    value: 30
    unit: minutes
    reported_as: exact
rationale_ko:
- 그림자·중간톤·하이라이트에 서로 다른 색을 넣으면 전역 색조보다 깊이와 분리를 만들기 쉽다.
- 보색 관계는 차가운 영역과 따뜻한 영역을 구분해 분위기를 강화하지만, 원래 색과 정서에 맞춰 절제해야 한다.
- 휴식과 Snapshot 비교는 색 피로로 인해 과보정을 알아채지 못하는 문제를 줄인다.
collection:
  collector_version: 1.0.0
  content_sha256: afdd6ac827d46cb41fa1dbbc4dbed101f2132c3cb8f2ff2805aa49dd3fb4a5ef
  collected_at: '2026-08-09T00:00:00Z'
---

# Lightroom 톤 영역에 보색을 나눠 배치하고 휴식 후 비교하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

화이트 밸런스는 맞지만 사진의 색 깊이와 분위기가 부족해, 그림자와 밝은 영역에 서로 다른 보색 관계를 절제해서 더하고 싶을 때 사용한다.

## 촬영/작업 순서

1. Temperature와 Tint로 기본 화이트 밸런스를 먼저 해결한다.
2. Color Grading에서 그림자·중간톤·하이라이트를 분리해 본다.
3. 밤 장면 등에는 푸른 그림자와 따뜻한 밝은 영역을, 필름 분위기에는 약한 녹색·붉은색 관계를 후보로 시험한다.
4. 각 변형을 Snapshot으로 저장한다.
5. 최소 30분 쉬고 돌아와 변형들을 비교한 뒤 과한 강도를 낮춘다.

## 추천 시작값 / 조작값

- Lightroom White Balance / Color Grading 전에 Temperature와 Tint로 기본 화이트 밸런스를 설정: 원문 정성 표현(수치 추정 없음)
- Lightroom Color Grading blue-orange / 그림자에 푸른색, 밝은 영역에 따뜻한 주황색을 절제해 배치: 원문 정성 표현(수치 추정 없음)
- Lightroom Color Grading green-red / 대안으로 그림자와 밝은 영역에 녹색·붉은색 관계를 약하게 시험: 원문 정성 표현(수치 추정 없음)
- Lightroom Snapshot / 서로 다른 그레이딩 변형을 보존: 원문 정성 표현(수치 추정 없음)
- Visual rest / 색 적응을 풀기 위한 최소 휴식 시간: 30 minutes

## 보정 루틴

- 각 톤 영역의 색을 하나씩 켜고 끄며 피사체와 분위기에 기여하는지 확인한다.
- Snapshot으로 보색 조합과 강도가 다른 변형을 각각 저장한다.
- 최소 30분 화면에서 벗어난 뒤 돌아와 과도한 색 이동과 균형을 다시 판단한다.
- 가장 강한 버전이 아니라 사진의 기존 팔레트와 정서를 가장 잘 지지하는 버전을 선택한다.

## 주의할 점

- 화이트 밸런스 문제를 창의적 Color Grading으로 덮지 않는다.
- 시연값은 효과를 보여주기 위해 강할 수 있으므로 완성본에서는 절제한다.
- 푸른 그림자·주황 하이라이트 또는 녹색·붉은색 조합이 모든 사진에 맞는다고 가정하지 않는다.
- 오래 본 뒤에는 눈이 색에 적응하므로 즉시 확정하지 않는다.

## 확실성과 근거

- 그림자·중간톤·하이라이트에 서로 다른 색을 넣으면 전역 색조보다 깊이와 분리를 만들기 쉽다.
- 보색 관계는 차가운 영역과 따뜻한 영역을 구분해 분위기를 강화하지만, 원래 색과 정서에 맞춰 절제해야 한다.
- 휴식과 Snapshot 비교는 색 피로로 인해 과보정을 알아채지 못하는 문제를 줄인다.

Sean Dalton이 화이트 밸런스를 먼저 정하고, 보색을 서로 다른 톤 영역에 배치하며, 최소 30분 쉬었다가 재평가하고 Snapshot으로 변형을 비교하라고 직접 설명했다. 개별 Hue·Saturation 수치는 원문에 없으므로 추정하지 않았다.

## 출처

- 원문 URL: https://fstoppers.com/education/how-color-grade-photos-lightroom-using-complementary-colors-902459
- 접근일: 2026-08-09

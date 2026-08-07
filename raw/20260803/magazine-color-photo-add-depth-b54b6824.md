---
schema_version: '1.0'
scenario_id: raw-20260803-complementgrade01
title_ko: 화이트 밸런스 후 보색을 톤 영역별로 색보정
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke; Sean Dalton
  url: https://fstoppers.com/education/how-color-grade-photos-lightroom-using-complementary-colors-902459
  published_at: '2026-05-19'
  accessed_at: '2026-08-03T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: color-photo
  condition:
  - flat-color-separation
  - creative-grading
  intent:
  - add-depth
  - build-mood
  - compare-variants
method:
  steps:
  - tool: Adobe Lightroom
    parameter: Temperature와 Tint로 중립 기반을 먼저 교정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Lightroom Color Grading
    parameter: Shadows, Midtones, Highlights에 보색을 독립 배치
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Lightroom Snapshot
    parameter: 여러 색보정 버전을 Snapshot으로 저장해 비교
    value: null
    unit: null
    reported_as: qualitative
  - tool: 휴식
    parameter: 최종 색 판단 전 시각 적응 해소
    value: 30
    unit: minutes minimum approximate
    reported_as: exact
rationale_ko:
- Color Grading은 톤 영역에 새 색을 도입할 수 있어 보색 대비로 깊이와 분위기를 만들 수 있다.
- 여러 버전을 보존하고 휴식 후 비교하면 장시간 편집의 색 피로를 줄일 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: b54b682457a0088adeb168f028302c3731ed0b824e7d21a9cdba8be6e04881fe
  collected_at: '2026-08-03T00:00:00Z'
---

# 화이트 밸런스 후 보색을 톤 영역별로 색보정

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

기본 화이트 밸런스는 맞출 수 있지만 톤 영역 간 색 분리가 약해 깊이나 분위기가 부족할 때 사용한다.

## 촬영/작업 순서

1. Temperature와 Tint로 기본 화이트 밸런스를 먼저 바로잡는다.
2. Color Grading에서 Shadows, Midtones, Highlights를 따로 보며 장면에 맞는 보색 관계를 만든다.
3. 야간 장면에는 차가운 그림자와 따뜻한 하이라이트를 검토하고 다른 분위기에는 녹색·빨강 조합을 작게 시험한다.
4. 각 해석을 Snapshot으로 저장해 비교한다.
5. 최종 판단 전에 최소 약 30분 화면을 떠났다가 다시 확인한다.

## 추천 시작값 / 조작값

- Adobe Lightroom / Temperature와 Tint로 중립 기반을 먼저 교정: 원문 정성 표현(수치 추정 없음)
- Adobe Lightroom Color Grading / Shadows, Midtones, Highlights에 보색을 독립 배치: 원문 정성 표현(수치 추정 없음)
- Adobe Lightroom Snapshot / 여러 색보정 버전을 Snapshot으로 저장해 비교: 원문 정성 표현(수치 추정 없음)
- 휴식 / 최종 색 판단 전 시각 적응 해소: 30 minutes minimum approximate

## 보정 루틴

- 강한 데모 값이 아니라 작은 색 변화부터 시작해 전후 비교한다.
- 휴식 후 피부, 중립 회색, 밝은 영역에 원치 않는 색이 묻었는지 다시 본다.

## 주의할 점

- 잘못된 화이트 밸런스를 Color Grading으로 보상하지 않는다.
- 보색 조합을 모든 사진에 고정 공식처럼 적용하지 않는다.
- 오래 바라본 직후에는 색 적응 때문에 오류를 놓칠 수 있다.

## 확실성과 근거

- Color Grading은 톤 영역에 새 색을 도입할 수 있어 보색 대비로 깊이와 분위기를 만들 수 있다.
- 여러 버전을 보존하고 휴식 후 비교하면 장시간 편집의 색 피로를 줄일 수 있다.

기초 화이트 밸런스 우선, 톤별 보색 배치, Snapshot 비교, 약 30분 휴식은 출처가 직접 설명했다. 색상 강도 수치는 제시되지 않았다.

## 출처

- 원문 URL: https://fstoppers.com/education/how-color-grade-photos-lightroom-using-complementary-colors-902459
- 접근일: 2026-08-03

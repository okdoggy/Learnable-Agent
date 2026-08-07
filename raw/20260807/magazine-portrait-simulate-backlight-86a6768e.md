---
schema_version: '1.0'
scenario_id: raw-20260807-skybacklit
title_ko: Radial Gradient와 Sky 교차 마스크로 인공 역광 글로우 만들기
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/lightroom/10-lightroom-secrets-will-change-how-edit-photos-901713
  published_at: '2026-04-18'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: portrait
  condition:
  - portrait
  - missing-backlight
  - mask-intersection-available
  intent:
  - simulate-backlight
  - create-wraparound-glow
  - subject-separation
method:
  steps:
  - tool: Lightroom Radial Gradient
    parameter: 글로우가 필요한 위치에 부드러운 Radial Gradient 배치
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Intersect with Sky
    parameter: Radial Gradient를 Sky 선택과 교차해 적용 범위 제한
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom local adjustment controls
    parameter: 실제 역광처럼 보이도록 밝기와 색을 절제해 조정
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Radial Gradient는 국소적인 광원 중심과 부드러운 감쇠를 만든다.
- Sky와의 교차는 글로우를 배경 성격의 영역에 제한해 피사체 위에 평평하게 덮이는 효과를 줄인다.
collection:
  collector_version: 1.0.0
  content_sha256: 86a6768e214fe93811d6e46a1ca463798bbc496378a50604e55388cf95f4b91c
  collected_at: '2026-08-07T00:00:00Z'
---

# Radial Gradient와 Sky 교차 마스크로 인공 역광 글로우 만들기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

인물 배경에 실제 역광이 약하거나 없지만, 피사체 주변을 감싸는 부드러운 배경광을 Lightroom 안에서 제한적으로 만들고 싶을 때 사용한다.

## 촬영/작업 순서

1. 기존 장면의 광원 방향과 피사체 윤곽을 먼저 읽는다.
2. 예상 광원 위치에 Radial Gradient를 놓는다.
3. Intersect with Sky로 광원의 적용 영역을 좁힌다.
4. 국소 밝기와 색을 조정한 뒤 확대·축소 전후 비교로 자연스러움을 확인한다.

## 추천 시작값 / 조작값

- Lightroom Radial Gradient / 글로우가 필요한 위치에 부드러운 Radial Gradient 배치: 원문 정성 표현(수치 추정 없음)
- Lightroom Intersect with Sky / Radial Gradient를 Sky 선택과 교차해 적용 범위 제한: 원문 정성 표현(수치 추정 없음)
- Lightroom local adjustment controls / 실제 역광처럼 보이도록 밝기와 색을 절제해 조정: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 글로우가 생길 배경 위치에 Radial Gradient를 배치한다.
- 해당 마스크를 Sky와 Intersect해 광원 효과가 적용될 영역을 제한한다.
- 밝기와 색을 정성적으로 조절해 피사체 가장자리 주변으로 빛이 감싸는 인상을 만든다.
- 마스크 오버레이와 전후 비교로 실제 조명과 방향이 맞고 효과가 과하지 않은지 확인한다.

## 주의할 점

- 실제 광원 방향과 맞지 않는 위치에 글로우를 만들면 합성 티가 난다.
- Sky 교차 마스크의 결과가 피사체 경계나 원치 않는 영역까지 번지는지 오버레이로 확인한다.
- 광원의 밝기·온도·채도를 과도하게 올리면 후처리 흔적이 두드러진다.

## 확실성과 근거

- Radial Gradient는 국소적인 광원 중심과 부드러운 감쇠를 만든다.
- Sky와의 교차는 글로우를 배경 성격의 영역에 제한해 피사체 위에 평평하게 덮이는 효과를 줄인다.

Fstoppers 기사에서 Serge Ramelli가 Radial Gradient를 배치한 뒤 Sky 마스크와 Intersect해 인물 주변을 감싸는 인공 역광을 만드는 절차를 직접 소개한다. 기사 요약에는 고정 밝기나 색온도 수치가 없으므로 정성 단계만 기록했다.

## 출처

- 원문 URL: https://fstoppers.com/lightroom/10-lightroom-secrets-will-change-how-edit-photos-901713
- 접근일: 2026-08-07

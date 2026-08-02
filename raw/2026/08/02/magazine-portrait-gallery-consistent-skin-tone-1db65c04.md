---
schema_version: '1.0'
scenario_id: raw-20260802-galleryskin01
title_ko: 혼합 조명 인물 갤러리의 피부색 일관성 맞추기
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/education/how-edit-portrait-skin-tones-lightroom-902830
  published_at: '2026-06-09'
  accessed_at: '2026-08-02T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: portrait-gallery
  condition:
  - mixed-lighting-gallery
  - green-orange-skin-cast
  intent:
  - consistent-skin-tone
  - cohesive-portrait-gallery
method:
  steps:
  - tool: White Balance
    parameter: 서로 다른 조명 조건의 사진 사이 화이트 밸런스 동기화
    value: null
    unit: null
    reported_as: qualitative
  - tool: HSL
    parameter: Red와 Orange Hue를 더 붉고 분홍빛이 도는 방향으로 이동
    value: null
    unit: null
    reported_as: qualitative
  - tool: HSL
    parameter: Orange Saturation 소폭 감소
    value: null
    unit: null
    reported_as: qualitative
  - tool: Crop
    parameter: 세트 전체의 종횡비와 크롭 동기화
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 화이트 밸런스를 먼저 맞추면 하루 동안 조명이 변한 갤러리도 일관된 출발점을 갖는다.
- Red와 Orange 영역을 조절해 녹색-주황색으로 치우친 피부를 더 자연스러운 붉은 분홍 계열로 옮긴다.
collection:
  collector_version: 1.0.0
  content_sha256: 1db65c04d01fb90cf417f25bcc7bc34779c0d0c511f8d24e6066077672ccb173
  collected_at: '2026-08-02T00:00:00Z'
---

# 혼합 조명 인물 갤러리의 피부색 일관성 맞추기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

하루 동안 여러 조명에서 촬영한 인물 갤러리의 피부가 컷마다 달라 보이거나 녹색-주황색으로 치우칠 때 전체 세트를 일관되게 정리한다.

## 촬영/작업 순서

1. 화이트 밸런스를 먼저 동기화한다.
2. 톤 스타일을 정한 뒤 HSL로 피부의 Red와 Orange를 조정한다.
3. Orange 채도를 소폭 낮추고 크롭과 종횡비도 세트에 맞춘다.

## 추천 시작값 / 조작값

- White Balance / 서로 다른 조명 조건의 사진 사이 화이트 밸런스 동기화: 원문 정성 표현(수치 추정 없음)
- HSL / Red와 Orange Hue를 더 붉고 분홍빛이 도는 방향으로 이동: 원문 정성 표현(수치 추정 없음)
- HSL / Orange Saturation 소폭 감소: 원문 정성 표현(수치 추정 없음)
- Crop / 세트 전체의 종횡비와 크롭 동기화: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 대표 컷에서 피부색을 정리한 뒤 같은 조명 조건의 사진에 설정을 동기화한다.
- 전체 갤러리를 훑으며 조명 변화 구간마다 화이트 밸런스와 피부색의 일관성을 재확인한다.

## 주의할 점

- Adobe Color가 모든 피부에 같은 문제를 만드는 것은 아니므로 실제 색을 보고 판단한다.
- Orange Saturation을 과도하게 낮추면 피부가 생기 없이 보일 수 있다.
- 서로 다른 조명에서 촬영한 컷은 화이트 밸런스를 먼저 통일해야 HSL 판단이 안정적이다.

## 확실성과 근거

- 화이트 밸런스를 먼저 맞추면 하루 동안 조명이 변한 갤러리도 일관된 출발점을 갖는다.
- Red와 Orange 영역을 조절해 녹색-주황색으로 치우친 피부를 더 자연스러운 붉은 분홍 계열로 옮긴다.

Fstoppers 기사에서 Gerard Needham의 다섯 단계 Lightroom 워크플로를 Alex Cooke가 설명한다. HSL 조정 방향은 직접 제시되지만 수치는 없어 정성값으로 기록했다.

## 출처

- 원문 URL: https://fstoppers.com/education/how-edit-portrait-skin-tones-lightroom-902830
- 접근일: 2026-08-02

---
schema_version: '1.0'
scenario_id: raw-20260807-endclip12
title_ko: Option·Alt 클리핑 미리보기로 검정점과 흰점의 1~2% 끝점 설정
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
  subject: general-photo
  condition:
  - flat-tonal-range
  - raw-development
  - endpoint-uncertain
  intent:
  - set-black-point
  - set-white-point
  - controlled-clipping
method:
  steps:
  - tool: Lightroom Blacks and Whites controls
    parameter: Option(macOS) 또는 Alt(Windows)를 누른 채 Black/White 끝점 클리핑 표시 확인
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom clipping preview
    parameter: 클리핑되는 픽셀 목표 범위
    value: 1-2
    unit: percent of pixels
    reported_as: exact
rationale_ko:
- 클리핑 미리보기는 눈대중보다 반복 가능한 방식으로 검정점과 흰점을 고정하게 한다.
- 아주 적은 픽셀만 끝점에 닿게 해 이미지의 톤 범위를 확보하면서 대규모 디테일 손실을 피한다.
collection:
  collector_version: 1.0.0
  content_sha256: 394b85555324cabcff26f433e52205bfd65a1d2a3da775d6f1c10606b4e083bf
  collected_at: '2026-08-07T00:00:00Z'
---

# Option·Alt 클리핑 미리보기로 검정점과 흰점의 1~2% 끝점 설정

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

RAW 현상에서 검정점과 흰점을 눈대중으로 정하기 어렵고, 톤 범위를 넓히면서도 과도한 디테일 손실을 피하고 싶을 때 사용한다.

## 촬영/작업 순서

1. 기본 노출을 먼저 정리한다.
2. Option 또는 Alt 기반 클리핑 미리보기를 켠 채 Blacks와 Whites를 각각 조정한다.
3. 약 1~2% 클리핑을 시작점으로 둔다.
4. 중요한 하이라이트와 암부가 보존되는지 사진 내용에 맞춰 미세 조정한다.

## 추천 시작값 / 조작값

- Lightroom Blacks and Whites controls / Option(macOS) 또는 Alt(Windows)를 누른 채 Black/White 끝점 클리핑 표시 확인: 원문 정성 표현(수치 추정 없음)
- Lightroom clipping preview / 클리핑되는 픽셀 목표 범위: 1-2 percent of pixels

## 보정 루틴

- Option 또는 Alt를 누른 채 Black 또는 White 끝점을 조정해 클리핑 표시를 본다.
- 표시가 전혀 없는 상태에서 천천히 움직여 첫 클리핑이 나타나는 위치를 찾는다.
- 전체 픽셀의 약 1~2%만 클리핑되도록 끝점을 설정한다.
- 중요 피사체의 디테일이 잘리지 않았는지 일반 화면과 히스토그램으로 재확인한다.

## 주의할 점

- 1~2%라는 목표를 이미지 전체의 중요한 하이라이트나 암부 디테일보다 우선하는 절대 규칙으로 쓰지 않는다.
- 표시되는 초기 클리핑이 의도적으로 순백 또는 순흑이어야 하는 영역인지 확인한다.
- 출력 매체와 후속 톤 조정에 따라 끝점을 다시 점검한다.

## 확실성과 근거

- 클리핑 미리보기는 눈대중보다 반복 가능한 방식으로 검정점과 흰점을 고정하게 한다.
- 아주 적은 픽셀만 끝점에 닿게 해 이미지의 톤 범위를 확보하면서 대규모 디테일 손실을 피한다.

Fstoppers 기사에서 Option/Alt를 누른 채 끝점을 조정하고 약 1~2% 픽셀만 클리핑하는 목표를 직접 제시한다. 어떤 픽셀을 보존해야 하는지는 사진 내용에 따른 해석이다.

## 출처

- 원문 URL: https://fstoppers.com/lightroom/10-lightroom-secrets-will-change-how-edit-photos-901713
- 접근일: 2026-08-07

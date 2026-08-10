---
schema_version: '1.0'
scenario_id: raw-20260810-mwblend
title_ko: 은하수 하늘과 전경을 별도 노출해 자연스럽게 블렌딩하기
status: validated
source:
  type: magazine
  publisher: PetaPixel
  author: Michael Bonocore / Matt Suess
  url: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
  published_at: '2026-06-24'
  accessed_at: '2026-08-10T00:00:00Z'
  original_language: en
device:
  capture_device: Camera capable of RAW capture
  editing_device: null
  software: Adobe Lightroom / Adobe Photoshop
scenario:
  subject: astrophotography
  condition:
  - night
  - milky-way
  - dark-foreground
  intent:
  - control-star-motion
  - retain-foreground-detail
  - blend-sky-and-ground
method:
  steps:
  - tool: Camera exposure
    parameter: 별 움직임을 억제하는 짧은 노출과 높은 ISO로 하늘을 별도 촬영
    value: null
    unit: null
    reported_as: qualitative
  - tool: Camera ISO
    parameter: 일반적인 Milky Way 촬영에서 사용하는 ISO 상한
    value: 6400
    unit: ISO
    reported_as: exact
  - tool: Camera exposure
    parameter: 전경은 하늘과 분리해 더 긴 노출로 촬영
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Sky Replacement
    parameter: 처리된 하늘을 전경 프레임에 삽입하고 산·능선 경계를 feather
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 희미한 은하수와 어두운 지상은 요구 노출이 달라 두 목적별 프레임이 한 장의 타협 노출보다 유리하다는 설명이다.
- 전경을 더 어둡게 유지하면 은하수가 주 피사체로 남는다.
collection:
  collector_version: 1.0.0
  content_sha256: 83d183aa3410899fce8e56e1388232157a47556fbbbf70cf3834dc8548c8e856
  collected_at: '2026-08-10T00:00:00Z'
---

# 은하수 하늘과 전경을 별도 노출해 자연스럽게 블렌딩하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

별 움직임은 억제하면서 매우 어두운 전경의 디테일도 확보해야 하는 은하수 풍경을 촬영·합성할 때 사용한다.

## 촬영/작업 순서

1. 하늘은 짧은 노출과 높은 ISO로, 전경은 별도의 긴 노출로 촬영한다.
2. 두 프레임을 각 영역의 목적에 맞게 따로 현상한다.
3. 전경은 은하수보다 어둡게 유지한다.
4. Photoshop에서 처리한 하늘을 전경 프레임과 결합한다.
5. 능선 경계를 feather하고 100% 확대에서 이음새를 검사한다.

## 추천 시작값 / 조작값

- Camera exposure / 별 움직임을 억제하는 짧은 노출과 높은 ISO로 하늘을 별도 촬영: 원문 정성 표현(수치 추정 없음)
- Camera ISO / 일반적인 Milky Way 촬영에서 사용하는 ISO 상한: 6400 ISO
- Camera exposure / 전경은 하늘과 분리해 더 긴 노출로 촬영: 원문 정성 표현(수치 추정 없음)
- Photoshop Sky Replacement / 처리된 하늘을 전경 프레임에 삽입하고 산·능선 경계를 feather: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 하늘 프레임은 별의 미세 구조와 움직임 억제를 우선해 처리한다.
- 전경 프레임은 자연스러운 암부 색과 낮은 밝기를 우선해 별도로 처리한다.
- 처리한 하늘을 전경 프레임에 합성하고 산이나 능선 경계를 부드럽게 feather한다.
- 100% 확대에서 경계 halo와 밝기 균형을 확인한다.

## 주의할 점

- 하늘과 지상을 한 노출로 타협하면 별 움직임 또는 전경 노이즈 중 하나가 악화될 수 있다.
- 전경을 은하수만큼 밝히면 시선이 분산된다.
- 능선 경계의 feather가 부족하면 합성 이음새와 halo가 드러난다.

## 확실성과 근거

- 희미한 은하수와 어두운 지상은 요구 노출이 달라 두 목적별 프레임이 한 장의 타협 노출보다 유리하다는 설명이다.
- 전경을 더 어둡게 유지하면 은하수가 주 피사체로 남는다.

기사에서 천체사진가 Matt Suess가 하늘과 전경의 별도 노출, 각각의 처리, Photoshop 블렌딩을 직접 권한다. 하늘·전경의 구체적 셔터 속도는 제공되지 않아 정성 단계로 기록했다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- 접근일: 2026-08-10

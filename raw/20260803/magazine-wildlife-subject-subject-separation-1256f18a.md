---
schema_version: '1.0'
scenario_id: raw-20260803-subjectlight01
title_ko: 배경 감광과 방향성 있는 빛으로 피사체 입체감 만들기
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke; Matt Shannon
  url: https://fstoppers.com/education/how-make-your-subject-pop-using-lightroom-and-photoshop-902810
  published_at: '2026-06-07'
  accessed_at: '2026-08-03T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom; Adobe Photoshop
scenario:
  subject: wildlife-subject
  condition:
  - busy-background
  - weak-separation
  intent:
  - subject-separation
  - directional-light
method:
  steps:
  - tool: Adobe Lightroom
    parameter: Linear Gradient에서 Subject를 subtract해 주변만 감광
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Lightroom
    parameter: Radial Gradient에 온기와 밝기를 더하고 Dehaze를 낮춰 안개광 조성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Lightroom
    parameter: Brush로 피사체 눈을 직접 밝힘
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Photoshop
    parameter: Solid Color 레이어에 Lens Flare를 만들고 Screen 혼합 모드 적용
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 선명도만 높이기보다 배경 밝기, 국소 광원, 따뜻한 하이라이트와 차가운 그림자를 누적하면 피사체가 잘라 붙인 듯하지 않으면서 입체적으로 분리된다.
collection:
  collector_version: 1.0.0
  content_sha256: 1256f18ac8e6e2941cbcf6656c8c1520b8b48e30cdb86098537979962539e56f
  collected_at: '2026-08-03T00:00:00Z'
---

# 배경 감광과 방향성 있는 빛으로 피사체 입체감 만들기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

피사체는 선명하지만 배경과 밝기·색이 비슷해 시선이 분산되고 평면적으로 보일 때 사용한다.

## 촬영/작업 순서

1. Linear Gradient로 피사체 주변을 어둡게 하고 Subject subtraction으로 피사체를 보호한다.
2. 자동 마스크 경계를 확인해 빠진 그림자를 Brush로 보완한다.
3. 실제 빛이 들어올 법한 방향에 Radial Gradient를 놓고 따뜻하게 밝힌 뒤 Dehaze를 줄인다.
4. 그림자는 차갑게, 빛 받은 부분은 따뜻하게 유지하고 눈을 소폭 밝힌다.
5. 필요하면 Photoshop에서 같은 방향의 Lens Flare를 더하고 피사체 위는 마스킹한다.

## 추천 시작값 / 조작값

- Adobe Lightroom / Linear Gradient에서 Subject를 subtract해 주변만 감광: 원문 정성 표현(수치 추정 없음)
- Adobe Lightroom / Radial Gradient에 온기와 밝기를 더하고 Dehaze를 낮춰 안개광 조성: 원문 정성 표현(수치 추정 없음)
- Adobe Lightroom / Brush로 피사체 눈을 직접 밝힘: 원문 정성 표현(수치 추정 없음)
- Adobe Photoshop / Solid Color 레이어에 Lens Flare를 만들고 Screen 혼합 모드 적용: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 작은 변화를 한 단계씩 누적하고 각 단계 전후를 비교한다.
- 부차적 플레어 아티팩트는 Remove 도구로 제거하고 피사체 질감이 씻기면 레이어 마스크를 강화한다.

## 주의할 점

- Subject subtraction 경계를 수동 보정하지 않으면 밝은 테두리와 halo가 생길 수 있다.
- Radial light와 Lens Flare 방향이 원래 조명과 맞지 않으면 합성 티가 난다.
- 강한 감광이나 플레어로 피사체가 오려 붙인 듯 보이거나 질감이 사라지지 않게 한다.

## 확실성과 근거

- 선명도만 높이기보다 배경 밝기, 국소 광원, 따뜻한 하이라이트와 차가운 그림자를 누적하면 피사체가 잘라 붙인 듯하지 않으면서 입체적으로 분리된다.

Lightroom과 Photoshop의 순서 및 정성적 조정 방향은 출처가 직접 설명했다. 슬라이더 수치는 공개되지 않아 추정하지 않았다.

## 출처

- 원문 URL: https://fstoppers.com/education/how-make-your-subject-pop-using-lightroom-and-photoshop-902810
- 접근일: 2026-08-03

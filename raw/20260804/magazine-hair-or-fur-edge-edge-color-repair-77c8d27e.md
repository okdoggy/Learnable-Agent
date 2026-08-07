---
schema_version: '1.0'
scenario_id: raw-20260804-hairclone01
title_ko: 배경색이 밴 머리카락 가장자리를 클리핑 복제로 복원
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/education/your-layer-mask-isnt-problem-heres-what-actually-causes-hair-fringing-902791
  published_at: '2026-06-04'
  accessed_at: '2026-08-04T00:00:40Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Photoshop
scenario:
  subject: hair-or-fur-edge
  condition:
  - changed-background
  - color-fringing
  - masked-hair
  intent:
  - edge-color-repair
  - preserve-texture
  - non-destructive-edit
method:
  steps:
  - tool: Clone Stamp
    parameter: Current and Below에서 안쪽의 깨끗한 결을 가장자리 방향으로 복제
    value: null
    unit: null
    reported_as: qualitative
  - tool: Layers
    parameter: 피사체 바로 위의 빈 보정 레이어를 피사체에 클리핑
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 색 테두리의 원인이 마스크 모양이 아니라 원래 배경색을 머금은 가장자리 픽셀이라면 마스크를 더 깎는 대신 실제 피사체 질감과 색으로 픽셀을 교체해야 한다.
- 클리핑 레이어는 실루엣 밖으로 뻗은 복제 픽셀을 숨기면서 수정 내용을 비파괴적으로 분리한다.
collection:
  collector_version: 1.0.0
  content_sha256: 77c8d27e26d86b76e09db06bfed24bed121bc24fe27b28d1b1b54bae3a398ce1
  collected_at: '2026-08-04T00:00:40Z'
---

# 배경색이 밴 머리카락 가장자리를 클리핑 복제로 복원

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

배경을 교체한 뒤 마스크 윤곽은 깨끗하지만 머리카락이나 털의 가장자리 픽셀에 원래 배경색이 남아 색 테두리가 보일 때 사용한다.

## 촬영/작업 순서

1. 마스크 자체의 누락이 아니라 가장자리 픽셀의 색 오염인지 먼저 확인한다.
2. 마스킹된 피사체 바로 위에 빈 보정 레이어를 만들고 피사체 레이어에 클리핑한다.
3. Clone Stamp를 Current and Below로 두고 피사체 안쪽의 깨끗한 결을 샘플링한다.
4. 안쪽에서 가장자리 쪽으로 칠해 오염된 색과 질감을 실제 피사체 결로 교체한다.
5. 수정 부위별로 클리핑 레이어를 나누어 비파괴적으로 정리한다.

## 추천 시작값 / 조작값

- Clone Stamp / Current and Below에서 안쪽의 깨끗한 결을 가장자리 방향으로 복제: 원문 정성 표현(수치 추정 없음)
- Layers / 피사체 바로 위의 빈 보정 레이어를 피사체에 클리핑: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 서로 다른 밝기와 색의 배경을 임시로 대어 잔여 색 테두리가 드러나는지 확인한다.
- 결이 필요한 곳은 Clone Stamp를 쓰고, 단순한 색 교정만 필요한 곳은 Brush를 고려한다.
- 확대 화면과 전체 화면을 번갈아 보며 반복 무늬와 두꺼워진 윤곽을 점검한다.

## 주의할 점

- 마스크를 계속 안쪽으로 깎으면 머리카락의 자연스러운 잔결이 사라질 수 있다.
- 가장자리 바깥으로 복제한 픽셀이 노출되지 않도록 보정 레이어의 클리핑 상태를 유지한다.
- 한 지점만 반복 샘플링하면 복제 패턴이 눈에 띌 수 있다.

## 확실성과 근거

- 색 테두리의 원인이 마스크 모양이 아니라 원래 배경색을 머금은 가장자리 픽셀이라면 마스크를 더 깎는 대신 실제 피사체 질감과 색으로 픽셀을 교체해야 한다.
- 클리핑 레이어는 실루엣 밖으로 뻗은 복제 픽셀을 숨기면서 수정 내용을 비파괴적으로 분리한다.

출처가 클리핑된 빈 레이어, Current and Below 샘플링, 안쪽의 깨끗한 결을 가장자리로 복제하는 절차를 직접 설명한다. 배경색 교체 후의 색 테두리를 픽셀 오염으로 진단하는 범위까지 직접 근거가 있으며, 수치형 브러시 설정은 제시되지 않았다.

## 출처

- 원문 URL: https://fstoppers.com/education/your-layer-mask-isnt-problem-heres-what-actually-causes-hair-fringing-902791
- 접근일: 2026-08-04

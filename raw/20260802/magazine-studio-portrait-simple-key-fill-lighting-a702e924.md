---
schema_version: '1.0'
scenario_id: raw-20260802-wallfill01
title_ko: 두 개의 연속광과 흰 벽 반사로 단순한 키·필 조명 구성
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/education/how-get-natural-looking-studio-light-901630
  published_at: '2026-04-14'
  accessed_at: '2026-08-02T00:00:00Z'
  original_language: en
device:
  capture_device: Camera with 50mm lens or Viltrox 85mm f/1.8
  editing_device: null
  software: Photoshop
scenario:
  subject: studio-portrait
  condition:
  - minimal-studio-gear
  - white-wall-available
  intent:
  - simple-key-fill-lighting
  - soft-shadow-detail
method:
  steps:
  - tool: Zhiyun Molus B500
    parameter: 원형 projector attachment를 단 키 라이트 배치
    value: null
    unit: null
    reported_as: qualitative
  - tool: Zhiyun Molus B500
    parameter: 두 번째 조명을 흰 벽으로 향해 반사 필 생성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Camera
    parameter: aperture
    value: 1.4
    unit: f-number
    reported_as: exact
  - tool: Camera
    parameter: shutter speed
    value: 1/200
    unit: s
    reported_as: exact
  - tool: Lens
    parameter: 50mm와 85mm 렌즈 사용
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 한 조명은 형태를 만드는 키, 다른 조명은 흰 벽을 넓은 반사면으로 쓰는 필 역할을 해 V-flat 없이도 단순한 두 광원 구성이 된다.
collection:
  collector_version: 1.0.0
  content_sha256: a702e924baf54e749be83b449d69765b70d73b5c989e33f77e98ab806562010d
  collected_at: '2026-08-02T00:00:00Z'
---

# 두 개의 연속광과 흰 벽 반사로 단순한 키·필 조명 구성

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

V-flat이나 별도 반사판 없이 흰 벽이 있는 스튜디오에서 두 개의 연속광만으로 방향성 있는 키와 부드러운 필을 만들 때 사용한다.

## 촬영/작업 순서

1. 원형 projector가 달린 첫 조명을 키로 둔다.
2. 두 번째 조명을 흰 벽에 비춰 반사 필을 만든다.
3. 키와 필의 비율을 조절해 얼굴 형태와 그림자 디테일을 균형 잡는다.
4. 렌즈별 구도를 비교해 최종 프레임을 정한다.

## 추천 시작값 / 조작값

- Zhiyun Molus B500 / 원형 projector attachment를 단 키 라이트 배치: 원문 정성 표현(수치 추정 없음)
- Zhiyun Molus B500 / 두 번째 조명을 흰 벽으로 향해 반사 필 생성: 원문 정성 표현(수치 추정 없음)
- Camera / aperture: 1.4 f-number
- Camera / shutter speed: 1/200 s
- Lens / 50mm와 85mm 렌즈 사용: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 키 라이트로 얼굴 형태가 충분히 잡히는지 먼저 확인한다.
- 두 번째 조명을 흰 벽에 반사한 뒤 그림자 디테일만 필요한 만큼 올린다.
- 50mm와 85mm 화각에서 배경 포함 범위와 얼굴 원근을 비교한다.

## 주의할 점

- 벽 반사 필의 색이 벽 색 영향을 받을 수 있으므로 흰 벽을 사용한다.
- 필 라이트가 너무 강하면 키 라이트가 만든 방향성과 얼굴 입체감이 사라진다.
- f/1.4와 1/200초는 해당 촬영의 기록값이며 현장 광량에 맞게 재측정한다.

## 확실성과 근거

- 한 조명은 형태를 만드는 키, 다른 조명은 흰 벽을 넓은 반사면으로 쓰는 필 역할을 해 V-flat 없이도 단순한 두 광원 구성이 된다.

Fstoppers 기사가 Zhiyun Molus B500 두 대, 원형 projector 키, 흰 벽 반사 필, f/1.4와 1/200초를 직접 제시한다.

## 출처

- 원문 URL: https://fstoppers.com/education/how-get-natural-looking-studio-light-901630
- 접근일: 2026-08-02

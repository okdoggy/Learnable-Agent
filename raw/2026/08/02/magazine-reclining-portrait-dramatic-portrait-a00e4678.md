---
schema_version: '1.0'
scenario_id: raw-20260802-papertexture01
title_ko: 구긴 검은 배경지와 스치는 후방광으로 조각적 인물 연출
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/lighting/simple-trick-more-dramatic-portraits-900497
  published_at: '2026-03-05'
  accessed_at: '2026-08-02T00:00:00Z'
  original_language: en
device:
  capture_device: Nikon Z6 II with 50mm lens
  editing_device: null
  software: Capture One Pro
scenario:
  subject: reclining-portrait
  condition:
  - small-studio
  - textured-black-background
  intent:
  - dramatic-portrait
  - reveal-surface-texture
method:
  steps:
  - tool: Seamless paper
    parameter: 검은 seamless paper 폭
    value: 9
    unit: ft
    reported_as: exact
  - tool: Set styling
    parameter: 종이를 구겨 모델 주위에 주름 배치
    value: null
    unit: null
    reported_as: qualitative
  - tool: Godox AD600Pro with 128 cm parabolic modifier
    parameter: 후방 키 라이트가 종이 표면을 비스듬히 스치도록 배치
    value: null
    unit: null
    reported_as: qualitative
  - tool: Godox AD600Pro with medium deep umbrella
    parameter: 필을 키보다 약하게 두어 얼굴 그림자와 눈 캐치라이트만 보완
    value: null
    unit: null
    reported_as: qualitative
  - tool: Camera position
    parameter: 위쪽 시점에서 촬영
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 비스듬히 스치는 빛은 주름의 돌출부와 골을 하이라이트와 그림자로 분리해 저렴한 종이를 조각적 배경으로 만든다.
- 약한 필은 어두운 분위기를 유지하면서 얼굴과 눈의 정보를 보존한다.
collection:
  collector_version: 1.0.0
  content_sha256: a00e4678e6a5b3508aafa1c7e03c5c71942e1136d7e5b41f05087daa8c4fa6fe
  collected_at: '2026-08-02T00:00:00Z'
---

# 구긴 검은 배경지와 스치는 후방광으로 조각적 인물 연출

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

작은 스튜디오에서 값비싼 세트 없이 검은 종이의 주름과 그림자를 활용해 질감이 강한 극적인 인물 사진을 만들 때 사용한다.

## 촬영/작업 순서

1. 검은 배경지를 구겨 모델 주위에 배치한다.
2. 주광을 뒤쪽에 두어 종이를 비스듬히 스치게 한다.
3. 약한 정면 필로 얼굴과 눈만 보완한다.
4. 위에서 촬영해 주름이 모델을 감싸는 구도를 만든다.

## 추천 시작값 / 조작값

- Seamless paper / 검은 seamless paper 폭: 9 ft
- Set styling / 종이를 구겨 모델 주위에 주름 배치: 원문 정성 표현(수치 추정 없음)
- Godox AD600Pro with 128 cm parabolic modifier / 후방 키 라이트가 종이 표면을 비스듬히 스치도록 배치: 원문 정성 표현(수치 추정 없음)
- Godox AD600Pro with medium deep umbrella / 필을 키보다 약하게 두어 얼굴 그림자와 눈 캐치라이트만 보완: 원문 정성 표현(수치 추정 없음)
- Camera position / 위쪽 시점에서 촬영: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 테더 촬영 화면에서 종이 주름의 하이라이트와 그림자 분리가 보이는지 확인한다.
- 얼굴 그림자에 디테일과 눈 캐치라이트가 남는 최소 필 강도를 찾는다.
- 위쪽 구도가 주름이 모델을 감싸며 퍼지는 형태를 충분히 담는지 점검한다.

## 주의할 점

- 뒤쪽 키 라이트 때문에 얼굴 그림자가 빠르게 깊어질 수 있어 눈 디테일을 확인한다.
- 필 라이트를 강하게 하면 어두운 분위기와 종이의 입체감이 사라진다.
- 정면광은 구겨진 종이 표면을 평평하게 보이게 한다.

## 확실성과 근거

- 비스듬히 스치는 빛은 주름의 돌출부와 골을 하이라이트와 그림자로 분리해 저렴한 종이를 조각적 배경으로 만든다.
- 약한 필은 어두운 분위기를 유지하면서 얼굴과 눈의 정보를 보존한다.

Fstoppers 기사가 Nathan Elson의 검은 seamless paper, 후방 사광, 보조 필, 위쪽 카메라 구성을 직접 설명한다. 미터링 수치는 제공하지 않는다.

## 출처

- 원문 URL: https://fstoppers.com/lighting/simple-trick-more-dramatic-portraits-900497
- 접근일: 2026-08-02

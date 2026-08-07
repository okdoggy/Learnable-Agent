---
schema_version: '1.0'
scenario_id: raw-20260802-warmlight01
title_ko: 색온도가 다른 키와 배경광으로 따뜻한 인물과 차가운 배경 분리
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
  capture_device: Sony a7R V
  editing_device: null
  software: Photoshop
scenario:
  subject: studio-portrait
  condition:
  - studio-portrait
  - mixed-color-temperature
  intent:
  - warm-cool-separation
  - shape-subject-with-light
method:
  steps:
  - tool: Zhiyun Molus B500
    parameter: continuous LED color temperature
    value: 2700
    unit: K
    reported_as: exact
  - tool: Camera
    parameter: camera white balance
    value: 5600
    unit: K
    reported_as: exact
  - tool: Godox spotlight attachment
    parameter: 원통형 attachment로 세로 띠 키 라이트 형성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Godox AD600 Pro
    parameter: V-flat에 반사한 스트로브로 배경 조명
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 카메라 기준보다 따뜻한 LED는 피사체를 따뜻하게 렌더링한다.
- 스트로브가 비추는 배경은 상대적으로 차갑고 파랗게 보여 후반 작업만으로 흉내 내기 어려운 물리적 색 분리가 생긴다.
collection:
  collector_version: 1.0.0
  content_sha256: 19a309da95fa1c50088e6e3055706edced2fa915cfd2ff6ec0fa52256d292390
  collected_at: '2026-08-02T00:00:00Z'
---

# 색온도가 다른 키와 배경광으로 따뜻한 인물과 차가운 배경 분리

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

스튜디오 인물에서 후보정보다 촬영 단계에서 따뜻한 피사체와 차가운 배경을 확실하게 분리하고 형태감 있는 세로 키 라이트를 만들 때 사용한다.

## 촬영/작업 순서

1. 따뜻한 연속광을 피사체 키로 배치한다.
2. 카메라 화이트 밸런스를 더 높은 색온도로 고정한다.
3. 스트로브를 V-flat에 반사해 배경을 비춘다.
4. 스필을 통제하며 색 분리와 형태를 확인한다.

## 추천 시작값 / 조작값

- Zhiyun Molus B500 / continuous LED color temperature: 2700 K
- Camera / camera white balance: 5600 K
- Godox spotlight attachment / 원통형 attachment로 세로 띠 키 라이트 형성: 원문 정성 표현(수치 추정 없음)
- Godox AD600 Pro / V-flat에 반사한 스트로브로 배경 조명: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 테스트 컷에서 피사체가 따뜻하고 배경이 약간 파랗게 보이는지 확인한다.
- 세로 띠 모양의 키 라이트가 피사체 형태를 살리는지 점검한다.
- 광원 스필을 조절해 따뜻함과 차가움의 물리적 분리를 유지한다.

## 주의할 점

- 2,700 K 광원과 5,600 K 화이트 밸런스는 의도적인 불일치이므로 자동 화이트 밸런스로 상쇄하지 않는다.
- 큰 spotlight attachment는 스틸 사진에 과도할 수 있어 공간과 용도에 맞는 작은 장비를 고려한다.
- 배경 스트로브 스필이 피사체에 섞이면 온도 분리가 약해진다.

## 확실성과 근거

- 카메라 기준보다 따뜻한 LED는 피사체를 따뜻하게 렌더링한다.
- 스트로브가 비추는 배경은 상대적으로 차갑고 파랗게 보여 후반 작업만으로 흉내 내기 어려운 물리적 색 분리가 생긴다.

Fstoppers 기사가 LED 2,700 K, 카메라 화이트 밸런스 5,600 K, V-flat 반사 AD600 Pro 배경광을 직접 명시한다.

## 출처

- 원문 URL: https://fstoppers.com/education/how-get-natural-looking-studio-light-901630
- 접근일: 2026-08-02

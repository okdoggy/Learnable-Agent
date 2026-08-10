---
schema_version: '1.0'
scenario_id: raw-20260809-denoisefirst
title_ko: 고감도 은하수 RAW를 현상 전에 먼저 노이즈 제거하기
status: validated
source:
  type: magazine
  publisher: PetaPixel
  author: Michael Bonocore; method by Matt Suess
  url: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
  published_at: '2026-06-24'
  accessed_at: '2026-08-09T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: DxO PureRAW, Adobe Lightroom
scenario:
  subject: milky-way-raw
  condition:
  - high-iso
  - raw
  - visible-noise
  intent:
  - reduce-noise
  - preserve-stars
  - natural-night-color
method:
  steps:
  - tool: DxO PureRAW noise reduction
    parameter: 개발·색 보정·선명화 전 손대지 않은 RAW에 먼저 적용
    value: null
    unit: null
    reported_as: qualitative
  - tool: DxO DeepPRIME 3
    parameter: 섬세한 별 디테일을 보존하기 위해 저자가 자주 선택하는 모델
    value: null
    unit: null
    reported_as: qualitative
  - tool: DxO Lens Sharpness Standard
    parameter: 저자가 유지하는 렌즈 선명도 수준
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Adobe Landscape profile
    parameter: 정리된 RAW의 기본 현상 프로필
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Clarity and Dehaze
    parameter: 은하수 구조와 노이즈 증가를 함께 보며 보수적으로 적용
    value: null
    unit: null
    reported_as: qualitative
  - tool: Preview zoom
    parameter: 주요 처리마다 별과 후광을 검사
    value: 100
    unit: percent
    reported_as: exact
rationale_ko:
- 노이즈 제거를 가장 먼저 하면 후속 대비·명료도·선명화가 거친 입자를 증폭하기 전에 깨끗한 기반을 만들 수 있다.
- 은하수 사진에서는 완전한 평활화보다 작은 별과 자연스러운 입자를 보존하는 것이 중요하다.
collection:
  collector_version: 1.0.0
  content_sha256: 6b14c18c3378f8c7093ed5800e4f0fc15f1feeca63647b980a2fa196253181dc
  collected_at: '2026-08-09T00:00:00Z'
---

# 고감도 은하수 RAW를 현상 전에 먼저 노이즈 제거하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

고감도 은하수 RAW가 평평하고 거칠며 작은 별 디테일이 노이즈에 묻혀 있어, 대비나 선명도를 올리기 전에 깨끗한 기반이 필요할 때 사용한다.

## 촬영/작업 순서

1. 아직 보정하지 않은 RAW를 노이즈 제거 단계로 먼저 보낸다.
2. 강한 평활화보다 별 보존을 우선해 처리 모델과 강도를 이미지별로 선택한다.
3. 렌즈 선명도는 Standard에서 시작한다.
4. 100% 보기로 작은 별의 소실과 인공적인 디테일을 확인한다.
5. 정리된 파일을 Lightroom에서 열어 화이트 밸런스부터 절제된 기본 현상을 진행한다.

## 추천 시작값 / 조작값

- DxO PureRAW noise reduction / 개발·색 보정·선명화 전 손대지 않은 RAW에 먼저 적용: 원문 정성 표현(수치 추정 없음)
- DxO DeepPRIME 3 / 섬세한 별 디테일을 보존하기 위해 저자가 자주 선택하는 모델: 원문 정성 표현(수치 추정 없음)
- DxO Lens Sharpness Standard / 저자가 유지하는 렌즈 선명도 수준: 원문 정성 표현(수치 추정 없음)
- Lightroom Adobe Landscape profile / 정리된 RAW의 기본 현상 프로필: 원문 정성 표현(수치 추정 없음)
- Lightroom Clarity and Dehaze / 은하수 구조와 노이즈 증가를 함께 보며 보수적으로 적용: 원문 정성 표현(수치 추정 없음)
- Preview zoom / 주요 처리마다 별과 후광을 검사: 100 percent

## 보정 루틴

- 처리 전후를 100%로 비교해 작은 별이 사라지거나 부풀지 않았는지 확인한다.
- 정리된 파일을 Lightroom에서 열어 Adobe Landscape 프로필로 절제된 기본 현상을 시작한다.
- 화이트 밸런스를 은하수 중심부의 자연스러운 노랑-마젠타 균형에 맞춘 뒤 대비·명료도·디헤이즈를 약하게 더한다.
- 각 슬라이더가 주는 구조 개선보다 노이즈 증가가 커지는 지점에서 되돌린다.

## 주의할 점

- 강한 RAW 노이즈 제거는 작은 별을 부드럽게 지울 수 있으므로 약간의 입자를 남기는 편이 낫다.
- 노이즈 제거 전에 선명도·대비·명료도를 올리면 거친 입자가 강화되어 후속 처리에 고착될 수 있다.
- Lens Sharpness의 Hard 설정은 인공적인 디테일과 노이즈를 함께 날카롭게 만들 수 있다.
- 모든 이미지에 같은 노이즈 모델을 고정하지 말고 별 보존 여부를 100% 보기에서 판단한다.

## 확실성과 근거

- 노이즈 제거를 가장 먼저 하면 후속 대비·명료도·선명화가 거친 입자를 증폭하기 전에 깨끗한 기반을 만들 수 있다.
- 은하수 사진에서는 완전한 평활화보다 작은 별과 자연스러운 입자를 보존하는 것이 중요하다.

원문은 손대지 않은 RAW를 먼저 노이즈 제거하고, 섬세한 별밭에서는 DeepPRIME 3과 Standard 렌즈 선명도를 자주 선택한다고 직접 설명한다. 설정 선택은 이미지별 판단이라고 명시되어 있어 보편적 고정값으로 확장하지 않았다. 기사는 DxO 협찬임을 공개하므로 특정 제품의 성능 주장은 유보하고 처리 순서와 검사 기준만 기록한다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- 접근일: 2026-08-09

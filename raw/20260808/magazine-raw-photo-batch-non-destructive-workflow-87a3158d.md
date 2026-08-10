---
schema_version: '1.0'
scenario_id: raw-20260808-purerawhandoff01
title_ko: Lightroom에서 원본 RAW를 PureRAW로 전달하고 이중 보정 방지
status: validated
source:
  type: magazine
  publisher: PetaPixel
  author: Michael Bonocore
  url: https://petapixel.com/2026/04/09/dxo-pureraw-6-the-ultimate-beginners-guide/
  published_at: '2026-04-09'
  accessed_at: '2026-08-08T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom Classic and DxO PureRAW 6
scenario:
  subject: raw-photo-batch
  condition:
  - raw-preprocessing
  - lightroom-catalog
  - noise-and-optical-correction
  intent:
  - non-destructive-workflow
  - avoid-double-processing
  - batch-validation
method:
  steps:
  - tool: Lightroom Classic selection
    parameter: 전체 작업 전 시험 처리할 RAW 파일 수
    value: 5-10
    unit: images
    reported_as: exact
  - tool: Lightroom Classic
    parameter: 원본 RAW 데이터를 전달하는 실행 경로
    value: File > Plug-in Extras > Preview and Process with DxO PureRAW 6
    unit: null
    reported_as: exact
  - tool: Preview zoom
    parameter: 처리 결과의 세부 상태를 검사한다
    value: 100
    unit: percent
    reported_as: exact
  - tool: Lightroom Lens Corrections and Noise Reduction
    parameter: PureRAW 처리 DNG에서 비활성화한다
    value: 'Off'
    unit: null
    reported_as: exact
rationale_ko:
- PureRAW는 원본 센서 데이터로 demosaicing·노이즈·광학 보정을 수행하므로 Lightroom이 먼저 렌더링한 TIFF나 PSD보다 원본 RAW 전달 경로가 필요하다.
- PureRAW가 이미 수행한 렌즈 보정과 노이즈 제거를 Lightroom에서 반복하면 이중 처리로 품질 저하가 생길 수 있다.
- 소량 시험과 100% 검토는 대규모 일괄 처리 전에 아티팩트와 과보정을 발견하게 한다.
collection:
  collector_version: 1.0.0
  content_sha256: 87a3158d31f86d49b3b0ae9cecb00e5c152f058f46dddb305b6c83007ae3003b
  collected_at: '2026-08-08T00:00:00Z'
---

# Lightroom에서 원본 RAW를 PureRAW로 전달하고 이중 보정 방지

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

Lightroom Classic 카탈로그의 RAW를 PureRAW 6에서 선처리한 뒤 DNG로 돌려받아 창의적 편집을 이어가면서, 원본 센서 데이터 손실과 중복 노이즈·렌즈 보정을 피해야 할 때 사용한다.

## 촬영/작업 순서

1. Lightroom Classic의 Edit In을 사용하지 않는다.
2. 원본 RAW를 File > Plug-in Extras 또는 Export의 PureRAW 6 명령으로 보낸다.
3. 처음에는 5~10장만 Preview and Process로 시험한다.
4. 처리 DNG가 카탈로그로 돌아오면 Lightroom의 Lens Corrections와 Noise Reduction을 끈다.
5. 100% 확대 검토를 통과한 설정만 전체 촬영분에 적용한다.

## 추천 시작값 / 조작값

- Lightroom Classic selection / 전체 작업 전 시험 처리할 RAW 파일 수: 5-10 images
- Lightroom Classic / 원본 RAW 데이터를 전달하는 실행 경로: File > Plug-in Extras > Preview and Process with DxO PureRAW 6
- Preview zoom / 처리 결과의 세부 상태를 검사한다: 100 percent
- Lightroom Lens Corrections and Noise Reduction / PureRAW 처리 DNG에서 비활성화한다: Off

## 보정 루틴

- Lightroom Classic에서 원본 RAW 5~10장을 선택한다.
- File > Plug-in Extras > Preview and Process with DxO PureRAW 6로 실행한다.
- 미리보기에서 노이즈와 광학 보정을 확인하고 Process Now를 눌러 DNG를 카탈로그로 돌려받는다.
- 반환 DNG에서 Lightroom의 Lens Corrections, Noise Reduction, AI Denoise를 끈 상태인지 확인한다.
- 100% 확대에서 디테일, 노이즈, 기하 보정, 색 이동을 검토한 뒤 전체 촬영분으로 확장한다.

## 주의할 점

- Lightroom의 Edit In은 RAW를 TIFF 또는 PSD로 먼저 렌더링하므로 PureRAW가 원본 센서 데이터를 사용하지 못한다.
- 처리된 DNG에서 Lightroom Lens Corrections, 일반 Noise Reduction, AI Denoise를 다시 켜면 이중 보정으로 디테일 연화, 아티팩트, 색 변화, 과도한 기하 보정이 생길 수 있다.
- 전체 촬영분을 일괄 처리하기 전에 5~10장을 시험하고 100% 확대에서 확인한다.
- 후원 기사이므로 제품 성능 평가는 홍보 맥락을 감안하되, 여기서는 명시된 데이터 흐름과 중복 처리 방지 절차만 기록한다.

## 확실성과 근거

- PureRAW는 원본 센서 데이터로 demosaicing·노이즈·광학 보정을 수행하므로 Lightroom이 먼저 렌더링한 TIFF나 PSD보다 원본 RAW 전달 경로가 필요하다.
- PureRAW가 이미 수행한 렌즈 보정과 노이즈 제거를 Lightroom에서 반복하면 이중 처리로 품질 저하가 생길 수 있다.
- 소량 시험과 100% 검토는 대규모 일괄 처리 전에 아티팩트와 과보정을 발견하게 한다.

PetaPixel의 DxO 후원 가이드가 Lightroom Classic에서 File > Plug-in Extras 또는 Export를 통해 원본 RAW를 보내고, 반환된 DNG에서는 Lightroom의 Lens Corrections와 Noise Reduction을 끄라고 직접 설명한다. 시험 묶음 5~10장과 100% 검토도 원문이 명시한다.

## 출처

- 원문 URL: https://petapixel.com/2026/04/09/dxo-pureraw-6-the-ultimate-beginners-guide/
- 접근일: 2026-08-08

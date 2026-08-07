---
schema_version: '1.0'
scenario_id: raw-20260803-fogdepth01
title_ko: 저노출 안개 풍경을 겹친 마스크로 입체화
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke; Christian Möhrle
  url: https://fstoppers.com/lightroom/how-add-real-depth-lightroom-without-overediting-900105
  published_at: '2026-02-08'
  accessed_at: '2026-08-03T00:00:00Z'
  original_language: en
device:
  capture_device: Drone camera
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: foggy-landscape
  condition:
  - underexposed-raw
  - fog
  - backlight
  intent:
  - recover-tones
  - add-natural-depth
method:
  steps:
  - tool: Adobe Lightroom Denoise
    parameter: 큰 폭의 노출·그림자 복구 전에 노이즈 선처리
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Lightroom
    parameter: Exposure, Shadows, Blacks를 올리고 Highlights를 낮춰 하늘 보호
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Lightroom
    parameter: Clarity와 Dehaze를 낮춰 부드러운 안개 유지
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Lightroom Brush
    parameter: 매우 부드러운 Brush, 높은 Density, 낮은 Flow로 안개 하이라이트 누적
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 저노출 파일은 밝히기 전에 노이즈를 관리해야 거친 질감 확대를 줄일 수 있다.
- 전경 안개, 하늘색, 수평선 빛, 국소 glow를 분리하면 평평한 안개에 자연스러운 깊이를 만들기 쉽다.
collection:
  collector_version: 1.0.0
  content_sha256: 348866a1fd6ab02047df48495ca336ac36636ecf48528b71853bde8360efec81
  collected_at: '2026-08-03T00:00:00Z'
---

# 저노출 안개 풍경을 겹친 마스크로 입체화

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

역광 안개 풍경의 RAW가 매우 어둡고 평평하지만 HDR처럼 거칠게 만들지 않고 공간감을 되살리고 싶을 때 사용한다.

## 촬영/작업 순서

1. 노출을 크게 올리기 전에 Denoise를 수행한다.
2. Exposure를 올리고 Highlights를 낮춰 하늘을 보호한 뒤 Shadows와 Blacks로 세부를 회복한다.
3. 화이트 밸런스를 약간 차갑게 하고 옅은 자홍 편향을 바로잡는다.
4. 전경 안개에는 Linear Gradient로 Highlights와 Whites를 올리고 필요한 만큼만 Clarity를 더한다.
5. 하늘 파란 영역은 Color Range로 어둡게 하되 Gradient subtraction으로 밝아야 할 영역을 제외한다.
6. 낮은 Flow의 부드러운 Brush로 안개의 일부 하이라이트만 반복해 쌓는다.

## 추천 시작값 / 조작값

- Adobe Lightroom Denoise / 큰 폭의 노출·그림자 복구 전에 노이즈 선처리: 원문 정성 표현(수치 추정 없음)
- Adobe Lightroom / Exposure, Shadows, Blacks를 올리고 Highlights를 낮춰 하늘 보호: 원문 정성 표현(수치 추정 없음)
- Adobe Lightroom / Clarity와 Dehaze를 낮춰 부드러운 안개 유지: 원문 정성 표현(수치 추정 없음)
- Adobe Lightroom Brush / 매우 부드러운 Brush, 높은 Density, 낮은 Flow로 안개 하이라이트 누적: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 수평선 쪽 하늘은 별도 마스크로 밝고 따뜻하게 만들어 차가운 안개와 분리한다.
- 태양 glow가 필요하면 여러 Radial Gradient를 겹쳐 형태를 만들고 각 기여를 비교한다.

## 주의할 점

- 노이즈를 확인하지 않고 Exposure를 먼저 크게 올리지 않는다.
- 과도한 Contrast, Clarity, Dehaze로 안개를 바삭하고 인공적으로 만들지 않는다.
- 높은 Flow의 강한 브러시 획은 붓자국과 거친 질감을 만들 수 있다.
- glow의 의도적 clipping은 선택 사항이며 장면에 맞지 않으면 피한다.

## 확실성과 근거

- 저노출 파일은 밝히기 전에 노이즈를 관리해야 거친 질감 확대를 줄일 수 있다.
- 전경 안개, 하늘색, 수평선 빛, 국소 glow를 분리하면 평평한 안개에 자연스러운 깊이를 만들기 쉽다.

보정 순서와 마스크 구성, 낮은 Flow·높은 Density 원칙은 출처가 직접 설명했다. 구체 슬라이더 값은 제시되지 않았다.

## 출처

- 원문 URL: https://fstoppers.com/lightroom/how-add-real-depth-lightroom-without-overediting-900105
- 접근일: 2026-08-03

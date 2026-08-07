---
schema_version: '1.0'
scenario_id: raw-20260806-onelightdiff01
title_ko: 좁은 공간에서 스피드라이트 이중 확산과 랩 필로 다목적 인물 촬영
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/education/one-light-setup-produces-headshots-and-brand-portraits-same-frame-902458
  published_at: '2026-05-19'
  accessed_at: '2026-08-06T00:00:00Z'
  original_language: en
device:
  capture_device: Sony a7R V with Sony F60RM II speedlight
  editing_device: null
  software: Camera capture with Sony WRC-1M and Atomos Ninja V monitoring
scenario:
  subject: studio-portrait
  condition:
  - small-home-studio
  - single-speedlight
  - ambient-light-suppressed
  intent:
  - soft-clean-light
  - multi-use-master-frame
  - retain-facial-dimension
method:
  steps:
  - tool: Studio space
    parameter: 시연 공간의 폭
    value: 2.5
    unit: meter
    reported_as: exact
  - tool: Studio space
    parameter: 시연 공간의 깊이
    value: 4
    unit: meter
    reported_as: exact
  - tool: Shoot-through umbrella
    parameter: 스피드라이트의 첫 번째 확산 우산 지름
    value: 65
    unit: centimeter
    reported_as: exact
  - tool: Diffusion panel
    parameter: 우산을 통과한 빛의 두 번째 확산 패널 크기
    value: 1 x 2
    unit: meter
    reported_as: exact
  - tool: Camera shutter speed
    parameter: 주변광을 억제한 시연 설정
    value: 1/400
    unit: second
    reported_as: exact
  - tool: Camera aperture
    parameter: 시연 설정
    value: f/1.4
    unit: null
    reported_as: exact
  - tool: Camera ISO
    parameter: 시연 설정
    value: 100
    unit: ISO
    reported_as: exact
  - tool: Flash power
    parameter: 시연 설정
    value: 1/4
    unit: power
    reported_as: exact
  - tool: White balance
    parameter: 시연 설정
    value: 4800
    unit: kelvin
    reported_as: exact
  - tool: Reflector
    parameter: 키 라이트 정반대가 아니라 빛이 얼굴을 감싸도록 각도와 위치를 조절한다
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 작은 우산 뒤에 더 큰 확산 패널을 두면 소형 스피드라이트의 겉보기 광원이 커져 부드럽고 깨끗한 빛을 만든다.
- 주변광을 거의 제거하면 스피드라이트가 사실상 유일한 광원이 되어 결과를 예측하기 쉽다.
- 반사판을 단순 정면 필이 아니라 감싸는 방향으로 배치하면 평평함을 줄이고 자연스러운 입체감을 유지한다.
collection:
  collector_version: 1.0.0
  content_sha256: 1244f105d14d61dcac0a2008cad4ec92e496348266f198f223f3f61be41a911d
  collected_at: '2026-08-06T00:00:00Z'
---

# 좁은 공간에서 스피드라이트 이중 확산과 랩 필로 다목적 인물 촬영

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

폭 2.5m, 깊이 4m 정도의 작은 홈 스튜디오에서 스피드라이트 하나로 헤드샷, 셋카드, 소셜 이미지, 브랜드 포스터에 재사용할 수 있는 깨끗한 인물을 촬영할 때 사용한다.

## 촬영/작업 순서

1. Sony F60RM II를 65cm shoot-through umbrella 뒤에 두고 불필요한 스필은 backing panel로 제어한다.
2. 우산 뒤에 1×2m diffusion panel을 추가해 두 번째로 확산한다.
3. 1/400초, f/1.4, ISO 100, 플래시 1/4 출력, 4,800K를 시연 시작값으로 설정해 주변광을 억제한다.
4. 반사판을 키 라이트 정반대에 고정하지 말고 얼굴을 감싸는 필이 생기도록 각도와 위치를 조절한다.
5. 포즈를 진행하면서 키 라이트를 조금씩 옮겨 얼굴 대비와 깊이 변화를 모니터로 비교한다.

## 추천 시작값 / 조작값

- Studio space / 시연 공간의 폭: 2.5 meter
- Studio space / 시연 공간의 깊이: 4 meter
- Shoot-through umbrella / 스피드라이트의 첫 번째 확산 우산 지름: 65 centimeter
- Diffusion panel / 우산을 통과한 빛의 두 번째 확산 패널 크기: 1 x 2 meter
- Camera shutter speed / 주변광을 억제한 시연 설정: 1/400 second
- Camera aperture / 시연 설정: f/1.4
- Camera ISO / 시연 설정: 100 ISO
- Flash power / 시연 설정: 1/4 power
- White balance / 시연 설정: 4800 kelvin
- Reflector / 키 라이트 정반대가 아니라 빛이 얼굴을 감싸도록 각도와 위치를 조절한다: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 촬영 중 얼굴 하이라이트, 그림자 밀도, 배경 스필을 실시간으로 확인한다.
- 키 라이트 위치를 작게 바꾼 프레임들을 비교해 표정과 입체감이 함께 좋은 마스터 컷을 고른다.
- 여러 출력 비율로 크롭할 수 있도록 얼굴 주변과 상반신의 여유 공간을 함께 검토한다.

## 주의할 점

- 시연 수치는 특정 공간과 장비의 값이므로 다른 방 크기와 광원 거리에서는 노출을 다시 맞춰야 한다.
- 반사판을 기계적으로 반대편에 놓으면 필이 평평하고 인공적으로 보일 수 있다.
- 키 라이트의 작은 이동도 얼굴 대비와 깊이를 크게 바꾸므로 위치를 한 번에 크게 바꾸지 않는다.
- backing panel 없이 스필이 퍼지면 배경과 주변광 제어가 약해질 수 있다.

## 확실성과 근거

- 작은 우산 뒤에 더 큰 확산 패널을 두면 소형 스피드라이트의 겉보기 광원이 커져 부드럽고 깨끗한 빛을 만든다.
- 주변광을 거의 제거하면 스피드라이트가 사실상 유일한 광원이 되어 결과를 예측하기 쉽다.
- 반사판을 단순 정면 필이 아니라 감싸는 방향으로 배치하면 평평함을 줄이고 자연스러운 입체감을 유지한다.

Fstoppers가 Jiggie Alejandrino의 장비, 공간 크기, 이중 확산 구성, 카메라·플래시·화이트밸런스 수치와 반사판 배치를 직접 상세히 전한다. 다른 공간에서의 재노출 필요성은 해당 설정의 적용 조건에 대한 실무적 해석이다.

## 출처

- 원문 URL: https://fstoppers.com/education/one-light-setup-produces-headshots-and-brand-portraits-same-frame-902458
- 접근일: 2026-08-06

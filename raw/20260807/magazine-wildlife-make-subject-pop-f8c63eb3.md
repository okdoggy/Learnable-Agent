---
schema_version: '1.0'
scenario_id: raw-20260807-subjectpop01
title_ko: 배경 감광과 방향성 빛을 겹쳐 야생동물 피사체를 자연스럽게 분리하기
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke; workflow by Matt Shannon
  url: https://fstoppers.com/education/how-make-your-subject-pop-using-lightroom-and-photoshop-902810
  published_at: '2026-06-07'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom; Adobe Photoshop
scenario:
  subject: wildlife
  condition:
  - subject-background-low-separation
  - imperfect-ai-mask-edge
  - directional-light-needed
  intent:
  - make-subject-pop
  - create-natural-depth
  - preserve-subject-detail
method:
  steps:
  - tool: Adobe Lightroom Masking
    parameter: 피사체 주변에 linear gradient와 adjustment layer를 두고 Subject Subtraction으로 피사체를 제외한 배경만 어둡게 함
    value: null
    unit: null
    reported_as: qualitative
  - tool: Mask brush
    parameter: 불완전한 빼기 경계에 shadow를 수동 브러시로 되돌려 halo 제거
    value: null
    unit: null
    reported_as: qualitative
  - tool: Radial Gradient
    parameter: 반대편에 radial gradient를 두어 밝기와 온기를 더하고 Dehaze를 낮춰 대기성 빛으로 연화
    value: null
    unit: null
    reported_as: qualitative
  - tool: Brush
    parameter: 눈을 확대해 브러시로 직접 밝힘
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Render > Lens Flare
    parameter: Photoshop Lens Flare를 solid-color layer에 적용하고 Screen blend mode로 빛만 유지
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Remove and Layer Mask
    parameter: Remove tool로 2차 flare artifact를 지우고 layer mask로 피사체를 보호
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 배경 어둡게, 경계 정리, 방향성 있는 따뜻한 빛, 눈 밝히기와 flare 정리를 작게 누적하면 과한 전역 선명도 없이 피사체를 분리할 수 있다.
- 따뜻한 하이라이트와 차가운 그림자의 대비는 깊이와 입체감을 강화한다.
- Screen 모드는 flare 레이어의 검은 배경을 제거하고 빛 효과를 남긴다.
collection:
  collector_version: 1.0.0
  content_sha256: f8c63eb3d972e2b9067b2c89ce8f884997dbb6d5229f9091bd6b4adbcb7f4108
  collected_at: '2026-08-07T00:00:00Z'
---

# 배경 감광과 방향성 빛을 겹쳐 야생동물 피사체를 자연스럽게 분리하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

야생동물 피사체와 배경의 밝기·색 차이가 약하고 AI 빼기 마스크 경계가 완벽하지 않아, 과한 샤프닝 없이 시선을 피사체로 모아야 할 때 사용한다.

## 촬영/작업 순서

1. Lightroom에서 피사체 주변에 linear gradient를 배치하고 Subject Subtraction으로 피사체를 보정 범위에서 뺀다.
2. 배경을 정성적으로 어둡게 한 뒤 불완전한 경계에는 수동 브러시로 그림자를 되돌려 전환을 자연스럽게 만든다.
3. 반대편에는 radial gradient로 밝기와 온기를 더하고 Dehaze를 낮춰 부드러운 대기광처럼 보이게 한다.
4. 피사체의 눈을 확대해 작은 브러시로 밝힌다.
5. Photoshop에서 solid-color layer에 Lens Flare를 만들고 기존 빛 방향과 맞는 모서리에 둔 뒤 Screen으로 전환한다.
6. 불필요한 보조 flare는 Remove tool로 지우고 Color Balance로 하이라이트는 따뜻하게, 그림자는 차갑게 조정한다.
7. 피사체 위에는 layer mask를 칠해 flare가 깃털 디테일을 씻어내지 않게 한다.

## 추천 시작값 / 조작값

- Adobe Lightroom Masking / 피사체 주변에 linear gradient와 adjustment layer를 두고 Subject Subtraction으로 피사체를 제외한 배경만 어둡게 함: 원문 정성 표현(수치 추정 없음)
- Mask brush / 불완전한 빼기 경계에 shadow를 수동 브러시로 되돌려 halo 제거: 원문 정성 표현(수치 추정 없음)
- Radial Gradient / 반대편에 radial gradient를 두어 밝기와 온기를 더하고 Dehaze를 낮춰 대기성 빛으로 연화: 원문 정성 표현(수치 추정 없음)
- Brush / 눈을 확대해 브러시로 직접 밝힘: 원문 정성 표현(수치 추정 없음)
- Photoshop Render > Lens Flare / Photoshop Lens Flare를 solid-color layer에 적용하고 Screen blend mode로 빛만 유지: 원문 정성 표현(수치 추정 없음)
- Photoshop Remove and Layer Mask / Remove tool로 2차 flare artifact를 지우고 layer mask로 피사체를 보호: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 각 보정을 낮은 강도로 쌓고 단계마다 피사체가 오려 붙인 듯 보이지 않는지 전후 비교한다.
- Subject Subtraction 뒤 피사체 윤곽의 밝은 halo를 확대해 수동 정리한다.
- radial gradient의 Dehaze를 낮출 때 빛이 딱딱한 스포트라이트가 아니라 장면 속 안개처럼 섞이는지 본다.
- 눈 밝히기는 시선 유도에 필요한 만큼만 적용하고 flare의 부수 artifact는 제거한다.

## 주의할 점

- Subject Subtraction이 남긴 경계를 방치하면 눈에 띄는 halo가 생긴다.
- 배경 감광과 눈 밝히기를 과도하게 적용하면 피사체가 인위적으로 분리된다.
- Lens Flare의 방향이 기존 광원과 맞지 않으면 합성 티가 난다.
- flare가 피사체를 덮으면 깃털 또는 표면 디테일이 씻겨 나간다.
- 원문은 각 조정의 수치를 명시하지 않았다.

## 확실성과 근거

- 배경 어둡게, 경계 정리, 방향성 있는 따뜻한 빛, 눈 밝히기와 flare 정리를 작게 누적하면 과한 전역 선명도 없이 피사체를 분리할 수 있다.
- 따뜻한 하이라이트와 차가운 그림자의 대비는 깊이와 입체감을 강화한다.
- Screen 모드는 flare 레이어의 검은 배경을 제거하고 빛 효과를 남긴다.

Fstoppers의 Alex Cooke가 Matt Shannon의 Lightroom·Photoshop 시연 순서와 각 도구의 역할을 설명한다. 효과 강도는 수치가 없어 정성적으로 기록했으며 경계 정리는 예시 장면에 따른다.

## 출처

- 원문 URL: https://fstoppers.com/education/how-make-your-subject-pop-using-lightroom-and-photoshop-902810
- 접근일: 2026-08-07

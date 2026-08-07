---
schema_version: '1.0'
scenario_id: raw-20260805-churchlight01
title_ko: 평평한 설경 속 건축물을 방향성 마스크로 분리
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke; Christian Möhrle
  url: https://fstoppers.com/lightroom/simple-lightroom-steps-make-subject-pop-722610
  published_at: '2026-01-28'
  accessed_at: '2026-08-05T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: winter-landscape-architecture
  condition:
  - flat-light
  - snow-scene
  - weak-subject-separation
  intent:
  - direct-attention
  - natural-subject-separation
method:
  steps:
  - tool: Lightroom Global Edit
    parameter: Exposure와 Highlights를 낮추고 Shadows와 Blacks는 암부가 뭉개지지 않을 만큼만 올림
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Linear Gradient
    parameter: 상단과 측면을 어둡게 하고 Landscape의 Architecture, Mountains, Snow 선택을 빼 건축물 보호
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Radial Gradient
    parameter: 중심을 프레임 밖에 둔 비스듬한 방사형 마스크로 은은한 유도선 형성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Radial Gradient
    parameter: 피사체 뒤의 길고 좁은 영역에서 Exposure와 Whites를 올리며 하이라이트 클리핑 감시
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Local Edit
    parameter: 건축물에 국소 Contrast와 Clarity를 더하고 필요하면 Saturation을 낮춤
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 전역 보정을 절제하고 마스크로 빛의 위치와 방향을 만들면 평평한 설경에서도 건축물이 자연스럽게 분리된다.
- 프레임 가장자리 감광과 피사체 뒤 밝기 증가는 시선을 중앙 피사체로 유도하면서 전체 장면의 겨울 분위기를 유지한다.
collection:
  collector_version: 1.0.0
  content_sha256: ce1eb25d84e8da8fbf03fce1c730fd58c3e4ad35a50c242d1248a59104b77f0d
  collected_at: '2026-08-05T00:00:00Z'
---

# 평평한 설경 속 건축물을 방향성 마스크로 분리

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

흰 건축물이 눈 덮인 풍경과 비슷한 밝기로 섞여 주 피사체가 약하게 보이고, 전역 대비만 높이면 하늘과 눈이 거칠어질 때 사용한다.

## 촬영/작업 순서

1. 하늘 복구와 암부 보호만 수행하는 절제된 전역 베이스를 만든다.
2. 선형 그라디언트로 프레임 가장자리를 감광하되 자동 Landscape 선택을 빼 건축물과 주요 지형을 보호한다.
3. 모든 마스크 오버레이를 확인하고 십자가 같은 작은 누락을 부드러운 브러시로 고친다.
4. 프레임 밖을 중심으로 둔 방사형 그라디언트로 빛의 방향을 만든다.
5. 피사체 뒤를 국소적으로 밝히고 건축물의 대비와 선명도를 별도로 보강한다.
6. 톤 보정 뒤 파랑이나 보라가 튀지 않는지 다시 확인하고 색을 정리한다.

## 추천 시작값 / 조작값

- Lightroom Global Edit / Exposure와 Highlights를 낮추고 Shadows와 Blacks는 암부가 뭉개지지 않을 만큼만 올림: 원문 정성 표현(수치 추정 없음)
- Lightroom Linear Gradient / 상단과 측면을 어둡게 하고 Landscape의 Architecture, Mountains, Snow 선택을 빼 건축물 보호: 원문 정성 표현(수치 추정 없음)
- Lightroom Radial Gradient / 중심을 프레임 밖에 둔 비스듬한 방사형 마스크로 은은한 유도선 형성: 원문 정성 표현(수치 추정 없음)
- Lightroom Radial Gradient / 피사체 뒤의 길고 좁은 영역에서 Exposure와 Whites를 올리며 하이라이트 클리핑 감시: 원문 정성 표현(수치 추정 없음)
- Lightroom Local Edit / 건축물에 국소 Contrast와 Clarity를 더하고 필요하면 Saturation을 낮춤: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 밝힌 하늘이 거칠면 Exposure만 되돌리기보다 해당 마스크의 Contrast를 낮춰 분리감은 유지하고 전환을 부드럽게 한다.
- 산과 설경의 국소 대비를 바꾼 뒤 파랑 채도가 증가했는지 점검한다.
- 최종 확대에서 AI 마스크의 윤곽선과 선택 누락이 보이지 않는지 검사한다.

## 주의할 점

- 방사형 마스크가 원형 스포트라이트처럼 보일 정도로 강하게 적용하지 않는다.
- 피사체 뒤를 밝힐 때 하이라이트 클리핑을 피한다.
- 국소 Contrast와 Clarity를 과도하게 올려 건축물과 눈이 거칠어지지 않게 한다.
- 실제 장면보다 지나치게 분리하면 사실성이 떨어질 수 있다.

## 확실성과 근거

- 전역 보정을 절제하고 마스크로 빛의 위치와 방향을 만들면 평평한 설경에서도 건축물이 자연스럽게 분리된다.
- 프레임 가장자리 감광과 피사체 뒤 밝기 증가는 시선을 중앙 피사체로 유도하면서 전체 장면의 겨울 분위기를 유지한다.

출처가 설경 속 흰 교회 예시와 전역 베이스, 가장자리 그라디언트, Landscape 선택 제외, 방사형 마스크, 피사체 뒤 밝기, 국소 대비 및 색 재점검 순서를 직접 설명한다. 강도는 정성적으로만 제시되어 수치화하지 않았다.

## 출처

- 원문 URL: https://fstoppers.com/lightroom/simple-lightroom-steps-make-subject-pop-722610
- 접근일: 2026-08-05

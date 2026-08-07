---
schema_version: '1.0'
scenario_id: raw-20260804-filmpreset01
title_ko: 디지털 사진을 절제된 컬러 필름풍 프리셋으로 시작해 장면별 보정
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/education/how-make-digital-photos-look-film-lightroom-902358
  published_at: '2026-05-14'
  accessed_at: '2026-08-04T00:00:40Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom Classic
scenario:
  subject: digital-photo
  condition:
  - digital-capture
  - mixed-subject-set
  - preset-workflow
  intent:
  - film-like-color
  - consistent-aesthetic
  - soften-digital-rendering
method:
  steps:
  - tool: Tone controls
    parameter: Highlights를 약간 올리고 Shadows와 Blacks를 들어 올림
    value: null
    unit: null
    reported_as: qualitative
  - tool: White Balance
    parameter: Temperature를 따뜻하게 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Clarity
    parameter: Clarity를 낮춤
    value: null
    unit: null
    reported_as: qualitative
  - tool: Dehaze
    parameter: Dehaze를 미세하게 낮춤
    value: null
    unit: null
    reported_as: qualitative
  - tool: Grain
    parameter: Grain을 추가하고 내보낸 파일에서 강도 확인
    value: null
    unit: null
    reported_as: qualitative
  - tool: HSL
    parameter: 장면의 지배색에 맞춰 Temperature와 HSL을 개별 조정
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 들어 올린 어두운 톤과 낮춘 미세 대비는 디지털의 완벽하게 또렷한 인상을 줄이고 부드러운 필름 스캔의 성격을 만든다.
- 프리셋을 시작점으로 두고 지배색을 장면별로 손봐야 여러 사진에서 그럴듯한 일관성을 얻을 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 53e1986473ed0c4fa56fefd9652cf3b6274dc5c8cf897586c47bca0892524b3d
  collected_at: '2026-08-04T00:00:40Z'
---

# 디지털 사진을 절제된 컬러 필름풍 프리셋으로 시작해 장면별 보정

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

디지털 사진 묶음에 Kodak Gold 200이나 Kodak ColorPlus와 비슷한 부드럽고 따뜻한 컬러 필름 인상을 일관되게 부여하되, 장면마다 다른 지배색을 보정해야 할 때 사용한다.

## 촬영/작업 순서

1. 하이라이트를 약간 올리고 섀도와 블랙을 들어 올려 파스텔처럼 부드러운 톤 기반을 만든다.
2. 화이트 밸런스를 따뜻하게 하고 Clarity를 낮춰 지나치게 또렷한 디지털 인상을 줄인다.
3. Dehaze를 미세하게 낮춰 절제된 대기감을 더한다.
4. Grain을 추가하고 기본 프리셋으로 저장한다.
5. 풍경·야간·인물 등 서로 다른 사진에 적용한 뒤 Temperature와 HSL을 장면별로 다시 조정한다.
6. 최종 내보내기 파일에서 Grain의 실제 인상을 확인한다.

## 추천 시작값 / 조작값

- Tone controls / Highlights를 약간 올리고 Shadows와 Blacks를 들어 올림: 원문 정성 표현(수치 추정 없음)
- White Balance / Temperature를 따뜻하게 조정: 원문 정성 표현(수치 추정 없음)
- Clarity / Clarity를 낮춤: 원문 정성 표현(수치 추정 없음)
- Dehaze / Dehaze를 미세하게 낮춤: 원문 정성 표현(수치 추정 없음)
- Grain / Grain을 추가하고 내보낸 파일에서 강도 확인: 원문 정성 표현(수치 추정 없음)
- HSL / 장면의 지배색에 맞춰 Temperature와 HSL을 개별 조정: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 프리셋 적용 전후의 블랙 깊이와 하이라이트 부드러움을 비교한다.
- 초록과 노랑이 지배적인 장면은 해당 색의 Luminance를 점검하고, 저녁의 파랑은 Hue 방향을 개별 검토한다.
- 보통 미리보기뿐 아니라 내보낸 결과를 실제 사용 크기로 확인한다.

## 주의할 점

- Dehaze를 과하게 낮추면 설득력 있는 필름 인상보다 과장되고 오래된 안개 효과처럼 보일 수 있다.
- 같은 프리셋도 지배색과 조명에 따라 다르게 작동하므로 원클릭 완성으로 취급하지 않는다.
- Lightroom의 일반 미리보기에서 절제돼 보인 Grain이 내보낸 파일에서는 과도할 수 있다.

## 확실성과 근거

- 들어 올린 어두운 톤과 낮춘 미세 대비는 디지털의 완벽하게 또렷한 인상을 줄이고 부드러운 필름 스캔의 성격을 만든다.
- 프리셋을 시작점으로 두고 지배색을 장면별로 손봐야 여러 사진에서 그럴듯한 일관성을 얻을 수 있다.

출처가 톤, 따뜻한 화이트 밸런스, 낮춘 Clarity와 Dehaze, Grain, 장면별 Temperature·HSL 보정을 직접 설명한다. 조정량은 정성적으로만 제시되어 임의 수치로 바꾸지 않았다.

## 출처

- 원문 URL: https://fstoppers.com/education/how-make-digital-photos-look-film-lightroom-902358
- 접근일: 2026-08-04

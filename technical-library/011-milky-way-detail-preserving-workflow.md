---
schema_version: '1.0'
number: 11
technical_id: milky-way-detail-preserving-workflow
title_ko: 별 디테일을 보존하는 은하수 촬영·현상·합성 흐름
summary_ko: 하늘·지상 분리 촬영, 선행 노이즈 제거, 별 보존형 현상, 광공해와 자연 대기광 분리, 경계 합성을 연결한 은하수 처리 흐름이다.
version: 0.1.0
status: candidate
supported_tools:
- remaster
- generate_ai
confidence: 0.72
raw_scenario_ids:
- raw-20260803-milkycapture01
- raw-20260803-milkydenoise01
- raw-20260803-milkylocal01
- raw-20260807-milkyway01
source_urls:
- https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 별 디테일을 보존하는 은하수 촬영·현상·합성 흐름

하늘·지상 분리 촬영, 선행 노이즈 제거, 별 보존형 현상, 광공해와 자연 대기광 분리, 경계 합성을 연결한 은하수 처리 흐름이다.

## 적용 조건

- 평평하고 노이즈가 많은 은하수 RAW에서 별 구조·광공해·전경 노출을 함께 다뤄야 할 때 적용한다.
- 하늘과 지상의 밝기 범위가 한 장의 노출을 넘어 별도 촬영 또는 합성이 필요한 야경에 적용한다.

## 기술 절차

1. 촬영 범위가 부족하면 별 디테일을 우선한 하늘 노출과 더 긴 지상 노출을 별도로 확보한다.
2. 현상·대비·샤프닝 전에 원본 RAW의 노이즈를 절제해 정리한다.
3. 100%에서 작은 별과 산 능선을 확인하며 하늘 구조를 회복한다.
4. 광공해는 국소적으로 낮추고 자연 대기광의 색은 별도 영역으로 보존한다.
5. 하늘과 지상을 각각 최적화해 합성하고 지평선·산 능선 경계를 자연스럽게 마무리한다.

## 파라미터 가이드

- 원문 저자가 일반적으로 사용하는 은하수 감도 상한은 ISO 6400이며 ISO 12800은 시험 파일이다.
- Lens Sharpness Standard와 100% 검사는 해당 워크플로의 출발점이다.
- ClearView 약 12는 해당 예시의 값이며 다른 이미지에 고정 적용하지 않는다.
- 셔터 시간·조리개·최종 Remaster 수치는 원문에 없으므로 새로 만들지 않는다.

## 판단 근거

- 촬영, 노이즈 제거, 국소 광공해 보정, 합성을 잇는 완전한 작업 흐름으로 결과 영향과 재사용 가치가 크다.
- Remaster의 denoise와 Generate AI compositing으로 지원할 수 있다.
- 하지만 모든 raw가 동일 PetaPixel 원문에서 분리된 근거이므로 active gate를 넘기지 않고 candidate로 보존한다.

## 주의사항

- ISO 12800은 원문의 스트레스 테스트 사례이며 일반 권장 상한으로 오해하지 않는다.
- 강한 노이즈 제거와 Dehaze는 작은 별을 지우거나 인공적인 별 테두리를 만들 수 있다.
- 광공해와 자연 대기광을 같은 색 번짐으로 취급하지 않는다.
- 하늘·지상 합성 경계가 부자연스럽지 않은지 확인한다.

## 충돌 및 예외

- 장면이 한 노출 범위에 들어오면 두 노출 합성을 무조건 사용할 필요가 없다.
- 노이즈 완전 제거보다 별 보존을 우선한다.

## raw 근거

- raw-20260803-milkycapture01
- raw-20260803-milkydenoise01
- raw-20260803-milkylocal01
- raw-20260807-milkyway01

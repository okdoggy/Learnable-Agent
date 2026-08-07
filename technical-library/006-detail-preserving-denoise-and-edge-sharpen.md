---
schema_version: '1.0'
number: 6
technical_id: detail-preserving-denoise-and-edge-sharpen
title_ko: 디테일 보존형 노이즈 제거와 에지 제한 샤프닝
summary_ko: 대비·선명화 전에 노이즈를 절제해 제거하고 샤프닝을 구조적 에지에만 제한해 별·피부·안개 등 미세하거나 매끄러운 영역을 보호한다.
version: 1.0.0
status: active
supported_tools:
- remaster
confidence: 0.94
raw_scenario_ids:
- raw-20260803-fogdepth01
- raw-20260803-milkydenoise01
- raw-20260804-detailsharp01
- raw-20260805-smartsharpen01
- raw-20260807-etherealedit01
source_urls:
- https://fstoppers.com/education/lightroom-settings-behind-hazy-ethereal-photography-style-901341
- https://fstoppers.com/lightroom/how-add-real-depth-lightroom-without-overediting-900105
- https://fstoppers.com/lightroom/lightrooms-4-sharpening-methods-and-when-use-each-one-901105
- https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- https://www.adobe.com/learn/photoshop/web/sharpen-a-photo
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 디테일 보존형 노이즈 제거와 에지 제한 샤프닝

대비·선명화 전에 노이즈를 절제해 제거하고 샤프닝을 구조적 에지에만 제한해 별·피부·안개 등 미세하거나 매끄러운 영역을 보호한다.

## 적용 조건

- 고감도 야경·은하수·저노출 풍경처럼 노이즈가 많고 미세 디테일을 보존해야 하는 이미지에 적용한다.
- 전역 샤프닝으로 피부·하늘·안개 같은 매끄러운 영역이 거칠어질 위험이 있는 사진에 적용한다.

## 기술 절차

1. 원본 상태에서 노이즈와 보존해야 할 미세 디테일을 식별한다.
2. 대비와 선명도를 올리기 전에 절제된 노이즈 제거를 적용한다.
3. 100% 부근 확대에서 별·털·윤곽·밝은 에지의 손상을 확인한다.
4. 샤프닝은 구조적 에지에 제한하고 하늘·피부·안개 등 매끄러운 영역을 보호한다.
5. 후속 대비·Clarity·Dehaze 이후 노이즈와 halo가 다시 두드러지는지 재검사한다.

## 파라미터 가이드

- 노이즈 제거는 대비·Clarity·Dehaze·샤프닝보다 먼저 수행한다.
- Lightroom Detail의 Masking 30~70은 한 근거의 전역 샤프닝 시작 범위이며 장면에 따라 조정한다.
- 몽환적 풍경에서 Sharpening Masking 80~90은 고대비 에지에만 제한하는 해당 스타일 예시다.
- 100% 검사는 별·halo·경계 손상을 찾기 위한 진단 배율로 사용한다.

## 판단 근거

- PetaPixel의 은하수 처리, Fstoppers의 안개 풍경과 Lightroom 샤프닝, Adobe의 Smart Filter 사례가 처리 순서와 에지 보호를 독립적으로 뒷받침한다.
- 디테일 손실과 아티팩트 방지 가치가 높고 Remaster의 denoise·sharpness로 직접 실행할 수 있다.

## 주의사항

- 노이즈를 완전히 제거하려다 별·털·미세 구조를 지우지 않는다.
- 강한 샤프닝은 halo, 링잉, 거친 노이즈를 만들 수 있다.
- 작은 미리보기만으로 판단하지 말고 확대와 전체 화면을 모두 확인한다.
- 안개나 몽환적 장면에서는 선명도 증가가 의도와 충돌할 수 있다.

## 충돌 및 예외

- 일반 사진의 구조적 에지는 선명화를 받을 수 있지만 안개·피부·매끈한 배경과 몽환적 스타일은 선명화 대상에서 보호해야 한다.

## raw 근거

- raw-20260803-milkydenoise01
- raw-20260803-fogdepth01
- raw-20260804-detailsharp01
- raw-20260805-smartsharpen01
- raw-20260807-etherealedit01

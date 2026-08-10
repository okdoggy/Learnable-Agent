---
schema_version: '1.0'
number: 6
technical_id: detail-preserving-denoise-and-edge-sharpen
title_ko: 디테일 보존형 노이즈 제거와 에지 제한 샤프닝
summary_ko: 대비·선명화 전에 노이즈를 절제해 한 번 처리하고 구조적 에지만 선명화하며, 별·털·깃털과 부드러운 영역의 상충 요구 및 이중 보정을 검증한다.
version: 1.0.2
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
- raw-20260808-localdenoise01
- raw-20260808-purerawhandoff01
- raw-20260809-denoisefirst
source_urls:
- https://fstoppers.com/education/lightroom-settings-behind-hazy-ethereal-photography-style-901341
- https://fstoppers.com/lightroom/how-add-real-depth-lightroom-without-overediting-900105
- https://fstoppers.com/lightroom/lightrooms-4-sharpening-methods-and-when-use-each-one-901105
- https://petapixel.com/2026/04/09/dxo-pureraw-6-the-ultimate-beginners-guide/
- https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- https://www.adobe.com/learn/photoshop/web/sharpen-a-photo
reviewed_at: '2026-08-09'
created_by: hermes-llm
---

# 디테일 보존형 노이즈 제거와 에지 제한 샤프닝

대비·선명화 전에 노이즈를 절제해 한 번 처리하고 구조적 에지만 선명화하며, 별·털·깃털과 부드러운 영역의 상충 요구 및 이중 보정을 검증한다.

## 적용 조건

- 고감도 야경·은하수·저노출 풍경·야생동물처럼 노이즈가 많고 미세 디테일을 보존해야 하는 이미지에 적용한다.
- 외부 RAW 전처리와 후속 편집 사이에서 노이즈 제거·렌즈 보정·샤프닝의 이중 적용을 막아야 할 때 적용한다.

## 기술 절차

1. 원본에서 노이즈, 보존할 미세 디테일, 매끄럽게 유지할 영역을 식별한다.
2. 대비·Clarity·Dehaze·샤프닝 전에 절제된 노이즈 제거를 한 번 적용한다.
3. 100% 부근 확대에서 별·털·깃털·윤곽과 부드러운 배경의 아티팩트를 확인한다.
4. 샤프닝은 구조적 에지에 제한하고 하늘·피부·안개·부드러운 배경을 보호한다.
5. 외부 전처리 결과에서는 이미 적용된 단계를 확인해 중복 처리를 끄고 후속 대비 적용 뒤 재검사한다.

## 파라미터 가이드

- Lightroom Masking 30~70과 몽환적 풍경 Masking 80~90은 각 근거의 출발 범위이며 장면별로 조정한다.
- 100% 검사는 별·털·깃털·halo·경계 손상을 찾는 진단 배율로 사용한다.
- DeepPRIME 3·XD3와 Lens Sharpness Standard는 DxO 고유 근거이므로 Remaster 수치로 환산하지 않는다.

## 판단 근거

- 은하수·안개·야생동물·일반 사진 근거가 노이즈 선처리, 디테일 보호, 에지 제한 원리를 독립적으로 뒷받침한다.
- 새 은하수 근거는 작은 별 보존을 완전한 평활화보다 우선하고 100%에서 검사해야 함을 보강한다.
- 디테일 손실과 아티팩트 방지 가치가 높으며 Remaster의 denoise·sharpness 순서로 직접 연결된다.

## 주의사항

- 노이즈를 완전히 제거하려다 별·털·깃털·미세 구조를 지우지 않는다.
- 강한 샤프닝과 Dehaze는 halo, 링잉, 거친 노이즈를 만들 수 있다.
- 외부 RAW 전처리에서 이미 수행한 보정을 후속 편집기에서 중복 적용하지 않는다.

## 충돌 및 예외

- 미세 질감 피사체와 부드러운 배경의 요구가 크게 다르면 하나의 강한 전역값으로 양쪽을 만족시키기 어렵다.
- 현재 Remaster가 영역별 엔진을 직접 지정하지 못하면 보수적인 전역값을 택하고 한계를 명시한다.

## raw 근거

- raw-20260803-milkydenoise01
- raw-20260803-fogdepth01
- raw-20260804-detailsharp01
- raw-20260805-smartsharpen01
- raw-20260807-etherealedit01
- raw-20260808-purerawhandoff01
- raw-20260808-localdenoise01
- raw-20260809-denoisefirst

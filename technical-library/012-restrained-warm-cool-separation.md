---
schema_version: '1.0'
number: 12
technical_id: restrained-warm-cool-separation
title_ko: 피부와 광원 관계를 보존하는 절제된 온냉 색 분리
summary_ko: 기본 색을 안정시킨 뒤 피사체·배경 또는 명도 영역에 따뜻함과 차가운 보색을 절제해 배치하여 색 깊이와 분리를 만든다.
version: 1.0.0
status: active
supported_tools:
- remaster
- lut
- generate_ai
confidence: 0.86
raw_scenario_ids:
- raw-20260802-vintageback01
- raw-20260802-warmlight01
- raw-20260803-complementgrade01
source_urls:
- https://fstoppers.com/education/how-color-grade-photos-lightroom-using-complementary-colors-902459
- https://fstoppers.com/education/how-edit-portrait-skin-tones-lightroom-902830
- https://fstoppers.com/education/how-get-natural-looking-studio-light-901630
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 피부와 광원 관계를 보존하는 절제된 온냉 색 분리

기본 색을 안정시킨 뒤 피사체·배경 또는 명도 영역에 따뜻함과 차가운 보색을 절제해 배치하여 색 깊이와 분리를 만든다.

## 적용 조건

- 피사체와 배경 또는 하이라이트와 그림자 사이에 따뜻함·차가움의 색 분리를 만들어 깊이를 강화할 때 적용한다.
- 중립 교정 후 보색 그레이드나 촬영된 혼합 색온도를 보존·강화할 때 적용한다.

## 기술 절차

1. 노출과 기본 화이트 밸런스를 먼저 안정시키되 의도적인 혼합 색온도는 보존한다.
2. 피사체와 배경 또는 명도 영역별로 따뜻한 색과 차가운 보색의 역할을 정한다.
3. 피부·주요 피사체는 자연스러운 온기를 유지하고 배경·그림자는 상대적으로 차갑게 조정한다.
4. LUT 또는 국소 색보정 강도를 낮게 시작해 색 경계와 중립색을 확인한다.
5. 전체 화면에서 깊이가 증가했는지, 색 효과가 피사체보다 먼저 보이지 않는지 검증한다.

## 파라미터 가이드

- 2700 K 키 라이트와 5600 K 카메라 화이트 밸런스는 특정 스튜디오 촬영 사례의 값이며 후처리 고정값으로 환산하지 않는다.
- LUT와 색온도 조정은 낮은 강도에서 시작해 피부·중립색·광원 방향을 확인하며 올린다.
- 수치가 없는 배경 냉각과 피부 온기 보존은 정성 방향으로만 사용한다.

## 판단 근거

- 촬영 단계의 혼합 색온도, 배경 국소 냉각, 톤 영역별 보색 그레이드가 서로 다른 장면에서 같은 깊이 원리를 뒷받침한다.
- LUT·Remaster·Generate AI로 실행 가능하고 인물·스튜디오·풍경에 재사용성이 높다.

## 주의사항

- 피부색을 차갑게 오염시키거나 배경과 피사체 경계에 색 띠를 만들지 않는다.
- 자동 화이트 밸런스로 의도적인 혼합 색온도까지 상쇄하지 않는다.
- 보색 채도를 과도하게 높이면 자연광 관계가 깨지고 상업적 필터처럼 보일 수 있다.

## 충돌 및 예외

- 흑백에 가까운 단일 tint 의도에서는 따뜻함·차가움의 양극 분리보다 낮은 채도의 전역 색조가 더 적합하다.

## raw 근거

- raw-20260802-vintageback01
- raw-20260802-warmlight01
- raw-20260803-complementgrade01

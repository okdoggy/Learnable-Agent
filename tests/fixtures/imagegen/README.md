# Image API 전환용 imagegen 회귀 fixture

이 디렉터리의 두 PNG는 사용자 이미지가 아닌 테스트 전용 합성 자료다. 과거 Codex `$imagegen`으로
생성·편집한 provenance를 유지하며, 현재 OpenAI Image API adapter의 입력 fixture와 metadata
회귀 검사에만 사용한다.

## 파일

- `backlit-still-life-source.png`: 강한 창가 역광으로 머그잔과 테이블의 그림자가 어두운 원본
- `backlit-still-life-edited.png`: 구도와 물체를 유지하고 어두운 부분만 자연스럽게 회복한 편집본

두 파일은 1536×1024 RGB PNG이며 EXIF, GPS, ICC, PNG text chunk를 포함하지 않는다.

## 프롬프트

원본 생성:

```text
Use case: photorealistic-natural
Asset type: Generate AI integration test fixture
Primary request: Create a realistic still life with a ceramic mug and folded linen cloth on a wooden table beside a sunlit window. Strong warm backlight should leave the mug and left side naturally underexposed.
Composition/framing: landscape, fixed camera, mug centered, folded cloth on the right, window behind
Constraints: no people, no logos, no text, no watermark
```

편집:

```text
Use case: lighting-weather
Asset type: Generate AI integration test fixture
Primary request: Recover only the underexposed shadows on the mug and table so their detail is natural and visible.
Input images: Image 1 is the edit target.
Constraints: preserve the mug, cloth, window, warm backlight, camera framing, geometry, and every object position.
Avoid: new objects, text, logos, watermark, composition changes
```

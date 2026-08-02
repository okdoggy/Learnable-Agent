from __future__ import annotations

import re
import shlex
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import numpy as np
import yaml
from PIL import Image, ImageOps

from lala.domain.errors import LalaError
from lala.domain.models import LutParameters
from lala.renderers.image_io import sha256_file
from lala.renderers.remaster import RenderResult, _linear_to_srgb, _luminance, _srgb_to_linear
from lala.storage.workspace import ensure_within
from lala.text import TextEncodingError, read_utf8_lf

LUT_ENGINE_VERSION = "1.0.0"
MAX_LUT_1D_SIZE = 65_536
MAX_LUT_3D_SIZE = 65
MAX_ABS_LUT_VALUE = 16.0


@dataclass(frozen=True, slots=True)
class CubeLut:
    kind: Literal["1d", "3d"]
    size: int
    domain_min: np.ndarray
    domain_max: np.ndarray
    table: np.ndarray
    title: str | None = None


@dataclass(frozen=True, slots=True)
class LutEntry:
    lut_id: str
    path: Path
    sha256: str | None
    status: str
    title: str


class LutCatalog:
    def __init__(self, manifest_path: Path) -> None:
        self.manifest_path = manifest_path.resolve()
        self.root = self.manifest_path.parent.resolve()

    @property
    def version(self) -> str:
        data = self._load()
        return str(data.get("catalog_version", "unknown"))

    def approved_entries(self) -> list[LutEntry]:
        data = self._load()
        entries: list[LutEntry] = []
        for raw in data.get("luts", []):
            if raw.get("status") != "approved":
                continue
            entries.append(self._entry(raw))
        return entries

    def resolve(self, lut_id: str) -> LutEntry:
        for entry in self.approved_entries():
            if entry.lut_id == lut_id:
                if not entry.path.is_file():
                    raise LalaError("LUT_NOT_FOUND", "등록된 LUT 파일을 찾을 수 없습니다.", False)
                if entry.sha256 and sha256_file(entry.path).lower() != entry.sha256.lower():
                    raise LalaError("INVALID_LUT", "LUT 파일 해시가 manifest와 다릅니다.", False)
                return entry
        raise LalaError("LUT_NOT_FOUND", "승인된 LUT ID가 아닙니다.", False)

    def _load(self) -> dict[str, object]:
        try:
            data = yaml.safe_load(read_utf8_lf(self.manifest_path)) or {}
        except (OSError, TextEncodingError, yaml.YAMLError) as exc:
            raise LalaError(
                "INVALID_LUT_MANIFEST", "LUT manifest를 읽을 수 없습니다.", False
            ) from exc
        if not isinstance(data, dict) or not isinstance(data.get("luts", []), list):
            raise LalaError("INVALID_LUT_MANIFEST", "LUT manifest 형식이 올바르지 않습니다.", False)
        return data

    def _entry(self, raw: object) -> LutEntry:
        if not isinstance(raw, dict):
            raise LalaError("INVALID_LUT_MANIFEST", "LUT 항목 형식이 올바르지 않습니다.", False)
        lut_id = str(raw.get("id", ""))
        relative = Path(str(raw.get("path", "")))
        sha256 = str(raw["sha256"]) if raw.get("sha256") else None
        if (
            not re.fullmatch(r"[a-zA-Z0-9._-]{3,128}", lut_id)
            or relative.is_absolute()
            or relative.suffix.lower() != ".cube"
            or (sha256 is not None and not re.fullmatch(r"[0-9a-fA-F]{64}", sha256))
        ):
            raise LalaError("INVALID_LUT_MANIFEST", "LUT 항목이 안전하지 않습니다.", False)
        path = ensure_within(self.root / relative, self.root)
        return LutEntry(
            lut_id=lut_id,
            path=path,
            sha256=sha256,
            status=str(raw.get("status", "")),
            title=str(raw.get("title", lut_id)),
        )


class LutRenderer:
    engine_version = LUT_ENGINE_VERSION

    def __init__(self, catalog: LutCatalog) -> None:
        self.catalog = catalog

    def render(self, source: Path, destination: Path, parameters: LutParameters) -> RenderResult:
        entry = self.catalog.resolve(parameters.lut_id)
        cube = parse_cube(entry.path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(source) as opened:
            opened.load()
            image = ImageOps.exif_transpose(opened)
            original_mode = image.mode
            alpha = image.getchannel("A") if "A" in image.getbands() else None
            rgb = np.asarray(image.convert("RGB"), dtype=np.float32) / 255.0
        transformed = apply_cube(rgb, cube)
        if parameters.preserve_luminance:
            original_linear = _srgb_to_linear(rgb)
            transformed_linear = _srgb_to_linear(np.clip(transformed, 0.0, 1.0))
            original_luminance = _luminance(original_linear)
            transformed_luminance = _luminance(transformed_linear)
            scale = np.divide(
                original_luminance,
                transformed_luminance,
                out=np.ones_like(original_luminance),
                where=transformed_luminance > 1e-5,
            )
            transformed = _linear_to_srgb(np.clip(transformed_linear * scale[..., None], 0.0, 1.0))
        strength = parameters.strength / 100.0
        output = rgb * (1.0 - strength) + transformed * strength
        encoded = Image.fromarray(
            np.clip(np.rint(output * 255.0), 0, 255).astype(np.uint8), mode="RGB"
        )
        if original_mode in {"L", "LA"}:
            encoded = encoded.convert("L")
        if alpha is not None:
            encoded.putalpha(alpha)
        encoded.save(destination, format="PNG", optimize=False)
        return RenderResult(
            path=destination.resolve(),
            sha256=sha256_file(destination),
            engine_version=self.engine_version,
            width=encoded.width,
            height=encoded.height,
        )


def parse_cube(path: Path) -> CubeLut:
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError) as exc:
        raise LalaError("INVALID_LUT", "LUT 파일을 읽을 수 없습니다.", False) from exc
    kind: Literal["1d", "3d"] | None = None
    size: int | None = None
    title: str | None = None
    domain_min = np.array([0.0, 0.0, 0.0], dtype=np.float32)
    domain_max = np.array([1.0, 1.0, 1.0], dtype=np.float32)
    values: list[list[float]] = []
    for line_number, original in enumerate(lines, start=1):
        line = original.split("#", 1)[0].strip()
        if not line:
            continue
        try:
            tokens = shlex.split(line)
            keyword = tokens[0].upper()
            if keyword == "TITLE":
                title = " ".join(tokens[1:])
            elif keyword in {"LUT_1D_SIZE", "LUT_3D_SIZE"}:
                if len(tokens) != 2:
                    raise ValueError("LUT size requires one value")
                next_kind: Literal["1d", "3d"] = "1d" if keyword == "LUT_1D_SIZE" else "3d"
                if kind is not None:
                    raise ValueError("multiple LUT sizes")
                kind = next_kind
                size = int(tokens[1])
            elif keyword in {"DOMAIN_MIN", "DOMAIN_MAX"}:
                if len(tokens) != 4:
                    raise ValueError("domain requires three values")
                parsed = np.array([float(value) for value in tokens[1:4]], dtype=np.float32)
                if parsed.shape != (3,):
                    raise ValueError("domain requires three values")
                if keyword == "DOMAIN_MIN":
                    domain_min = parsed
                else:
                    domain_max = parsed
            else:
                parsed_values = [float(value) for value in tokens]
                if len(parsed_values) != 3:
                    raise ValueError("table row requires three values")
                values.append(parsed_values)
        except (IndexError, ValueError, OverflowError) as exc:
            raise LalaError(
                "INVALID_LUT", f"LUT {line_number}행 형식이 올바르지 않습니다.", False
            ) from exc
    if kind is None or size is None:
        raise LalaError("INVALID_LUT", "LUT 크기 선언이 없습니다.", False)
    if kind == "1d" and not 2 <= size <= MAX_LUT_1D_SIZE:
        raise LalaError("INVALID_LUT", "1D LUT 크기가 허용 범위를 벗어났습니다.", False)
    if kind == "3d" and not 2 <= size <= MAX_LUT_3D_SIZE:
        raise LalaError("INVALID_LUT", "3D LUT 크기가 허용 범위를 벗어났습니다.", False)
    expected = size if kind == "1d" else size**3
    table = np.asarray(values, dtype=np.float32)
    if (
        table.shape != (expected, 3)
        or not np.isfinite(table).all()
        or np.max(np.abs(table), initial=0.0) > MAX_ABS_LUT_VALUE
    ):
        raise LalaError("INVALID_LUT", "LUT 데이터 수 또는 값이 올바르지 않습니다.", False)
    if not np.isfinite(domain_min).all() or not np.isfinite(domain_max).all():
        raise LalaError("INVALID_LUT", "LUT domain에 NaN/Inf가 있습니다.", False)
    if np.any(domain_max <= domain_min):
        raise LalaError("INVALID_LUT", "LUT DOMAIN_MAX는 DOMAIN_MIN보다 커야 합니다.", False)
    if kind == "3d":
        table = table.reshape((size, size, size, 3))  # file order: blue, green, red
    return CubeLut(kind, size, domain_min, domain_max, table, title)


def apply_cube(rgb: np.ndarray, cube: CubeLut) -> np.ndarray:
    normalized = np.clip((rgb - cube.domain_min) / (cube.domain_max - cube.domain_min), 0.0, 1.0)
    position = normalized * (cube.size - 1)
    lower = np.floor(position).astype(np.int32)
    upper = np.minimum(lower + 1, cube.size - 1)
    fraction = position - lower
    if cube.kind == "1d":
        output = np.empty_like(rgb)
        for channel in range(3):
            low = cube.table[lower[..., channel], channel]
            high = cube.table[upper[..., channel], channel]
            output[..., channel] = (
                low * (1 - fraction[..., channel]) + high * fraction[..., channel]
            )
        return output
    r0, g0, b0 = lower[..., 0], lower[..., 1], lower[..., 2]
    r1, g1, b1 = upper[..., 0], upper[..., 1], upper[..., 2]
    fr, fg, fb = fraction[..., 0:1], fraction[..., 1:2], fraction[..., 2:3]
    table = cube.table
    c000 = table[b0, g0, r0]
    c100 = table[b0, g0, r1]
    c010 = table[b0, g1, r0]
    c110 = table[b0, g1, r1]
    c001 = table[b1, g0, r0]
    c101 = table[b1, g0, r1]
    c011 = table[b1, g1, r0]
    c111 = table[b1, g1, r1]
    c00 = c000 * (1 - fr) + c100 * fr
    c10 = c010 * (1 - fr) + c110 * fr
    c01 = c001 * (1 - fr) + c101 * fr
    c11 = c011 * (1 - fr) + c111 * fr
    c0 = c00 * (1 - fg) + c10 * fg
    c1 = c01 * (1 - fg) + c11 * fg
    return c0 * (1 - fb) + c1 * fb

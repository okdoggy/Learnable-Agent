from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True, slots=True)
class Settings:
    project_root: Path
    var_dir: Path
    output_dir: Path
    slack_cache_dir: Path
    raw_dir: Path
    technical_library_dir: Path
    lut_manifest_path: Path
    sources_path: Path
    database_path: Path
    api_key: str
    signing_secret: str
    public_base_url: str
    planner_prompt_path: Path
    parameter_registry_path: Path
    max_asset_bytes: int = 25 * 1024 * 1024
    max_image_pixels: int = 40_000_000
    asset_ttl_seconds: int = 86_400
    upload_url_ttl_seconds: int = 900
    hermes_base_url: str = "http://127.0.0.1:8642"
    hermes_api_key: str = ""
    hermes_model: str = "hermes-agent"
    hermes_timeout_seconds: float = 120.0
    hermes_max_attempts: int = 3
    hermes_circuit_failures: int = 5
    hermes_circuit_recovery_seconds: int = 30
    imagegen_openai_api_key: str = ""
    imagegen_model: str = "gpt-image-2"
    imagegen_quality: str = "low"
    imagegen_size: str = "1024x1024"
    imagegen_timeout_seconds: int = 180
    imagegen_max_attempts: int = 3
    imagegen_max_calls_per_hour: int = 20
    rate_limit_per_minute: int = 60
    enable_local_uploads: bool = True

    @classmethod
    def from_env(cls, project_root: Path | None = None) -> Settings:
        initial_root_value = os.getenv("LALA_PROJECT_ROOT")
        initial_root = project_root or (
            Path(initial_root_value) if initial_root_value else _default_root()
        )
        load_dotenv(initial_root.expanduser().resolve() / ".env", override=False)
        root_value = os.getenv("LALA_PROJECT_ROOT")
        root = project_root or (Path(root_value) if root_value else _default_root())
        root = root.expanduser().resolve()
        var_dir = Path(os.getenv("LALA_VAR_DIR", str(root / "var"))).expanduser().resolve()
        output_dir = Path(os.getenv("LALA_OUTPUT_DIR", str(root / "output"))).expanduser().resolve()
        slack_cache_dir = Path(
            os.getenv("LALA_SLACK_CACHE_DIR", str(root / "var" / "slack-cache"))
        ).expanduser().resolve()
        # 수집 지식은 Hermes의 세션/임시 작업공간과 분리된 프로젝트 자산이다.
        # 외부 환경변수로 이 두 경로를 덮어쓰지 않고 프로젝트 루트에 고정한다.
        raw_dir = (root / "raw").resolve()
        technical_dir = (root / "technical-library").resolve()
        planner_prompt_path = (
            Path(
                os.getenv(
                    "LALA_PLANNER_PROMPT",
                    str(root / "skills" / "lala-coordinator" / "references" / "planner-prompt.md"),
                )
            )
            .expanduser()
            .resolve()
        )
        api_key = os.getenv("LALA_API_KEY", "local-development-key")
        signing_secret = os.getenv("LALA_SIGNING_SECRET", api_key)
        return cls(
            project_root=root,
            var_dir=var_dir,
            output_dir=output_dir,
            slack_cache_dir=slack_cache_dir,
            raw_dir=raw_dir,
            technical_library_dir=technical_dir,
            lut_manifest_path=Path(
                os.getenv("LALA_LUT_MANIFEST", str(root / "luts" / "manifest.yaml"))
            )
            .expanduser()
            .resolve(),
            sources_path=Path(
                os.getenv("LALA_SOURCES_CONFIG", str(root / "config" / "sources.yaml"))
            )
            .expanduser()
            .resolve(),
            database_path=Path(os.getenv("LALA_DATABASE_PATH", str(var_dir / "lala.sqlite3")))
            .expanduser()
            .resolve(),
            api_key=api_key,
            signing_secret=signing_secret,
            public_base_url=os.getenv("LALA_PUBLIC_BASE_URL", "http://127.0.0.1:8000").rstrip("/"),
            max_asset_bytes=int(os.getenv("LALA_MAX_ASSET_BYTES", 25 * 1024 * 1024)),
            max_image_pixels=int(os.getenv("LALA_MAX_IMAGE_PIXELS", 40_000_000)),
            asset_ttl_seconds=int(os.getenv("LALA_ASSET_TTL_SECONDS", 86_400)),
            upload_url_ttl_seconds=int(os.getenv("LALA_UPLOAD_URL_TTL_SECONDS", 900)),
            hermes_base_url=os.getenv("HERMES_BASE_URL", "http://127.0.0.1:8642").rstrip("/"),
            hermes_api_key=os.getenv("HERMES_API_KEY", ""),
            hermes_model=os.getenv("HERMES_MODEL", "hermes-agent"),
            planner_prompt_path=planner_prompt_path,
            parameter_registry_path=(root / "config" / "parameter-registry.yaml").resolve(),
            hermes_timeout_seconds=float(os.getenv("HERMES_TIMEOUT_SECONDS", 120)),
            hermes_max_attempts=int(os.getenv("HERMES_MAX_ATTEMPTS", 3)),
            hermes_circuit_failures=int(os.getenv("HERMES_CIRCUIT_FAILURES", 5)),
            hermes_circuit_recovery_seconds=int(os.getenv("HERMES_CIRCUIT_RECOVERY_SECONDS", 30)),
            imagegen_openai_api_key=os.getenv("LALA_IMAGEGEN_OPENAI_API_KEY", ""),
            imagegen_model="gpt-image-2",
            imagegen_quality="low",
            imagegen_size="1024x1024",
            imagegen_timeout_seconds=int(os.getenv("LALA_IMAGEGEN_TIMEOUT_SECONDS", 180)),
            imagegen_max_attempts=int(os.getenv("LALA_IMAGEGEN_MAX_ATTEMPTS", 3)),
            imagegen_max_calls_per_hour=int(os.getenv("LALA_IMAGEGEN_MAX_CALLS_PER_HOUR", 20)),
            rate_limit_per_minute=int(os.getenv("LALA_RATE_LIMIT_PER_MINUTE", 60)),
            enable_local_uploads=_env_bool("LALA_ENABLE_LOCAL_UPLOADS", True),
        )

    def ensure_directories(self) -> None:
        if len(self.api_key) < 16 or len(self.signing_secret) < 16:
            raise ValueError("LALA_API_KEY and LALA_SIGNING_SECRET must be at least 16 characters")
        positive_values = {
            "max_asset_bytes": self.max_asset_bytes,
            "max_image_pixels": self.max_image_pixels,
            "asset_ttl_seconds": self.asset_ttl_seconds,
            "upload_url_ttl_seconds": self.upload_url_ttl_seconds,
            "rate_limit_per_minute": self.rate_limit_per_minute,
            "imagegen_max_calls_per_hour": self.imagegen_max_calls_per_hour,
        }
        invalid = [name for name, value in positive_values.items() if value <= 0]
        if invalid:
            raise ValueError(f"settings must be positive: {', '.join(sorted(invalid))}")
        for path in (
            self.var_dir,
            self.var_dir / "assets",
            self.var_dir / "jobs",
            self.output_dir / "imagegen",
            self.raw_dir,
            self.technical_library_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)


def _default_root() -> Path:
    return Path(__file__).resolve().parents[2]

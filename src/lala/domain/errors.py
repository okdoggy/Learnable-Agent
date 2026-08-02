from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class LalaError(Exception):
    code: str
    user_message_ko: str
    retryable: bool = False
    internal_message: str | None = None

    def __str__(self) -> str:
        return self.internal_message or self.user_message_ko


class InvalidImageError(LalaError):
    def __init__(self, message: str = "유효한 이미지 파일이 아닙니다.") -> None:
        super().__init__("INVALID_IMAGE", message, False)


class UnsupportedFormatError(LalaError):
    def __init__(self, message: str = "지원하지 않는 이미지 형식입니다.") -> None:
        super().__init__("UNSUPPORTED_FORMAT", message, False)


class PlanValidationError(LalaError):
    def __init__(self, message: str = "추천 설정을 검증하지 못했습니다.") -> None:
        super().__init__("PLAN_VALIDATION_FAILED", message, False)


class AgentTimeoutError(LalaError):
    def __init__(self, message: str = "추천 생성 시간이 초과되었습니다.") -> None:
        super().__init__("AGENT_TIMEOUT", message, True)


class ExecutionError(LalaError):
    def __init__(
        self, message: str, *, retryable: bool = True, internal: str | None = None
    ) -> None:
        super().__init__("EXECUTION_FAILED", message, retryable, internal)


class NotFoundError(LalaError):
    def __init__(self, message: str = "요청한 항목을 찾을 수 없습니다.") -> None:
        super().__init__("NOT_FOUND", message, False)

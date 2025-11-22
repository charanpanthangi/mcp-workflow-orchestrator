"""Lightweight pydantic stub for offline testing."""
from typing import Any


def Field(default: Any = None, description: str | None = None, default_factory=None, **kwargs: Any) -> Any:
    if default_factory is not None:
        return default_factory()
    return default


class BaseModel:
    def __init__(self, **data: Any) -> None:
        for k, v in data.items():
            setattr(self, k, v)

    def model_dump(self) -> dict:  # pragma: no cover - helper
        return self.__dict__

    def __iter__(self):  # pragma: no cover - mimic pydantic behavior
        return iter(self.__dict__.items())

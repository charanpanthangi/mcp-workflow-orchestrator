"""Retry policy wrapper for MCP and LiteLLM calls."""
import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry_with_policy(fn: Callable[[], T], attempts: int = 3, delay: float = 0.2) -> T:
    """Retry helper with exponential backoff for transient failures."""
    last_exception = None
    for i in range(attempts):
        try:
            return fn()
        except Exception as exc:  # pragma: no cover - tested via behavior
            last_exception = exc
            time.sleep(delay * (2 ** i))
    if last_exception:
        raise last_exception
    raise RuntimeError("Retry policy failed without exception")

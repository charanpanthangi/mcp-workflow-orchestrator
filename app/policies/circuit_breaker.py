"""Lightweight circuit breaker to prevent repeated failures."""
import time
from typing import Callable, TypeVar

T = TypeVar("T")


class CircuitBreaker:
    """Simple counter-based circuit breaker suitable for demos."""

    def __init__(self, failure_threshold: int = 3, reset_timeout: float = 1.0) -> None:
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.failures = 0
        self.last_failure_time = 0.0

    def call(self, fn: Callable[[], T]) -> T:
        """Execute function unless circuit is open."""
        if self.failures >= self.failure_threshold:
            if time.time() - self.last_failure_time < self.reset_timeout:
                raise RuntimeError("Circuit breaker open")
            # Reset after timeout
            self.failures = 0
        try:
            result = fn()
            self.failures = 0
            return result
        except Exception:
            self.failures += 1
            self.last_failure_time = time.time()
            raise

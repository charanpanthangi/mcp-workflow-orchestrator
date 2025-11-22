"""Simple metrics counters to illustrate observability hooks."""
from collections import defaultdict
from typing import Dict


class Metrics:
    """In-memory metrics accumulator for agent and MCP calls."""

    def __init__(self) -> None:
        self.counters: Dict[str, int] = defaultdict(int)

    def increment(self, name: str) -> None:
        self.counters[name] += 1

    def snapshot(self) -> Dict[str, int]:
        return dict(self.counters)


metrics = Metrics()

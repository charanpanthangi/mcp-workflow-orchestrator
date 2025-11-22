"""Base agent definition used by all specialized agents."""
from typing import Any, Dict

import litellm

from app.config import LLMConfig
from app.memory.store import PreferenceStore
from app.policies.retry import retry_with_policy
from app.policies.circuit_breaker import CircuitBreaker
from app.policies.safety import enforce_safety
from app.observability.logging_utils import logger


class BaseAgent:
    """Common contract for agents handling reasoning and MCP interactions."""

    def __init__(self, llm_config: LLMConfig, memory_store: PreferenceStore) -> None:
        self.llm_config = llm_config
        self.memory_store = memory_store
        self.circuit_breaker = CircuitBreaker()

    def call_llm(self, messages: list, planner: bool = False) -> str:
        """Invoke LiteLLM with retry and circuit breaker protections."""
        def _call() -> Any:
            return self.circuit_breaker.call(
                lambda: litellm.completion(messages=messages, **self.llm_config.as_kwargs(planner))
            )

        response = retry_with_policy(_call)
        content = response["choices"][0]["message"]["content"]
        return enforce_safety(content)

    def run(self, request: Any, context: Dict[str, Any], history: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the agent logic. To be implemented by subclasses."""
        raise NotImplementedError

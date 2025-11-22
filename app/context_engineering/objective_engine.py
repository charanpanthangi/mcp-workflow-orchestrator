"""Objective extraction and analysis for workflow planning."""
from typing import Dict, Any

import litellm

from app.config import LLMConfig
from app.context_engineering.constraints import build_constraints
from app.policies.retry import retry_with_policy
from app.policies.circuit_breaker import CircuitBreaker
from app.observability.logging_utils import logger
from app.schemas.workflow import WorkflowRequest


class ObjectiveEngine:
    """Analyzes workflow requests to derive constraints and required agents."""

    def __init__(self, llm_config: LLMConfig) -> None:
        self.llm_config = llm_config
        self.circuit_breaker = CircuitBreaker()

    def analyze_request(self, request: WorkflowRequest) -> Dict[str, Any]:
        """Call LiteLLM to summarize requirements and propose agents."""
        constraints = build_constraints(request)
        prompt = (
            f"System: {constraints['system_prompt']}\n"
            f"User: {constraints['user_prompt']}\n"
            "List relevant agents (weather, budget, calendar, visa, flight, hotel, taxi)"
            " and summarize constraints. Respond in JSON with keys agents and summary."
        )

        def _call_llm() -> Dict[str, Any]:
            # Wrap LiteLLM call with circuit breaker and retry for resilience.
            return self.circuit_breaker.call(
                lambda: litellm.completion(
                    messages=[{"role": "user", "content": prompt}],
                    **self.llm_config.as_kwargs(planner=True),
                )
            )

        response = retry_with_policy(_call_llm)
        try:
            content = response["choices"][0]["message"]["content"]
        except Exception:  # pragma: no cover - defensive
            content = "{\"agents\": [\"response\"], \"summary\": \"fallback\"}"
        logger.debug("Objective engine raw response: %s", content)
        # Simple parse; in production use json schema validation.
        agents = []
        if "weather" in content:
            agents.append("weather")
        if "budget" in content:
            agents.append("budget")
        if "calendar" in content:
            agents.append("calendar")
        if "visa" in content:
            agents.append("visa")
        if "flight" in content:
            agents.append("flight")
        if "hotel" in content:
            agents.append("hotel")
        if "taxi" in content or "transport" in content:
            agents.append("taxi")
        # Ensure deterministic order for tests.
        agents = list(dict.fromkeys(agents))
        return {"agents": agents, "summary": content}

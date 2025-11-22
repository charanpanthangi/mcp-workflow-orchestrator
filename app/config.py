"""Configuration utilities for the Multi-Agent Workflow Orchestrator."""
import os
from typing import Dict, Any

from dotenv import load_dotenv
import litellm

# Load environment variables early for configuration.
load_dotenv()

# Default LiteLLM model selection with fallbacks defined in requirements.
DEFAULT_PLANNER_MODEL = os.getenv("LITELLM_MODEL_PLANNER", "gpt-4o-mini")
DEFAULT_AGENT_MODEL = os.getenv("LITELLM_MODEL_AGENT", "gpt-4o-mini")
FALLBACK_MODELS = ["gpt-4o-mini", "groq/llama3-8b", "claude-3-haiku"]


class LLMConfig:
    """Container for LiteLLM settings used across planner and agents."""

    def __init__(self) -> None:
        # Store model names so orchestration can swap in one place.
        self.planner_model = DEFAULT_PLANNER_MODEL
        self.agent_model = DEFAULT_AGENT_MODEL
        self.fallback_models = FALLBACK_MODELS

    def as_kwargs(self, planner: bool = False) -> Dict[str, Any]:
        """Return keyword arguments for litellm.completion calls."""
        model = self.planner_model if planner else self.agent_model
        return {
            "model": model,
            "fallback_models": self.fallback_models,
            "temperature": 0.3,
        }


def get_llm_client() -> LLMConfig:
    """Provide shared LiteLLM configuration for orchestrator components."""
    return LLMConfig()

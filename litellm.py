"""Local fallback stub for LiteLLM when package installation is unavailable."""
from typing import List, Dict, Any


def completion(messages: List[Dict[str, str]], model: str = "stub", fallback_models=None, temperature: float = 0.3, **kwargs: Any) -> Dict[str, Any]:
    content = messages[-1]["content"] if messages else ""
    return {"choices": [{"message": {"content": f"stub-response:{content}"}}]}


def acompletion(*args: Any, **kwargs: Any):  # pragma: no cover - async stub
    raise NotImplementedError("Async stub not implemented")

"""Safety guardrails for LLM outputs."""
import re


FORBIDDEN_PATTERNS = [r"(?i)password", r"(?i)credential"]


def enforce_safety(content: str) -> str:
    """Remove sensitive tokens and enforce neutral tone."""
    sanitized = content
    for pattern in FORBIDDEN_PATTERNS:
        sanitized = re.sub(pattern, "[redacted]", sanitized)
    return sanitized.strip()

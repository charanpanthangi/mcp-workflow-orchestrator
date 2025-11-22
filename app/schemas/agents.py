"""Schema describing agent outputs."""
from typing import Dict, Any
from pydantic import BaseModel


class AgentResult(BaseModel):
    """Standardized agent result payload."""

    agent: str
    data: Dict[str, Any]
    summary: str

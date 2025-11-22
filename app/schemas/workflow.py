"""Workflow request and response schemas."""
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class WorkflowRequest(BaseModel):
    """Incoming workflow request provided to the orchestrator."""

    objective: str = Field(..., description="User goal to accomplish")
    budget: Optional[float] = Field(None, description="Budget if applicable")
    context: Optional[Dict[str, Any]] = Field(default=None, description="Domain-specific context")
    user_preferences: Optional[Dict[str, Any]] = Field(default=None, description="Stored preferences")


class WorkflowResponse(BaseModel):
    """Structured response emitted after agent orchestration."""

    plan: str
    agents_used: List[str]
    tools_invoked: List[str]
    result: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

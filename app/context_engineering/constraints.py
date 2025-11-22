"""Prompt constraint builder for orchestrator and agents."""
from typing import Dict, Any

from app.schemas.workflow import WorkflowRequest


def build_constraints(request: WorkflowRequest) -> Dict[str, Any]:
    """Construct system/user prompts and memory slices for LLM calls."""
    # System prompt sets overall behavior guidelines.
    system_prompt = (
        "You are the Multi-Agent Workflow Orchestrator. Maintain professionalism, "
        "respect safety policies, and prefer concise, verifiable steps."
    )
    # User prompt is derived directly from incoming workflow request.
    user_prompt = f"User objective: {request.objective}. Preferences: {request.user_preferences}"

    # Placeholder for retrieval augmented context and memory slices.
    retrieved_docs = ["No external documents retrieved; using built-in stubs."]
    short_term_memory = request.context or {}
    long_term_memory = {"preferences": request.user_preferences or {}}

    # Structured output enforcement hints.
    structured_output = {
        "type": "workflow_response",
        "fields": ["plan", "agents_used", "tools_invoked", "result"],
    }

    return {
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "retrieved_docs": retrieved_docs,
        "short_term_memory": short_term_memory,
        "long_term_memory": long_term_memory,
        "structured_output": structured_output,
    }

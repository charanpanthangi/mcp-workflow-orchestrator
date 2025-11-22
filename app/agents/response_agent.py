"""Agent responsible for assembling the final workflow response."""
from typing import Dict, Any

from app.agents.base_agent import BaseAgent


class ResponseAgent(BaseAgent):
    """Formats aggregated agent outputs into schema-compliant response."""

    def run(self, request: Any, context: Dict[str, Any], history: Dict[str, Any]) -> Dict[str, Any]:
        # Collect summaries from prior agents and build a concise plan.
        summaries = {k: v.get("summary") for k, v in history.items() if isinstance(v, dict)}
        final_summary = self.call_llm([
            {"role": "system", "content": "Compose final workflow summary using given agent outputs."},
            {"role": "user", "content": str(summaries)},
        ])
        agents_used = list(history.keys()) + ["response"]
        return {
            "plan": final_summary,
            "agents_used": agents_used,
            "tools_invoked": list(history.keys()),
            "result": final_summary,
            "metadata": {"preferences": context.get("preferences", {})},
        }

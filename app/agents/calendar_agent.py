"""Agent responsible for aligning workflow with calendar availability."""
from typing import Dict, Any

from app.agents.base_agent import BaseAgent
from app.mcp.client import call_server


class CalendarAgent(BaseAgent):
    """Retrieves free slots and proposes scheduling options."""

    def run(self, request: Any, context: Dict[str, Any], history: Dict[str, Any]) -> Dict[str, Any]:
        calendar_data = call_server("calendar", {})
        summary = self.call_llm([
            {"role": "system", "content": "Pick best time slot for the workflow."},
            {"role": "user", "content": str(calendar_data)},
        ])
        return {"agent": "calendar", "data": calendar_data, "summary": summary}

"""Agent that checks visa requirements for destinations."""
from typing import Dict, Any

from app.agents.base_agent import BaseAgent
from app.mcp.client import call_server


class VisaAgent(BaseAgent):
    """Summarizes visa needs based on nationality and destination."""

    def run(self, request: Any, context: Dict[str, Any], history: Dict[str, Any]) -> Dict[str, Any]:
        nationality = request.user_preferences.get("nationality") if request.user_preferences else "unknown"
        destination = request.context.get("destination") if request.context else "unknown"
        visa_data = call_server("visa", {"nationality": nationality, "destination": destination})
        summary = self.call_llm([
            {"role": "system", "content": "Explain visa requirements clearly."},
            {"role": "user", "content": str(visa_data)},
        ])
        return {"agent": "visa", "data": visa_data, "summary": summary}

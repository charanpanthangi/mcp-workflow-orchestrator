"""Agent that plans ground transportation using MCP taxi stub."""
from typing import Dict, Any

from app.agents.base_agent import BaseAgent
from app.mcp.client import call_server


class TaxiAgent(BaseAgent):
    """Summarizes local transport plans to connect itinerary steps."""

    def run(self, request: Any, context: Dict[str, Any], history: Dict[str, Any]) -> Dict[str, Any]:
        city = request.context.get("destination", "unknown") if request.context else "unknown"
        taxi_data = call_server("taxi", {"city": city})
        summary = self.call_llm([
            {"role": "system", "content": "Outline arrival transport choices."},
            {"role": "user", "content": str(taxi_data)},
        ])
        return {"agent": "taxi", "data": taxi_data, "summary": summary}

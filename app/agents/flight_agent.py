"""Agent that proposes flight itineraries via MCP stub."""
from typing import Dict, Any

from app.agents.base_agent import BaseAgent
from app.mcp.client import call_server


class FlightAgent(BaseAgent):
    """Drafts flight options and validates them against context."""

    def run(self, request: Any, context: Dict[str, Any], history: Dict[str, Any]) -> Dict[str, Any]:
        origin = request.context.get("origin", "AAA") if request.context else "AAA"
        destination = request.context.get("destination", "BBB") if request.context else "BBB"
        flight_data = call_server("flight", {"origin": origin, "destination": destination})
        summary = self.call_llm([
            {"role": "system", "content": "Summarize flight options succinctly."},
            {"role": "user", "content": str(flight_data)},
        ])
        return {"agent": "flight", "data": flight_data, "summary": summary}

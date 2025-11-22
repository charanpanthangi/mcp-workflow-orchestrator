"""Agent that recommends hotel options."""
from typing import Dict, Any

from app.agents.base_agent import BaseAgent
from app.mcp.client import call_server


class HotelAgent(BaseAgent):
    """Curates accommodation choices using MCP hotel stub."""

    def run(self, request: Any, context: Dict[str, Any], history: Dict[str, Any]) -> Dict[str, Any]:
        city = request.context.get("destination", "unknown") if request.context else "unknown"
        hotel_data = call_server("hotel", {"city": city})
        summary = self.call_llm([
            {"role": "system", "content": "Compare hotels and pick two options."},
            {"role": "user", "content": str(hotel_data)},
        ])
        return {"agent": "hotel", "data": hotel_data, "summary": summary}

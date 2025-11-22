"""Agent responsible for gathering weather intelligence via MCP."""
from typing import Dict, Any

from app.agents.base_agent import BaseAgent
from app.mcp.client import call_server


class WeatherAgent(BaseAgent):
    """Collects weather forecasts and summarizes findings."""

    def run(self, request: Any, context: Dict[str, Any], history: Dict[str, Any]) -> Dict[str, Any]:
        payload = {"city": request.context.get("city", "unknown") if request.context else "unknown"}
        weather_data = call_server("weather", payload)
        summary = self.call_llm([
            {"role": "system", "content": "Summarize weather data concisely."},
            {"role": "user", "content": str(weather_data)},
        ])
        return {"agent": "weather", "data": weather_data, "summary": summary}

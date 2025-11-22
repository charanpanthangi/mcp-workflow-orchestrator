"""Stub MCP server returning simulated weather forecasts."""
from typing import Any, Dict
from datetime import datetime, timedelta

from app.mcp.base_server_stub import BaseMCPServerStub


class WeatherServerStub(BaseMCPServerStub):
    """Provide deterministic weather forecasts for orchestrator tests."""

    name = "weather"

    def query(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        # Simulate weather data for requested city and date range.
        city = payload.get("city", "unknown")
        start = datetime.utcnow()
        forecast = []
        for i in range(3):
            day = start + timedelta(days=i)
            forecast.append({
                "date": day.strftime("%Y-%m-%d"),
                "city": city,
                "condition": "sunny" if i % 2 == 0 else "cloudy",
                "high_c": 25 + i,
                "low_c": 15 + i,
            })
        return {"forecast": forecast}

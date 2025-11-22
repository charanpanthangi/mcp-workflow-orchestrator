"""Stub MCP server returning hotel options."""
from typing import Any, Dict

from app.mcp.base_server_stub import BaseMCPServerStub


class HotelServerStub(BaseMCPServerStub):
    """Provide predictable hotel listings for demos and tests."""

    name = "hotel"

    def query(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        city = payload.get("city", "unknown")
        return {
            "city": city,
            "hotels": [
                {"name": "Central Suites", "price": 180, "rating": 4.4},
                {"name": "Budget Inn", "price": 95, "rating": 3.8},
            ],
        }

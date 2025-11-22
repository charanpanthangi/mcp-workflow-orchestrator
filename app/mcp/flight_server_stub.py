"""Stub MCP server suggesting flight options."""
from typing import Any, Dict
from datetime import datetime, timedelta

from app.mcp.base_server_stub import BaseMCPServerStub


class FlightServerStub(BaseMCPServerStub):
    """Return basic flight itineraries for given route."""

    name = "flight"

    def query(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        origin = payload.get("origin", "AAA")
        destination = payload.get("destination", "BBB")
        depart_date = datetime.utcnow() + timedelta(days=payload.get("days_ahead", 7))
        return {
            "origin": origin,
            "destination": destination,
            "options": [
                {
                    "carrier": "MAW",
                    "depart": depart_date.strftime("%Y-%m-%dT08:00Z"),
                    "arrive": depart_date.strftime("%Y-%m-%dT12:00Z"),
                    "price": 450,
                }
            ],
        }

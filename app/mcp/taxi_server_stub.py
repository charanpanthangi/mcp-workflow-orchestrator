"""Stub MCP server returning local transport options."""
from typing import Any, Dict

from app.mcp.base_server_stub import BaseMCPServerStub


class TaxiServerStub(BaseMCPServerStub):
    """Provide simple transport quotes for last-mile planning."""

    name = "taxi"

    def query(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        city = payload.get("city", "unknown")
        return {"city": city, "options": [{"service": "rideshare", "estimate": 25}]}

"""Stub MCP server evaluating visa requirements."""
from typing import Any, Dict

from app.mcp.base_server_stub import BaseMCPServerStub


class VisaServerStub(BaseMCPServerStub):
    """Return simplified visa guidance for target countries."""

    name = "visa"

    def query(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        nationality = payload.get("nationality", "unknown")
        destination = payload.get("destination", "unknown")
        requirement = "visa-free" if nationality == destination else "visa-required"
        return {"nationality": nationality, "destination": destination, "requirement": requirement}

"""Stub MCP server returning available calendar slots."""
from typing import Any, Dict
from datetime import datetime, timedelta

from app.mcp.base_server_stub import BaseMCPServerStub


class CalendarServerStub(BaseMCPServerStub):
    """Return deterministic calendar openings for scheduling."""

    name = "calendar"

    def query(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        start = datetime.utcnow() + timedelta(days=1)
        slots = [
            (start + timedelta(hours=2)).strftime("%Y-%m-%dT%H:00Z"),
            (start + timedelta(hours=5)).strftime("%Y-%m-%dT%H:00Z"),
        ]
        return {"available_slots": slots}

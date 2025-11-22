"""Stub MCP server estimating budget feasibility."""
from typing import Any, Dict

from app.mcp.base_server_stub import BaseMCPServerStub


class BudgetServerStub(BaseMCPServerStub):
    """Return simple budget validation and recommendations."""

    name = "budget"

    def query(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        budget = payload.get("budget", 0)
        estimated_cost = max(budget * 0.8, 100)
        return {"budget": budget, "estimated_cost": estimated_cost, "status": "ok"}

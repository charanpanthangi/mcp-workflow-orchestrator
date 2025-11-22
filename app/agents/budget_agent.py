"""Agent responsible for budget validation and optimization."""
from typing import Dict, Any

from app.agents.base_agent import BaseAgent
from app.mcp.client import call_server


class BudgetAgent(BaseAgent):
    """Checks feasibility of the requested workflow against budget constraints."""

    def run(self, request: Any, context: Dict[str, Any], history: Dict[str, Any]) -> Dict[str, Any]:
        payload = {"budget": request.budget or 0}
        budget_result = call_server("budget", payload)
        summary = self.call_llm([
            {"role": "system", "content": "Explain if the budget is sufficient."},
            {"role": "user", "content": str(budget_result)},
        ])
        return {"agent": "budget", "data": budget_result, "summary": summary}

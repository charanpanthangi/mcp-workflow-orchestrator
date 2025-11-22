"""Base class for MCP server stubs used in tests and local runs."""
from typing import Any, Dict


class BaseMCPServerStub:
    """Template for MCP servers; replace with real tools in production."""

    name: str = "base"

    def query(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Return structured stub data based on input payload."""
        raise NotImplementedError

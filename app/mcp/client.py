"""MCP client wrapper that routes calls to stubbed servers."""
from typing import Dict, Any

from app.mcp.weather_server_stub import WeatherServerStub
from app.mcp.budget_server_stub import BudgetServerStub
from app.mcp.calendar_server_stub import CalendarServerStub
from app.mcp.visa_server_stub import VisaServerStub
from app.mcp.flight_server_stub import FlightServerStub
from app.mcp.hotel_server_stub import HotelServerStub
from app.mcp.taxi_server_stub import TaxiServerStub
from app.policies.retry import retry_with_policy
from app.observability.logging_utils import logger


SERVER_REGISTRY = {
    "weather": WeatherServerStub(),
    "budget": BudgetServerStub(),
    "calendar": CalendarServerStub(),
    "visa": VisaServerStub(),
    "flight": FlightServerStub(),
    "hotel": HotelServerStub(),
    "taxi": TaxiServerStub(),
}


def call_server(server_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Invoke a stub MCP server with retry for transient errors."""
    if server_name not in SERVER_REGISTRY:
        raise ValueError(f"Unknown MCP server: {server_name}")
    server = SERVER_REGISTRY[server_name]

    def _query() -> Dict[str, Any]:
        logger.debug("Calling MCP server %s with payload %s", server_name, payload)
        return server.query(payload)

    return retry_with_policy(_query)

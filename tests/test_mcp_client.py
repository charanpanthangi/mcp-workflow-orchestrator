"""Tests for MCP client routing to stub servers."""
from app.mcp.client import call_server


def test_call_server_weather():
    result = call_server("weather", {"city": "Paris"})
    assert "forecast" in result


def test_call_server_invalid():
    try:
        call_server("unknown", {})
    except ValueError:
        assert True
    else:  # pragma: no cover - defensive
        assert False

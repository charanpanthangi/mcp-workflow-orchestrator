"""Agent tests with LiteLLM mocked for deterministic summaries."""
from app.agents.weather_agent import WeatherAgent
from app.agents.response_agent import ResponseAgent
from app.config import get_llm_client
from app.memory.store import PreferenceStore
from app.schemas.workflow import WorkflowRequest


class DummyResponse:
    def __getitem__(self, item):
        if item == "choices":
            return [{"message": {"content": "summary"}}]
        raise KeyError(item)


def fake_completion(*args, **kwargs):
    return DummyResponse()


def test_weather_agent(monkeypatch):
    monkeypatch.setattr("litellm.completion", fake_completion)
    agent = WeatherAgent(get_llm_client(), PreferenceStore())
    result = agent.run(WorkflowRequest(objective="", budget=None, context={"city": "Paris"}, user_preferences={}), {}, {})
    assert result["agent"] == "weather"
    assert "forecast" in result["data"]


def test_response_agent(monkeypatch):
    monkeypatch.setattr("litellm.completion", fake_completion)
    agent = ResponseAgent(get_llm_client(), PreferenceStore())
    history = {"weather": {"summary": "sunny"}}
    result = agent.run(WorkflowRequest(objective="", budget=None, context={}, user_preferences={}), {}, history)
    assert result["plan"]
    assert "weather" in result["agents_used"]

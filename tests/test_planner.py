"""Tests for planner orchestrator flow using mocked LiteLLM."""
import pytest

from app.orchestrator.planner import PlannerOrchestrator
from app.schemas.workflow import WorkflowRequest


class DummyResponse:
    def __getitem__(self, item):
        if item == "choices":
            return [{"message": {"content": "agents: weather, budget"}}]
        raise KeyError(item)


def test_planner_builds_plan(monkeypatch):
    planner = PlannerOrchestrator()

    def fake_completion(*args, **kwargs):
        return DummyResponse()

    monkeypatch.setattr("litellm.completion", fake_completion)
    request = WorkflowRequest(objective="Test", budget=100, context={}, user_preferences={})
    plan = planner.build_plan(request)
    assert "response" in plan
    assert len(plan) >= 1


def test_planner_execute(monkeypatch):
    planner = PlannerOrchestrator()

    def fake_completion(*args, **kwargs):
        return DummyResponse()

    monkeypatch.setattr("litellm.completion", fake_completion)
    request = WorkflowRequest(objective="Test", budget=100, context={}, user_preferences={})
    response = planner.execute(request)
    assert response.plan
    assert "response" in response.agents_used

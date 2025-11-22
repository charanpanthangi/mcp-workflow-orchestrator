"""Planner and orchestrator coordinating the multi-agent workflow."""
from typing import Dict, List, Any

from app.config import get_llm_client
from app.context_engineering.objective_engine import ObjectiveEngine
from app.orchestrator.router import get_agent_class
from app.schemas.workflow import WorkflowRequest, WorkflowResponse
from app.memory.store import PreferenceStore
from app.observability.logging_utils import logger


class PlannerOrchestrator:
    """Builds execution plans and orchestrates agent execution."""

    def __init__(self) -> None:
        # Shared resources such as LLM configuration and memory store.
        self.llm_config = get_llm_client()
        self.objective_engine = ObjectiveEngine(self.llm_config)
        self.memory_store = PreferenceStore()

    def build_plan(self, request: WorkflowRequest) -> List[str]:
        """Leverage the objective engine to decide agent ordering."""
        analysis = self.objective_engine.analyze_request(request)
        logger.debug("Objective analysis produced: %s", analysis)
        required_agents = analysis.get("agents", [])
        # Always end with response agent to format output.
        if "response" not in required_agents:
            required_agents.append("response")
        return required_agents

    def execute(self, request: WorkflowRequest) -> WorkflowResponse:
        """Run the plan by invoking each agent and assemble the final response."""
        # Persist preferences before execution for continuity.
        self.memory_store.save_preferences(request.user_preferences or {})
        agent_names = self.build_plan(request)
        context: Dict[str, Any] = {"preferences": self.memory_store.load_preferences()}
        agent_outputs: Dict[str, Any] = {}

        # Sequentially run agents with shared context and cumulative outputs.
        for agent_name in agent_names:
            agent_cls = get_agent_class(agent_name)
            agent = agent_cls(self.llm_config, self.memory_store)
            logger.info("Running agent: %s", agent_name)
            agent_outputs[agent_name] = agent.run(request, context, agent_outputs)

        # Response agent returns structured workflow response.
        response_payload = agent_outputs.get("response", {})
        return WorkflowResponse(**response_payload)

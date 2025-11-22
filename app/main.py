"""FastAPI entrypoint exposing workflow orchestrator APIs."""
from fastapi import FastAPI

from app.orchestrator.planner import PlannerOrchestrator
from app.schemas.workflow import WorkflowRequest, WorkflowResponse
from app.orchestrator.router import AGENT_REGISTRY

app = FastAPI(title="Multi-Agent Workflow Orchestrator", version="1.0.0")
planner = PlannerOrchestrator()


@app.get("/health")
async def health() -> dict:
    """Liveness check endpoint."""
    return {"status": "ok"}


@app.get("/agents")
async def list_agents() -> dict:
    """Return available agent identifiers."""
    return {"agents": list(AGENT_REGISTRY.keys())}


@app.post("/run-workflow", response_model=WorkflowResponse)
async def run_workflow(request: WorkflowRequest) -> WorkflowResponse:
    """Execute the orchestrated workflow for a given request."""
    return planner.execute(request)

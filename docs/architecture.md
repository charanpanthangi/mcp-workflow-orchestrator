# Multi-Agent Workflow Orchestrator Architecture

This document outlines the layers of the orchestrator:

- **API Layer**: FastAPI surfaces `/run-workflow`, `/health`, and `/agents`.
- **Context Engineering**: Builds prompts, constraints, and memory context.
- **Planner / Orchestrator**: Uses LiteLLM to analyze objectives and pick agents.
- **Multi-Agent Layer**: Weather, Budget, Calendar, Visa, Flight, Hotel, Taxi, and Response agents.
- **MCP Layer**: Client and stub servers returning deterministic data.
- **Policies**: Safety filters, retry policy, and circuit breaker around LLM and MCP calls.
- **Memory**: JSON preference store persisting user choices across runs.
- **Observability**: Logging plus stub metrics for instrumentation.

Refer to `../diagrams/orchestrator-architecture.png` for the visual depiction.

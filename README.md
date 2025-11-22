# Multi-Agent Workflow Orchestrator (LiteLLM Edition)

## Overview
This project implements a multi-layer workflow orchestrator powered by LiteLLM. It coordinates objective analysis, context engineering, specialized agents, MCP tool calls, safety policies, memory persistence, and observability hooks to deliver structured workflow results for any domain.

![Architecture](diagrams/orchestrator-architecture.png)

## Layers
- **Context Engineering**: Builds constraints, prompts, and memory context for each call.
- **Multi-Agent Layer**: Weather, Budget, Calendar, Visa, Flight, Hotel, Taxi, and Response agents handle domain reasoning.
- **MCP Client & Servers**: Stub servers provide deterministic tool outputs to keep tests offline-ready.
- **Planner / Orchestrator**: Uses LiteLLM to interpret the request, choose agents, and execute them in sequence.
- **Preference / Memory Store**: JSON-backed store capturing user preferences between runs.
- **Retry / Circuit Breaker**: Protects all LiteLLM and MCP interactions for resilience.
- **Policy / Safety**: Lightweight sanitization and safety filters on model outputs.
- **Observability / Feedback Loop**: Logging and metrics stubs to trace each call.

## LiteLLM Integration
LiteLLM is the unified model interface. Models are configurable via environment variables:
- `LITELLM_MODEL_PLANNER`
- `LITELLM_MODEL_AGENT`

Fallbacks are enabled automatically (`gpt-4o-mini`, `groq/llama3-8b`, `claude-3-haiku`). Switching models is a single env change.

## Prompts
- System prompt: `examples/prompts/system_prompt.txt`
- Planner prompt: `examples/prompts/planner_prompt.txt`

## Example Workflow
Request (`examples/sample_workflow_request.json`):
```json
{
  "objective": "Plan a business trip to Berlin",
  "budget": 1500,
  "context": {"origin": "LON", "destination": "BER", "city": "Berlin"},
  "user_preferences": {"nationality": "UK", "hotel_style": "business"}
}
```

Response shape (`examples/sample_workflow_response.json`):
```json
{
  "plan": "Concise workflow summary",
  "agents_used": ["weather", "budget", "flight", "hotel", "taxi", "response"],
  "tools_invoked": ["weather", "budget", "flight", "hotel", "taxi"],
  "result": "Final orchestrated plan with recommendations",
  "metadata": {"preferences": {"hotel_style": "business"}}
}
```

## Setup
1. Clone the repository.
2. Create `.env` based on `.env.example` to set LiteLLM models and storage paths.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the API:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

## Docker
Build and run via Docker:
```bash
docker build -t workflow-orchestrator .
docker run -p 8000:8000 workflow-orchestrator
```
Or use docker-compose:
```bash
docker-compose up --build
```

## Tests
Run pytest to validate planner logic, agents, memory store, and MCP client stubs:
```bash
pytest
```

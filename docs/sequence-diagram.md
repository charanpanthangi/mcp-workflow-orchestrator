# Sequence Diagram Overview

1. Client calls `/run-workflow` with a `WorkflowRequest` payload.
2. Planner invokes Objective Engine powered by LiteLLM to determine agents.
3. Agents run sequentially, calling MCP servers for data and LiteLLM for reasoning.
4. ResponseAgent merges outputs into a `WorkflowResponse` schema.
5. Logs and metrics capture each step for observability.

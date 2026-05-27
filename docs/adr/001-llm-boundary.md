# ADR 001: LLM workflow boundary

## Status

Accepted

## Context

The team will build a custom multi-modal LLM choreo workflow. DimOS already provides agent infrastructure (`McpClient`, `McpServer`, `@skill` modules, streams).

## Decision

1. **Do not fork DimOS** for LLM orchestration.
2. Keep LLM/provider code in `workflow/` only.
3. Actuation goes through **MCP** (`http://localhost:9990/mcp`) or existing DimOS skills — never reimplement skill RPC.
4. Only `blueprints/` may import `dimos.robot.*`.
5. Phase A: stock `McpClient` + team prompts/skills. Phase B: custom orchestrator module calling MCP.

## Consequences

- Swappable LLM stack without touching robot code
- Contract tests on expected MCP tool names
- Clear review rule: workflow PRs must not import robot internals

"""Orchestrator protocol — implement in Phase B; MCP remains the actuation boundary."""

from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@dataclass(frozen=True)
class ToolCall:
    """One MCP tool invocation planned by the workflow layer."""

    name: str
    arguments: dict[str, object]


@runtime_checkable
class ChoreoOrchestrator(Protocol):
    """Contract for custom multi-modal choreo brains."""

    def plan_beat(self, beat_id: str, context: dict[str, object]) -> list[ToolCall]:
        """Map a choreo beat to ordered MCP tool calls."""
        ...

    def narrate(self, event: str, context: dict[str, object]) -> str:
        """Optional narration line for speak() or logging."""
        ...

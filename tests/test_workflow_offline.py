"""Offline workflow tests — no robot, no MCP server."""

from workflow.orchestrator import ChoreoOrchestrator, ToolCall


def test_tool_call_dataclass() -> None:
    call = ToolCall(name="stop_navigation", arguments={})
    assert call.name == "stop_navigation"


def test_orchestrator_protocol_is_runtime_checkable() -> None:
    class Stub:
        def plan_beat(self, beat_id: str, context: dict[str, object]) -> list[ToolCall]:
            return [ToolCall(name="demo_status", arguments={})]

        def narrate(self, event: str, context: dict[str, object]) -> str:
            return "ready"

    assert isinstance(Stub(), ChoreoOrchestrator)

"""Snapshot of MCP tools expected at dimos b45e5d5 + team skills."""

import inspect

from dimos.agents.annotation import skill
from skills.team_skills import TeamSkillContainer

# Core agentic tools from dimos @ b45e5d5 (stable contract for team_demo stack)
EXPECTED_DIMOS_TOOLS = frozenset(
    {
        "navigate_with_text",
        "stop_navigation",
        "tag_location",
        "follow_person",
        "stop_following",
        "relative_move",
        "execute_sport_command",
        "speak",
        "observe",
        "wait",
        "current_time",
    }
)

EXPECTED_TEAM_TOOLS = frozenset({"demo_status", "safe_demo_accent"})


def _skill_methods(cls: type) -> set[str]:
    names: set[str] = set()
    for name, member in inspect.getmembers(cls):
        if callable(member) and getattr(member, "__skill__", False):
            names.add(name)
    return names


def test_team_skill_container_exposes_expected_tools() -> None:
    assert _skill_methods(TeamSkillContainer) == EXPECTED_TEAM_TOOLS


def test_expected_dimos_tool_list_documented() -> None:
    """Guardrail: if you bump dimos, re-verify this list against `dimos mcp list-tools`."""
    assert len(EXPECTED_DIMOS_TOOLS) >= 10
    assert "execute_sport_command" in EXPECTED_DIMOS_TOOLS


def test_skill_decorator_present() -> None:
    assert hasattr(skill, "__call__")

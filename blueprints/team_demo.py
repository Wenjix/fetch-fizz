"""Team demo blueprint — spatial stack + agentic skills + team extensions."""

from dimos.agents.mcp.mcp_client import McpClient
from dimos.agents.mcp.mcp_server import McpServer
from dimos.core.coordination.blueprints import autoconnect
from dimos.robot.unitree.go2.blueprints.agentic._common_agentic import _common_agentic
from dimos.robot.unitree.go2.blueprints.smart.unitree_go2_spatial import unitree_go2_spatial

from skills.team_skills import TeamSkillContainer

team_demo = autoconnect(
    unitree_go2_spatial,
    McpServer.blueprint(),
    McpClient.blueprint(),
    _common_agentic,
    TeamSkillContainer.blueprint(),
).global_config(n_workers=10)

__all__ = ["team_demo"]

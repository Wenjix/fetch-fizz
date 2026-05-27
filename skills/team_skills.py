"""Demo-only skills for the fetch-fizz choreo stack."""

from dimos.agents.annotation import skill
from dimos.core.module import Module


class TeamSkillContainer(Module):
    """Extension point for hackathon-specific @skill tools."""

    @skill
    def demo_status(self) -> str:
        """Report that the fetch-fizz team demo stack is running.

        Use when the operator asks whether the custom demo blueprint is active.
        """
        return "fetch-fizz team_demo blueprint is active"

    @skill
    def safe_demo_accent(self, accent: str = "Hello") -> str:
        """Run an allowlisted sport accent for choreographed demos.

        Args:
            accent: One of Hello, Stretch, Sit, Pose, Content.
        """
        allowed = {"Hello", "Stretch", "Sit", "Pose", "Content"}
        if accent not in allowed:
            return f"Rejected accent {accent!r}. Allowed: {sorted(allowed)}"
        return f"Approved demo accent: {accent}. Call execute_sport_command with this name."

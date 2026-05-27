.PHONY: sync test replay demo nav agentic mcp-tools

sync:
	uv sync

test:
	uv run pytest -q

replay:
	bash scripts/run_replay.sh

demo:
	: $${ROBOT_IP:?Set ROBOT_IP}; uv run python scripts/run_demo.py

nav:
	bash scripts/run_nav.sh

agentic:
	bash scripts/run_agentic.sh

mcp-tools:
	uv run dimos mcp list-tools

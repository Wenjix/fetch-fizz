#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
: "${ROBOT_IP:?Set ROBOT_IP first}"
echo "Start stack: uv run dimos run unitree-go2-agentic"
echo "Then in another terminal: uv run humancli"
exec uv run dimos run unitree-go2-agentic

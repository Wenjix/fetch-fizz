#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
: "${ROBOT_IP:?Set ROBOT_IP first}"
exec uv run dimos run unitree-go2

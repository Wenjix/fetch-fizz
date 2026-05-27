#!/usr/bin/env bash
# Replay smoke — no hardware, no Foxglove. Ctrl+C to stop.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "Starting dimos replay (unitree-go2). Press Ctrl+C to stop."
exec uv run dimos --replay run unitree-go2

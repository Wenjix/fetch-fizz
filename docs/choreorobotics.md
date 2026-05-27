# Go2 Choreorobotics — fetch-fizz

Human–robot interaction reference for DimOS on the Unitree Go2. **Primary control:** `humancli` and MCP. Foxglove is optional — see [foxglove.md](foxglove.md).

## Setup

```bash
cd fetch-fizz
cp .env.example .env
export ROBOT_IP=192.168.12.1    # Go2 on dimair11

uv sync
uv run python scripts/run_demo.py    # team blueprint
# other terminal:
uv run humancli
```

| Surface | Required? | Purpose |
|---------|-----------|---------|
| **`humancli`** | Primary | Natural language → agent skills |
| **MCP** (`localhost:9990`) | Primary | Scripted choreo, workflow, tests |
| **DimOS web** (`localhost:7779`) | Built-in | Browser chat via `WebInput` |
| **Foxglove `command-center`** | Optional | Click goals on costmap |
| **Rerun viewer** | Built-in | 3D lidar, map, camera |

Pre-flight: `ping $ROBOT_IP`, flat ground, clear ~3 m radius, know stop/cancel before moving.

Set `OPENAI_API_KEY` **before** joining offline robot Wi-Fi.

## Capability groups

### 1. Co-presence and posture

| Skill / command | Source |
|-----------------|--------|
| `StandUp`, `Sit`, `BalanceStand`, `Hello`, `Stretch` | `execute_sport_command(...)` |
| `observe()` | Agentic stack |

### 2. Shared steering

| Action | How |
|--------|-----|
| Set nav goal | Agent: `navigate_with_text(...)` or optional Foxglove click |
| Relative nudge | `relative_move(forward=..., left=..., degrees=...)` |
| Stop | `stop_navigation()` |

### 3. Place-making

| Skill | Example phrase |
|-------|----------------|
| `tag_location(name)` | "Tag this location as home base" |
| `navigate_with_text(query)` | "Go to home base" |

### 4. Following

| Skill | Example phrase |
|-------|----------------|
| `follow_person(query)` | "Follow me" |
| `stop_following()` | "Stop following" |

### 5. Accent + voice

| Skill | Example phrase |
|-------|----------------|
| `safe_demo_accent(accent)` | Team skill — allowlists sport names |
| `execute_sport_command(name)` | "Do a Hello gesture" |
| `speak(text)` | "Say: Demo complete." |

### 6. Safety cut

Always end sequences with `stop_navigation`, `stop_following`, then `RecoveryStand` or `Sit`.

## Minimal demo beats

| # | Beat | You do | Robot does |
|---|------|--------|------------|
| 0 | Prelude | Confirm stand + map | Auto standup |
| 1 | Steer | "Go forward" / nav goal | Move |
| 2 | Place | Tag + return | Semantic nav |
| 3 | Follow | Follow + stop | Visual follow |
| 4 | Accent | Hello + speak | Sport + TTS |
| 5 | Cut | Stop all + sit | Neutral pose |

### Example utterances (`humancli`)

```text
Tag this location as home base
Go to home base
Follow me
Stop following
Do a Hello gesture
Say: Demo complete.
Stop navigation
```

### MCP (when stack is running)

```bash
uv run dimos mcp list-tools
uv run dimos mcp call demo_status
uv run dimos mcp call execute_sport_command --arg command_name=Hello
```

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| No agent skills | Run `scripts/run_demo.py`, not spatial-only |
| MCP connection refused | Wait for stack boot; check `:9990` |
| TTS fails offline | Set `OPENAI_API_KEY` before joining robot Wi-Fi |
| Foxglove empty | Optional — use `humancli` instead; see [foxglove.md](foxglove.md) |

## DimOS source reference

Upstream docs: [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) @ `b45e5d5`

# fetch-fizz

DimOS Go2 choreorobotics demo for the **Shanghai hackathon (May 2026)**. Depends on [DimOS](https://github.com/dimensionalOS/dimos) as a library — no fork required for normal team work.

## Quick start

```bash
git clone https://github.com/Wenjix/fetch-fizz.git
cd fetch-fizz
cp .env.example .env   # edit ROBOT_IP, OPENAI_API_KEY

# Requires uv >= 0.11, Python 3.12, and git-lfs
git lfs install
# If LFS smudge fails (offline), skip optional Foxglove assets:
GIT_LFS_SKIP_SMUDGE=1 uv sync
uv sync

# Smoke test without hardware or Foxglove
make test
make replay            # optional: long-running dimos replay (Ctrl+C to stop)
```

## Hardware demo (primary path — no Foxglove required)

```bash
export ROBOT_IP=192.168.12.1   # Go2 on dimair11
uv run python scripts/run_demo.py
# In another terminal:
uv run humancli
```

Example utterances: see [docs/choreorobotics.md](docs/choreorobotics.md).

## Shipped DimOS blueprints (reference)

```bash
export ROBOT_IP=192.168.12.1
make nav       # unitree-go2 spatial stack
make agentic   # unitree-go2-agentic + humancli
```

## Team onboarding

Each teammate: open this repo in Cursor, read [AGENTS.md](AGENTS.md), and let your agent run the interview in [docs/team-onboarding.md](docs/team-onboarding.md).

## Optional: Foxglove Studio

For 2D costmap click-nav during rehearsal — [docs/foxglove.md](docs/foxglove.md). Not required for dev or CI.

## Architecture

- [docs/architecture.md](docs/architecture.md)
- [docs/adr/001-llm-boundary.md](docs/adr/001-llm-boundary.md)

## DimOS pin

Commit `b45e5d5816632ab44f9516d4eee12ff2161ce9a8` (2026-05-25). Bump intentionally via PR; see [docs/architecture.md](docs/architecture.md#upgrading-dimos).

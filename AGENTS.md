You are a Cursor agent working in **fetch-fizz** — a DimOS Go2 choreorobotics demo repo for the Shanghai hackathon (May 2026).

## Before you write code

Run the **onboarding interview** with your human teammate. Read:

- `docs/team-onboarding.md`
- `docs/work-areas.md`
- `docs/architecture.md`

Propose a work stream, get approval, then write `docs/plans/<name>.md` before opening a PR.

## Layer rules (non-negotiable)

| Layer | Paths | May import `dimos.robot.*`? |
|-------|-------|------------------------------|
| Blueprint | `blueprints/` | Yes |
| Skills | `skills/` | No — use `@skill` on `Module` only |
| Workflow / LLM | `workflow/` | No |
| Docs / scripts | `docs/`, `scripts/` | No |

Custom LLM orchestration lives in `workflow/`. Robot actuation goes through DimOS **MCP** (`http://localhost:9990/mcp`) or `@skill` modules — do not reimplement skill RPC.

## DimOS dependency

Pinned git commit: `b45e5d5816632ab44f9516d4eee12ff2161ce9a8` (`b45e5d5`).

- Install: `uv sync`
- Bump pin only in a dedicated PR after smoke test
- Fork dimos only when patching upstream modules you cannot wrap here

## Run commands

```bash
uv sync
make replay          # no hardware
make demo            # team_demo blueprint + humancli
export ROBOT_IP=192.168.12.1
make nav             # spatial stack (shipped dimos blueprint)
make agentic         # shipped agentic blueprint + humancli
```

Foxglove Studio is **optional** — see `docs/foxglove.md`.

## Environment

Copy `.env.example` → `.env`. Set `OPENAI_API_KEY` **before** joining offline robot Wi-Fi (`dimair11`).

## Safety (LLM + real dog)

- Allowlisted sport accents only (`Hello`, `Stretch`, `Sit`, `Pose`, `Content`)
- Cap `relative_move` distances in choreo scripts
- Every sequence ends with `stop_navigation` / `stop_following`
- Human override (stop skills, Ctrl+C) always wins

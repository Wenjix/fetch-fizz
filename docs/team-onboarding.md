# Team onboarding

Each teammate's Cursor agent runs this **once** before writing code.

## Agent steps

1. Read `AGENTS.md`, this file, and `docs/work-areas.md`.
2. Interview your human (questions below).
3. Propose **one primary + one backup** work stream from `docs/work-areas.md`.
4. Write `docs/plans/<name>.md` with scope, out-of-scope, first PR target.
5. Wait for human approval before coding.

## Interview questions

Ask your human:

1. What do you want to learn or showcase in this demo?
2. Do you have Go2 hardware access, or replay-only for now?
3. What are you most comfortable with — Python/robot stack, LLM orchestration, docs/ops, or live demo performance?
4. Any hard constraints? (offline Wi-Fi, no Foxglove, specific model/provider)
5. How much time until the demo rehearsal?

## Plan file template

Create `docs/plans/<your-name>.md`:

```markdown
# Plan: <name>

## Primary stream
(e.g. Skills / MCP)

## Backup stream
(e.g. Demo / ops)

## Paths I may edit
- skills/
- tests/

## Out of scope
- workflow/ (unless agreed with teammate)

## First deliverable
- Add `begin_choreo_beat` skill + test

## Blockers / coordination
- Need blueprint owner to wire new skill into team_demo.py
```

## Conflict resolution

If two teammates pick the same stream, sync in standup and adjust plans. Re-run only the conflicting slice of the interview.

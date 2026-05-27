# Work areas

Agents map teammates here **after the onboarding interview** — this is a menu, not a fixed org chart.

## Runtime / blueprint

**Paths:** `blueprints/`, `scripts/`, `pyproject.toml`, pin bumps

**Good if human says:** "I want the stack to boot reliably", "CI and install"

**First deliverables:** `run_demo.py`, replay script, Makefile, CI workflow

---

## Workflow / LLM

**Paths:** `workflow/`, `workflow/prompts/`

**Good if human says:** "I'm building the multi-modal choreo brain", "prompts and orchestration"

**First deliverables:** implement `ChoreoOrchestrator`, beat scripts, prompt v2

**Rule:** no `dimos.robot.*` imports

---

## Skills / MCP

**Paths:** `skills/`, `tests/test_mcp_tools.py`

**Good if human says:** "I want new robot moves/tools", "MCP contract tests"

**First deliverables:** new `@skill` methods, expand contract test list

---

## Demo / ops

**Paths:** `docs/choreorobotics.md`, `docs/plans/`, network runbooks

**Good if human says:** "I'll run the show on demo day", "rehearsal checklist"

**First deliverables:** rehearsal script, pre-flight checklist, offline Wi-Fi notes

---

## Optional visualization

**Paths:** `docs/foxglove.md`

**Good if human says:** "I want costmap click-nav for rehearsal"

**First deliverables:** Foxglove setup doc (extension is optional, not required)

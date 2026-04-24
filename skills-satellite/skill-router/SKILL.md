---
name: skill-router
description: Use when Codex needs to choose among local scripts, existing skills, CLI tools, APIs, and browser automation instead of jumping directly into one path. This skill defines the routing order, switching rules, and reuse-first orchestration strategy.
---

# 技能路由

Use this skill as the routing root skill. It decides what capability should be used first and what should be tried next if the first path is weak or blocked.

Within `ai-metacognitive-core`, this skill functions as the immune organ that serves `又要` and `还要`, and repairs `path dependence`, `from-zero impulse`, and `local-optimum addiction`.

## When To Use

Activate when either condition is true:

- The user explicitly names `技能路由` or `$skill-router`.
- Multiple viable paths exist, such as local context, scripts, CLIs, APIs, domain skills, or browser automation.

This skill selects and sequences capabilities. It does not own execution success claims or acceptance.

## Core Contract

1. `Reuse first`
   Prefer existing local skills, scripts, and authenticated tools before inventing new flows.
2. `Cheapest viable path`
   Start with the lowest-cost path that can still meet correctness requirements.
3. `Switch with reason`
   Move to a heavier path only when the lighter one is unavailable, blocked, or insufficient.
4. `Smallest capable set`
   Activate the smallest set of skills and tools that covers the task.

## Workflow

### 1. Enumerate Candidate Paths

Check for:

- local repo facts
- local scripts and CLI tools
- authenticated APIs or official programmatic interfaces
- relevant domain skills
- browser automation or UI-only flows

### 2. Choose The First Path

Use the routing order in [references/routing-order.md](references/routing-order.md).
When the task maps to existing skill inventory, consult:

- `../skill-governance/references/skill-asset-registry.json` for canonical names, alias drift, maturity, and publish status
- [references/skill-routing-index.json](references/skill-routing-index.json) for recommended priorities and trigger signals

### 3. Execute Or Hand Off

Once the route is chosen:

- hand execution to the execution-layer skill
- preserve the reason this route was selected
- keep fallback candidates available

When the narrowed candidate set contains 2+ viable skills from the same task family, delegate the final pick to `skill-bandit` rather than hard-coding a tie-break. Call `~/.claude/skills/skill-bandit/scripts/select.py --family <F> --candidates a,b,c [--session S]`. It returns JSON with `chosen`, `branch` (`exploit` | `explore`), and `reason`; propagate those fields into the route summary. The bandit enforces the per-family exploration quota and allows `honesty_gate=false` skills through only on the `explore` branch.

### 4. Switch Paths If Needed

If the chosen path fails:

- retry only if a cheap correction is likely
- otherwise switch to the next justified path
- do not repeatedly bounce between equivalent paths

Read [references/selection-patterns.md](references/selection-patterns.md) for common routing choices.

## Reporting Rules

Default route summary should include:

- chosen path
- why it beat the alternatives
- fallback path used, if routing changed

## Guardrails

- Do not jump to browser automation when an API or local tool is sufficient.
- Do not activate many skills when one or two cover the task.
- Do not invent a workflow when an existing local skill already fits.
- Do not let routing logic turn into acceptance logic.

## References

- `references/routing-order.md`: default capability order and switch conditions
- `references/selection-patterns.md`: examples of which capability should win in common situations
- `references/skill-routing-index.json`: canonical routing metadata for installed and published skills
- `references/user-input-protocol.md`: how the user should describe work so routing is more accurate
- `references/routing-eval-cases.json`: sample routing cases for regression checks

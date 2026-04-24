# 系统行为审计 Playbook

## 何时使用

Use this playbook when the request is:

- a system-wide audit
- a skill-ecology review
- a runtime maturity review
- a historical behavior assessment
- a scoring-model based evaluation

This is a high-order mixed mode:

`研究审计 + 治理协作`

Use `full mode` only.

## Evidence Order

Use local evidence in this order:

1. `canonical docs`
2. `runtime state and artifacts`
3. `skill ecology and root-skill files`
4. `historical runs / reviews / soul logs`

Treat Feishu and GitHub mirrors as secondary or excluded unless the local canonical log is missing.

If the user explicitly asks for external benchmark, insert a separate layer after local evidence:

5. `external benchmark layer`

This layer may use GitHub, official documentation, or strong public best-practice sources, but it must not replace local canonical truth.

## Workflow

### 1. Define The Audit Object

State:

- what is being audited
- what time boundary applies
- what evidence counts as canonical
- what the score is supposed to help decide

### 2. Build The Evidence Base

Collect:

- current local snapshot
- historical artifacts that explain repetition or drift
- representative high-evidence samples

Do not start scoring before the evidence surface is stable.

### 3. Apply The Rubric

Use [audit-rubric.md](audit-rubric.md).

Score:

- the total system
- each chosen subsystem
- representative samples when they materially clarify the result

### 4. Write The Scorecards

At minimum include:

- `System Scorecard`
- `Subsystem Scorecards`
- `Deduction Ledger`
- `Roadmap`

If the audit is becoming an operating surface, also include:

- `External Intel`
- `Benchmark Links`
- `Recursion Queue`

### 5. Extract The Governance Meaning

Translate the audit into:

- what is already working
- what is structurally weak
- what should be fixed now
- what should become an evolution rule later

### 6. End With Evolution

Write one `Evolution Note`:

- what was learned from the audit
- what was still noisy
- what the next audit should sharpen

If the user asks to land the audit in Feishu:

- keep local artifacts canonical
- mirror the scorecards and gaps to Feishu
- open explicit benchmark gaps for objects with no external evidence
- write unresolved gaps into a recursion queue

## Default Output Shape

Use this order:

1. `Inquiry Brief`
2. `Analysis Card`
3. `Audit Run Sheet`
4. `Audit Pack`
5. `Decision Pack`
6. `Evolution Note`

## Stop Conditions

Stop or narrow the audit if:

- the audit object is still ambiguous
- the evidence base is too weak for scoring
- the requested scope would explode into a giant inventory dump
- the scoring would become impressionistic

## Typical Evidence Sources

- `FORCE-CLAW/*.md`
- `workspace state / runtime-artifacts`
- `~/.codex/skills/*`
- `AI大管家 inventories / reviews / runs / soul`

## Non-Goals

- Do not produce a 100+ skill score ledger unless explicitly asked.
- Do not repeat an older audit verbatim.
- Do not let the report become only narrative without scoring detail.

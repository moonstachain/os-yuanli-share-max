---
name: evidence-gate
description: Use when results must be accepted through independent evidence rather than agent self-reporting. This skill defines artifact checks, goal-match checks, and read-back confirmation so completion is based on proof, not effort or tool exit codes.
---

# 证据质检

Use this skill as the acceptance root skill. It verifies whether a claimed result is real, complete, and aligned with the user's actual objective.

Within `ai-metacognitive-core`, this skill functions as the immune organ that serves `真完成` and repairs `pseudo-completion`.

## When To Use

Activate when either condition is true:

- The user explicitly names `证据质检` or `$evidence-gate`.
- The task outcome needs independent validation, especially for reports, screenshots, data extraction, automation outcomes, or external writes.

This skill is verification-specific. It should be usable after any execution flow, not just after `jiyao-youyao-haiyao`.

## Core Contract

1. `Artifact proof`
   Confirm the output exists and can be opened, read, or queried.
2. `Goal proof`
   Confirm the output matches the intended target, not just a surface-level success signal.
3. `Read-back discipline`
   For external writes or state changes, verify by reading the resulting state.
4. `Independent judgment`
   Do not accept execution-layer claims without evidence.

## Workflow

### 1. Identify The Claimed Result

Pin down:

- what artifact or state was supposed to be produced
- what counts as evidence
- which part is objective and which part is preference-sensitive

### 2. Run Artifact Check

Confirm the output exists in a concrete form:

- file path
- remote object
- page state
- returned dataset
- changed external record

### 3. Run Goal Match Check

Verify the result against the user's real target:

- expected sections
- expected content
- expected page or UI state
- expected record count or fields
- expected remote system state

Read [references/acceptance-matrix.md](references/acceptance-matrix.md) for output-specific checks.

### 4. Decide Acceptance

Only accept completion when both are true:

- the artifact or state exists
- the artifact or state matches the intended result

If only one layer passes, report failure or incompleteness clearly.

## Reporting Rules

Default output should include:

- acceptance result
- evidence summary
- mismatch or missing piece, if any

## Reward Bridge

After any acceptance decision on a skill-driven result, post the verdict to the skill-bandit reward stream. This closes the loop from `evidence-gate` back to routing decisions.

```bash
python3 ~/.claude/skills/skill-bandit/scripts/bridge_reward.py evidence-gate \
  --skill <skill_name> \
  --verdict passed|failed \
  --session <session_id> \
  [--note "<one-line reason>"]
```

Rules:
- Call it for every terminal verdict — both `passed` and `failed` matter for scoring.
- Use the skill that actually produced the claimed result, not the verifier. If the run went through a chain, attribute to the last execution-layer skill.
- The bridge is non-blocking (exits 0 even on failure) — do not let it gate the acceptance report.
- Skip only when there is no identifiable producing skill (e.g. raw user work with no routing).

## Guardrails

- Do not accept based only on logs, tool success, or agent confidence.
- Do not confuse "artifact exists" with "goal achieved".
- Do not skip read-back after external writes.
- Do not let subjective polish override objective correctness unless the user said preference dominates.

## References

- `references/acceptance-matrix.md`: default evidence checks by artifact type
- `references/evidence-patterns.md`: reporting patterns for proof-oriented acceptance

---
name: intent-grounding
description: Use when a request is still fuzzy and needs to be turned into a concrete target before execution. This skill compresses user intent into goals, success criteria, artifacts, constraints, escalation boundaries, and non-goals so later skills do not execute against the wrong target.
---

# 意图压实

Use this skill as the target-shaping root skill. It turns a vague or high-level request into a concrete execution target that the rest of the stack can reliably follow.

Within `ai-metacognitive-core`, this skill functions as the immune organ that serves `既要` and repairs `goal drift` and `pseudo-understanding`.

## When To Use

Activate when either condition is true:

- The user explicitly names `意图压实` or `$intent-grounding`.
- The task is underspecified enough that execution risk comes from misunderstanding the target rather than from implementation difficulty.

This skill should usually run before routing or execution when the target is still soft.

## Core Contract

1. `Concrete target`
   Define what success looks like in observable terms.
2. `Boundary clarity`
   Define what is in scope, out of scope, and what needs user approval.
3. `Artifact clarity`
   Define what must be produced or changed.
4. `Non-goal discipline`
   Prevent later skills from optimizing for things the user did not ask for.

## Workflow

### 1. Extract The Raw Ask

Identify:

- stated goal
- implied goal
- obvious ambiguities
- visible constraints

### 2. Compress Into Execution Inputs

Turn the task into:

- objective
- done condition
- expected artifacts
- constraints
- escalation boundaries
- non-goals

Use [references/grounding-checklist.md](references/grounding-checklist.md) as the default conversion checklist.

### 3. Decide Readiness

If the target is now concrete enough:

- hand off to `human-ai-collab-loop` or `skill-router`

If not:

- ask the smallest necessary clarifying question
- avoid asking for details that can be discovered locally

### 4. Preserve The Contract

Carry the compressed target forward so later skills do not reinterpret the ask.

Read [references/success-criteria-patterns.md](references/success-criteria-patterns.md) when translating soft requests into concrete done conditions.

## Reporting Rules

Default output should include:

- objective
- success criteria
- artifacts
- boundaries
- key assumptions

## Guardrails

- Do not over-clarify when a reasonable default is enough.
- Do not skip target shaping when ambiguity can change the result materially.
- Do not let later execution overwrite the agreed target silently.
- Do not confuse means with ends.

## References

- `references/grounding-checklist.md`: default target-shaping checklist
- `references/success-criteria-patterns.md`: examples of turning soft asks into concrete done conditions

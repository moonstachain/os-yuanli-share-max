---
name: closure-evolution
description: Use when a completed task should be reviewed for reusable upgrades. This skill decides what should be promoted into a protocol rule, a domain skill, a script, or nothing, so one-off work can become structured future capability without uncontrolled skill bloat.
---

# 闭环进化

Use this skill as the upgrade root skill. It turns execution experience into reusable capability when the pattern is worth keeping.

Within `ai-metacognitive-core`, this skill functions as the immune organ that serves `再要` and repairs `pseudo-evolution`.

## When To Use

Activate when either condition is true:

- The user explicitly names `闭环进化` or `$closure-evolution`.
- A task exposed a repeated pattern, missing protocol, missing script, or reusable domain heuristic that may deserve formalization.

This skill is about selective promotion, not endless self-expansion.

## Core Contract

1. `Promote only reusable value`
   Do not turn one-off pain into permanent skill surface area.
2. `Choose the right destination`
   Route the insight into a root skill, domain skill, script, template, or nowhere.
3. `Upgrade after closure`
   Reflection happens after a real task has reached completion or a stable blocker.
4. `Keep the tree sharp`
   New capability should reduce future friction, not create more protocol weight.

## Workflow

### 1. Review The Run

Identify:

- repeated failure or recovery patterns
- missing verification rules
- missing routing rules
- missing domain heuristics
- repeated manual steps that should become scripts

### 2. Evaluate Reusability

Use [references/promotion-rubric.md](references/promotion-rubric.md) to decide if the insight is worth promotion.

### 3. Choose A Destination

Send the upgrade to the correct layer:

- root skill rule
- domain skill update
- script or automation
- no promotion

### 4. Record The Upgrade Direction

If the insight is actionable, report:

- what should change
- where it should live
- why it will reduce future friction

Read [references/upgrade-destinations.md](references/upgrade-destinations.md) when the right destination is not obvious.

## Reporting Rules

Default reflection output should include:

- pattern observed
- promotion decision
- chosen destination
- reason for promotion or rejection

## Reward Bridge

After the promotion decision lands, post it to the skill-bandit reward stream so future routing reflects which skills actually generated keepable upgrades.

```bash
python3 ~/.claude/skills/skill-bandit/scripts/bridge_reward.py closure-evolution \
  --skill <skill_name> \
  --verdict kept|dropped \
  --session <session_id> \
  [--note "<what was kept or why dropped>"]
```

Rules:
- `kept` = insight was promoted into a rule/skill/script. `dropped` = reviewed and rejected.
- Attribute to the skill whose run exposed the pattern, not to `closure-evolution` itself.
- One call per promotion decision; if a single run yields multiple upgrades, emit one call per skill that contributed.
- Non-blocking: errors go to `logs/bridge_reward.err`, do not retry or gate the reflection output on it.

## Guardrails

- Do not promote every annoyance.
- Do not upgrade a root skill when the issue is domain-specific.
- Do not hide upgrade-worthy patterns once they have repeated.
- Do not let reflection become a second execution project.

## References

- `references/promotion-rubric.md`: deciding whether an insight deserves promotion
- `references/upgrade-destinations.md`: how to choose between root skills, domain skills, scripts, or no change

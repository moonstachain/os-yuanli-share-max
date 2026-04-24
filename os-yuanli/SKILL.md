---
name: os-yuanli
description: "Use when the user explicitly asks for OS-原力, 原力OS, or wants a standalone root skill that takes over a task via 治理OS × 工作OS: start with six judgments, pass through 主题层 / 策略层 / 执行层, adapt artifact names by task family, support system audits and maturity scoring, verify before claiming completion, and end with an evolution note."
invokes: intent-grounding, skill-router, evidence-gate
---

# OS-原力

`os-yuanli` is a callable root skill for running work through `原力OS`.

Treat it as an operating protocol, not as a domain skill and not as a document index.

Its default order is:

1. `六判断`
2. `主题层 gate`
3. `策略层 gate`
4. `执行层 route`
5. `验真`
6. `进化`

## Overview

Use this skill to take over a task through `治理OS × 工作OS`.

Do not start from tools. Do not start from execution. Do not start from output shape.

Start from:

- whether the task is worth entering
- how the task should win
- how the task should be closed as a real loop

Then adapt the artifact pack to the task family.

When the request is a system-wide audit, score model, capability review, maturity evaluation, or historical behavior assessment, run the high-order mixed protocol in [references/system-audit-playbook.md](references/system-audit-playbook.md).

When the user explicitly wants that audit to become a long-lived operating surface in Feishu, also apply [references/system-audit-feishu-loop.md](references/system-audit-feishu-loop.md). Keep local artifacts canonical, add external benchmark as a separate layer, then mirror the result into Feishu through a bridge or repo-side sync script.

## Core Contract

Apply these rules on every qualifying task:

1. `六判断先行`
   - `自治判断`
   - `全局最优判断`
   - `能力复用判断`
   - `验真判断`
   - `进化判断`
   - `当前最大失真`
2. `先主题，后策略，再执行`
   Do not jump into execution before the task passes `主题层` and `策略层`.
3. `每层都过三条治理线`
   Check `递归进化 / 全局最优 / 人类友好` at each layer.
4. `先止损，再推进`
   If the task fails the theme gate, stop at the brief. If the strategy is weak, stop before execution.
5. `完成前必须验真`
   Route claimed completion through `evidence-gate`.
6. `完成后必须进化`
   End with an `Evolution Note`, then hand reusable upgrades to `closure-evolution`.

See [references/constitution.md](references/constitution.md) for the compressed constitution.

## Universal Interface

Always expose two layers of output.

### Universal Preamble

Always surface:

- `六判断`
- `任务族判断`
- `mode 判断`

### Adaptive Artifact Pack

Map the task into one of the packs in [references/task-family-map.md](references/task-family-map.md).

Default families:

- `内容生产`
- `研究审计`
- `工作流自动化`
- `接线部署`
- `治理协作`
- `软件开发`
- `未知或混合任务`

Use `full mode` for multi-stage, high-value, high-tradeoff, or explicitly deep tasks.

Use `light mode` for small, low-risk, low-complexity tasks. Keep internal gates intact even when the visible output is shorter.

See [references/output-contract.md](references/output-contract.md) for exact output rules.

For system audits that land in Feishu, keep the score kernel in `os-yuanli`, but delegate the actual schema sync and record upserts to the bridge layer described in [references/system-audit-feishu-loop.md](references/system-audit-feishu-loop.md).

## Workflow

Run this protocol in order.

### 1. Shape The Task

Compress the request into:

- real objective
- done condition
- human-only boundaries
- obvious constraints

If the request is vague, call `intent-grounding`. If it is already clear, do only a light compression.

### 2. Classify The Task Family

Choose the smallest valid family from [references/task-family-map.md](references/task-family-map.md).

Do not leave the task unclassified unless it is truly mixed or unclear.

### 3. Choose The Mode

Select:

- `full mode`
- `light mode`

Default to `full mode` when the task is multi-stage, cross-skill, or materially important.

### 4. Run The Theme Gate

Ask whether this task should enter at all.

Output the family-specific brief object.

Stop here if:

- the task does not serve the current goal
- the objective is too weak or too vague
- a higher-value theme clearly dominates

### 5. Run The Strategy Gate

Ask how this task should win.

Always state the current strategy layer:

- `数据`
- `特征`
- `观点`
- `洞察`
- `全局最优`

Output the family-specific card object.

Stop before execution if:

- the strategy is only a slogan
- the evidence path is weak
- the route does not solve the core contradiction

### 6. Route The Execution Layer

Use `skill-router` to choose the smallest capable set, then run execution under `jiyao-youyao-haiyao-zaiyao`.

Always show:

- who or what will execute
- why this route won
- what the verification target is

See [references/routing-bridges.md](references/routing-bridges.md) for the fixed bridge rules.

### 7. Verify Before Claiming Completion

Before claiming done:

- check the artifact exists
- check the result meets the objective
- check the task did not drift from the chosen theme and strategy

Use `evidence-gate` when a real completion claim is made.

### 8. End With Evolution

Always produce an `Evolution Note`.

If the run exposed reusable value, send the upgrade decision to `closure-evolution`.

Do not promote every annoyance.

## Task-Family Adaptation

Adapt the artifact pack by family.

### 内容生产

Use:

- `Theme Brief`
- `Strategy Card`
- `Execution Run Sheet`
- `Publish Pack`
- `Evolution Note`

Canonical content chain is defined in [references/routing-bridges.md](references/routing-bridges.md).

### 研究审计

Use:

- `Inquiry Brief`
- `Analysis Card`
- `Audit Run Sheet`
- `Audit Pack`
- `Evolution Note`

### 工作流自动化

Use:

- `Automation Brief`
- `Design Card`
- `Build Run Sheet`
- `Delivery Pack`
- `Evolution Note`

### 接线部署

Use:

- `Rollout Brief`
- `Rollout Card`
- `Deployment Run Sheet`
- `Release Pack`
- `Evolution Note`

### 治理协作

Use:

- `Governance Brief`
- `Policy Card`
- `Governance Run Sheet`
- `Decision Pack`
- `Evolution Note`

### 软件开发

Use:

- `Dev Brief`
- `Architecture Card`
- `Dev Run Sheet`
- `Delivery Pack`
- `Evolution Note`

Route to `auto-dev` after both gates pass. See [references/routing-bridges.md](references/routing-bridges.md) for the fixed chain.

### 未知或混合任务

Fallback to:

- `Task Brief`
- `Strategy Card`
- `Execution Run Sheet`
- `Result Pack`
- `Evolution Note`

## Integration Boundaries

Do not overlap blindly with other root skills.

### With AI大管家

If the user explicitly calls both `AI大管家` and `OS-原力`:

- `AI大管家` owns external inventory, top-level route, and closure sync
- `os-yuanli` owns the `3 × 3` method kernel and adaptive artifact pack

Do not copy Feishu or GitHub sync logic into `os-yuanli`.

### With jiyao-operating-system

Do not nest two total entrypoints.

If both appear:

- keep `os-yuanli` as the visible operating method
- reuse the lower organs directly instead of wrapping `jiyao-operating-system`

### With skill-router

`os-yuanli` owns the gates and artifact structure.

`skill-router` owns path selection.

Do not blur those roles.

See [references/integration-boundaries.md](references/integration-boundaries.md) for the full boundary map.

## Guardrails

- Do not turn this skill into a giant prompt.
- Do not skip the theme gate just because execution looks easy.
- Do not treat a good viewpoint as a finished strategy.
- Do not claim completion before evidence exists.
- Do not expose more human checkpoints than necessary.
- Do not hardcode many domain workflows when `skill-router` can choose them.

## References

- [references/constitution.md](references/constitution.md): compressed 原力OS constitution
- [references/task-family-map.md](references/task-family-map.md): family detection, adaptive packs, stop conditions
- [references/routing-bridges.md](references/routing-bridges.md): fixed internal bridge rules and family chains
- [references/output-contract.md](references/output-contract.md): `full mode` and `light mode` output rules
- [references/integration-boundaries.md](references/integration-boundaries.md): boundaries with other root skills
- [references/audit-rubric.md](references/audit-rubric.md): 6-axis scoring model for system and task maturity
- [references/system-audit-playbook.md](references/system-audit-playbook.md): high-order audit path for skill ecology, runtime, and operating-system reviews
- [references/system-audit-feishu-loop.md](references/system-audit-feishu-loop.md): Feishu mirror, external benchmark layer, and recursion queue rules
- [references/context-compaction-protocol.md](references/context-compaction-protocol.md): context compression protocol for long sessions — what to keep, what to compress, when to trigger
- [references/pattern-card-spec.md](references/pattern-card-spec.md): pattern language spec for skills — problem/forces/solution/tradeoffs format and 5 exemplar cards

## Local Health Check

``bash
python3 /Users/liming/.codex/skills/os-yuanli/scripts/doctor.py
``

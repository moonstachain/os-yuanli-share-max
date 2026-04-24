# 集成边界

## With `AI大管家`

If the user explicitly invokes both:

- `AI大管家` owns:
  - inventory
  - top-level route
  - local canonical closure
  - Feishu / GitHub sync policy
- `os-yuanli` owns:
  - `治理OS × 工作OS` method kernel
  - task-family adaptation
  - theme / strategy / execution gates
  - adaptive artifact pack

Do not duplicate `AI大管家` sync or governance payload logic inside `os-yuanli`.

## With `jiyao-operating-system`

Do not nest two total entrypoints.

If both are present:

- keep `os-yuanli` as the visible operator
- reuse `intent-grounding`
- reuse `skill-router`
- reuse `jiyao-youyao-haiyao-zaiyao`
- reuse `evidence-gate`
- reuse `closure-evolution`

Do not wrap through `jiyao-operating-system` first.

## With `skill-router`

`skill-router` decides among scripts, APIs, tools, and domain skills.

`os-yuanli` decides:

- whether the task should enter
- what family it belongs to
- what artifact structure it should produce
- when the route may proceed

## With `evidence-gate`

`os-yuanli` may define the verification target.

`evidence-gate` decides whether the claimed result is real.

Do not merge these roles.

## With `closure-evolution`

`os-yuanli` always emits an `Evolution Note`.

`closure-evolution` decides whether any part deserves promotion into:

- root skill rule
- domain skill update
- script / automation
- no promotion

## With Domain Skills

Domain skills own the actual domain heuristics and actions.

`os-yuanli` must not swallow them into a giant generic prompt.

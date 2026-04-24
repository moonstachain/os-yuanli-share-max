# 路由桥接

## Core Chain

Do not wrap another total entrypoint.

Use this internal chain by default:

1. `intent-grounding`
2. `skill-router`
3. `family skills`
4. `jiyao-youyao-haiyao-zaiyao`
5. `evidence-gate`
6. `closure-evolution`

## Content Family Canonical Chain

For high-rigor content tasks, use this fixed chain:

1. `wechat-style-profiler`
   - only when Style DNA is missing or weak
2. `wechat-topic-outline-planner`
3. `wechat-draft-writer`
4. `wechat-title-generator`

For fast, lower-rigor content tasks, allow:

- `wechat-article-writer`

Do not let the fast path replace the canonical path when the task needs reusable quality.

## Research And Audit Family

Default to `skill-router`, then select the smallest capable chain.

Common candidates include:

- `openai-docs`
- `feishu-reader`
- `pdf`
- `spreadsheet`
- `notion-research-documentation`

## Workflow Automation Family

Default to `skill-router`, then select among:

- `n8n-workflow-engineer`
- `dify-workflow-engineer`
- `coze-workflow-operator`
- `feishu-workflow-builder`

Choose the system after the strategy gate, not before.

## Rollout And Deployment Family

Default to `skill-router`, then select the smallest valid chain.

Typical deployment paths may involve:

- `cloudflare-deploy`
- repo-local scripts and validators
- browser automation only when no API or local path is sufficient

## Software Development Family

Default to `auto-dev` for PRD-driven autonomous development.

Fixed chain:

1. `os-yuanli` theme gate — confirm PRD is clear and worth entering
2. `os-yuanli` strategy gate — confirm parallelism, coder, and test strategy
3. `auto-dev` — Phase 1 (Init) → Phase 2 (Parallel Dev) → Phase 3 (Verify)
4. `evidence-gate` — verify delivery report against original PRD acceptance criteria
5. `closure-evolution` — extract reusable patterns

Entry condition: PRD must pass both gates before `auto-dev` Phase 1 begins.

If the task is too small for the full pipeline (single file, trivial change), do not route to `auto-dev`. Use direct execution instead.

## Governance And Collaboration Family

Default to `skill-router`, then select among:

- `skill-governance`
- `human-ai-collab-loop`
- `linear`

Use `AI大管家` only when the user explicitly asks for its outer governance role or the task needs its canonical local closure stack.

## Non-Goals

- Do not route through `jiyao-operating-system` as a wrapper.
- Do not activate many equivalent domain skills at once.
- Do not let `skill-router` decide whether the task is worth entering. That belongs to the theme gate.

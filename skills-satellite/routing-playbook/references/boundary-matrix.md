# Boundary Matrix

Use this file when the task sits near a known overlap.

## `skill-trainer-recursive` vs `skill-creator`

- Choose `skill-trainer-recursive` when the user wants method, intent clarification, first principles, benchmark alignment, or recursive improvement.
- Switch to `skill-creator` when the job is already clear and mainly needs file scaffolding, metadata, and validation.

## `guide-benchmark-learning` vs `openai-docs`

- Choose `guide-benchmark-learning` when the user first needs a manual-first learning layer, benchmark comparison, and execution-readiness judgment.
- Switch to `openai-docs` as the second hop when the unfamiliar domain is specifically OpenAI products or APIs.

## `guide-benchmark-learning` vs `skill-trainer-recursive`

- Choose `guide-benchmark-learning` when the domain itself is unfamiliar and still needs manuals, source-of-truth docs, and benchmark guides.
- Switch to `skill-trainer-recursive` after the domain is understood well enough to train a reusable skill method.

## `feishu-open-platform` vs `feishu-bitable-bridge` vs `feishu-reader`

- Choose `feishu-open-platform` when the question is about rules, auth, scopes, APIs, callbacks, manifests, or official capability verification.
- Switch to `feishu-bitable-bridge` when the task is already narrowed to bitable schema inspection or row upsert.
- Switch to `feishu-reader` when the task is to read or extract content from a Feishu or Lark page.

## `jiyao-youyao-haiyao` vs `jiyao-youyao-haiyao-zaiyao`

- Choose `jiyao-youyao-haiyao` when the job is a single closure pass with low interruption and strong autonomy.
- Switch to `jiyao-youyao-haiyao-zaiyao` when the work is clearly multi-stage and needs stronger convergence plus short reflection.

## `self-evolution-max` vs `AI大管家` review

- Choose `AI大管家` review when the task is to assess the skill system, count skills, map capabilities, or propose next actions.
- Switch to `self-evolution-max` only when the user wants explicit multi-round plan-execute-evaluate loops.

## `ai-da-guan-jia` review path vs `skill-creator`

- Choose `AI大管家` review path when the task is about system review, capability mapping, duplication, or routing quality.
- Switch to `skill-creator` only when the user wants to build or update a specific skill artifact.

## `openclaw-xhs-coevolution-lab` vs `opencli-platform-bridge + get-biji-transcript`

- Choose `openclaw-xhs-coevolution-lab` when the user wants to CREATE XHS content (account strategy, note blueprints, topic planning, viral mechanics design).
- Choose `opencli-platform-bridge` + `get-biji-transcript` when the user wants to READ/AUDIT an existing XHS account (note listing, transcript extraction, style analysis, IP benchmarking).
- Key signal words for creation: 爆款, 共进化, 内容策略, 发布, 博主定位, 笔记蓝图.
- Key signal words for reading: 盘点, 分析, 拆解, 口播, 逐字稿, 风格, IP分析, 对标, 内容审计.

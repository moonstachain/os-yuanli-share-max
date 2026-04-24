# Task Playbooks

> **Genome-first rule**: Before using a manual playbook entry below, check `routing-templates.json` for a genome-validated template. Genome templates carry empirical co-selection evidence and take priority when `success_rate >= 0.8`.

Use the same template for every playbook:

- `任务画像`
- `推荐 skill 组合`
- `何时用`
- `何时不要用`
- `默认顺序`
- `最小验真目标`
- `常见误路由`
- `真实样例 prompt`

## 1. Skill 创建 / 训练

### 任务画像

User wants to create a new skill, train a skill method, or turn a repeated workflow into a reusable local skill.

### 推荐 skill 组合

`ai-da-guan-jia -> skill-trainer-recursive -> skill-creator`

### 何时用

- user asks to train a new skill
- user wants first-principles decomposition before writing `SKILL.md`
- user wants recursive improvement instead of a one-off scaffold

### 何时不要用

- the user already has a finished spec and only wants the file scaffold
- the task is not about skills at all

### 默认顺序

1. `ai-da-guan-jia`
2. `skill-trainer-recursive`
3. `skill-creator`

### 最小验真目标

- `intent-canvas.json`
- `first_principles.md`
- `benchmark-map.json`
- candidate skill spec
- validator pass on the generated skill

### 常见误路由

- only because the prompt contains `skill`, route directly to `skill-creator`

### 真实样例 prompt

`帮我训练一个新的 Feishu 能力 skill，先想清楚方法，再生成真正可用的本地 skill。`

## 2. Feishu 平台与知识能力

### 任务画像

User wants Feishu official platform rules, auth flows, event subscriptions, knowledge capability calls, page reading, or table operations.

### 推荐 skill 组合

Primary: `ai-da-guan-jia -> feishu-open-platform`

Optional branches:

- add `feishu-bitable-bridge` for base or bitable writes
- add `feishu-reader` for page or wiki reading

### 何时用

- user asks about 飞书开放平台 rules or capabilities
- auth, scope, token, callback, manifest, release, knowledge APIs

### 何时不要用

- the request is only about reading a Feishu page
- the request is only about writing one bitable row and the platform rules are already known

### 默认顺序

1. `ai-da-guan-jia`
2. `feishu-open-platform`
3. optional specialized Feishu skill

### 最小验真目标

- official Feishu rule path identified
- correct app type assumption stated
- exact API / capability / scope path confirmed

### 常见误路由

- any prompt containing `飞书` goes straight to `feishu-bitable-bridge`

### 真实样例 prompt

`判断飞书知识问答能力的开放平台调用方式，并优先按官方资料完成验真。`

## 3. Yuanli / 知识星球发布闭环

### 任务画像

User wants to publish or close a content loop around Yuanli / 知识星球 / 原力内容系统 with low interruption.

### 推荐 skill 组合

Primary: `ai-da-guan-jia -> jiyao-youyao-haiyao`

Optional branches:

- add `yuanli-zsxq-coevolution-assistant` when the content system is already clear
- add `self-evolution-max` only when the task truly needs multiple explicit feedback rounds

### 何时用

- MVP publish loop
- low-interruption execution
- content package is mostly defined and the main problem is closing the loop

### 何时不要用

- the user is still defining the content strategy from scratch
- the task is a broad content evolution exercise rather than a concrete publish closure

### 默认顺序

1. `ai-da-guan-jia`
2. `jiyao-youyao-haiyao`
3. optional content-domain skill

### 最小验真目标

- publish target is explicit
- human-only boundary is explicit for final publish
- result is reported with actual closure evidence

### 常见误路由

- prompts containing `MVP`, `闭环`, or `复盘` get pulled into `self-evolution-max` even when only one closure pass is needed

### 真实样例 prompt

`用 yuanli-zsxq-coevolution-assistant 把已有 MVP 内容发到知识星球，完成一次发布闭环测试，尽量少打扰我。`

## 4. Skill 体系盘点与评估

### 任务画像

User wants a system-wide review of installed skills, a capability map, overlap analysis, or next-step evolution actions.

### 推荐 skill 组合

`ai-da-guan-jia -> ai-metacognitive-core`

### 何时用

- inventory all installed skills
- build a capability map
- assess duplication, gaps, or routing quality
- propose candidate evolution actions

### 何时不要用

- the user wants a new skill scaffold
- the user wants a multi-round implementation loop rather than one review pass

### 默认顺序

1. `ai-da-guan-jia`
2. `ai-metacognitive-core`

### 最小验真目标

- top-level skill count is correct
- `artifacts/**` are excluded
- review summary is structured
- exactly 3 candidate actions are produced

### 常见误路由

- because the prompt contains `skill`, route to `skill-creator`
- because the prompt contains `复盘`, route to `self-evolution-max`

### 真实样例 prompt

`请帮我盘点所有顶层 skill，做能力地图、去重评估，并给出 3 个后续动作。`

## 5. 陌生领域学习 / 说明书优先 / 对标学习

### 任务画像

User wants to learn an unfamiliar API, platform, tool, method, or workflow before execution, and explicitly values manuals, official docs, guides, best practices, or benchmark comparisons.

### 推荐 skill 组合

Primary: `ai-da-guan-jia -> guide-benchmark-learning`

Optional branches:

- add `openai-docs` for OpenAI product or API learning
- add `skill-trainer-recursive -> skill-creator` when the unfamiliar domain is being turned into a new skill

### 何时用

- user says to read the official docs first
- the domain is unfamiliar and execution risk is high
- the user wants benchmark guidance before coding or workflow design

### 何时不要用

- a stable local workflow already exists and the learning debt is clearly low
- the task is a narrow domain lookup already fully covered by a dedicated docs skill

### 默认顺序

1. `ai-da-guan-jia`
2. `guide-benchmark-learning`
3. optional domain docs or skill-training path

### 最小验真目标

- `source-map.json`
- `benchmark-grid.md`
- `learning-handbook.md`
- `execution-readiness.md`
- explicit split between source-of-truth rules and reference-only guidance

### 常见误路由

- start coding or executing only because examples exist
- jump straight to `skill-creator` before the unfamiliar domain is understood
- let community tips outrank official manuals

### 真实样例 prompt

`帮我学会一个陌生 API，先读官方说明书、最佳实践和攻略，再决定怎么实现。`

## 6. XHS IP 内容盘点与风格分析

### 任务画像

User wants to audit an existing XHS/小红书 account: list all notes, extract video oral transcripts, and analyze the IP's speaking style.

### 推荐 skill 组合

`ai-da-guan-jia -> opencli-platform-bridge -> get-biji-transcript`

### 何时用

- user wants to audit/analyze an XHS IP or creator account
- user needs video oral transcripts (口播逐字稿)
- user wants language style analysis (风格分析) of an XHS creator
- user wants to benchmark/compare multiple XHS accounts

### 何时不要用

- user wants to CREATE content for XHS (use `openclaw-xhs-coevolution-lab`)
- user only needs one specific note's transcript (use `get-biji-transcript` directly)
- user needs image-text note content only (use `opencli-platform-bridge` alone)

### 默认顺序

1. `ai-da-guan-jia` (route + situation map)
2. `opencli-platform-bridge` (CLI batch-list user notes, filter video type, structured JSON output)
3. `get-biji-transcript` (transcribe-link per video URL, output transcript .txt/.json)
4. LLM synthesis (read all transcripts, output style analysis report)

### 最小验真目标

- note list JSON with note_id, title, type, url, likes for all notes
- transcript .txt files for each video note
- style analysis report with quantified patterns (opening, closing, rhythm, vocabulary fingerprint)

### 常见误路由

- any prompt containing "小红书" blindly goes to `openclaw-xhs-coevolution-lab` (content creation, not reading)
- browser automation via Chrome MCP for XHS video notes (extremely slow, cannot extract audio transcripts)
- skipping `opencli-platform-bridge` and trying to scrape note list via curl (XHS is SPA, returns empty HTML)

### 真实样例 prompt

`帮我盘点小红书这个IP的账号和内容，提取所有视频口播逐字稿，分析他的语言风格。`

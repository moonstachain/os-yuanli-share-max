---
title: Sample Wiki Schema
type: schema
updated: 2026-04-24
audience: both
---

# Sample Wiki Schema （脱敏样例 · 学员可修改）

本文件是 Wiki 的**宪法**。LLM agent 在任何 Wiki 操作前必须先读它。

## 4-Layer Architecture

严格分层，职责不混。

### Layer 1 · Raw Sources （`sources/` + `artifacts/`）

- **只读**。LLM 只读不改。
- `sources/` 子目录：`articles/` / `papers/` / `books/` / `transcripts/`
- `artifacts/` 放自动化产物的只读 JSON 镜像（如果有）

每个 source 必须有 frontmatter：

```yaml
---
title: 原文标题
source_url: https://...
ingested: YYYY-MM-DD
tags: [topic1, topic2]
---
```

### Layer 2 · Wiki Pages （可写）

由 LLM 生成和维护。

**知识页**（研究与学习）：
- `entities/people/` — 人物档
- `entities/companies/` — 公司/机构档
- `entities/projects/` — 项目档
- `concepts/` — 概念/框架定义
- `comparisons/` — 横向对比
- `syntheses/` — 跨源综合

**运营页**（治理追踪，可选）：
- `operations/clones/` — 克隆档
- `operations/skills/` — skill 档
- `operations/runs/` — 任务运行记录
- `operations/digests/` — 日摘要
- `operations/decisions/` — 决策方案
- `operations/governance/` — 治理契约
- `operations/reports/` — 平台报告
- `operations/dashboards/` — 概览面板

每页 frontmatter：

```yaml
---
title: 页名
type: entity|concept|comparison|synthesis|clone|skill|run|digest|decision|governance|report|dashboard
sources: [source-file-1.md, source-file-2.md]
related: [[Other Page]]
created: YYYY-MM-DD
updated: YYYY-MM-DD
audience: human|ai|both
---
```

### Layer 3 · Human Insights （`insights/`）

- **人类专属**。LLM **永不修改**。
- 个人反思、决策、立场、判断。
- LLM 可读可引，但不写。

### Layer 4 · Metabolism （`_factory/` + `_staging/` + `_feedback/`）

- `_factory/` — LLM 内容工厂（生成中间态）
- `_staging/` — 待审核产物
- `_feedback/` — 反馈收集区

## 操作规则

1. **读**：任何 layer 都可读
2. **写**：仅 Layer 2 + Layer 4，且路径白名单：
   - `concepts/` `entities/` `syntheses/` `comparisons/` `operations/` `dashboards/` `_factory/` `_staging/`
3. **删**：Layer 2 可删，Layer 1/3 禁止
4. **重命名**：需同步 `_index.md`

## 新陈代谢引擎（可选）

`scripts/` 下放自动化脚本（例如日摘要、Wiki 校验、打标签）。
本样例 Wiki 不提供脚本实现，学员自己写或从作者 Wiki 拉。

## 学员的自定义空间

- 可改：任何目录名、任何 type 枚举
- **改完必须**：同步 `knowledge-liming` 和 `llm-wiki-operator` 里的目录白名单

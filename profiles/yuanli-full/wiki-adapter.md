---
title: Wiki Adapter · 参数化说明
version: 0.1.0
---

# Wiki Adapter

`yuanli-full` 档下，所有原本硬编码 `/Users/liming/Documents/LLM-Wiki/` 的 skill 都会被改写为 `$WIKI_ROOT`。

## 需要改写的 skill

- `knowledge-liming` — 跨项目只读通道
- `llm-wiki-operator` — Wiki 内部 CRUD
- `yuanli-knowledge` — 原力域路由
- `knowledge-orchestrator` — 多源编排

## 改写规则

| 原字面量 | 替换为 |
|---|---|
| `/Users/liming/Documents/LLM-Wiki/` | `$WIKI_ROOT/` |
| `/Users/liming/Documents/LLM-Wiki/_schema.md` | `${WIKI_SCHEMA:-$WIKI_ROOT/_schema.md}` |
| `/Users/liming/Documents/LLM-Wiki/_index.md` | `$WIKI_ROOT/_index.md` |
| `/Users/liming/Documents/LLM-Wiki/dashboards/metabolism-dashboard.md` | `$WIKI_ROOT/dashboards/metabolism-dashboard.md` |
| `/Users/liming/Documents/LLM-Wiki/scripts/close_task_hook.py` | `$WIKI_ROOT/scripts/close_task_hook.py`（opt-in） |
| `/Users/liming/Documents/LLM-Wiki/_bridge-log.jsonl` | `$WIKI_ROOT/_bridge-log.jsonl` |

## 由 install 脚本自动执行

```bash
# install-profile --profile yuanli-full 内部等价于：
find skills-satellite profiles/yuanli-full -type f \( -name "*.md" -o -name "*.py" -o -name "*.sh" \) \
  -exec sed -i.bak "s|/Users/liming/Documents/LLM-Wiki|$WIKI_ROOT|g" {} \;
```

## 学员自检

```bash
grep -r "/Users/liming" . --exclude-dir=.git
# 应无输出。如果有，说明某个 skill 漏了改写，提 issue。
```

## Wiki 宪法

样例 Wiki 的 `_schema.md`（见 `sample-wiki/_schema.md`）是从作者真实 Wiki 脱敏抽出的 4-layer 规则。
学员应在装完后**自己读一遍**，决定哪些 layer 和分类要保留、哪些重命名。

`_schema.md` 本身是可改的，但改完务必同步更新：
- `knowledge-liming` 里的"可写路径白名单"
- `llm-wiki-operator` 的目录扫描规则

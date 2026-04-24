# profile / yuanli-full

**目标**：把作者 liming 的「原力OS × 知识图谱 × 炼丹切角 × 管家」全栈给学员还原。
**还原度**：≈80%（剩余 20% 是作者私有 memory、token、飞书 bridge 实例等，不迁移）

## 装什么

基于 `lite` + 五组：

1. **原力五大域** — `yuanli-core` / `yuanli-knowledge` / `yuanli-status` / `yuanli-geo` / `yuanli-ontology-manager` / `yuanli-design-sys-prompt` / `yuanli-xiaoshitou` / `yuanli-zsxq-coevolution-assistant`
2. **知识层** — `knowledge-liming` / `knowledge-orchestrator` / `llm-wiki-operator`
3. **炼丹/切角** — `jiyao-youyao-haiyao` / `info-5l` / `brainstorming`
4. **AI 管家** — `ai-da-guan-jia` / `ai-da-guan-jia-prompt`
5. **反演产物** — `reverse-engineer-product` / `cursor-plan-todo-execute`

## 必须配置的环境变量

| 变量 | 含义 | 举例 |
|---|---|---|
| `WIKI_ROOT` | 学员自己的 Wiki 根目录绝对路径 | `/Users/alice/Documents/MyWiki` |
| `WIKI_SCHEMA` | Wiki 宪法文件（可选） | `$WIKI_ROOT/_schema.md` |

## 参数化 Wiki adapter

作者本机的路径 `/Users/liming/Documents/LLM-Wiki/` 已全部替换为 `$WIKI_ROOT`。

学员第一次装：

```bash
export WIKI_ROOT="$HOME/Documents/MyYuanliWiki"
bin/os-yuanli-install-profile --profile yuanli-full --materialize-sample-wiki
```

这会：
1. 把 `profiles/yuanli-full/sample-wiki/` 的 4-layer 骨架复制到 `$WIKI_ROOT`
2. 替换所有 skill 里的 `/Users/liming/Documents/LLM-Wiki/` 为 `$WIKI_ROOT`
3. 在 `~/.claude/CLAUDE.md` 注册 Knowledge Base Pointers 段（参考 `examples/claude-md.template`）

## 样例 Wiki 骨架

见 [sample-wiki/](./sample-wiki/)：
- `_schema.md` — Wiki 宪法（从作者 Wiki 抽出的脱敏版）
- `_index.md` — 入口索引
- `concepts/` `entities/` `syntheses/` `comparisons/` — Layer 2 示例
- `sources/` `artifacts/` `insights/` — Layer 1 示例（只读）
- `operations/` `dashboards/` `_factory/` — 其他 Layer 2
- `scripts/` — 新陈代谢脚本占位（learner 自己装）

## 不迁移的东西

- 作者个人 memory（`/Users/liming/.claude/projects/*/memory/`）
- 飞书 / 知识星球 / 小红书的私有 bridge 配置
- `close_task_hook.py` / `skill-bandit` 所需的本地数据库
- MCP token（需要学员自己重新授权）

## 验真

```bash
bin/os-yuanli-doctor --profile yuanli-full
```

应看到：
- ✅ `$WIKI_ROOT` 可达
- ✅ Wiki 4-layer 骨架存在
- ✅ 19 个 yuanli/knowledge 相关 skill 可达
- ⚠️ `close_task_hook.py` 未启用（预期，属 opt-in）

# Capability Matrix · 能力还原矩阵

> 本仓库是 `os-yuanli-skill-share` 的**增强版**，目标：让同事/学员 `git clone` 后**最大程度还原作者 liming 本机已连接的能力**。
>
> 但 100% 还原不可能，也不应该。本矩阵说清：**哪些能装、哪些选装、哪些不迁移**。

## 作者本机盘点（截至 2026-04-24）

| 层 | 数量 | 状态 |
|---|---|---|
| `~/.claude/skills/` | 169 个 skill | 见下表 |
| MCP server | ~15 个 | 部分需 token 授权 |
| Wiki `$WIKI_ROOT` | 593 concepts / 5700+ sources / 14 domains / 4-layer | 193MB |
| hooks | 3 个 Python hook | opt-in |
| agents | 1 个（code-reviewer） | 可迁移 |
| slash commands | 3 个 | 可迁移 |

## 169 skill 分家族一览

| 家族 | 数量 | profile 归属 | 迁移策略 |
|---|---|---:|---|
| `gstack-*` | 38 | engineer | `local:` source，学员需本机有 |
| `lark-*` | 20 | lark-ops | `local:` source |
| `yuanli-*` | 9 | yuanli-full | 核心身份 skill，做了参数化 |
| `ai-*` | 9 | content / yuanli-full | 混合 |
| `agency-*` | 8 | （未列入 profile） | 如需自己加 |
| `skill-*` | 6 | governance | 治理基础设施 |
| `feishu-*` | 5 | lark-ops | bridge 层 |
| `angle-*` | 5 | content | 切角系列 |
| `knowledge-*` | 2 | yuanli-full | 强耦合 Wiki |
| `jiyao-*` | 2 | lite (satellite) + yuanli-full | 炼丹核心 |
| 卫星 9 个（`skill-router` 等） | 9 | lite（嵌入仓库） | **本仓库完整拷贝** |
| 其他 | ~56 | 未列入 profile | 学员自己加 |

**合计归属**：lite 9 + engineer 17 + content 12 + yuanli-full 19 + governance 11 + lark-ops 25 = **93/169 ≈ 55%** 明确有家可归。

剩 ~76 个（包括 obsidian-*, writing-*, playwright, defuddle, n8n-*, playwright-interactive, conversation-archive, architecture-diagram 等）属于**工具型 skill**，不绑定 profile，学员按需从本机自己拉。

## profile 还原率对照表

| profile | 估计还原率 | 主要覆盖面 | 关键依赖 |
|---|---|---|---|
| `lite` | ~10% | 三层 gate + 验真 + 进化 | 无 |
| `engineer` | ~55% | 工程开发 + gstack 全链 | `gh` CLI |
| `content` | ~45% | 切角 + 内容引擎 + 文风 | 无 |
| `yuanli-full` | ~80% | 原力全生态 + Wiki + 炼丹 | `$WIKI_ROOT` |
| `governance` | ~35% | skill 孵化 + 审计 + 演化 | 无 |
| `lark-ops` | ~60% (在飞书维度) | 飞书 20 skill + 5 bridge | `FEISHU_APP_ID/SECRET` |

> 组合安装是推荐做法。比如 `yuanli-full + engineer + content` 可以叠加到 ~90%。

## 不迁移的东西（显式声明）

以下**永不**进入本仓库，即使 profile 覆盖到相关路径：

- 作者个人 memory（`~/.claude/projects/*/memory/*.md`）
- Wiki 全量实际内容（193MB，含隐私）
- 飞书 / 知识星球 / 小红书的**私有 bridge 实例**（`FEISHU_APP_ID` 等 token）
- MCP OAuth 授权 token
- `~/.claude/settings.json` 里的 env 段（含私密变量）
- 作者的个人 `CLAUDE.md`（含路径硬编码）

学员装完 profile 后，**必须自己**：

1. 在 `~/.claude/CLAUDE.md` 写自己的身份和知识库指针
2. `export WIKI_ROOT=...`（yuanli-full 档）
3. `export FEISHU_APP_ID=... SECRET=...`（lark-ops 档）
4. 授权所需的 MCP server

## 验真命令

```bash
bin/os-yuanli-doctor --profile <name>
```

会同时检查：
- 卫星 skill 可达
- external_skills 每个都能找到（或已被符号链接）
- env_required 全部已 export
- Wiki（yuanli-full）结构合法

## 本矩阵的更新节奏

作者本机 skill 数量每周在变（见 `profiles/yuanli-full/sample-wiki/operations/digests/` 样例）。
本矩阵的数字**截至 commit 时刻**。想看最新数字：跑作者本机的 `skill-bandit/scripts/list_active_skills.py`（需 opt-in hooks）。

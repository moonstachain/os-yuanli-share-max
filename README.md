# OS-原力 · MAX 版（share-max）

> **一套可迁移的「治理OS × 工作OS」** · **kernel + profile** 双层设计
> `git clone` → 按档位一键装 → 学员本机最大程度还原作者已连接的 169 skill 生态
> 是 [`os-yuanli-skill-share`](https://github.com/moonstachain/os-yuanli-skill-share) 的增强超集

[![validate](https://github.com/moonstachain/os-yuanli-share-max/actions/workflows/validate.yml/badge.svg)](https://github.com/moonstachain/os-yuanli-share-max/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 目录

- [这是什么](#这是什么)
- [谁适合看](#谁适合看)
- [⚡️ 5 分钟极速上手](#️-5-分钟极速上手)
- [前置条件](#前置条件)
- [🎚 决定装哪个 profile](#-决定装哪个-profile)
- [按档位部署](#按档位部署)
  - [lite · 最小可用](#-lite--最小可用)
  - [engineer · 软件开发栈](#-engineer--软件开发栈)
  - [content · 内容生产栈](#-content--内容生产栈)
  - [yuanli-full · 原力全生态 + Wiki](#-yuanli-full--原力全生态--wiki)
  - [governance · skill 治理栈](#-governance--skill-治理栈)
  - [lark-ops · 飞书中枢](#-lark-ops--飞书中枢)
- [🧪 验真（验收清单）](#-验真验收清单)
- [注册到 Claude Code / Codex](#注册到-claude-code--codex)
- [opt-in · 启用 hooks](#opt-in--启用-hooks)
- [🔧 故障排除](#-故障排除)
- [升级 & 卸载](#升级--卸载)
- [协议边界](#协议边界)
- [ROADMAP](#roadmap)
- [贡献 & 反馈](#贡献--反馈)
- [License](#license)

---

## 这是什么

`os-yuanli-share-max` 是**「原力OS」的运行骨架 + 能力生态打包**。

- **kernel**：`治理OS × 工作OS` 的方法协议（六判断 → 主题/策略/执行三层 gate → 验真 → 进化）
- **satellite**：kernel `invokes:` 的 9 个下游 skill，完整拷贝进仓库，学员开箱即用
- **profiles**：6 档可选能力包（lite / engineer / content / yuanli-full / governance / lark-ops）
- **CLI**：`os-yuanli-install-profile` 按档位一键装到 `~/.claude/skills/`

### 🆕 2026-04-24 更新：Harness Patterns 四层基建

从 [12 Agentic Harness Patterns (Claude Code)](https://generativeprogrammer.com/p/12-agentic-harness-patterns-from) 对标审计后落地的四个基础设施升级：

| 优先级 | 升级 | 说明 |
|---|---|---|
| **P0** | 确定性治理钩子 | 3 个 lifecycle hooks（`SessionStart` / `PostToolUse:Agent` / `Stop`）把治理检查从 prompt 层下沉到系统层 |
| **P1** | 上下文压缩协议 | 4 层信息衰减（锚点→决策→过程→噪声），长会话中治理链条不断裂 |
| **P2** | 权限分级 | 4 级子agent权限（`read-only` / `plan-only` / `full` / `guarded`），最小权限路由 |
| **P3** | 模式语言规范 | 每个 skill 用 `pattern_card`（problem / forces / solution / tradeoffs）标准描述 |

新增文件：`scripts/governance_checkpoint.py`、`scripts/evolution_capture.py`、`scripts/session_governance_init.py`、`references/context-compaction-protocol.md`、`references/pattern-card-spec.md`

---

与普通 share 版的差异：

| 维度 | `os-yuanli-skill-share` | `os-yuanli-share-max`（本仓库） |
|---|---|---|
| 身份 | 方法论 kernel 分享 | kernel + 能力生态 + profile 档位 |
| 参考文件 | 3 个 reference | 8 个 reference（含 audit-rubric / system-audit-playbook 等） |
| 协议文件 | 8 个 protocol | 8 个 protocol（同） |
| 模板 | 6 个 template | 6 个 template（同） |
| 卫星 skill | ❌ | ✅ 9 个完整拷贝 |
| profile 档位 | ❌ | ✅ 6 档 |
| Wiki adapter | ❌ | ✅ 参数化路径 + 样例 Wiki 骨架 |
| hooks 示例 | ❌ | ✅ opt-in 3 个 Python hook |
| 能力还原矩阵 | ❌ | ✅ [docs/capability-matrix.md](docs/capability-matrix.md) |
| 一键安装 CLI | ❌ | ✅ `os-yuanli-install-profile` |

---

## 谁适合看

- **Claude Code / Codex 用户**，想把"先判断再执行"作为默认接管方式
- **原力OS 内部同事 / 学员**，想快速还原 liming 本机的工作能力栈
- **AI 工作流研究者**，想拆解一套成型的「治理 × 工作」方法论

不适合：
- 只想要领域 skill（如单独 n8n、飞书）而不需要方法 kernel 的人 —— 可直接克隆对应专项仓库
- 完全没有 Claude Code / Codex 运行时 —— 可以把 `os-yuanli/SKILL.md` 当 system prompt 粘贴使用，但失去 CLI 便利

---

## ⚡️ 5 分钟极速上手

**目标**：跑通 `lite` 档，立刻就能在 Claude Code 里触发 `/os-yuanli`。

```bash
# 1. 克隆
git clone https://github.com/moonstachain/os-yuanli-share-max.git
cd os-yuanli-share-max

# 2. 环境自检
python3 bin/os-yuanli-doctor
# 期望：✅ 18 通过 / 0 警告 / 0 错误

# 3. 装可选依赖
pip install -r requirements.txt

# 4. 装最小档（干跑先预览）
python3 bin/os-yuanli-install-profile --profile lite --dry-run
python3 bin/os-yuanli-install-profile --profile lite

# 5. 在 Claude Code / Codex 会话里输入 `/os-yuanli` 即可触发
```

接下来可能想：
- 深入装某个 profile → 跳到 [按档位部署](#按档位部署)
- 验证装成功没 → 跳到 [验真](#-验真验收清单)
- 出问题了 → 跳到 [故障排除](#-故障排除)

---

## 前置条件

| 必需 | 版本 | 检查命令 |
|---|---|---|
| **Python** | ≥ 3.9 | `python3 --version` |
| **git** | ≥ 2.30 | `git --version` |
| **PyYAML** | 任意 | `python3 -c "import yaml"` |

| 按档可选 | 何时需要 | 安装提示 |
|---|---|---|
| `gh` CLI | engineer 档（gstack-ship/canary 依赖） | `brew install gh` / `sudo apt install gh` |
| `jq` | 调试 MCP / JSON 配置 | `brew install jq` |
| **Claude Code** | 要自动触发 skill 的运行时 | [claude.ai/download](https://claude.ai/download) |
| **Codex CLI** | 备选运行时 | OpenAI Codex CLI |

**平台兼容性**：

| 平台 | 状态 | 说明 |
|---|---|---|
| macOS 12+ | ✅ 全测 | 作者日常开发环境 |
| Ubuntu 22.04+ | ✅ CI 验证 | GitHub Actions ubuntu-latest 跑通 |
| WSL2 (Ubuntu) | ✅ 理论支持 | Python 路径可能需手动调 |
| Windows 原生 | ⚠️ 未测 | CLI 用 `python` 而非 `python3`；建议用 WSL |

---

## 🎚 决定装哪个 profile

一张决策树：

```
你想用 os-yuanli 主要做什么？
├─ 先跑通方法协议，不碰生态 ─────────────→ lite
├─ 写代码 / 重构 / CR / 部署 ─────────────→ lite + engineer
├─ 写公众号 / 小红书 / 短视频脚本 ────────→ lite + content
├─ 跑整套原力OS + 知识图谱 ───────────────→ lite + yuanli-full  ⚠ 需 $WIKI_ROOT
├─ 做 skill 设计 / 基础设施 / 审计 ───────→ lite + governance
├─ 以飞书为运营中枢 ──────────────────────→ lite + lark-ops    ⚠ 需飞书 app
└─ 全都要（≈ 90% 还原作者本机）───────────→ lite + engineer + content + yuanli-full
```

每档还原率和依赖详见 [docs/capability-matrix.md](docs/capability-matrix.md)、[docs/profiles.md](docs/profiles.md)。

profile 可以**叠加安装**（后装不会覆盖已装）：

```bash
python3 bin/os-yuanli-install-profile --profile lite
python3 bin/os-yuanli-install-profile --profile engineer
python3 bin/os-yuanli-install-profile --profile content
```

---

## 按档位部署

### 🟢 lite · 最小可用

**还原率**：~10% | **依赖**：无 | **耗时**：< 30 秒

装的东西：
- `os-yuanli` kernel（SKILL + 8 references + 8 protocols + 6 templates）
- 9 个卫星 skill：`skill-router` / `evidence-gate` / `intent-grounding` / `closure-evolution` / `jiyao-youyao-haiyao-zaiyao` / `content-quality-gate` / `evolution-log` / `routing-playbook` / `strategy-governor`

```bash
# 干跑预览
python3 bin/os-yuanli-install-profile --profile lite --dry-run

# 正式装
python3 bin/os-yuanli-install-profile --profile lite

# 验真
python3 bin/os-yuanli-doctor
ls ~/.claude/skills/os-yuanli
```

期望输出：
```
· 安装 profile: lite (version 0.1.0)
· 还原度估计：~10%
✓ kernel → /Users/you/.claude/skills/os-yuanli
✓ satellite skill-router → /Users/you/.claude/skills/skill-router
... (其余 8 个)
✓ 安装完成。下一步：bin/os-yuanli-doctor 自检
```

---

### 🔵 engineer · 软件开发栈

**还原率**：~55% | **依赖**：`gh` 已登录 | **耗时**：~1 分钟

装 lite + 17 个工程 skill（gstack 全链、TDD、系统调试、架构图、git worktrees、CR 协作等）。

详见 [profiles/engineer/README.md](profiles/engineer/README.md)。

```bash
# 检查 gh 已登录
gh auth status

# 装
python3 bin/os-yuanli-install-profile --profile engineer

# 验真：每个 gstack-* 都应已存在
ls ~/.claude/skills/gstack*
```

**⚠️ 注意**：本档的 `external_skills` 当前指向 `local:~/.claude/skills/gstack` 等。
如果你**不是作者本机**、也没事先装过这些 skill，安装会打印警告而不中断。
解决方法两种：
1. 自己从上游仓库克隆这些 skill 到 `~/.claude/skills/`
2. 在 `profiles/engineer/profile.yaml` 里把 `source:` 改成 `git+https://...`（PR 欢迎）

---

### 🟣 content · 内容生产栈

**还原率**：~45% | **依赖**：无 | **耗时**：~30 秒

装 lite + 切角 5 件套 + 内容引擎 + 文风门 + 跨平台分发，共 12 个外部 skill。

详见 [profiles/content/README.md](profiles/content/README.md)。

```bash
python3 bin/os-yuanli-install-profile --profile content

# 验真：切角 5 件套 + 爆文引擎
ls ~/.claude/skills/angle-* ~/.claude/skills/ai-viral-content-engine
```

`content-quality-gate`（随 lite 装好）会在 `full mode` 的 Publish Pack 步骤自动拦截"还没到洞察层"的稿子。

---

### 🟡 yuanli-full · 原力全生态 + Wiki

**还原率**：~80% | **依赖**：`$WIKI_ROOT` 已设置 | **耗时**：~2 分钟

装 lite + 原力五域 + 知识层（knowledge-liming / llm-wiki-operator / knowledge-orchestrator）+ 炼丹/切角 + AI 管家 + 反演产物，共 18 个外部 skill + 一份样例 Wiki 骨架。

**两步走：**

**Step 1 · 设置 Wiki 路径**

```bash
# 选择你自己的 Wiki 位置（示例）
export WIKI_ROOT="$HOME/Documents/MyYuanliWiki"

# 建议写入 shell profile 持久化
echo 'export WIKI_ROOT="$HOME/Documents/MyYuanliWiki"' >> ~/.zshrc
source ~/.zshrc
```

**Step 2 · 装 + 落地样例 Wiki**

```bash
python3 bin/os-yuanli-install-profile \
  --profile yuanli-full \
  --materialize-sample-wiki
```

这会：
1. 把 kernel + 9 卫星装到 `~/.claude/skills/`
2. symlink 18 个原力相关 skill
3. 把 [profiles/yuanli-full/sample-wiki/](profiles/yuanli-full/sample-wiki/) 的 4-layer 骨架复制到 `$WIKI_ROOT`
4. 把所有 skill 里的 `/Users/liming/Documents/LLM-Wiki/` 替换为你的 `$WIKI_ROOT`

**Step 3 · 在 `~/.claude/CLAUDE.md` 注册 Knowledge Base Pointers**

把下面段落追加到 `~/.claude/CLAUDE.md`（没有就新建）：

```markdown
## Knowledge Base Pointers

**Primary wiki**: `${WIKI_ROOT}`

| 资源 | 路径 |
|---|---|
| Entry 目录索引 | `${WIKI_ROOT}/_index.md` |
| Constitution 宪法 | `${WIKI_ROOT}/_schema.md` |

## Default Retrieval Skill

On any non-trivial task, invoke `/knowledge-liming "<topic>"` first
to fetch relevant Wiki context before acting.
```

详见 [profiles/yuanli-full/README.md](profiles/yuanli-full/README.md) 和 [profiles/yuanli-full/wiki-adapter.md](profiles/yuanli-full/wiki-adapter.md)。

---

### 🔴 governance · skill 治理栈

**还原率**：~35% | **依赖**：无 | **耗时**：~30 秒

装 lite + 11 个 skill 治理工具（skill-creator / skill-audit / skill-bandit / skill-trainer-recursive / wiki-lint 等）。

详见 [profiles/governance/README.md](profiles/governance/README.md)。

```bash
python3 bin/os-yuanli-install-profile --profile governance
```

和 `engineer` 的关系：
- `engineer` 让你**写业务代码**
- `governance` 让你**写"让业务代码被写出来的基础设施"**
- 两档可并存

---

### 🟠 lark-ops · 飞书中枢

**还原率**：~60%（飞书维度）| **依赖**：飞书 app 凭证 | **耗时**：~1 分钟

装 lite + 飞书家族 20 skill + 5 个 feishu bridge。

**Step 1 · 准备飞书自建应用**

1. 登录 [开发者后台](https://open.feishu.cn)
2. 创建企业自建应用，记下 `app_id` 和 `app_secret`
3. 开通需要的 API 权限（文档 / 多维表 / 消息等，按需）

**Step 2 · 注入凭证**

```bash
# 方法 A: 环境变量（快但重启丢）
export FEISHU_APP_ID=cli_xxxxxxxx
export FEISHU_APP_SECRET=xxxxx

# 方法 B: macOS Keychain（推荐，不落盘明文）
security add-generic-password -a "$USER" -s FEISHU_APP_SECRET -w
# 然后运行脚本前用：
export FEISHU_APP_SECRET=$(security find-generic-password -a "$USER" -s FEISHU_APP_SECRET -w)

# 方法 C: 1Password CLI / Vault 等密管工具
```

**Step 3 · 装**

```bash
python3 bin/os-yuanli-install-profile --profile lark-ops

# 验真
ls ~/.claude/skills/lark-*  # 应列出 20 个
ls ~/.claude/skills/feishu-* # 应列出 5 个
```

详见 [profiles/lark-ops/README.md](profiles/lark-ops/README.md)。

---

## 🧪 验真（验收清单）

**每次装完都跑**：

### 1. doctor · 仓库文件完整性

```bash
python3 bin/os-yuanli-doctor
```

期望：
```
总结：18 通过 / 0 警告 / 0 错误
```

### 2. audit · 协议合规

```bash
python3 bin/os-yuanli-audit
```

期望：
```
── os-yuanli-audit ──
  ✅ 全部通过
```

### 3. golden-path · 集成测试

```bash
bash tests/golden-path.sh
```

期望末行：
```
── golden-path PASS ──
```

### 4. 装机态检查（✨ 建议做这一步）

```bash
# kernel 到位？
test -f ~/.claude/skills/os-yuanli/SKILL.md && echo "✓ kernel"

# 9 个卫星都到位？
for s in skill-router evidence-gate intent-grounding closure-evolution \
         jiyao-youyao-haiyao-zaiyao content-quality-gate evolution-log \
         routing-playbook strategy-governor; do
  test -d ~/.claude/skills/$s && echo "✓ $s" || echo "✗ $s 缺失"
done
```

### 5. Claude Code / Codex 触发测试

在 Claude Code 会话里：

```
/os-yuanli 帮我审一下这段 Python 代码
```

应看到：
- ✅ 输出"六判断 preamble"
- ✅ 判定任务族（此处应为 `研究审计` 或 `软件开发`）
- ✅ 进入主题/策略 gate

如果没触发 → 去 [故障排除](#-故障排除) 查 `skill 未被发现`。

---

## 注册到 Claude Code / Codex

`install-profile` 已经把 kernel 放到 `~/.claude/skills/os-yuanli/`。Claude Code 默认会扫这个目录，无需额外注册。

**Codex CLI** 学员：

```bash
# 方法 A: symlink
ln -s ~/.claude/skills/os-yuanli ~/.codex/skills/os-yuanli

# 方法 B: 复制
cp -r ~/.claude/skills/os-yuanli ~/.codex/skills/
```

入口由 [os-yuanli/agents/openai.yaml](os-yuanli/agents/openai.yaml) 自动注册，`display_name` 为 `OS-原力`。

**纯手工 / 其他 LLM**：把 [os-yuanli/SKILL.md](os-yuanli/SKILL.md) 当 system prompt 粘贴到任意对话里即可。

---

## opt-in · 启用 hooks

作者本机有 3 个 `~/.claude/settings.json` hook：

1. **`PostToolUse · Edit|Write|MultiEdit`** → `close_task_hook.py`（Wiki 任务自动收尾）
2. **`PostToolUse · Skill`** → `log_invocation.py`（skill-bandit 记录调用）
3. **`UserPromptSubmit`** → `detect_rollback.py`（检测用户回滚）

**默认不装**。要开：

```bash
# 1. 拷贝脚本
cp examples/hooks/*.py ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.py

# 2. 合并 examples/hooks/settings.hooks.json.example 里的 hooks 段到 ~/.claude/settings.json
# （用 jq 或手动编辑）

# 3. 重启 Claude Code
```

⚠️ 注意：
- `close_task_hook.py` 依赖 `$WIKI_ROOT`，只在装了 `yuanli-full` 档时才有意义
- hooks 每次 Edit/Write/Skill/UserPromptSubmit 都会执行。写挂了会拖慢整个 Claude Code

详见 [examples/hooks/README.md](examples/hooks/README.md)。

---

## 🔧 故障排除

### ❓ `python3 bin/os-yuanli-doctor` 报 `ModuleNotFoundError: No module named 'yaml'`

```bash
pip install -r requirements.txt
# 或
pip install pyyaml
```

### ❓ `install-profile` 打印大量 `external XXX 本机未找到`

预期行为 —— 你不是作者本机，那些 `local:~/.claude/skills/*` 的 skill 确实不存在。

不中断，只警告。要消除警告：

1. 从各自的上游仓库克隆到 `~/.claude/skills/`
2. 或改 `profiles/<name>/profile.yaml` 里的 `source:` 为 `git+https://...`
3. 或接受警告 —— lite + 卫星 skill 仍可正常工作

### ❓ Claude Code 里触发 `/os-yuanli` 没反应

检查顺序：

```bash
# 1. kernel 是否在 Claude 扫描路径
ls ~/.claude/skills/os-yuanli/SKILL.md

# 2. SKILL.md frontmatter 是否完整
head -10 ~/.claude/skills/os-yuanli/SKILL.md

# 3. 重启 Claude Code（完全退出，不是重新开对话）
```

还不行 → 发 issue，附上 `python3 bin/os-yuanli-doctor` 输出。

### ❓ macOS 提示 `zsh: bad CPU type in executable`

你可能在 Apple Silicon 装了 x86 Python。检查：

```bash
python3 -c "import platform; print(platform.machine())"
# 应输出 arm64（Apple Silicon）或 x86_64（Intel）
```

不对就重装对应架构的 Python（建议用 Homebrew）。

### ❓ `yuanli-full` 档装完 `knowledge-liming` 找不到 Wiki

```bash
echo $WIKI_ROOT                              # 应非空
ls $WIKI_ROOT/_schema.md                     # 应存在
grep -r "/Users/liming" ~/.claude/skills/knowledge-liming/  # 应无输出
```

最后一条有输出 → 路径替换没完成，重装：

```bash
python3 bin/os-yuanli-install-profile --profile yuanli-full --force
```

### ❓ `lark-ops` 档报"飞书 token 错误"

依次检查：
1. `app_secret` 是否用了测试版而非生产版
2. 自建应用是否已发布（草稿态不可用）
3. 所需 API 权限是否已开通
4. 企业可用范围是否包含当前用户

### ❓ CI（GitHub Actions）跑失败

在你 fork 的仓库里：
1. `Settings` → `Actions` → `General` → 确认 Actions 已启用
2. 检查 workflow 文件是否存在于 `.github/workflows/validate.yml`
3. 查看 Actions 页面的错误日志

---

## 升级 & 卸载

### 升级

```bash
cd /path/to/os-yuanli-share-max
git pull origin main

# 覆盖式重装（保留你自己加的 skill）
python3 bin/os-yuanli-install-profile --profile lite --force
```

### 卸载某档（保留其他档）

目前 `install-profile` 不提供 `--uninstall`。手动删：

```bash
# 只删 kernel（最安全，卫星 skill 保留）
rm -rf ~/.claude/skills/os-yuanli

# 全删 lite 档（kernel + 9 卫星）
rm -rf ~/.claude/skills/{os-yuanli,skill-router,evidence-gate,intent-grounding,\
closure-evolution,jiyao-youyao-haiyao-zaiyao,content-quality-gate,\
evolution-log,routing-playbook,strategy-governor}
```

### 彻底清理

```bash
# 小心：这会删除所有用 install-profile 装过的 skill
# 强烈建议先 backup
cp -r ~/.claude/skills ~/.claude/skills.bak.$(date +%Y%m%d)

rm -rf ~/.claude/skills
```

---

## 协议边界

这是**方法 + 配套卫星 + profile 档位**，**不是**学员本机的完整备份。

以下**永不**进入仓库，即使 profile 涉及：

- 作者个人 memory（`~/.claude/projects/*/memory/`）
- Wiki 全量实际内容（193MB，含隐私）
- 飞书 / 知识星球 / 小红书的**私有 bridge 实例 token**
- MCP OAuth 授权 token
- `~/.claude/settings.json` 里的 env 私密变量

学员装完 profile 后**必须自己做**：
1. 在 `~/.claude/CLAUDE.md` 写自己的身份和知识库指针
2. `export WIKI_ROOT=...`（yuanli-full 档）
3. `export FEISHU_APP_ID=... SECRET=...`（lark-ops 档）
4. 授权所需的 MCP server

每档具体还原率见 [docs/capability-matrix.md](docs/capability-matrix.md)。

---

## 目录结构

```
os-yuanli-share-max/
├── .github/workflows/
│   └── validate.yml              # CI：doctor + audit + golden-path + 6 profile dry-run
├── os-yuanli/                    # kernel
│   ├── SKILL.md                  # 主入口（Claude Code 自动识别）
│   ├── agents/openai.yaml        # Codex 入口
│   ├── references/               # 8 个 reference（含本仓库独有 5 个）
│   ├── protocols/                # 8 个 protocol
│   ├── templates/                # 6 个实例化模板
│   └── scripts/
├── skills-satellite/             # 9 个卫星 skill（完整拷贝）
├── profiles/                     # 6 档位 manifests
│   ├── lite/                     # 最小可用
│   ├── engineer/                 # 软件开发
│   ├── content/                  # 内容生产
│   ├── yuanli-full/              # 原力全生态
│   │   ├── wiki-adapter.md
│   │   └── sample-wiki/          # 4-layer Wiki 骨架
│   ├── governance/               # skill 治理
│   └── lark-ops/                 # 飞书中枢
├── bin/
│   ├── os-yuanli-doctor          # 环境自检
│   ├── os-yuanli-init            # 交互式向导
│   ├── os-yuanli-audit           # repo 合规审计
│   └── os-yuanli-install-profile # 按档位装 skill（本仓库独有）
├── docs/
│   ├── quickstart.md
│   ├── concepts.md
│   ├── adapter-guide.md
│   ├── faq.md
│   ├── capability-matrix.md      # 诚实标注各档还原率
│   ├── profiles.md               # profile 使用指南
│   └── enable-ci.md              # CI 启用说明
├── examples/
│   ├── minimal-setup/
│   ├── team-engineer-setup/
│   ├── hay-setup/
│   └── hooks/                    # opt-in Python hooks
├── tests/
│   └── golden-path.sh            # 集成测试
├── requirements.txt
├── ROADMAP.md
└── README.md                     # 本文件
```

---

## ROADMAP

见 [ROADMAP.md](ROADMAP.md)。主要里程碑：

- **v0.1**（当前）：kernel + 9 卫星 + 6 profile + Wiki adapter + CI
- **v0.2**（计划）：真实工作流案例脱敏入库、`install-profile` 支持 `git+` 批量拉取
- **v0.3**：跨 profile 组合验真、CI 覆盖 6 档 × 3 组合
- **v1.0**：学员 onboarding 视频、可迁移度自动评分

---

## 贡献 & 反馈

### 提 Issue

遇到 bug / 想要新 profile / 想加新 skill 进某档：

👉 https://github.com/moonstachain/os-yuanli-share-max/issues

请附：
- 操作系统 + Python 版本
- `python3 bin/os-yuanli-doctor` 输出
- 复现步骤

### 发 PR

**欢迎的 PR**：
- 把 `local:~/.claude/skills/X` 的 source 改成 `git+https://...` 公开地址
- 新增 profile 档位（示例见 `profiles/lite/profile.yaml`）
- 文档修订、i18n、故障排除补充
- CI 增强

**PR 前请跑**：

```bash
python3 bin/os-yuanli-doctor
python3 bin/os-yuanli-audit
bash tests/golden-path.sh
python3 bin/os-yuanli-install-profile --profile lite --dry-run
```

四条都通过再 push。

### 反馈哲学

本仓库的方法论沉淀遵循：
- **先判断，再执行**
- **完成前验真，完成后进化**
- **不做 100% 还原的承诺**（见 [docs/capability-matrix.md](docs/capability-matrix.md)）

PR 触及 kernel 行为变更时请同步更新 `os-yuanli/references/constitution.md`。

---

## License

[MIT](LICENSE) · 方法论思想来自作者「原力OS」实践沉淀

作者：[@moonstachain](https://github.com/moonstachain)

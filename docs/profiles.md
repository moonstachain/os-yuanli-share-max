# Profiles Guide

## 什么是 profile

Profile = 一组 skill 清单 + 必要环境变量 + 装机脚本。

六档开箱即用：

| profile | 用户画像 | 一句话 |
|---|---|---|
| `lite` | 任何人第一次装 | 只要三层 gate + 9 个卫星，不碰生态 |
| `engineer` | 写代码的 | lite + gstack 全链 + TDD + 工程治理 |
| `content` | 搞内容的 | lite + 切角 + 爆文引擎 + 文风门 |
| `yuanli-full` | 要跑原力OS全栈 | lite + 原力五域 + Wiki + 知识图谱 |
| `governance` | 做基础设施 / skill 设计 | lite + skill-creator + skill-audit + 演化 |
| `lark-ops` | 飞书中枢运营 | lite + 飞书 20 skill + 5 bridge |

## 选谁

- 不确定 → 装 `lite`。先跑通三层 gate，再按需升级。
- 程序员 → `lite + engineer`
- 知识工作者 → `lite + yuanli-full`（准备 `$WIKI_ROOT`）
- 创作者 → `lite + content`
- 平台/运营 → `lite + lark-ops`（准备飞书 app）
- 大杂烩 → `lite + engineer + content + yuanli-full`（≈90% 还原作者本机）

## 安装

```bash
# 最小
bin/os-yuanli-install-profile --profile lite

# 工程 + 原力全
bin/os-yuanli-install-profile --profile engineer
bin/os-yuanli-install-profile --profile yuanli-full --materialize-sample-wiki

# 干跑检查
bin/os-yuanli-install-profile --profile yuanli-full --dry-run
```

## extends 机制

每个 profile 的 `profile.yaml` 可以 `extends: lite`（或其他档位）。
install 脚本会递归合并 `external_skills` 列表，避免重复声明。

```yaml
# profiles/engineer/profile.yaml
extends: lite
external_skills:
  - name: gstack
    source: local:~/.claude/skills/gstack
  - ...
```

## source 语法

`external_skills[*].source` 当前支持两种：

| 前缀 | 含义 | 示例 |
|---|---|---|
| `local:<path>` | 符号链到学员本机已有 skill | `local:~/.claude/skills/gstack` |
| `git+<url>` | `git clone` 到 `~/.claude/skills/<name>/` | `git+https://github.com/moonstachain/skill-router.git` |

**当前作者 profile 大量使用 `local:`**——因为这些 skill 还没独立发仓。欢迎 PR 换成 `git+` 版本。

## 自己加一档

1. 拷 `profiles/lite/profile.yaml` 成 `profiles/myprofile/profile.yaml`
2. 改 `name` + `extends`
3. 列出要装的 `external_skills`
4. 在 `profiles/myprofile/README.md` 说清楚目标用户

跑 `bin/os-yuanli-audit --profile myprofile` 验证合规。

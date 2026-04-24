# profile / engineer

**目标**：把 OS-原力 kernel + 作者本机的工程能力栈装到学员的环境。

## 装什么

基于 `lite` + 以下三组：

1. **gstack 家族**（计划 → 审查 → 交付 → 灰度 → 回顾的全链路）
   - `gstack` / `gstack-autoplan` / `gstack-ship` / `gstack-canary` / `gstack-review` / `gstack-retro`
2. **工程辅助**
   - `auto-dev` / `architecture-diagram` / `test-driven-development` / `systematic-debugging`
3. **协作与验真**
   - `using-git-worktrees` / `executing-plans` / `writing-plans` / `receiving-code-review` / `requesting-code-review` / `dispatching-parallel-agents` / `verification-before-completion`

## 依赖

- `gh` CLI 已登录（`gstack-ship`、`gstack-canary` 使用）
- `git` ≥ 2.40
- 无 Wiki 依赖

## 一键安装

```bash
bin/os-yuanli-install-profile --profile engineer
```

## 注意

本 profile 的 `external_skills` 当前指向 `local:~/.claude/skills/*`。
如果你**不是本仓库作者**，这些 skill 需要先存在于你本机 `~/.claude/skills/`，
或者将 `source:` 换成公开仓库 URL（PR 欢迎）。

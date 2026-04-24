# Roadmap · os-yuanli-share-max

本仓库是 `os-yuanli-skill-share` 的**增强版（MAX）**。

## v0.1 · 初版（本次）

- [x] 合并 `os-yuanli-skill-share` v1.0（kernel / protocols / templates / bin / docs / examples / tests）
- [x] 补齐本机独有 5 个 reference：`audit-rubric` / `integration-boundaries` / `routing-bridges` / `system-audit-playbook` / `system-audit-feishu-loop`
- [x] SKILL.md 采用本机版（含 `invokes:` 声明 + 系统审计入口段）
- [x] 嵌入 9 个卫星 skill（`skills-satellite/`）
- [x] 6 档 profile（`lite` / `engineer` / `content` / `yuanli-full` / `governance` / `lark-ops`）
- [x] `os-yuanli-install-profile` CLI
- [x] Wiki adapter + 样例 Wiki 骨架（`yuanli-full` 档）
- [x] opt-in hooks 示例（3 个 Python hook）
- [x] `capability-matrix.md` 诚实标注还原率

## v0.2 · 真实工作流沉淀

- [ ] 把作者实际跑过的 3-5 个 full-mode 案例脱敏后放 `examples/real-cases/`
- [ ] `install-profile` 支持 `source: git+` 批量拉取
- [ ] 把卫星 skill 里的 `closure-evolution` / `evidence-gate` 增强版同步进来
- [ ] `os-yuanli-doctor --profile <name>` 细化到"每个 external_skill 可达性检查"

## v0.3 · 跨 profile 组合验真

- [ ] 支持 `install-profile --profile engineer --profile content`（多档并行）
- [ ] Golden path 测试覆盖 6 档 + 3 个组合
- [ ] CI：GitHub Actions 在 PR 时自动跑 doctor + audit + golden-path

## v1.0 · 稳定版

- [ ] 完整的学员 onboarding 视频 / 图文教程
- [ ] profile 作者签名机制（可选）
- [ ] 可迁移度自动评分：跑完后给出"你的装机态 vs 作者本机"的 6 轴分

## 不做的事

与上游 `os-yuanli-skill-share` 一致 —— **以下永不进入仓库**，即使有 profile 涉及：

- 作者个人 memory（`~/.claude/projects/*/memory/`）
- Wiki 全量内容（193MB + 隐私）
- 飞书/知识星球/小红书私有 bridge 实例 token
- MCP OAuth token
- `~/.claude/settings.json` 里的 env 私密变量
- 任何写死作者身份的 prompt 或文案

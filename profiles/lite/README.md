# profile / lite

**目标**：30 秒可用，0 外部依赖。

## 装什么

- `os-yuanli` kernel（SKILL + 8 references + 8 protocols + 6 templates）
- 9 个卫星 skill（`skill-router` / `evidence-gate` / `intent-grounding` / `closure-evolution` / `jiyao-youyao-haiyao-zaiyao` / `content-quality-gate` / `evolution-log` / `routing-playbook` / `strategy-governor`）

## 不装什么

- `gstack-*` / `lark-*` / `yuanli-*` / `angle-*` / `knowledge-*` / `llm-wiki-operator`
- Wiki / MCP 配置 / hooks

## 一键安装

```bash
bin/os-yuanli-install-profile --profile lite
```

## 验真

```bash
bin/os-yuanli-doctor --profile lite
```

应看到：
- ✅ kernel 文件完整
- ✅ 9 个卫星 skill 可达
- ⚠️ 未装 engineer/content/yuanli-full 档（预期）

# Hooks · opt-in 示例

作者本机 `~/.claude/settings.json` 启用了 3 个 hook：

1. **PostToolUse · Edit|Write|MultiEdit** → `close_task_hook.py`
   用途：每次写完文件触发一次"任务自动收尾"检查（Wiki 配套功能）

2. **PostToolUse · Skill** → `skill-bandit/log_invocation.py`
   用途：记录每次 Skill 调用，供 skill-bandit 做 A/B 评估和漂移检测

3. **UserPromptSubmit** → `skill-bandit/detect_rollback.py`
   用途：检测"刚才的 skill 路由是不是被用户回滚了"，帮 skill-bandit 学习

## 安装方式（opt-in）

默认不启用。如果要开，三步：

### 1. 拷贝脚本到你自己的位置

```bash
cp examples/hooks/*.py ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.py
```

### 2. 合并 hook 配置到 settings.json

把 `examples/hooks/settings.hooks.json.example` 的 `hooks` 段合并到你的 `~/.claude/settings.json`。
注意：`path_to_script` 替换成你实际的路径。

### 3. 准备 skill-bandit 后端（可选）

`log_invocation.py` 默认把调用写到 `~/.claude/skill-bandit/invocations.sqlite`。
不想装数据库？可以把脚本改成 append 到 JSONL。

## 警告

- 这些脚本**会在每次 Edit/Write/Skill/UserPromptSubmit 时执行**。写挂了会拖慢整个 Claude Code。
- 作者的原版脚本有 `try/except` 包住、失败静默。直接删除或改动前请先 dry-run。
- `close_task_hook.py` 需要 Wiki 存在（依赖 `$WIKI_ROOT`）。不用 `yuanli-full` profile 就别开它。

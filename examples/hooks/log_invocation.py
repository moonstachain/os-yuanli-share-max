#!/usr/bin/env python3
"""skill-bandit · log_invocation.py （示例版）

作者本机版本 at /Users/liming/.claude/skills/skill-bandit/scripts/log_invocation.py
本文件是**脱敏骨架**，把复杂依赖剥掉，只保留「每次 Skill 调用 append 一条 JSONL」。

放在 PostToolUse · matcher=Skill。
Claude Code 会在每次 Skill 工具调用后把事件 JSON 通过 stdin 传进来。
"""
import json
import os
import sys
from datetime import datetime
from pathlib import Path

LOG_PATH = Path(os.path.expanduser("~/.claude/skill-bandit/invocations.jsonl"))


def main() -> int:
    try:
        event = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        event = {"raw": sys.stdin.read()}

    record = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "tool_name": event.get("tool_name"),
        "tool_input": event.get("tool_input"),
    }

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # 永不阻塞主流程

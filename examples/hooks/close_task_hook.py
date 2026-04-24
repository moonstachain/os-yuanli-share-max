#!/usr/bin/env python3
"""Wiki · close_task_hook.py （示例骨架）

作者本机版本 at $WIKI_ROOT/scripts/close_task_hook.py
放在 PostToolUse · matcher=Edit|Write|MultiEdit。

真实版做的事（摘要）：
- 每次写文件后扫描 $WIKI_ROOT/_factory/ 里的"待收尾"任务
- 把满足完成条件的任务挪到 $WIKI_ROOT/operations/runs/YYYY-MM-DD/
- 在 _digest-log.jsonl 里加一条

本示例只做日志记录，不执行真正的收尾逻辑。
学员想要真正的自动化，需要自己在 Wiki 里补脚本。
"""
import json
import os
import sys
from datetime import datetime
from pathlib import Path

WIKI_ROOT = os.environ.get("WIKI_ROOT")
if not WIKI_ROOT:
    sys.exit(0)  # 没配 Wiki 就什么都不做

LOG_PATH = Path(WIKI_ROOT) / "_bridge-log.jsonl"


def main() -> int:
    try:
        event = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        event = {}

    file_path = (event.get("tool_input") or {}).get("file_path", "")

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "ts": datetime.utcnow().isoformat() + "Z",
            "hook": "close_task_hook",
            "file": file_path,
            "note": "skeleton only — 把真逻辑写这里",
        }, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)

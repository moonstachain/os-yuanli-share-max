#!/usr/bin/env python3
"""skill-bandit · detect_rollback.py （示例骨架）

在 UserPromptSubmit 钩子上跑，尝试从用户这轮的 prompt 判断：
是不是在回滚刚才 agent 选的 skill 路由？

检测规则（非常轻量版）：
- 用户 prompt 含 "不是这个" / "改回" / "别用" / "stop using" / "rollback" / "换个 skill"
  → 记一条 rollback 事件到 jsonl

真实版本有更精细的语义匹配、skill 名提取、A/B 评分回灌。
"""
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

LOG_PATH = Path(os.path.expanduser("~/.claude/skill-bandit/rollbacks.jsonl"))
SIGNALS = [
    r"不是这个",
    r"改回",
    r"别用",
    r"stop using",
    r"rollback",
    r"换个 ?skill",
    r"wrong skill",
]


def main() -> int:
    text = sys.stdin.read()
    try:
        event = json.loads(text or "{}")
        prompt = event.get("prompt", "")
    except json.JSONDecodeError:
        prompt = text

    hit = next((s for s in SIGNALS if re.search(s, prompt, flags=re.IGNORECASE)), None)
    if not hit:
        return 0

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "ts": datetime.utcnow().isoformat() + "Z",
            "signal": hit,
            "prompt_excerpt": prompt[:200],
        }, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)

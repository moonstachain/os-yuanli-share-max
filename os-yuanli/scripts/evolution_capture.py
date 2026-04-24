#!/usr/bin/env python3
"""
进化价值捕获提醒 — PostToolUse(Agent) hook
当子 agent 完成时，提醒主 agent 捕获可复用的进化价值。
"""

import sys


def main():
    try:
        print("🔄 子agent已完成 — 检查是否有可复用的进化价值需要沉淀")
    except Exception:
        pass  # 静默失败，不阻塞用户


if __name__ == "__main__":
    main()

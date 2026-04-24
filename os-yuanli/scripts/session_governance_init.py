#!/usr/bin/env python3
"""
会话治理线初始化 — SessionStart hook
在会话启动时输出治理线锚点，确保三条治理线始终存在于上下文中。
"""

import sys


def main():
    try:
        print("原力OS 治理线已激活：递归进化 | 全局最优 | 人类友好")
    except Exception:
        pass  # 静默失败，不阻塞用户


if __name__ == "__main__":
    main()

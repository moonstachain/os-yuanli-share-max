#!/usr/bin/env python3
"""
原力OS 治理检查点 — Stop hook
当 agent 准备结束回复时，如果当前任务涉及 os-yuanli，注入治理检查提醒。

Claude Code hooks 通过 stdin 传入 JSON 上下文。
"""

import json
import sys


YUANLI_SIGNALS = [
    "os-yuanli", "yuanli", "原力", "治理线",
    "递归进化", "全局最优", "人类友好",
    "六判断", "主题层", "策略层",
]


def is_yuanli_context():
    """从 stdin JSON 中判断当前会话是否涉及 os-yuanli。"""
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return False
        data = json.loads(raw)
        # Claude Code Stop hook 的 stdin 包含 transcript / tool_input 等字段
        # 将整个 JSON 转为字符串做关键词匹配（兼容不同版本的 stdin 格式）
        haystack = json.dumps(data, ensure_ascii=False).lower()
        for signal in YUANLI_SIGNALS:
            if signal in haystack:
                return True
    except Exception:
        return False
    return False


def main():
    try:
        if is_yuanli_context():
            print(
                "⚡ 原力OS 治理检查点\n"
                "□ 验真：结果是否有证据支撑？\n"
                "□ 进化：本轮是否产出了可复用价值？\n"
                "□ 全局最优：这一步是推动整体还是只优化局部？"
            )
    except Exception:
        pass  # 静默失败，不阻塞用户


if __name__ == "__main__":
    main()

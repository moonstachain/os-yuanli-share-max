---
name: evolution-log
description: 当用户要看进化日志、最近里程碑或历史演进时使用。读取进化编年史并输出最近五轮，不做新写入。
metadata:
  openclaw:
    emoji: "🧬"
    skillKey: "evolution-log"
---

# Evolution Log

## 触发
- `进化日志`
- `最近进化了什么`
- `里程碑`
- `/evolution-log`

## 工作流
1. 读取进化编年史。
2. 只取最近 5 轮。
3. 标出已解决与未解决部分。
4. 保持历史，不改历史。

## 输出契约
- 版本 / 轮次
- 解决项
- 未解决项
- 最近趋势

## 边界
- 只读。
- 不生成新的闭环记录。

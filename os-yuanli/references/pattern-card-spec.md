# Pattern Card 规范

> 原力OS 的模式语言规范。每个 skill 本质上是一个"命名的模式"——
> 识别重复决策 → 命名为模式 → 用标准格式描述。
> 本规范定义 `pattern_card` 字段，使这一结构显式化。

---

## 1. 字段定义

```yaml
pattern_card:
  category: "记忆与上下文 | 工作流与编排 | 工具与权限 | 治理与进化"
  problem: "什么重复出现的决策或痛点催生了这个 skill？（一句话）"
  forces:
    - "力量A vs 力量B（体现矛盾，不是问题列表）"
    - "力量C vs 力量D"
  solution: "这个 skill 用什么核心机制解决问题？（一句话）"
  tradeoffs:
    - "采用这个方案后放弃了什么？承受了什么成本？"
  known_uses:
    - "在原力OS生态中，这个模式的已知实例"
  related_patterns:
    - "与哪些其他 skill/模式有结构性关系？"
```

### 字段约束

| 字段 | 必填 | 数量 | 要求 |
|---|---|---|---|
| `category` | 是 | 1 | 从四类中选一 |
| `problem` | 是 | 1 句 | 一句话，不能写成小作文 |
| `forces` | 是 | 2–4 条 | 必须体现矛盾（X vs Y），不是问题列表 |
| `solution` | 是 | 1 句 | 一句话，点明核心机制 |
| `tradeoffs` | 是 | ≥1 条 | 必须诚实承认代价 |
| `known_uses` | 推荐 | 不限 | 生态中的已知实例 |
| `related_patterns` | 推荐 | 不限 | 结构性关系，非泛泛列举 |

---

## 2. 分类体系

借鉴 Bilgin Ibryam 12 Harness Patterns 的四类划分，适配原力OS：

| 类别 | 管理什么 | 典型 skill |
|---|---|---|
| **记忆与上下文** | agent 知道什么 | knowledge-liming, llm-wiki-operator |
| **工作流与编排** | agent 怎么做事 | skill-router, os-yuanli, intent-grounding |
| **工具与权限** | agent 能做什么 | evidence-gate, feishu-bitable-bridge |
| **治理与进化** | agent 该不该做 | closure-evolution, strategy-governor |

---

## 3. 与已有模式语言的对齐

```
K8s Patterns        : Problem → Forces → Solution → Consequences
Prompt Patterns      : Pattern Name → Problem → Solution → Example
原力OS pattern_card : problem → forces → solution → tradeoffs → known_uses → related_patterns
```

- `problem` 对齐 K8s 的 Problem、Prompt Patterns 的 Problem
- `forces` 对齐 K8s 的 Forces（原力OS 要求显式写矛盾对）
- `solution` 对齐 K8s 的 Solution
- `tradeoffs` 对齐 K8s 的 Consequences（原力OS 侧重代价而非中性后果）
- `known_uses` 和 `related_patterns` 是 GoF 模式语言的经典字段，K8s/Prompt Patterns 省略了但原力OS 保留

---

## 4. 使用方式

### 写在哪里

`pattern_card` 写在 SKILL.md 的 frontmatter 中，作为 YAML 字段：

```yaml
---
name: my-skill
description: "Use when..."
pattern_card:
  category: "工作流与编排"
  problem: "..."
  forces:
    - "..."
  solution: "..."
  tradeoffs:
    - "..."
---
```

### 性质

`pattern_card` 是**描述性**的（帮助 agent 和人理解这个 skill 是什么模式），不是**执行性**的（不改变 skill 的运行逻辑）。

### 谁消费它

- **skill-router**：用 `pattern_card.problem` 匹配当前任务，判断哪个 skill 最合适
- **closure-evolution**：用 `pattern_card.forces` 判断新发现的模式是否值得固化为 skill
- **人类**：快速理解一个 skill 解决什么问题、付出什么代价

### 渐进式添加

不强制所有 skill 立即添加 pattern_card。采用渐进策略：

1. 核心 skill 先添加（见下方示范）
2. 其他 skill 在下次修改时补充
3. 新建 skill 时推荐同步编写

---

## 5. 示范 Pattern Cards

以下 5 个核心 skill 的完整 pattern_card，可直接嵌入各自 SKILL.md 的 frontmatter。

### 5.1 os-yuanli

```yaml
pattern_card:
  category: "治理与进化"
  problem: "任务直接跳入执行，没有经过'值不值得做'和'怎么赢'的判断"
  forces:
    - "执行速度 vs 决策质量"
    - "局部最优 vs 全局最优"
  solution: "三层 gate（主题→策略→执行）+ 三条治理线（递归进化/全局最优/人类友好）"
  tradeoffs:
    - "轻任务会显得流程过重"
    - "gate 本身消耗 token"
  known_uses:
    - "所有通过原力OS执行的任务入口"
    - "system-audit-playbook 作为特化实例"
  related_patterns:
    - "intent-grounding（主题层的需求压实）"
    - "skill-router（执行层的路径选择）"
    - "evidence-gate（验真层的独立验证）"
```

### 5.2 skill-router

```yaml
pattern_card:
  category: "工作流与编排"
  problem: "多条执行路径存在时，agent 倾向于跳到最熟悉的而非最合适的"
  forces:
    - "路径熟悉度 vs 路径适合度"
    - "探索成本 vs 局部最优风险"
  solution: "按成本递增排序候选路径，选最小可行集"
  tradeoffs:
    - "路由判断本身消耗一轮"
    - "可能低估不熟悉路径的价值"
  known_uses:
    - "os-yuanli 执行层的路径分发"
    - "yuanli-knowledge 的多域路由"
  related_patterns:
    - "os-yuanli（调用 skill-router 做执行层路由）"
    - "intent-grounding（路由前的需求澄清）"
    - "skill-bandit（探索-利用的另一种策略）"
```

### 5.3 evidence-gate

```yaml
pattern_card:
  category: "工具与权限"
  problem: "agent 自报'完成了'但实际结果不可靠"
  forces:
    - "完成速度 vs 完成质量"
    - "agent 自信 vs 真实证据"
  solution: "独立于执行的验证层，检查 artifact 存在 + 目标匹配 + 结果回读"
  tradeoffs:
    - "增加一轮验证延迟"
    - "某些任务难以客观验证"
  known_uses:
    - "os-yuanli 验真步骤"
    - "gstack-qa 的产出物校验"
  related_patterns:
    - "os-yuanli（evidence-gate 是其验真层）"
    - "intent-grounding（验证需要回溯原始意图）"
    - "content-quality-gate（内容领域的特化验证）"
```

### 5.4 closure-evolution

```yaml
pattern_card:
  category: "治理与进化"
  problem: "有价值的执行经验散落在对话中，不被沉淀"
  forces:
    - "沉淀所有 vs 精选沉淀"
    - "进化速度 vs skill 膨胀风险"
  solution: "选择性提升——只有重复出现的模式才值得固化为 skill/protocol"
  tradeoffs:
    - "可能漏掉一次性但有价值的洞察"
    - "升级判断本身需要经验积累"
  known_uses:
    - "os-yuanli 进化步骤"
    - "auto-skill-extraction-sqlite 的自动提取"
    - "skill-creator 的手动创建"
  related_patterns:
    - "os-yuanli（closure-evolution 是其进化层）"
    - "self-evolution-max（更激进的自我进化策略）"
    - "skill-audit（进化后的质量审计）"
```

### 5.5 intent-grounding

```yaml
pattern_card:
  category: "工作流与编排"
  problem: "模糊请求导致执行偏离真实目标"
  forces:
    - "立即执行的效率 vs 理解正确的保障"
    - "用户耐心 vs 需求准确度"
  solution: "将模糊请求压缩为：目标/成功标准/产出物/约束/非目标"
  tradeoffs:
    - "清晰请求不需要压实，额外一轮是浪费"
    - "压实本身可能引入 agent 的假设"
  known_uses:
    - "os-yuanli 主题层的需求压实"
    - "task-spec 的任务规格书生成"
  related_patterns:
    - "os-yuanli（intent-grounding 是其主题层）"
    - "skill-router（压实后的路径选择）"
    - "evidence-gate（压实产出的成功标准供验真使用）"
```

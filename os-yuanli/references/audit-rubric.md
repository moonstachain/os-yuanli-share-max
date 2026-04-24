# OS-原力审计评分标准

## 目标

This rubric turns `原力OS` from a qualitative lens into a repeatable scoring system.

Use it for:

- system audits
- skill maturity reviews
- runtime and workflow audits
- representative sample scoring

## 总公式

`6 轴 × 10 分 = 原力OS评分模型`

The six axes are:

1. `主题层`
2. `策略层`
3. `执行层`
4. `递归进化`
5. `全局最优`
6. `人类友好`

Each axis contains `5` checkpoints.

Each checkpoint uses:

- `2 分 = 已形成`
- `1 分 = 部分形成`
- `0 分 = 缺口`

Axis score range:

- `0-10`

System or subsystem total:

- average the six axis scores
- keep one decimal place

## 等级带

- `9.0-10.0 = A`
- `8.0-8.9 = B+`
- `7.0-7.9 = B`
- `6.0-6.9 = C+`
- `5.0-5.9 = C`
- `<5.0 = D`

## Reporting Rules

Every scored axis must explain:

1. `怎么得来的`
2. `扣在哪儿`
3. `证据是什么`
4. `下一步怎么改`

Do not report a naked score.

## Axis Checkpoints

### 1. 主题层

| 检查点 | 2 分 | 1 分 | 0 分 |
| --- | --- | --- | --- |
| 目标清晰 | audit object and objective are explicit | partial objective exists but still blurred | no stable object or objective |
| 优先级成立 | the theme clearly deserves entry now | it may deserve entry but priority is weak | no case for entry |
| 边界清楚 | in/out of scope are explicit | edges exist but leak | everything is mixed together |
| 长期价值 | the work compounds into long-term capability | some value compounds, some is one-off | mostly one-off output |
| 停止条件 | stop rules are explicit and respected | stop rules exist but are soft | no stop condition |

### 2. 策略层

| 检查点 | 2 分 | 1 分 | 0 分 |
| --- | --- | --- | --- |
| 层级定位 | current level is explicitly named | the strategy exists but level is fuzzy | no strategy level awareness |
| 核心矛盾 | core contradiction is explicit | some tension is visible but not distilled | only surface activity is described |
| 备选比较 | meaningful alternatives were compared | alternatives were mentioned but not weighed | no alternatives considered |
| 路径合理 | route matches objective and constraints | route is plausible but not well defended | route is ad hoc |
| 风险边界 | risks and failure modes are explicit | some risks are visible but incomplete | no risk boundary |

### 3. 执行层

| 检查点 | 2 分 | 1 分 | 0 分 |
| --- | --- | --- | --- |
| 链路存在 | execution chain is explicit and stable | chain exists but has gaps | execution is improvised |
| 责任清楚 | owners or execution roles are clear | roles exist but blur in places | nobody clearly owns the flow |
| 产物存在 | concrete artifacts are produced | some artifacts exist but not the full set | output is mostly claims |
| 验真明确 | verification target and evidence are explicit | some verification exists but is partial | no real verification path |
| 闭环清楚 | closure state and next step are clear | partial closure exists | task ends in ambiguity |

### 4. 递归进化

| 检查点 | 2 分 | 1 分 | 0 分 |
| --- | --- | --- | --- |
| 复盘存在 | reflection is explicit and preserved | reflection exists but is weak | no reflection |
| 写回系统 | learnings are written back into rules, skills, or docs | some writeback exists | no writeback |
| 重复错误减少 | repeated failures are visibly reduced | reduction is partial or unclear | the same gaps repeat unchanged |
| 升级落点清楚 | upgrade destination is explicit | destination exists but is fuzzy | no clear place for learning to go |
| 下一轮动作明确 | concrete next action is named | next action is vague | no next action |

### 5. 全局最优

| 检查点 | 2 分 | 1 分 | 0 分 |
| --- | --- | --- | --- |
| 考虑替代方案 | alternatives are seriously weighed | alternatives are lightly considered | first path wins by default |
| 复用优先 | reuse beats from-zero work | some reuse exists | from-zero behavior dominates |
| 层级不混乱 | theme, strategy, and execution stay distinct | some layer confusion remains | layers are mixed |
| 资源投入合理 | time, compute, and human effort are proportionate | cost is acceptable but not sharp | cost is obviously wasteful |
| 跨系统 leverage 存在 | the work uses leverage across skills, runtimes, or assets | some leverage exists | the work stays isolated |

### 6. 人类友好

| 检查点 | 2 分 | 1 分 | 0 分 |
| --- | --- | --- | --- |
| 少打扰 | human checkpoints are minimal and meaningful | some avoidable interruption remains | the human is dragged into routine work |
| 少重做 | structure prevents obvious rework | some rework still leaks through | rework dominates the flow |
| 少耗算 | compute and search are restrained | cost is acceptable but not sharp | compute waste is obvious |
| 少隐性复杂度 | rollback, review, and coordination cost stay low | complexity is manageable but sticky | hidden complexity dominates |
| 最终输出可用 | output is directly usable by the human | output is usable after cleanup | output is mostly intermediate noise |

## Scoring Workflow

Use this order:

1. define the audit object
2. collect canonical evidence
3. score all 30 checkpoints
4. subtotal each axis
5. average the six axes
6. assign grade band
7. explain deductions and improvement path

## Non-Goals

- Do not turn the rubric into a giant inventory spreadsheet by default.
- Do not score from impression alone.
- Do not let one strong artifact hide structural gaps.

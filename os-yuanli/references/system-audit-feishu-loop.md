# 系统审计 Feishu 递归闭环

Use this reference when the user wants:

- 系统审计落到飞书多维表
- 审计结果进入长期运营底座
- 外部 benchmark 成为固定输入
- 审计结果进入递归复审队列

## Canonical Truth Order

Keep this order hard:

1. `本地 canonical audit artifacts`
2. `外部 benchmark 层`
3. `Feishu mirror / collaboration surface`

Do not let Feishu replace local truth.

## Default Structure

When this loop is requested, the operating stack is:

- `os-yuanli`
  - owns score model, deductions, recursion rules
- repo sync script
  - builds the table payloads
  - merges external benchmark scores
  - writes recursion queue rows
- `feishu-bitable-bridge`
  - owns schema sync and idempotent upsert

`os-yuanli` should not copy bridge implementation details into the root prompt.

## Default Weights

Use:

- `内部成熟度 = 70%`
- `外部对标分 = 30%`

If an object has no valid external benchmark evidence:

- do not let its `全局最优` claim look complete
- open an explicit external benchmark gap
- place it into the `递归队列`

## Default Cadence

- `日更`
  - internal evidence
  - scorecards
  - deduction ledger
  - action status
- `周更`
  - external benchmark refresh
  - mapping refresh
  - composite score recompute
  - recursion queue refresh

## Output Expectations

When a system audit lands in Feishu, keep these public objects explicit:

- `System Scorecard`
- `Subsystem Scorecards`
- `Deduction Ledger`
- `External Intel`
- `Benchmark Links`
- `Recursion Queue`

## Boundary Rule

If the user asks for strategy or governance only, do not jump into Feishu sync.

Only enter this loop when:

- the audit object is already defined
- the score model is fixed
- the user explicitly wants the audit system to become operational

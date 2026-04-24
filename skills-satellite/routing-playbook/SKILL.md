---
name: routing-playbook
description: Use when AI大管家 or the user needs a stable mid-layer routing handbook that maps recurring task types to the smallest sufficient skill combinations, explains why the combination is preferred, and clarifies nearby boundary conflicts. Trigger for requests about routing playbooks, task-to-skill mapping, skill combination guidance, or choosing the right local skill chain for high-frequency workflows.
---

# Routing Playbook

Use this skill as a mid-layer routing handbook.

It does not replace `AI大管家` as the top-level governor.
It does not replace downstream skills as executors.
It exists to make repeated routing decisions stable, explainable, and cheaper.

## Data Sources

- **Genome-validated templates** — auto-generated co-selection patterns from Skill Genome analysis. Located at `../ai-da-guan-jia/artifacts/ai-da-guan-jia/skill-genome/routing-templates.json`. These templates carry empirical evidence (co-selection counts, success rates, source runs) and should be checked before falling back to manual playbook entries.

## Workflow

1. Check `routing-templates.json` for a genome-validated template matching the task keywords. If a match exists with `success_rate >= 0.8`, prefer it over manual playbook entries.
2. Classify the task into one of the covered playbook families.
3. Read [references/task-playbooks.md](references/task-playbooks.md) for the recommended combination.
4. Read [references/boundary-matrix.md](references/boundary-matrix.md) if the task sits near a known overlap.
5. Use [references/routing-rubric.md](references/routing-rubric.md) to explain why this combination is better than adjacent options.
6. Return:
   - the recommended skill chain
   - why this chain is the smallest sufficient one
   - the minimum verification target
   - the most likely misroute to avoid

## Covered Families

- skill creation and skill training
- Feishu platform and knowledge capability work
- Yuanli / 知识星球 publishing closure
- skill inventory review and system evaluation
- unfamiliar-domain learning with manuals, official docs, guides, and benchmark cases

If the task is outside these families, fall back to `AI大管家` core routing instead of stretching this playbook.

## Output Contract

For each routing answer, include:

- `任务画像`
- `推荐 skill 组合`
- `默认顺序`
- `最小验真目标`
- `不要误走的相邻路径`

Keep the answer concise.

## References

- [references/task-playbooks.md](references/task-playbooks.md)
- [references/routing-rubric.md](references/routing-rubric.md)
- [references/boundary-matrix.md](references/boundary-matrix.md)
- [Genome routing templates](../ai-da-guan-jia/artifacts/ai-da-guan-jia/skill-genome/routing-templates.json)

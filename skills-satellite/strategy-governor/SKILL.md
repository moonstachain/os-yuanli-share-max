# Strategy Governor

Maintain the strategic operating system for AI大管家. Turn the skill universe from a loose toolbox into a governed system with strategic goals, registries, thread programs, and initiative tracking.

## Trigger

Invoke this skill when the user says any of:

- "战略盘点" / "刷新战略" / "战略刷新"
- "strategy refresh" / "strategy review" / "initiative status"
- "治理仪表盘" / "governance dashboard"
- "刷新治理状态" / "refresh governance"
- "看看战略全景" / "战略全景"
- Any request to review, refresh, or update the strategic governance layer

Do NOT invoke for narrow single-skill questions or thread-level task execution.

## Input

The governor consumes these sources:

1. **Strategic Goals** - `artifacts/ai-da-guan-jia/strategy/current/strategic-goals.json`
2. **Theme / Strategy / Experiment / Workflow Registries** - same directory
3. **Canonical Thread Registry** - `canonical-thread-registry.json` (dispositions, wave assignments, blockers)
4. **Initiative Registry** - `initiative-registry.json` (I-GOV-001, I-AUTO-001, I-INC-001, I-CLONE-001)
5. **Active Threads** - `active-threads.json` (runtime session tracking)
6. **Skill Inventory** - core-roster.md, routing-credit.json
7. **Clone Portfolio** - `artifacts/ai-da-guan-jia/clones/current/` (clone scorecards, promotion queue)
8. **Recent Evolution Runs** - evolution log entries from prior sessions

## Output

All output is written to `artifacts/ai-da-guan-jia/strategy/current/`:

| File | Purpose |
|---|---|
| `governance-dashboard.md` | Human-readable strategic state panorama |
| `proposal-queue.json` | Pending proposals (thread, clone-promotion, skill-recruitment) |
| `skill-gap-report.json` | Missing or under-hardened skills vs. strategy needs |
| `initiative-registry.json` | Initiative status with gap assessment |
| `strategic-goals.json` | Goal definitions and alignment mappings |
| `strategy-map.json` | Goal -> theme -> strategy -> experiment -> workflow graph |
| `theme-registry.json` | Fixed v1 seed themes (only 3 themes in this phase) |
| `strategy-registry.json` | Strategy slots with validation status |
| `experiment-registry.json` | Experiment verdicts and scopes |
| `workflow-registry.json` | Only rows whose linked strategy is `validated` |
| `canonical-thread-registry.json` | Thread -> disposition -> goal -> theme -> strategy mapping |
| `active-threads.json` | Runtime thread tracking |
| `agent-scorecard.json` | Agent performance metrics |
| `clone-scorecard.json` | Clone portfolio status |
| `routing-credit.json` | Skill routing credit ledger |
| `autonomy-tier.json` | Per-agent autonomy levels |
| `cbm-mapping-view.json` | CBM component mapping (read-only reference) |
| `cbm-mapping-view.md` | CBM absorption status and missing bindings |
| `org-taxonomy.md` | Organizational taxonomy |
| `governance-penalty-rules.md` | Penalty enforcement rules |
| `promotion-demotion-policy.md` | Clone and skill promotion/demotion rules |
| `strategic-proposal.md` | Current strategic proposal drafts |

## Procedure

1. Navigate to the ai-da-guan-jia project root:
   ```bash
   cd "${AI_DA_GUAN_JIA_ROOT:-$HOME/.claude/skills/ai-da-guan-jia}"
   ```

2. Run the strategy-governor command:
   ```bash
   python3 scripts/ai_da_guan_jia.py strategy-governor
   ```

3. Review the generated `governance-dashboard.md` for correctness.

4. If the command reports errors or missing inputs, surface them to the user with specific remediation steps.

5. Present a summary of key changes:
   - Initiative status changes
   - New proposals in queue
   - Skill gaps identified
   - Thread disposition changes
   - Clone portfolio movements

## Governance Rules

### Frontstage Cap
- Maximum **3 frontstage threads** at any time
- The benchmark thread (`原力OS：宰相制度的萌芽`) stays outside the working load count

### Autonomy Level
- Default: **建议 + 待批** (propose + await approval)
- The strategic layer may propose new threads, initiatives, and skill recruitment
- It must NOT silently execute high-impact expansion work
- All proposals go to `proposal-queue.json` with status `pending_approval`

### Registry Freeze Rules
- `theme-registry.json` only keeps the fixed v1 seed themes (3 themes)
- `theme-human-ai-coevolution` is the only `active` theme in this phase
- Frontstage focus override can differ from registry-active theme
- `workflow-registry.json` may only contain rows whose linked strategy is already `validated`
- Governance mainline closure strategies stay frozen at `strategy + experiment + verdict`; they do not emit workflows yet

### Dual-Axis View
- `goal_id` tracks governance alignment (G1, G2, G3)
- `theme / strategy / experiment / workflow` track production position
- Both axes must be present in every registry entry

### CBM Mapping
- `cbm-mapping-view.json` is read-only
- `cbm-mapping-view.md` must name both absorbed structure and still-missing runtime bindings
- Do not claim full CBM adoption when execute rows lack action/writeback coverage

## Integration

### Reads From
- Evolution runs (evolution log entries)
- Skill inventory (core-roster.md, routing-credit.json)
- Clone factory artifacts (`artifacts/ai-da-guan-jia/clones/current/`)
- Active thread sessions

### Writes To
- `artifacts/ai-da-guan-jia/strategy/current/` (all output files listed above)

### Consumed By
- Governance dashboard viewers (human review)
- Initiative tracking (I-AUTO-001, I-GOV-001, I-INC-001, I-CLONE-001)
- Skill routing decisions (routing-credit.json feeds skill-router)
- Clone promotion pipeline (proposal-queue.json)

## Allowed Dispositions

Threads in `canonical-thread-registry.json` use these dispositions:
- `frontstage_now` - actively worked (max 3)
- `background_merge_queue` - completed but awaiting merge
- `waiting_human_boundary` - blocked on human action
- `deferred_after_narrowing` - scope too broad, needs narrowing
- `candidate_pool` - future candidates

## Wave Ordering

- `wave_0_remap` - canonical remap, ensure unique owners
- `wave_1_frontstage` - serial frontstage execution
- `wave_2_closure_only` - near-complete items only
- `wave_3_cleanup` - merge / background / defer cleanup

# User Input Protocol

Use this as the default intake protocol when the user wants work done and should not need to remember skill names.

## Preferred user input shape

Ask for or infer these fields in this order:

1. `目标系统`
   - examples: `Dify`, `Feishu`, `GitHub`, `Notion`, `YouQuant`, `browser`, `local repo`
2. `最终产物`
   - examples: `方案`, `代码`, `DSL`, `部署`, `排障`, `同步`, `逐字稿`, `报告`
3. `是否允许动真实环境`
   - `只分析`
   - `可改测试环境`
   - `可改生产环境`
4. `现成资产`
   - links
   - repo path
   - app URL
   - doc URL
   - instance ID
5. `成功标准`
   - observable outcome, not vague intent

## Default routing stance

- The user does not need to name the skill.
- Route from business goal and environment first.
- Prefer the smallest capable set of skills.
- Only ask for confirmation when route conflict changes real-world risk.

## Good prompt examples

- `目标系统是 Dify，我要一个客服分诊工作流，产物是 DSL + 部署方案，先不要动真实环境。`
- `目标系统是 Feishu，这里有一个 doc 链接，帮我读完并导出结构化摘要。`
- `目标系统是 GitHub + Feishu，我要把仓库 inventory 同步到多维表，允许你改测试环境。`
- `目标系统是浏览器，我要你帮我在这个后台页面跑一遍提交流程。`

## If the user is vague

Compress the ambiguity into these minimum clarifiers:

- `系统是什么`
- `你最终要我产出什么`
- `能不能动真实环境`

## Anti-patterns

- Do not force the user to learn 100+ skill names.
- Do not begin with long skill catalogs.
- Do not ask for technical fields the route can infer from links, repos, or files.
- Do not expose internal routing complexity unless it changes authorization or risk.

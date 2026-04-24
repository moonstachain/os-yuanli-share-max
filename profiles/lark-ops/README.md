# profile / lark-ops

**目标**：把飞书 20 skill 家族 + 5 个 feishu-bridge 装给以飞书为中枢的学员。

## 装什么

基于 `lite` +：

- **基础 skill**（20 个）：`lark-base` / `lark-sheets` / `lark-doc` / `lark-wiki` / `lark-drive` / `lark-mail` / `lark-calendar` / `lark-event` / `lark-task` / `lark-im` / `lark-vc` / `lark-minutes` / `lark-approval` / `lark-contact` / `lark-shared` / `lark-whiteboard`
- **OpenAPI 层**：`lark-openapi-explorer` / `lark-skill-maker`
- **workflow 封装**：`lark-workflow-meeting-summary` / `lark-workflow-standup-report`
- **bridge**（5 个）：`feishu-bitable-bridge` / `feishu-dashboard-automator` / `feishu-km` / `feishu-open-platform` / `feishu-reader`

## 必须配置

| 变量 | 含义 |
|---|---|
| `FEISHU_APP_ID` | 飞书自建应用 app_id |
| `FEISHU_APP_SECRET` | 应用 secret（建议用 keychain / 1Password CLI，不放明文） |

## 一键安装

```bash
export FEISHU_APP_ID=cli_xxxxxxxx
export FEISHU_APP_SECRET=xxxxx
bin/os-yuanli-install-profile --profile lark-ops
```

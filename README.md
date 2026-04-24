# OS-原力 · MAX 版（share-max）

> **一套可迁移的「治理OS × 工作OS」** —— **kernel + profile** 双层设计。
> 是 [`os-yuanli-skill-share`](https://github.com/moonstachain/os-yuanli-skill-share) 的超集版本：
> **同事/学员 `git clone` 后，能按 profile 档位最大程度还原作者本机已连接的能力。**

## 与普通 share 版的区别

| 维度 | `os-yuanli-skill-share` | `os-yuanli-share-max`（本仓库） |
|---|---|---|
| 身份 | 方法论 kernel 分享 | kernel + 能力生态 + profile 档位 |
| 参考文件 | 3 个 reference | 8 个 reference（含 audit-rubric / system-audit-playbook 等） |
| 协议文件 | 8 个 protocol | 8 个 protocol（同） |
| 模板 | 6 个 template | 6 个 template（同） |
| 卫星 skill | ❌ | ✅ 9 个完整拷贝（kernel `invokes:` 的下游 skill） |
| profile 档位 | ❌ | ✅ 6 档（lite / engineer / content / yuanli-full / governance / lark-ops） |
| Wiki adapter | ❌ | ✅ 参数化路径 + 样例 Wiki 骨架 |
| hooks 示例 | ❌ | ✅ opt-in 3 个 Python hook |
| 能力还原矩阵 | ❌ | ✅ `docs/capability-matrix.md` |

## 30 秒上手

```bash
git clone https://github.com/moonstachain/os-yuanli-share-max.git
cd os-yuanli-share-max
pip install -r requirements.txt
bin/os-yuanli-doctor
bin/os-yuanli-install-profile --profile lite
```

## 选个档

读 [docs/profiles.md](docs/profiles.md) 决定装哪档。快速建议：

- 先跑通三层 gate → `lite`
- 写代码 → `lite + engineer`
- 搞内容 → `lite + content`
- 跑原力全栈 → `lite + yuanli-full`（需 `$WIKI_ROOT`）
- 做治理/skill 设计 → `lite + governance`
- 飞书中枢 → `lite + lark-ops`（需飞书 app 凭证）

## 目录

```
os-yuanli-share-max/
├── os-yuanli/                    # kernel: SKILL + 8 ref + 8 protocol + 6 template
├── skills-satellite/             # 9 个卫星 skill（完整拷贝）
├── profiles/                     # 6 档位 manifests
│   ├── lite/
│   ├── engineer/
│   ├── content/
│   ├── yuanli-full/              # 含 wiki-adapter.md + sample-wiki/
│   ├── governance/
│   └── lark-ops/
├── bin/
│   ├── os-yuanli-doctor          # 环境自检
│   ├── os-yuanli-init            # 交互式向导
│   ├── os-yuanli-audit           # repo 合规审计
│   └── os-yuanli-install-profile # 按档位装 skill（本仓库独有）
├── docs/
│   ├── quickstart.md
│   ├── concepts.md
│   ├── adapter-guide.md
│   ├── faq.md
│   ├── capability-matrix.md      # 本仓库独有：诚实标注还原率
│   └── profiles.md               # 本仓库独有
├── examples/
│   ├── minimal-setup/
│   ├── team-engineer-setup/
│   ├── hay-setup/
│   └── hooks/                    # opt-in hooks（本仓库独有）
├── tests/
│   └── golden-path.sh
├── requirements.txt
├── ROADMAP.md
└── README.md
```

## 核心理念

1. **先判断，再执行**：`六判断` → 主题 gate → 策略 gate → 执行层路由
2. **完成前验真**：走 `evidence-gate`，artifact 真实存在
3. **完成后进化**：`Evolution Note` + `closure-evolution`
4. **可迁移 ≠ 全栈复刻**：profile 透明标注每档还原率，不做 100% 承诺

## 协议边界

这是**方法 + 配套卫星 + profile 档位**，不是学员本机的完整备份。

- 作者私有的 memory / token / Wiki 全量 / bridge 实例**不上传**
- `yuanli-full` 档只提供 Wiki 骨架和参数化路径，学员自己养
- `lark-ops` 档不附带飞书 token，学员自己配

详见 [docs/capability-matrix.md](docs/capability-matrix.md)。

## ROADMAP

见 [ROADMAP.md](ROADMAP.md)。

## License

MIT（方法论思想来自作者「原力OS」实践沉淀）

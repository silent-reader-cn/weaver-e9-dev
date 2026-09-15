# weaver-e9-dev

**泛微 E9（E-Cology 9）全栈开发知识库与 AI Skill** —— 数据库 + 后端接口 + 前端 JS API + 集成扩展，四大块内容用一套全文检索脚本统一检索。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Ecology](https://img.shields.io/badge/Ecology-9%20%28KB200601%2B%29-green.svg)
![APIs](https://img.shields.io/badge/REST%20APIs-538-orange.svg)
![Tables](https://img.shields.io/badge/DB%20tables-1%2C699-orange.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-3776AB.svg)

> **本仓库是 [`weaver-oa-dev`](https://github.com/silent-reader-cn/weaver-oa-dev) 与 [`weaver-e9-backend`](https://github.com/silent-reader-cn/weaver-e9-backend) 的合并后继版本。**
> 两个原仓库已停止维护（archived），所有内容与后续更新均在本仓库。

---

## 这是什么

泛微 E9 二开时最常查的四类资料，全部收在一处，**并且都能用同一个命令搜出来**：

| 块 | 内容 | 规模 | 入口 |
| :--- | :--- | :--- | :--- |
| **块一 数据库** | 全量物理表结构、核心表全景字典、高频业务 SQL | 1,699 张表 / 26 模块 | [`references/01_database/`](./references/01_database/) |
| **块二 后端接口** | 官方全量 REST API + Token 认证鉴权 | 538 个接口 / 8 模块 | [`references/02_backend_api/`](./references/02_backend_api/) |
| **块三 前端 JSAPI** | 流程表单 `WfForm` + 建模表单 `ModeForm` | 138 个方法 | [`references/03_frontend_jsapi/`](./references/03_frontend_jsapi/) |
| **块四 集成与扩展** | SOAP / Java 二次开发 / 消息推送 / SSO | 4 篇专题 | [`references/04_integration/`](./references/04_integration/) |

另有一块横切的 **认证**（[`references/auth/`](./references/auth/)）：三步握手流程、RSA 加密、防串号、排错手册。

---

## 30 秒上手

```bash
git clone https://github.com/silent-reader-cn/weaver-e9-dev.git
cd weaver-e9-dev

# 不知道某个接口怎么调？直接搜，返回方式/地址/参数/返回结构
python scripts/search.py getToDoWorkflowRequestList

# 不知道某张表有哪些字段？直接搜
python scripts/search.py workflow_currentoperator --scope db -d

# 不确定前端怎么联动字段？直接搜
python scripts/search.py convertFieldNameToId --scope js
```

只依赖 Python 3（标准库），无需安装任何第三方包。

---

## 安装为 Skill

把仓库内容复制到 WorkBuddy 的 skills 目录：

```bash
git clone https://github.com/silent-reader-cn/weaver-e9-dev.git
mkdir -p ~/.workbuddy-ai/skills/weaver-e9-dev
cp -r weaver-e9-dev/. ~/.workbuddy-ai/skills/weaver-e9-dev/
```

> 部分较早的安装使用 `~/.workbuddy/skills/` 路径，按你本地实际的 skills 目录放即可。

重启 / 刷新 WorkBuddy 后，对话中调用 `weaver-e9-dev` 即可加载本 Skill。

---

## 快速上手

### 1. 统一检索（四大块共用一个脚本）

```bash
PY="<你的 python3 路径>"

# —— 块二 后端接口 ——
"$PY" scripts/search.py 待办                                    # 全块检索
"$PY" scripts/search.py getToDoWorkflowRequestList --full        # 命中接口完整正文
"$PY" scripts/search.py 分部 --scope api --brief                 # 精简：标题|方式|地址|文件
"$PY" scripts/search.py 人员 --scope api --method GET --limit 10
"$PY" scripts/search.py 请假 流程 --all                          # 多词全命中

# —— 块一 数据库 ——
"$PY" scripts/search.py workflow_currentoperator --scope db -d   # 完整字段定义
"$PY" scripts/search.py 待办 --scope db                          # 按中文名/字段名搜表
"$PY" scripts/search.py 离职 --scope db --limit 10

# —— 块三 前端 JSAPI ——
"$PY" scripts/search.py convertFieldNameToId --scope js
"$PY" scripts/search.py 明细表 --scope js

# —— 块四 集成与扩展 ——
"$PY" scripts/search.py 钉钉 --scope int
"$PY" scripts/search.py BaseCronJob --scope int

# —— 认证 ——
"$PY" scripts/search.py 串号 --scope auth
```

**选项**

| 选项 | 说明 |
|---|---|
| `--scope S` | 检索范围：`api` / `db` / `js` / `int` / `auth`，可逗号组合，默认 `all` |
| `--brief` | 精简输出，仅一行：范围 \| 标题 \| 定位 |
| `--full` / `-d` | 输出完整正文，不截断 |
| `--all` | 多个关键词需全部命中（默认任一命中即可） |
| `--method M` | 仅块二有效，按请求方式过滤（GET / POST / PUT / DELETE） |
| `--limit N` | 最多返回条数（默认 20）。**截断时会显式告知真实总数** |
| `--max N` | 非 `--full` 时每条正文最多展示字符数（默认 1600） |

默认输出即包含命中条目的完整正文（参数表、返回示例、返回字段说明），**足够直接照着调用，无需再打开 `.md` 文件**。

### 2. 重新生成索引

```bash
"$PY" scripts/build_index.py
```

从 Markdown 反向生成四块的 `_INDEX.md`，保证索引永不与正文脱节。

### 3. 自检

```bash
"$PY" tools/selftest.py
```

27 项检查，逐条验证 538 接口 / 1699 表 / 138 方法的可召回性与内容完整性。

### 4. 调用 E9 接口

见 [`SKILL.md`](./SKILL.md) 第二节（认证三步）与
[`examples/todo_workflow.md`](./examples/todo_workflow.md)（脱敏的端到端可运行示例）。
[`scripts/ecology_token_client.js`](./scripts/ecology_token_client.js) 与
[`scripts/ecology_token_client.py`](./scripts/ecology_token_client.py) 是零依赖的鉴权 SDK，
自动完成 RSA 握手与 Cookie 隔离。

---

## 设计要点

- **Markdown 是唯一真相源**。检索脚本直接读 Markdown，不依赖预生成字典，
  因此不存在「改了文档忘了重建索引导致搜不到」的漂移问题。
  实测检索全部 1,699 张表约 **0.23 秒**，无需 JSON 加速层
  （这也是合并时删掉原仓库 4.5MB 的 `apis_dictionary.json` / `db_dictionary.json` 的原因）。
- **文档范式统一**。块二每个接口的结构固定为
  `## 标题` → `### 概述 / 请求方式 / 请求地址 / 版本信息 / 模块归属 / 请求参数说明 / 返回值类型 / 返回示例 / 返回参数说明`。
  检索脚本正是按 `^## ` 切块、正则抓 `### 请求方式` / `### 请求地址`，所以格式统一才能搜得全。
- **表结构列格式统一**。源仓库混有两套导出格式，已归一化为
  `序号 | 列名 | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注`。

---

## 目录结构

```
weaver-e9-dev/
├── SKILL.md                       # 主入口：认证（必读）+ 四块导航 + 检索用法
├── references/
│   ├── auth/                      # 认证（横切，必读）
│   │   ├── auth_token.md          #   深度参考：服务端配置 / 多语言代码 / jar 冲突 / FAQ / 时序图
│   │   └── auth_quickstart.md     #   避坑红线速查
│   ├── 01_database/               # 【块一】数据库
│   │   ├── _INDEX.md              #   1,699 张表总索引（模块统计 + 分模块清单）
│   │   ├── core_tables.md         #   核心表全景字典
│   │   ├── sql_cookbook.md        #   高频业务 SQL 模版
│   │   └── tables/<26 模块>/      #   1,699 个表结构定义
│   ├── 02_backend_api/            # 【块二】后端接口
│   │   ├── _INDEX.md              #   538 个接口总索引
│   │   └── <模块>_NN.md           #   22 个切块文件（≤30 接口/文件）
│   ├── 03_frontend_jsapi/         # 【块三】前端 JS API
│   │   ├── _INDEX.md
│   │   ├── wfform.md              #   流程表单 WfForm
│   │   └── modeform.md            #   建模表单 ModeForm
│   └── 04_integration/            # 【块四】集成与扩展
│       ├── _INDEX.md
│       ├── webservice_soap.md     #   SOAP 接口规范
│       ├── custom_backend_dev.md  #   Java 后端二次开发
│       ├── message_push.md        #   消息中心与第三方推送
│       └── sso_and_sync.md        #   第三方 SSO 与组织架构同步
├── scripts/                       # 运行时脚本
│   ├── search.py                  #   统一检索（四大块）
│   ├── build_index.py             #   从 Markdown 生成各块 _INDEX.md
│   ├── ecology_token_client.js    #   Node.js 鉴权 SDK（零依赖）
│   └── ecology_token_client.py    #   Python 鉴权 SDK（零依赖）
├── examples/                      # 可运行示例（JS / Java / 脱敏端到端）
└── tools/                         # 开发与验证脚本（非运行时依赖）
    ├── convert_apis.py            #   一次性：oa-dev 接口 → 本仓库文档范式
    ├── build_blocks.py            #   一次性：数据库/前端/集成内容归位
    ├── normalize_tables.py        #   一次性：统一两套表结构列格式
    └── selftest.py                #   检索脚本自检（27 项）
```

---

## 合并说明

### 来源仓库

| 来源 | 贡献 | 状态 |
|---|---|---|
| [weaver-oa-dev](https://github.com/silent-reader-cn/weaver-oa-dev) | 全部内容：数据库表结构、前端 JSAPI、WebService、Java 二次开发、SSO、SQL 字典 | 已归档 |
| [weaver-e9-backend](https://github.com/silent-reader-cn/weaver-e9-backend) | 文档范式、认证深度参考、全文检索机制 | 已归档 |

### 为什么合并

两个仓库**天生互补，不存在取舍冲突**：

1. **接口集合是包含关系**。用接口路径去重比对：`weaver-e9-backend` 的 494 个唯一路径
   **100% 被 `weaver-oa-dev` 的 537 个覆盖**（"仅 e9-backend 有"的数量为 0）。
   因此取并集即可，合并后还多出 43 个接口。

2. **检索脚本是格式驱动的**，这正是合并的钥匙。`weaver-e9-backend` 的检索脚本只做四件事：
   扫描目录下所有 `*.md` → 按 `## ` 切块 → 跳过标题含"索引"的块 → 正则抓 `### 请求方式` / `### 请求地址`。
   它不关心内容来自哪个仓库。而 `weaver-oa-dev` 的接口是 `### N. 标题` + `#### 请求参数` 结构，所以搜不到。
   **只要把格式重排为目标范式，同一套机制立刻就能搜到全部 538 个接口。**

3. **转换是机械的**。`weaver-oa-dev` 全部 538 个接口块结构高度统一
   （`请求参数` 538/538、`响应示例` 538/538、`响应字段` 492/538、`版本要求` 537/538），
   缺失项仅 1 处，可脚本批量完成。

### 合并同时修掉的问题

- **同一份内容存了三份**（`docs/` + `skills/` + `.agents/`，约 36MB）。合并后只保留一份规范目录，**38MB → 12MB**。
- **`skills/weaver-oa-dev/` 那份是残的**：缺整个 `scripts/` 目录（检索脚本与字典全无），
  表文件只有 920/1699。按该仓库 README 安装 `skills/` 那份，拿到的是没有搜索能力的半成品。

---

## 与源仓库的差异

| 项 | 说明 |
|---|---|
| 接口数 | 538（并集，比 `weaver-e9-backend` 多 43 个） |
| 接口文档格式 | 全部重排为统一范式，使 538 个接口可被同一脚本检索 |
| 描述信息 | 原 `weaver-oa-dev` 中 34 个接口同时含「功能说明」与「补充说明」，两者均保留 |
| **表结构列格式** | 源仓库混有**两套导出格式**（主流格式 1636 张 + 右移格式 62 张 + 1 张同构），已统一，涉及 63 个文件 / 584 行；逐字段比对确认 **0 处取值变化** |
| 目录副本 | 由 3 份（`docs/` + `skills/` + `.agents/`）合并为 1 份 |
| 检索脚本 | 由 2 套（JS + Python，基于 JSON 字典）合并为 1 套统一脚本（基于 Markdown） |
| 截断提示 | 修复原脚本「截断时谎报总数」的问题（命中 137 条却只报 20 条） |
| 已移除 | `apis_dictionary.json`、`db_dictionary.json`、重复的 JS/Python 检索脚本、三份冗余副本 |
| 已保留 | Node.js / Python 鉴权 SDK、全部 JS 与 Java 示例 |

### 关于「1,699 张表」

`1,699` 是**表定义文件数**；去重后为 **1,687 张唯一表**。有 12 个表名跨模块重复，
全部集中在 `E9新版考勤表结构` 与 `人力资源` 之间（kq_* 考勤表）。
列格式统一后，这 12 张表在两处的字段名/中文说明/类型/长度/备注已完全一致，
仅 `允许为空` 一列不同——因为源格式本身不含该列，属信息缺失而非丢失。

### 已知的源数据问题（保留原样，未擅自修改）

- `/api/portal/element/cooperation` 的「获取门户【我的协作】元素列表信息」在源文档中**被收录两次**，
  标题、路径、方法完全相同，正文长度不同（1566 / 2166 字符）。检索时会返回两条。
- 有 2 组接口共用同一路径但方法不同（`/api/public/browser/data/1`、`data/17`），属正常设计。

---

## 适用版本

**Ecology 9（E9）**，以主流 **KB200601 以上**为准。

不同 KB 版本（KB190601 以下 / KB190601–KB190901 / KB190901–KB200601 / KB200601 以上）
在 `loginid/pwd` 是否废除、regist 与 update 是否隔离等细节上有差异，
每个接口文档都含「Ecology版本 / 生效 KB 版本」两列，调用前请核对目标环境。

---

## License

[MIT](./LICENSE)

## 免责声明

本仓库内容整理自泛微（Weaver）官方公开文档，仅供学习、对接与二次开发参考。
接口名称、参数、返回结构及数据库表结构等版权归泛微所有。
示例中的真实凭据（appid / spk / secrit / 服务器地址 / 用户 id）均已脱敏，
使用前请替换为你自己的值。请遵守泛微相关许可与数据合规要求。

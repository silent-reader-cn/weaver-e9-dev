---
name: weaver-e9-dev
summary: 泛微 E9（E-Cology 9）全栈开发知识库 —— 数据库 + 后端 REST 接口 + 前端 JS API + 集成扩展，内置统一全文检索。
description: >-
  泛微OA（Weaver E-Cology 9 / E9）全栈开发指南，覆盖四大块内容：
  (1) 数据库 —— 1,699 张物理表结构、核心表全景字典、高频业务 SQL 模版；
  (2) 后端接口 —— 538 个官方 REST API（工作流程/人力资源/知识管理/考勤/表单建模/门户/协作/邮件）与 Token 认证鉴权；
  (3) 前端 JS API —— 流程表单 WfForm 与建模表单 ModeForm 全量接口；
  (4) 集成与扩展 —— WebService (SOAP)、Java 后端二次开发、消息中心推送、第三方 SSO 与组织架构同步。
  当需要进行泛微OA后端接口调用、E9 REST API 对接、认证鉴权（AppID/RSA/AES/Token）、
  组织架构同步、表单建模、流程流转、编写业务 SQL、查询底层表结构、
  开发流程表单代码块（WfForm/ModeForm）、对接钉钉/企业微信/飞书或排错时使用。
  接口参数与表结构均可用内置统一检索脚本按关键词定位，无需逐个打开文档。
---

# 泛微 E9 全栈开发指南

本 skill 由两个来源合并而成：**weaver-oa-dev**（全栈内容）提供数据库、前端 JSAPI、SOAP、Java 二次开发、SSO 等全部知识，
**weaver-e9-backend**（文档范式）提供统一的文档格式、认证深度参考与全文检索机制。
合并后按四大块组织，全部内容都可用同一套检索脚本定位。

> 适用版本：**Ecology 9（E9）**，主流 KB200601 以上。
> 不同 KB 版本（KB190601 以下 / KB190601–KB190901 / KB190901–KB200601 / KB200601 以上）
> 在 `loginid/pwd` 是否废除、regist 与 update 是否隔离等细节上有差异，本文以 KB200601 以上为准。

---

## 一、何时用本 skill

| 场景 | 去哪一块 |
|---|---|
| 调用 `/api/...` 后端接口、构造认证请求头 | 块二 后端接口 + 认证 |
| 写业务 SQL、查某张表有哪些字段 | 块一 数据库 |
| 流程表单代码块联动、建模卡片前端扩展 | 块三 前端 JSAPI |
| SOAP 对接、Java 二次开发、消息推送、钉钉/企微/飞书集成 | 块四 集成与扩展 |
| token 解密失败 / 500 / userid 串号 等排错 | 认证 + 第六节排错 |

---

## 二、认证（必读，第一步）

E9 的 Rest API 采用 **RSA 非对称加密 + Token**（云商店模式）。调用任何业务接口前，必须先完成三步：

```
注册 regist  →  取 token applytoken  →  携带 token 调业务接口
```

### 2.1 第 1 步：注册 regist（只做一次）

- **请求**：`POST /api/ec/dev/auth/regist`
- **请求头**：

| 参数 | 必选 | 说明 |
|---|---|---|
| `appid` | 是 | 许可证号码（需先在 OA 库 `ECOLOGY_BIZ_EC` 表发放） |
| `cpk` | 是 | 异构系统 RSA 公钥（实际无用但必传，可传 `123`） |
| `loginid` / `pwd` | 否* | **KB1906 及以上已废除** |

- **返回**：`spk`（系统公钥）、`secrit`（密钥，注意官方拼写如此，原词 secret）
- ⚠️ **只注册一次！** 重复 regist 会刷新密钥，导致旧 token 解密失败。

### 2.2 第 2 步：取 token applytoken

- **请求**：`POST /api/ec/dev/auth/applytoken`
- **请求头**：

| 参数 | 必选 | 说明 |
|---|---|---|
| `appid` | 是 | 许可证号码 |
| `secret` | 是 | 用 2.1 返回的 `spk` 对 `secrit` 做 RSA 加密后的密文 |
| `time` | 否 | token 有效期（秒），默认 `1800`（30 分钟） |

- **返回**：`token`（建议缓存并按 `time` 续期）

### 2.3 第 3 步：调用业务接口（带 token）

- **请求**：`GET / POST / PUT / DELETE /api/<业务接口地址>`
- **请求头（业务接口必带）**：

| Header | 必填 | 说明 |
|---|---|---|
| `appid` | 是 | 许可证号码 |
| `token` | 是 | 2.2 获取的 token |
| `userid` | 是 | 用 `spk` 对 OA 用户 id 加密后的密文 |
| `skipsession` | 否 | 白名单接口填 `1` 跳过 session 拦截 |
| `Content-Type` | 否* | POST 必须 `application/x-www-form-urlencoded; charset=utf-8` |
| `Content-Length` | 是 | 传 `0` |

- **返回结构**：`{ "status": true, "code": "0", "msg": "ok", ... }`，成功判定 `status===true && code==="0"`。

### 2.4 最小调用示例（curl）

```bash
# 1) 注册（仅一次）
curl -X POST 'http://<oa>/api/ec/dev/auth/regist' \
  -H 'appid: <appid>' -H 'cpk: 123'
# → 返回 spk(系统公钥) 与 secrit

# 2) 取 token：secret = RSA(spk, secrit) 密文
curl -X POST 'http://<oa>/api/ec/dev/auth/applytoken' \
  -H 'appid: <appid>' -H 'secret: <RSA(spk,secrit)>' -H 'time: 3600'
# → 返回 token

# 3) 调业务接口：userid = RSA(spk, 用户id) 密文
curl -X GET 'http://<oa>/api/<业务接口>' \
  -H 'appid: <appid>' -H 'token: <token>' \
  -H 'userid: <RSA(spk,用户id)>' -H 'skipsession: 1'
```

> RSA 加密用 **OPENSSL 格式公钥**（`spk`），填充模式必须 `RSA/ECB/PKCS1Padding`。
> Java 用 hutool `new RSA(null, spk).encryptBase64(...)`；其它语言与完整代码见
> [`references/auth/auth_token.md`](./references/auth/auth_token.md)。

### 2.5 关键注意

- `regist` **只调一次**；重复调会刷新密钥，旧 token 解密失败。
- 请求时**禁用 Cookie 传递**（如 hutool `disableCookie()`），否则 session 串号、userid 错乱。
- `token` 有时效，缓存并按 `time` 续期；集群环境 token 不存在/超时优先查 redis。

> 完整认证手册（服务端配置、Java/C# 三段式代码、jar 冲突、FAQ、时序图）见
> [`references/auth/auth_token.md`](./references/auth/auth_token.md)，
> 避坑红线见 [`references/auth/auth_quickstart.md`](./references/auth/auth_quickstart.md)。

---

## 三、四大块导航

| 块 | 内容 | 规模 | 入口 |
| :--- | :--- | :--- | :--- |
| **块一 数据库** | 全量物理表结构、核心表全景字典、高频业务 SQL | 1,699 张表 / 26 模块 | [`references/01_database/`](./references/01_database/) |
| **块二 后端接口** | 官方全量 REST API（认证见第二节） | 538 个接口 / 8 模块 | [`references/02_backend_api/`](./references/02_backend_api/) |
| **块三 前端 JSAPI** | 流程表单 `WfForm` + 建模表单 `ModeForm` | 138 个方法 | [`references/03_frontend_jsapi/`](./references/03_frontend_jsapi/) |
| **块四 集成与扩展** | SOAP / Java 二次开发 / 消息推送 / SSO | 4 篇专题 | [`references/04_integration/`](./references/04_integration/) |

各块都有 `_INDEX.md` 总索引（由 `scripts/build_index.py` 从 Markdown 自动生成）。

**块一 数据库** 还包含两篇速查：

- [`core_tables.md`](./references/01_database/core_tables.md) —— 最常用核心表（流程引擎、组织架构、知识文档）的表名/中文说明/关键字段/关联关系。
- [`sql_cookbook.md`](./references/01_database/sql_cookbook.md) —— 生产级 SQL 模版：待办分页、审批流转历史、部门递归 CTE、主子表动态关联。

> `tables/` 下 1,699 个表定义文件已统一为同一列格式
> （`序号 | 列名 | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注`）。
> 注意 `1,699` 是文件数，去重后为 1,687 张唯一表——12 张考勤表在
> `E9新版考勤表结构` 与 `人力资源` 下各有一份。

**块二 后端接口** 覆盖 8 个模块：工作流程 (45)、人力资源 (225)、知识管理 (60)、
考勤 (107)、表单建模 (19)、门户管理 (76)、协作管理 (3)、邮件模块 (3)。

**块四 集成与扩展**：

- [`webservice_soap.md`](./references/04_integration/webservice_soap.md) —— `WorkflowService` / `DocService` / `HrmService` WSDL 规范与 SOAP 报文。
- [`custom_backend_dev.md`](./references/04_integration/custom_backend_dev.md) —— Java 自定义 Action、`RecordSet`/`RecordSetTrans`、`BaseCronJob` 定时调度、JAX-RS 自定义 REST 服务。
- [`message_push.md`](./references/04_integration/message_push.md) —— E9 与第三方系统双向消息推送、待办状态同步。
- [`sso_and_sync.md`](./references/04_integration/sso_and_sync.md) —— 钉钉 / 企业微信 / 飞书免密登录与通讯录实时同步。

---

## 四、统一检索（核心用法）

**四大块全部内容用同一个脚本检索**，直接返回命中条目的完整正文，无需再打开 `.md` 文件。

```bash
PY="<你的 python3 路径>"
"$PY" "$SKILL_DIR/scripts/search.py" <关键词...> [选项]
```

`$SKILL_DIR` 指本 skill 根目录。常用示例：

```bash
# —— 块二 后端接口 ——
"$PY" scripts/search.py 待办                                   # 全块检索
"$PY" scripts/search.py getToDoWorkflowRequestList --full       # 命中接口完整正文
"$PY" scripts/search.py 分部 --scope api --brief                # 精简：标题|方式|地址|文件
"$PY" scripts/search.py 人员 --scope api --method GET --limit 10
"$PY" scripts/search.py 请假 流程 --all                         # 多词全命中

# —— 块一 数据库 ——
"$PY" scripts/search.py workflow_currentoperator --scope db -d  # 完整字段定义
"$PY" scripts/search.py 待办 --scope db                         # 按中文名/字段名搜表
"$PY" scripts/search.py 离职 --scope db --limit 10

# —— 块三 前端 JSAPI ——
"$PY" scripts/search.py convertFieldNameToId --scope js
"$PY" scripts/search.py 明细表 --scope js

# —— 块四 集成 ——
"$PY" scripts/search.py 钉钉 --scope int
"$PY" scripts/search.py BaseCronJob --scope int

# —— 认证 ——
"$PY" scripts/search.py 串号 --scope auth
```

**选项**：`--scope S`（`api`/`db`/`js`/`int`/`auth`，可逗号组合，默认 `all`）·
`--brief`（精简一行）· `--full` / `-d`（完整正文，不截断）· `--all`（多词全命中）·
`--method GET|POST`（仅块二）· `--limit N`（默认 20）· `--max N`（非 `--full` 时每条正文上限，默认 1600）

> 检索**直接读 Markdown**，不依赖预生成字典，因此不存在「改了文档忘了重建索引导致搜不到」的漂移问题。
> 实测检索全部 1,699 张表约 0.23 秒。
> 修改过文档后，可用 `python scripts/build_index.py` 重新生成各块 `_INDEX.md`。

---

## 五、Node.js / Python 客户端 SDK

[`scripts/ecology_token_client.js`](./scripts/ecology_token_client.js)（Node.js）与
[`scripts/ecology_token_client.py`](./scripts/ecology_token_client.py)（Python）已封装完整鉴权流程，
**零第三方依赖**，自动完成 RSA 加密握手与 Cookie 隔离：

```javascript
const EcologyClient = require('./scripts/ecology_token_client');

const client = new EcologyClient({
  baseUrl: 'http://oa.yourcompany.com:8088',
  appId: 'your-appid',
  defaultUserId: '1'        // 系统管理员或指定员工工号
});

async function main() {
  // 查询待办列表（自动完成 regist → token → RSA userid 加密）
  const todoList = await client.request({
    path: '/api/workflow/paService/getToDoWorkflowRequestList',
    method: 'POST',
    data: { pageSize: '20', pageNo: '1' }
  });
  console.log('待办数据:', todoList);
}
main();
```

更多可运行示例见 [`examples/`](./examples/)：含脱敏的端到端待办查询
（[`todo_workflow.md`](./examples/todo_workflow.md)）、工作流集成、组织架构同步、
表单代码块、SOAP 客户端，以及 Java 自定义 Action / 定时任务 / REST 服务。

---

## 六、常见排错速查

| 现象 | 原因与处理 |
|---|---|
| `applytoken` 解密失败 | 先用 postman 测；检查 jar 冲突（北森 `Beisen.OIDC.SDK`、bcprov），见 `auth_token.md` |
| token 不存在 / 超时 | 集群环境查 redis 共享；或缓存问题导致 token 很快过期 |
| `userid` 不对 / 串号 | 请求头带了 Cookie → 必须禁用 Cookie 传递 |
| 500 + html 报错 | 老版本 KB（≤KB900210208）人力资源 `DoUserSessionCmd` 的 session invalidate 问题，需注释对应行 |
| 注册失败找不到 APPID | appid 含特殊字符/换行、未 `COMMIT`、库不对、缓存未清（`/commcache/cacheMonitor.jsp`） |
| 接口报无权限 | 确认 `userid` 对应账号对目标流程/文档有权限；监控权限删除流程需传 `{"ismonitor":"1"}` |

---

## 七、目录结构

```
weaver-e9-dev/
├── SKILL.md                       # 本文件：认证 + 四块导航 + 检索
├── references/
│   ├── auth/                      # 认证（横切，必读）
│   │   ├── auth_token.md          #   深度参考：服务端配置/多语言代码/jar冲突/FAQ
│   │   └── auth_quickstart.md     #   避坑红线速查
│   ├── 01_database/               # 【块一】数据库
│   │   ├── _INDEX.md              #   1,699 张表总索引
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
│       ├── webservice_soap.md
│       ├── custom_backend_dev.md
│       ├── message_push.md
│       └── sso_and_sync.md
├── scripts/
│   ├── search.py                  # 统一检索（四大块）
│   ├── build_index.py             # 从 Markdown 生成各块 _INDEX.md
│   ├── ecology_token_client.js    # Node.js 鉴权 SDK（零依赖）
│   └── ecology_token_client.py    # Python 鉴权 SDK（零依赖）
└── examples/                      # 可运行示例（JS / Java / 脱敏端到端）
```

---

## 八、免责声明

本 skill 内容整理自泛微（Weaver）官方公开文档，仅供学习、对接与二次开发参考。
接口名称、参数、返回结构及数据库表结构等版权归泛微所有。
示例中的真实凭据（appid / spk / secrit / 服务器地址 / 用户 id）均已脱敏，
使用前请替换为你自己的值。请遵守泛微相关许可与数据合规要求。

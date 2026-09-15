# 实战示例：获取最近 N 条待办流程

本示例演示如何用本 skill 的**三步认证**（regist → applytoken → 调业务接口）调用
`POST /api/workflow/paService/getToDoWorkflowRequestList`，获取指定用户的待办流程，
并按接收时间倒序取最近 N 条。

> ⚠️ **已脱敏**：下列脚本中所有真实的 appid / spk / secrit / 服务器地址 / 用户 id 均已替换为
> 占位符 `<...>`，**实际运行前请按 `SKILL.md` 第 2 节填入你自己的值**（或保留 spk/secrit 为空，
> 由脚本首次运行时自动 `regist` 获取并提示你保存）。

---

## 1. 完整脚本（Node，仅用内置模块，无需 npm install）

将下面脚本保存为 `get_todo_workflow.js`，填好顶部 `CONFIG` 后运行：`node get_todo_workflow.js`

```javascript
#!/usr/bin/env node
'use strict';
// 泛微 E9 待办流程查询 —— 获取最近 N 条待办（基于 weaver-e9-backend skill）
// 依赖：仅 Node 内置 (crypto + http/https)
const crypto = require('crypto');
const http = require('http');
const https = require('https');

// ============================ 配置区（运行前填写） ============================
const CONFIG = {
  baseURL: 'http://<oa域名或IP>:<端口>',     // 例如 http://oa.example.com:8089
  appid: '<你的 appid>',                       // 需先在 OA 库 ECOLOGY_BIZ_EC 表发放
  spk: '<regist 返回的系统公钥 spk>',          // 留空则首次自动 regist
  secrit: '<regist 返回的密钥 secrit>',        // 留空则首次自动 regist
  userid: '<目标用户的 OA id>',                // 例如 58（用 spk 做 RSA 加密后传入）
  pageSize: 10,                               // 先取一页（用于排序后取最近 N 条）
  topN: 3,                                   // 取最近几条
  tokenTTL: 3600,                            // token 有效期（秒）
  skipSession: false,                        // 若接口已加白名单，可设 true 并带 skipsession:1
};
// ===========================================================================

// 把 spk 规范成 PEM
function toPem(spk) {
  if (spk.includes('-----BEGIN')) return spk;
  const body = spk.replace(/\s+/g, '').match(/.{1,64}/g).join('\n');
  return `-----BEGIN PUBLIC KEY-----\n${body}\n-----END PUBLIC KEY-----`;
}

// RSA 加密（PKCS1 填充，等同官方 hutool RSA/ECB/PKCS1Padding）
function rsaEncrypt(spk, plain) {
  const buf = crypto.publicEncrypt(
    { key: toPem(spk), padding: crypto.constants.RSA_PKCS1_PADDING },
    Buffer.from(String(plain), 'utf-8')
  );
  return buf.toString('base64');
}

// 发 HTTP 请求（POST form-urlencoded / GET）
function request(method, path, headers, body) {
  return new Promise((resolve, reject) => {
    const url = new URL(path, CONFIG.baseURL);
    const lib = url.protocol === 'https:' ? https : http;
    const data = body ? Buffer.from(body) : null;
    const opt = {
      method,
      hostname: url.hostname,
      port: url.port || (url.protocol === 'https:' ? 443 : 80),
      path: url.pathname + url.search,
      headers: { ...headers },
    };
    if (data) {
      opt.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=utf-8';
      opt.headers['Content-Length'] = data.length; // Node 自动算，勿手动设 0
    }
    const req = lib.request(opt, (res) => {
      let raw = '';
      res.on('data', (c) => (raw += c));
      res.on('end', () => {
        try { resolve(JSON.parse(raw)); }
        catch (e) { reject(new Error('返回非 JSON: ' + raw.slice(0, 300))); }
      });
    });
    req.on('error', reject);
    if (data) req.write(data);
    req.end();
  });
}

// 步骤1：注册（仅当未提供 spk/secrit 时）
async function ensureCreds() {
  if (CONFIG.spk && CONFIG.secrit) return { spk: CONFIG.spk, secrit: CONFIG.secrit };
  console.log('① 未提供 spk/secrit，执行 regist 注册…');
  const r = await request('POST', '/api/ec/dev/auth/regist', { appid: CONFIG.appid, cpk: '123' }, null);
  if (!r || !r.spk) throw new Error('regist 失败: ' + JSON.stringify(r));
  console.log('   注册成功！请保存下面两个值并填入 CONFIG.spk / CONFIG.secrit：');
  console.log('   spk   =', r.spk);
  console.log('   secrit=', r.secrit);
  return { spk: r.spk, secrit: r.secrit };
}

// 步骤2：取 token
async function applyToken(spk, secrit) {
  const secret = rsaEncrypt(spk, secrit);
  const r = await request('POST', '/api/ec/dev/auth/applytoken',
    { appid: CONFIG.appid, secret, time: String(CONFIG.tokenTTL) }, null);
  if (!r || !r.token) throw new Error('applytoken 失败: ' + JSON.stringify(r));
  return r.token;
}

// 步骤3：调待办接口
async function getToDo(token, spk) {
  const useridEnc = rsaEncrypt(spk, CONFIG.userid);
  const headers = { appid: CONFIG.appid, token, userid: useridEnc };
  if (CONFIG.skipSession) headers['skipsession'] = '1';
  const body = `pageNo=1&pageSize=${CONFIG.pageSize}`;
  const r = await request('POST', '/api/workflow/paService/getToDoWorkflowRequestList', headers, body);
  // 适配多种返回结构：顶层数组 / {root} / {data:{root}} / {datas:{root}}
  const root = Array.isArray(r)
    ? r
    : (r.root) || (r.data && r.data.root) || (r.datas && r.datas.root) || [];
  return root;
}

// 主流程
(async () => {
  try {
    if (!CONFIG.baseURL || !CONFIG.appid || !CONFIG.userid) {
      throw new Error('请先填写 CONFIG.baseURL / appid / userid');
    }
    const { spk, secrit } = await ensureCreds();
    const token = await applyToken(spk, secrit);
    console.log('② token 获取成功，查询待办…');
    const list = await getToDo(token, spk);

    // 按时间倒序取最近 N 条（优先 receiveTime，否则 createTime）
    const sorted = [...list].sort((a, b) => {
      const ta = new Date((b.receiveTime || b.createTime || '').replace(/-/g, '/')).getTime();
      const tb = new Date((a.receiveTime || a.createTime || '').replace(/-/g, '/')).getTime();
      return ta - tb;
    });
    const top = sorted.slice(0, CONFIG.topN);

    console.log(`\n✅ 共 ${list.length} 条待办，最近 ${top.length} 条：\n`);
    top.forEach((it, i) => {
      const wf = it.workflowBaseInfo || {};
      console.log(`【${i + 1}】${it.requestName || '(无标题)'}`);
      console.log(`     requestId     : ${it.requestId}`);
      console.log(`     创建人        : ${it.creatorName || ''} (${it.creatorId || ''})`);
      console.log(`     当前节点      : ${it.currentNodeName || ''}`);
      console.log(`     创建时间      : ${it.createTime || ''}`);
      console.log(`     接收时间      : ${it.receiveTime || ''}`);
      console.log(`     流程         : ${wf.workflowName || ''} (id=${wf.workflowId || ''})`);
      console.log('');
    });
    if (top.length === 0) console.log('（当前没有待办流程）');
  } catch (e) {
    console.error('❌ 出错:', e.message);
    process.exit(1);
  }
})();
```

---

## 2. 关键实现点（踩坑记录）

1. **RSA 加密**用 `RSA_PKCS1_PADDING` + OPENSSL 格式公钥（`spk`），与官方 hutool
   `new RSA(null, spk).encryptBase64(...)` 等价。Java/C# 完整代码见 `references/auth_token.md`。
2. **切勿手动设 `Content-Length: 0`**：Node 的 `http` 模块会按实际 body 自动计算正确长度；
   按官方文档那种「硬传 0」反而会把请求体截断、导致参数丢失。
3. **该对外接口直接返回顶层 JSON 数组**（不是 `{status, root}` 包装），解析时先用
   `Array.isArray(r)` 判断，再回退到 `r.root` / `r.data.root` 等结构。
4. **接口不保证默认排序**，故先取一页（pageSize）再在本地按 `receiveTime`/`createTime` 倒序，取最近 N 条。
5. **`userid` 要用 `spk` 加密后传入**；若接口已在 OA 后台加白名单，可把 `skipSession` 设 `true`
   并在请求头带 `skipsession: 1`。

---

## 3. 脱敏后的运行示例输出

首次运行（自动 regist）会先打印凭证，再输出待办；凭证固化后重跑则直接查：

```
① 未提供 spk/secrit，执行 regist 注册…
   注册成功！请保存下面两个值并填入 CONFIG.spk / CONFIG.secrit：
   spk   = MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A…(省略)…
   secrit= xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
② token 获取成功，查询待办…

✅ 共 10 条待办，最近 3 条：

【1】发票开具申请单-赵**(脱敏)-…小象沈阳…
     requestId     : 106****
     创建人        : 赵**(58)
     当前节点      : 财务税务会计开票
     创建时间      : 2026-09-08 14:30:00
     接收时间      : 2026-09-08 14:59:50
     流程         : 发票开具申请单 (id=173)

【2】发票开具申请单-赵**(脱敏)-…小象北京…
     requestId     : 106****
     创建人        : 赵**(58)
     当前节点      : 财务税务会计开票
     创建时间      : 2026-09-08 14:28:00
     接收时间      : 2026-09-08 14:59:13
     流程         : 发票开具申请单 (id=173)

【3】发票开具申请单-何**(脱敏)-…慧诚…
     requestId     : 106****
     创建人        : 何**(58)
     当前节点      : 财务税务会计开票
     创建时间      : 2026-09-08 13:50:00
     接收时间      : 2026-09-08 14:12:27
     流程         : 发票开具申请单 (id=173)
```

---

## 4. 接口参数速查

调用前可用内置搜索脚本确认参数与返回结构（无需打开大文件）：

```bash
PY="<managed python 路径>"
"$PY" "$SKILL_DIR/scripts/search_apis.py" getToDoWorkflowRequestList --full
```

返回的接口正文含：请求方式 `POST`、请求地址 `/api/workflow/paService/getToDoWorkflowRequestList`、
请求参数（`pageNo` / `pageSize` / `conditions` 高级搜索）、返回字段
（`requestId` / `requestName` / `creatorName` / `receiveTime` / `currentNodeName` / `workflowBaseInfo` 等）。

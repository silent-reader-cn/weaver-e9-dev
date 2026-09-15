/**
 * 泛微OA (E-Cology 9) 开放平台全功能标准认证与 API 调用客户端 (Node.js 版)
 * 官方标准规范实现：
 * 1. 注册获取密钥与公钥 (POST /api/ec/dev/auth/regist) [可选]
 * 2. 申请并激活 Token (POST /api/ec/dev/auth/applytoken)
 * 3. 自动使用 RSA 公钥 (spk) 对 userid 加密，杜绝身份串号
 * 4. 彻底禁用 Cookie，避免 Session 串号与用户状态污染
 * 5. 内置 Token 过期自动刷新与自动重试
 * 6. 纯原生实现，基于 Node.js 内置 crypto 与 http/https 模块，零第三方依赖！
 */

const crypto = require('crypto');
const http = require('http');
const https = require('https');
const { URL } = require('url');

class EcologyClient {
  /**
   * @param {Object} options
   * @param {string} options.baseUrl - 泛微 OA 服务地址 (如: http://oa.company.com:8088)
   * @param {string} options.appId - 许可证号码 / 在泛微后台注册的 AppID (如: b59e05ced89f43d69ed7d6bdb6c57140)
   * @param {string} [options.secret] - 第一步 regist 返回的 secret (若无则自动调用 regist 获取)
   * @param {string} [options.spk] - 第一步 regist 返回的服务端 RSA 公钥 (若无则自动调用 regist 获取)
   * @param {string} [options.defaultUserId='1'] - 默认操作人工号或用户ID (如: '1' 代表管理员)
   * @param {boolean} [options.autoRefresh=true] - Token 过期是否自动刷新并重试
   */
  constructor({ baseUrl, appId, secret = null, spk = null, defaultUserId = '1', autoRefresh = true }) {
    this.baseUrl = baseUrl.replace(/\/+$/, '');
    this.appId = appId;
    this.secret = secret;
    this.spk = spk;
    this.defaultUserId = String(defaultUserId);
    this.autoRefresh = autoRefresh;

    this.token = null;
    this.expireTime = 0;
  }

  /**
   * 格式化公钥为标准 PEM
   */
  _formatSpkToPem(spkBase64) {
    let pem = spkBase64.trim();
    if (!pem.startsWith('-----BEGIN')) {
      const lines = pem.match(/.{1,64}/g) || [pem];
      pem = `-----BEGIN PUBLIC KEY-----\n${lines.join('\n')}\n-----END PUBLIC KEY-----`;
    }
    return pem;
  }

  /**
   * 使用服务端 RSA 公钥加密文本 (RSA/ECB/PKCS1Padding)
   */
  _rsaEncrypt(plainText, spkBase64) {
    const pem = this._formatSpkToPem(spkBase64);
    const buffer = Buffer.from(plainText, 'utf8');
    const encrypted = crypto.publicEncrypt(
      {
        key: pem,
        padding: crypto.constants.RSA_PKCS1_PADDING
      },
      buffer
    );
    return encrypted.toString('base64');
  }

  /**
   * 发起 HTTP 请求 (严格禁用 Cookie 传递)
   */
  _httpRequest({ urlStr, method = 'POST', headers = {}, body = null, timeout = 30000 }) {
    return new Promise((resolve, reject) => {
      const urlObj = new URL(urlStr);
      const isHttps = urlObj.protocol === 'https:';
      const transport = isHttps ? https : http;

      // 强制移除 Cookie，杜绝泛微 OA 用户 Session 串号问题
      const reqHeaders = { ...headers };
      delete reqHeaders['Cookie'];
      delete reqHeaders['cookie'];

      let bodyData = null;
      if (body !== null && body !== undefined) {
        if (typeof body === 'string' || Buffer.isBuffer(body)) {
          bodyData = body;
        } else {
          bodyData = JSON.stringify(body);
          if (!reqHeaders['Content-Type']) {
            reqHeaders['Content-Type'] = 'application/json; charset=utf-8';
          }
        }
        reqHeaders['Content-Length'] = Buffer.byteLength(bodyData);
      }

      const options = {
        hostname: urlObj.hostname,
        port: urlObj.port || (isHttps ? 443 : 80),
        path: urlObj.pathname + urlObj.search,
        method: method.toUpperCase(),
        headers: reqHeaders,
        timeout
      };

      const req = transport.request(options, (res) => {
        let chunks = [];
        res.on('data', (chunk) => chunks.push(chunk));
        res.on('end', () => {
          const raw = Buffer.concat(chunks).toString('utf8');
          try {
            const parsed = JSON.parse(raw);
            resolve(parsed);
          } catch (e) {
            resolve({ raw, status: res.statusCode === 200 });
          }
        });
      });

      req.on('error', (err) => reject(err));
      req.on('timeout', () => {
        req.destroy();
        reject(new Error(`请求超时: ${urlStr}`));
      });

      if (bodyData) {
        req.write(bodyData);
      }
      req.end();
    });
  }

  /**
   * 第一步：注册应用并获取服务端公钥与密钥 (仅在未配置 secret/spk 时调用)
   */
  async registApp() {
    const url = `${this.baseUrl}/api/ec/dev/auth/regist`;
    const formBody = `appid=${encodeURIComponent(this.appId)}&cpcode=`;
    const res = await this._httpRequest({
      urlStr: url,
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8' },
      body: formBody
    });

    if (!res.status && String(res.code) !== '0') {
      throw new Error(`Regist 失败: ${JSON.stringify(res)}`);
    }

    this.secret = res.secret;
    this.spk = res.spk;
    console.log(`[EcologyClient] 应用注册成功. AppId=${this.appId}, Secret=${this.secret}`);
    return { secret: this.secret, spk: this.spk };
  }

  /**
   * 第二步：申请访问 Token (使用 RSA 加密后的 secret)
   */
  async applyToken() {
    if (!this.secret || !this.spk) {
      await this.registApp();
    }

    const secretEncrypted = this._rsaEncrypt(this.secret, this.spk);
    const url = `${this.baseUrl}/api/ec/dev/auth/applytoken`;
    const formBody = `appid=${encodeURIComponent(this.appId)}&secret=${encodeURIComponent(secretEncrypted)}&time=3600`;

    const res = await this._httpRequest({
      urlStr: url,
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        appid: this.appId,
        secret: secretEncrypted,
        time: '3600'
      },
      body: formBody
    });

    if (!res.status && String(res.code) !== '0') {
      throw new Error(`ApplyToken 失败: ${JSON.stringify(res)}`);
    }

    this.token = res.token;
    this.expireTime = Date.now() + 3500 * 1000; // 缓存 58 分钟
    console.log(`[EcologyClient] Token 获取成功: ${this.token}`);
    return this.token;
  }

  /**
   * 获取有效 Token
   */
  async getValidToken() {
    if (this.token && Date.now() < this.expireTime) {
      return this.token;
    }
    return await this.applyToken();
  }

  /**
   * 第三步：发起业务请求
   */
  async request({ path, method = 'POST', params = null, data = null, userId = null, isJson = true }) {
    const token = await this.getValidToken();
    const uid = userId ? String(userId) : this.defaultUserId;

    // 对 userid 进行 RSA 公钥加密
    let encryptedUserId = uid;
    if (this.spk) {
      try {
        encryptedUserId = this._rsaEncrypt(uid, this.spk);
      } catch (e) {
        console.warn('[EcologyClient] RSA 加密 userid 失败，降级为明文:', e.message);
      }
    }

    let targetUrl = `${this.baseUrl}/${path.replace(/^\/+/, '')}`;
    if (params) {
      const queryStr = Object.entries(params)
        .map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`)
        .join('&');
      targetUrl += (targetUrl.includes('?') ? '&' : '?') + queryStr;
    }

    const headers = {
      appid: this.appId,
      token: token,
      userid: encryptedUserId,
      skipsession: '0',
      'User-Agent': 'Weaver-Ecology-Node-SDK/2.0'
    };

    let bodyData = null;
    if (data !== null && data !== undefined) {
      if (isJson) {
        headers['Content-Type'] = 'application/json; charset=utf-8';
        bodyData = typeof data === 'string' ? data : JSON.stringify(data);
      } else {
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=utf-8';
        bodyData = Object.entries(data)
          .map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`)
          .join('&');
      }
    }

    try {
      const res = await this._httpRequest({
        urlStr: targetUrl,
        method,
        headers,
        body: bodyData
      });

      // 如果 Token 超时 (code === -1 或 msg 包含 token)，自动重新获取 Token 并重试
      if (
        (String(res.code) === '-1' || (res.msg && res.msg.includes('token'))) &&
        this.autoRefresh
      ) {
        console.warn('[EcologyClient] 检测到 Token 失效，自动重新申请并重试...');
        this.token = null;
        return await this.request({ path, method, params, data, userId, isJson });
      }

      return res;
    } catch (err) {
      return { status: false, code: -1, error: err.message };
    }
  }
}

module.exports = EcologyClient;

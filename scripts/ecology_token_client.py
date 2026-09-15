#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
泛微OA (E-Cology 9) 开放平台标准鉴权与 API 调用客户端 (Python 版)
功能：
1. 自动完成 applytoken (获取临时 Token 与 RSA 公钥)
2. 自动生成 16 字节 AES 密钥并通过 RSA 加密完成 token 激活
3. 自动在 Header 中组装 appid, token, userid 调用业务接口
4. 支持 Token 过期自动重新激活与重试机制
"""

import os
import sys
import time
import json
import random
import string
import base64
import urllib.request
import urllib.parse
from typing import Dict, Any, Optional

try:
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_v1_5, AES
    from Crypto.Util.Padding import pad, unpad
    HAS_CRYPTO = True
except ImportError:
    HAS_CRYPTO = False


class EcologyClient:
    def __init__(self, base_url: str, appid: str, default_userid: str = "1", auto_refresh: bool = True):
        self.base_url = base_url.rstrip("/")
        self.appid = appid
        self.default_userid = default_userid
        self.auto_refresh = auto_refresh
        self.token: Optional[str] = None
        self.secret: Optional[str] = None
        self.token_expire_time: float = 0

    def _generate_secret(self, length: int = 16) -> str:
        """生成 16 字节随机 AES 密钥"""
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(length))

    def _rsa_encrypt(self, text: str, spk_base64: str) -> str:
        """使用 RSA 公钥加密密钥 (RSA/ECB/PKCS1Padding)"""
        if not HAS_CRYPTO:
            raise RuntimeError(
                "未检测到 pycryptodome 库。请运行: pip install pycryptodome"
            )
        
        # 补全 PEM 格式
        if not spk_base64.startswith("-----BEGIN"):
            spk_pem = f"-----BEGIN PUBLIC KEY-----\n{spk_base64}\n-----END PUBLIC KEY-----"
        else:
            spk_pem = spk_base64

        pub_key = RSA.import_key(spk_pem.encode("utf-8"))
        cipher = PKCS1_v1_5.new(pub_key)
        encrypted_bytes = cipher.encrypt(text.encode("utf-8"))
        return base64.b64encode(encrypted_bytes).decode("utf-8")

    def apply_and_activate_token(self) -> str:
        """完成 applytoken 与 token 激活两步握手"""
        # 1. 申请临时 Token 与服务端公钥
        apply_url = f"{self.base_url}/api/ec/dev/auth/applytoken"
        apply_data = urllib.parse.urlencode({"appid": self.appid}).encode("utf-8")
        req = urllib.request.Request(
            apply_url,
            data=apply_data,
            headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            apply_res = json.loads(resp.read().decode("utf-8"))

        if not apply_res.get("status") and str(apply_res.get("code")) != "1":
            raise RuntimeError(f"ApplyToken 失败: {apply_res}")

        temp_token = apply_res.get("token")
        spk = apply_res.get("spk")
        if not temp_token or not spk:
            raise RuntimeError(f"ApplyToken 返回异常数据: {apply_res}")

        # 2. 生成本地 Secret 并使用 RSA 公钥加密
        secret = self._generate_secret(16)
        secret_encrypted = self._rsa_encrypt(secret, spk)

        # 3. 提交加密密钥以激活 Token
        token_url = f"{self.base_url}/api/ec/dev/auth/token"
        token_data = urllib.parse.urlencode({
            "appid": self.appid,
            "token": temp_token,
            "secret": secret_encrypted
        }).encode("utf-8")
        req2 = urllib.request.Request(
            token_url,
            data=token_data,
            headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        )
        with urllib.request.urlopen(req2, timeout=15) as resp2:
            token_res = json.loads(resp2.read().decode("utf-8"))

        if not token_res.get("status") and str(token_res.get("code")) != "1":
            raise RuntimeError(f"Token 激活失败: {token_res}")

        self.token = temp_token
        self.secret = secret
        # 默认有效时长按 1.5 小时缓存
        self.token_expire_time = time.time() + 5400
        print(f"泛微OA Token 获取并激活成功: {self.token}")
        return self.token

    def get_token(self) -> str:
        """获取当前有效 Token，若过期则自动刷新"""
        if not self.token or time.time() >= self.token_expire_time:
            self.apply_and_activate_token()
        return self.token

    def request(
        self,
        path: str,
        method: str = "POST",
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        userid: Optional[str] = None,
        is_json: bool = True
    ) -> Dict[str, Any]:
        """发起业务接口请求"""
        token = self.get_token()
        uid = userid or self.default_userid

        url = f"{self.base_url}/{path.lstrip('/')}"
        if params:
            url += "?" + urllib.parse.urlencode(params)

        headers = {
            "appid": self.appid,
            "token": token,
            "userid": uid,
            "User-Agent": "Weaver-Ecology-Python-SDK/1.0"
        }

        body_bytes = None
        if data is not None:
            if is_json:
                headers["Content-Type"] = "application/json; charset=UTF-8"
                body_bytes = json.dumps(data, ensure_ascii=False).encode("utf-8")
            else:
                headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
                body_bytes = urllib.parse.urlencode(data).encode("utf-8")

        req = urllib.request.Request(url, data=body_bytes, headers=headers, method=method.upper())
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8", errors="ignore")
                try:
                    res_json = json.loads(raw)
                    # 检查是否 Token 过期
                    if str(res_json.get("code")) == "-1" and self.auto_refresh:
                        print("检测到 Token 过期，正在重新激活并重试请求...")
                        self.apply_and_activate_token()
                        return self.request(path, method, params, data, userid, is_json)
                    return res_json
                except json.JSONDecodeError:
                    return {"raw_content": raw, "status": "1"}
        except Exception as e:
            return {"status": "0", "error": str(e)}


if __name__ == "__main__":
    print("泛微 E9 接口客户端示例:")
    print("用法：")
    print("  client = EcologyClient(base_url='http://oa.example.com', appid='ERP_DEV_01')")
    print("  res = client.request('/api/workflow/paService/getForwardWorkflowRequestList', method='POST', data={'workflowId': '101'})")
    print("  print(res)")

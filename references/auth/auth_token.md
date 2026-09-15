# 泛微 E9 后端接口 — Token 认证（深度参考）

> 来源：e-cloudstore.com 云商店《Token认证使用步骤》官方文档。
> 适用：Ecology 9（仅支持 E9）。本文以「主流 KB200601 以上」为准（低于该版本在 `loginid/pwd` 是否废除、regist 与 update 是否隔离等细节有差异）。

> **本文定位**：`SKILL.md` 第二节已含「认证三步流程 + token 使用方式 + curl 示例（必读）」。本文保留**服务端配置、代码实现、jar 冲突、FAQ、时序图**等深度内容。

泛微 E9 的 Rest API 采用 **RSA 非对称加密 + Token** 的认证模式（云商店模式）：注册（regist）→ 获取 token（applytoken）→ 携带 token 调用业务接口。

---

## 一、ECOLOGY 系统配置（在 OA 服务器端做）

### 1. 配置接口白名单
文件：`ecology/WEB-INF/prop/weaver_session_filter.properties`

```properties
checkurl=/api/hrm/emmanager;/api/userPhrase;
uncheckurl=/api/ec/dev/app/getCheckSystemInfo;/api/ec/dev/app/emjoin;
unchecksessionurl=/api/ec/dev/util/accesspage;.../api/loginportal/element/;/api/edc/fillin/;
```

- 把需要**免登录访问**的接口地址全路径追加到 `unchecksessionurl=` 后面，以英文分号 `;` 结尾。
- **自行开发的接口**需加到 `ecology/WEB-INF/prop/weaver_session_filter_dev.properties`。
- 改完**重启生效**。

### 2. 发放 / 生成许可证（appid）
向数据库插入一条记录即可（appid 用于身份认证）：

```sql
INSERT INTO ECOLOGY_BIZ_EC(ID, APPID, NAME)
VALUES('123456', 'test', '上海泛微网络科技股份有限公司');
COMMIT;
```

字段说明：
- `ID`：数据库主键，保证与其它系统发放的许可证主键不冲突（示例 `123456`）。
- `APPID`：许可证号码，最终发给异构系统，**多个 appid 必须唯一**（示例 `test`）。
- `NAME`：许可证名称，便于辨识发放方。

> ⚠️ 不要直接使用示例数据；插入后必须 `COMMIT`，且请求服务器对应的数据库就是插入记录的库，否则报「注册失败没有在找到正确的 APPID」。

### 3. 限制许可证使用 IP 地址
文件：`ecology/WEB-INF/prop/weaver_rest_token.properties`

```properties
# 限制 Rest API Token Invoke 注册端 IP 地址，多个用逗号分隔
allowIp=127.0.0.1,192.168.0.1,172.10.0.1,10.10.10.1
```

- 不设置 = 不限制任何 IP；**生产环境建议设置**。

---

## 二、异构系统编码实现认证（Java 三段式）

### 1. 引入 RSA 加密算法
- **Java**：直接用 OA 自带的 `ecology/WEB-INF/lib/hutool-all-5.3.0.jar`，或自行引用 hutool（https://hutool.cn/）。
- **C#**：参见官方 C# RSA 案例。
- 其它语言：自行实现 RSA（OPENSSL 格式公钥），在线测试可用各大 RSA 网站。

### 2. JAVA 演示代码（核心三段式）
```java
package weaver.demo;
import cn.hutool.core.util.CharsetUtil;
import cn.hutool.core.util.StrUtil;
import cn.hutool.crypto.asymmetric.KeyType;
import cn.hutool.crypto.asymmetric.RSA;
import cn.hutool.http.HttpRequest;
import cn.hutool.json.JSONUtil;
import java.util.HashMap; import java.util.Map; import java.util.Objects;

public class MainTest {
    private static final Map<String,String> SYSTEM_CACHE = new HashMap<>();
    // ecology 发放的许可证 appid
    private static final String APPID = "62acf88c-55d0-465c-b08d-99cd36271231";

    // 第一步：注册，拿回服务端公钥 spk 与密钥 secrit
    public static Map<String,Object> testRegist(String address){
        RSA rsa = new RSA();
        String publicKey = rsa.getPublicKeyBase64();
        String privateKey = rsa.getPrivateKeyBase64();
        SYSTEM_CACHE.put("LOCAL_PRIVATE_KEY",privateKey);
        SYSTEM_CACHE.put("LOCAL_PUBLIC_KEY",publicKey);
        String data = HttpRequest.post(address + "/api/ec/dev/auth/regist")
                .header("appid",APPID).header("cpk",publicKey)
                .timeout(2000).disableCookie().execute().body();
        Map<String,Object> datas = JSONUtil.parseObj(data);
        SYSTEM_CACHE.put("SERVER_PUBLIC_KEY",StrUtil.nullToEmpty((String)datas.get("spk")));
        SYSTEM_CACHE.put("SERVER_SECRET",StrUtil.nullToEmpty((String)datas.get("secrit")));
        return datas;
    }

    // 第二步：用 spk 加密 secret，换 token
    public static Map<String,Object> testGetoken(String address){
        String secret = SYSTEM_CACHE.get("SERVER_SECRET");
        String spk = SYSTEM_CACHE.get("SERVER_PUBLIC_KEY");
        if (Objects.isNull(secret)||Objects.isNull(spk)){ testRegist(address);
            secret = SYSTEM_CACHE.get("SERVER_SECRET"); spk = SYSTEM_CACHE.get("SERVER_PUBLIC_KEY"); }
        RSA rsa = new RSA(null,spk);
        String encryptSecret = rsa.encryptBase64(secret,CharsetUtil.CHARSET_UTF_8,KeyType.PublicKey);
        String data = HttpRequest.post(address+ "/api/ec/dev/auth/applytoken")
                .header("appid",APPID).header("secret",encryptSecret)
                .header("time","3600").disableCookie().execute().body();
        Map<String,Object> datas = JSONUtil.parseObj(data);
        SYSTEM_CACHE.put("SERVER_TOKEN",StrUtil.nullToEmpty((String)datas.get("token")));
        return datas;
    }

    // 第三步：带 token 调业务接口（GET 示例；POST 需设置 Content-Type）
    public static String testRestful(String address,String api,String jsonParams){
        String token= SYSTEM_CACHE.get("SERVER_TOKEN");
        if (StrUtil.isEmpty(token)){ token = (String) testGetoken(address).get("token"); }
        String spk = SYSTEM_CACHE.get("SERVER_PUBLIC_KEY");
        RSA rsa = new RSA(null,spk);
        String encryptUserid = rsa.encryptBase64("1",CharsetUtil.CHARSET_UTF_8,KeyType.PublicKey);
        String data = HttpRequest.disableCookie().get(address + api)
                .header("appid",APPID).header("token",token)
                .header("userid",encryptUserid).disableCookie()
                .body(jsonParams).execute().body();
        return data;
    }
}
```

---

## 三、jar 包冲突导致的问题
- **3.1 北森 jar 冲突**：`Beisen.OIDC.SDK.1.8.jar has unsigned entries` → 屏蔽该 jar 并重启测试；北森目前只能提供源码解决依赖冲突。
- **3.2 bcprov 问题**：`bcprov-jdk15on-1.68.jar has unsigned entries` → 替换为 1.68 最新版（需重启 ecology）。

---

## 四、常见疑问解答
- **4.1 公钥私钥有效期**：只要不被更新就永久有效；23 年之后的 KB 默认不更新，永久有效。
- **4.2 applytoken 一直解密失败**：先用 postman 测通；仍失败按「三、jar 冲突」排查。
- **4.3 regist 后之前的解密失败**：regist 不要多次调用；不同应用用多个 appid 隔离。
- **4.4 KB900210208 及更早版本**调 OA 接口一直 500（带 html 报错）：人力资源 `DoUserSessionCmd` 中 `request.getSession(true).invalidate()` 导致 session 被立刻移除，提交问题处理流程注释该行（新 KB 已删除）。
- **4.5 userid 不对**：三方调用时传递了 Cookie 导致接口未重新认证 → 代码层禁用 Cookie 传递（如 hutool 的 `disableCookie()`）。
- **4.6 集群环境频繁报 token 不存在/超时**：检查 redis 是否正常；可改为只用数据库存储 token。

---

## 认证时序（速查）
```
异构系统                           Ecology(OA)
   │                                    │
   │  1) POST /api/ec/dev/auth/regist   │
   │     header: appid, cpk(本系统公钥)  │
   ├──────────────────────────────────► │
   │◄──────── 返回 spk(系统公钥), secrit │
   │                                    │
   │  2) POST /api/ec/dev/auth/applytoken│
   │     header: appid,                  │
   │       secret=RSA(spk, secrit)       │
   ├──────────────────────────────────► │
   │◄──────────── 返回 token             │
   │                                    │
   │  3) GET/POST /api/<业务接口>        │
   │     header: appid, token,           │
   │       userid=RSA(spk, 用户id)       │
   ├──────────────────────────────────► │
   │◄──────────── 业务数据              │
```

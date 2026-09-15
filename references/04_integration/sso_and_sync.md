# 泛微OA (E-Cology) 第三方单点登录 (SSO) 与组织架构集成

本文档汇总钉钉 (DingTalk)、企业微信 (WeChat Work)、飞书 (Feishu) 以及标准 OAuth2 / CAS 与泛微 OA 进行单点登录与组织架构双向打通的标准方案。

---

## 1. 单点登录 (SSO) 集成模式

### 1.1 模式一：泛微移动端免登 (E-Mobile / 企微 / 钉钉 H5 免密进入)
- **原理**：第三方 App 打开 OA 页面时，在 URL 中携带第三方授权 code。
- **流程**：
  1. 第三方应用配置入口地址：`http://oa.company.com/sp/custom/cloudStoreSso?type=dingtalk`
  2. OA 后端过滤器获取临时 code，向钉钉/企微 API 换取用户工号 `userId`。
  3. OA 内部调用 `weaver.login.VerifyLogin` 创建 Session 并设置浏览器 Cookie，完成免密跳转。

### 1.2 模式二：外部系统单点登录进入 OA (Token 换取 Session)
通过自定义 SSO 校验接口：
```java
// 泛微后台单点登录无侵入拦截器
package com.custom.sso;

import weaver.general.BaseBean;
import weaver.login.VerifyLogin;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class CustomSsoHandler extends BaseBean {
    public boolean doAutoLogin(String thirdToken, HttpServletRequest request, HttpServletResponse response) {
        // 1. 调用第三方系统鉴权接口校验 thirdToken 合法性
        String workcode = queryWorkcodeByThirdToken(thirdToken);
        if (workcode != null) {
            // 2. 获取对应的 Ecology 用户 ID 并注入会话
            VerifyLogin verifyLogin = new VerifyLogin();
            verifyLogin.getUser(workcode, request, response);
            return true;
        }
        return false;
    }
}
```

---

## 2. 钉钉/企业微信/飞书通讯录实时同步策略

1. **增量监听（WebHook 模式，推荐）**：
   - 在钉钉/企微管理后台配置通讯录变更 WebHook 回调 URL（如 `/api/custom/sync/webhook`）。
   - 监听事件：`user_add`, `user_modify`, `user_leave`, `org_dept_create`, `org_dept_modify`。
   - 收到事件后实时更新 `HrmResource` / `HrmDepartment` 并调用泛微 `ResourceCominfo.removeResourceCache()` 刷新缓存。
2. **全量定时校验（BaseCronJob 模式）**：
   - 每天凌晨 2 点执行定时任务，从第三方拉取全量部门人员比对差异，确保数据一致性。

# 集成与扩展总索引

> 覆盖 WebService (SOAP)、Java 后端二次开发、消息中心推送、第三方单点登录与组织架构同步。

> 索引由 `scripts/build_index.py` 自动生成，请勿手工编辑。
> 检索请用统一检索脚本：
> ```bash
> python scripts/search.py 钉钉 --scope int
> python scripts/search.py BaseCronJob --scope int
> ```

## 泛微OA (E-Cology 9) 后端 Java 二次开发实战指南

> 文件：[`custom_backend_dev.md`](./custom_backend_dev.md)

- 1. 流程自定义 Action 开发 (`Action`)
- 2. 数据库访问与事务管理 (`RecordSet` / `RecordSetTrans`)
- 3. 定时调度任务开发 (`BaseCronJob`)
- 4. 自定义 RESTful WebService 开发 (JAX-RS)
- 5. 常用数据字典与核心系统表对照

## 泛微OA (E-Cology 9) 消息中心与第三方推送开发指南

> 文件：[`message_push.md`](./message_push.md)

- E9二开、第三方系统推送消息 KB1908以后
- 四、补充：

## 泛微OA (E-Cology) 第三方单点登录 (SSO) 与组织架构集成

> 文件：[`sso_and_sync.md`](./sso_and_sync.md)

- 1. 单点登录 (SSO) 集成模式
- 2. 钉钉/企业微信/飞书通讯录实时同步策略

## 泛微OA (E-Cology) WebService (SOAP) 接口开发规范与指南

> 文件：[`webservice_soap.md`](./webservice_soap.md)

- 1. 核心 WebService 接口服务清单
- 2. 前置准备与 IP 白名单配置
- 3. WorkflowService 核心方法详解
- 4. DocService 创建文档与附件上传 (`createDoc`)

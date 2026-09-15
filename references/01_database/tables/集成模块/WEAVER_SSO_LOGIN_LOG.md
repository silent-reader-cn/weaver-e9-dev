# 泛微OA 数据表: `WEAVER_SSO_LOGIN_LOG`

- **所属模块**: `集成模块`
- **数据库表名**: `WEAVER_SSO_LOGIN_LOG`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识 | `integer` | - | 否 | 标识 |
| 2 | `appid` | 应用标识 | `varchar2` | 100 | 是 | 应用标识 |
| 3 | `loginid` | 登录账号 | `varchar2` | 100 | 是 | 登录账号 |
| 4 | `apploginid` | 应用账号 | `varchar2` | 100 | 是 | 应用账号 |
| 5 | `createdate` | 创建日期 | `varchar2` | 10 | 是 | 创建日期 |
| 6 | `createtime` | 创建时间 | `varchar2` | 8 | 是 | 创建时间 |
| 7 | `ts` | token | `varchar2` | 20 | 是 | 加密的串 |
| 8 | `isuse` | 是否使用 | `varchar2` | 20 | 是 | 是否使用:1,使用;0,未使用 |
| 9 | `ip` | 客户端ip | `varchar2` | 100 | 是 | 客户端ip |

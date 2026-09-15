# 泛微OA 数据表: `WEAVER_SSO_USER_MAPPING`

- **所属模块**: `集成模块`
- **数据库表名**: `WEAVER_SSO_USER_MAPPING`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识 | `integer` | - | 否 | 标识 |
| 2 | `appid` | 应用标识 | `varchar2` | 100 | 是 | 应用标识 |
| 3 | `userid` | 用户标识 | `integer` | - | 是 | 用户标识 |
| 4 | `loginid` | 登录账号 | `varchar2` | 100 | 是 | 登录账号 |
| 5 | `apploginid` | 应用账号 | `varchar2` | 100 | 是 | 应用账号 |
| 6 | `createdate` | 创建日期 | `varchar2` | 10 | 是 | 创建日期 |
| 7 | `createtime` | 创建时间 | `varchar2` | 8 | 是 | 创建时间 |
| 8 | `modifydate` | 修改日期 | `varchar2` | 10 | 是 | 修改日期 |
| 9 | `modifytime` | 修改时间 | `varchar2` | 8 | 是 | 修改时间 |

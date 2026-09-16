# 泛微OA 数据表: `int_webseal_setting`

- **中文名称**: WebSEAL集成配置表
- **所属模块**: `集成模块`
- **数据库表名**: `int_webseal_setting`
- **主键**: `无`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `IsUse` | 启用 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是，0：否(默认值) |
| 2 | `WebSealParamMethod` | WebSEAL参数获取方法 | `varchar2` | 10 | 是 | 否 | 否 | - | - | WebSEAL参数获取方法 |
| 3 | `WebSealParamName` | 参数名称 | `varchar2` | 500 | 是 | 否 | 否 | - | - | 参数名称 |
| 4 | `EcologyLoginPage` | Ecology登录地址 | `varchar2` | 500 | 是 | 否 | 否 | - | - | Ecology登录地址 |
| 5 | `EcologyLogoutPage` | Ecology退出地址 | `varchar2` | 500 | 是 | 否 | 否 | - | - | Ecology退出地址 |
| 6 | `AccountType` | 账号规则 | `varchar2` | 50 | 是 | 否 | 否 | - | - | loginid：登录账号(默认值)， certificatenum：身份证号码， id：人员ID， workcode：人员编号， email：电子邮箱， mobile：手机号码， customsql：自定义sql |
| 7 | `customsql` | 自定义sql | `varchar2` | 2000 | 是 | 否 | 否 | - | - | 自定义sql |

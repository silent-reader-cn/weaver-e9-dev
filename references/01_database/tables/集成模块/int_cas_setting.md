# 泛微OA 数据表: `int_cas_setting`

- **中文名称**: cas集成配置表
- **所属模块**: `集成模块`
- **数据库表名**: `int_cas_setting`
- **主键**: `无`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `IsUse` | 启用 | `integer` | - | 是 | 否 | 否 | - | - | 1：是 0：否，默认值 |
| 2 | `CasServerUrl` | CAS Server地址 | `varchar2` | 500 | 是 | 否 | 否 | - | - | CAS Server地址 |
| 3 | `CasServerLoginPage` | CAS Server登录地址 | `varchar2` | 500 | 是 | 否 | 否 | - | - | CAS Server登录地址 |
| 4 | `CasServerLogoutPage` | CAS Server退出地址 | `varchar2` | 500 | 是 | 否 | 否 | - | - | CAS Server退出地址 |
| 5 | `EcologyLoginPage` | Ecology登录地址 | `varchar2` | 500 | 是 | 否 | 否 | - | - | Ecology登录地址 |
| 6 | `PcAuth` | PcAuth | `integer` | - | 是 | 否 | 否 | - | - | 1：是 0：否，默认值 |
| 7 | `AppAuth` | AppAuth | `integer` | - | 是 | 否 | 否 | - | - | 1：是 0：否，默认值 |
| 8 | `AccountType` | AccountType | `integer` | - | 是 | 否 | 否 | - | - | 1:loginid：登录账号，默认值 2:certificatenum：身份证号码 3:id：人员ID 4:workcode：人员编号 5:email：电子邮箱 6:mobile：手机号码 7:customsql：自定义sql |
| 9 | `customsql` | customsql | `varchar2` | 2000 | 是 | 否 | 否 | - | - | customsql |

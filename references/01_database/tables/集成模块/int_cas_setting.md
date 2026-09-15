# 泛微OA 数据表: `int_cas_setting`

- **所属模块**: `集成模块`
- **数据库表名**: `int_cas_setting`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `IsUse` | 启用 | `integer` | - | 是 | 1：是 0：否，默认值 |
| 2 | `CasServerUrl` | CAS Server地址 | `varchar2` | 500 | 是 | CAS Server地址 |
| 3 | `CasServerLoginPage` | CAS Server登录地址 | `varchar2` | 500 | 是 | CAS Server登录地址 |
| 4 | `CasServerLogoutPage` | CAS Server退出地址 | `varchar2` | 500 | 是 | CAS Server退出地址 |
| 5 | `EcologyLoginPage` | Ecology登录地址 | `varchar2` | 500 | 是 | Ecology登录地址 |
| 6 | `PcAuth` | PcAuth | `integer` | - | 是 | 1：是 0：否，默认值 |
| 7 | `AppAuth` | AppAuth | `integer` | - | 是 | 1：是 0：否，默认值 |
| 8 | `AccountType` | AccountType | `integer` | - | 是 | 1:loginid：登录账号，默认值 2:certificatenum：身份证号码 3:id：人员ID 4:workcode：人员编号 5:email：电子邮箱 6:mobile：手机号码 7:customsql：自定义sql |
| 9 | `customsql` | customsql | `varchar2` | 2000 | 是 | customsql |

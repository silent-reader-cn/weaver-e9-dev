# 泛微OA 数据表: `ldap_sync`

- **所属模块**: `集成模块`
- **数据库表名**: `ldap_sync`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `ldapid` | LDAP标识 | `varchar2` | 800 | 否 | LDAP标识 |
| 3 | `syncorg` | 是否同步组织架构 | `char` | 1 | 是 | 1:同步，0不同步 |
| 4 | `syncuser` | 是否同步人员 | `char` | 1 | 是 | 1:同步，0不同步 |
| 5 | `subcompanyid` | 分部ID | `integer` | - | 是 | 分部ID |
| 6 | `departmentid` | 部门ID | `integer` | - | 是 | 部门ID |
| 7 | `basedomain` | 基础域 | `varchar2` | 1000 | 是 | 基础域 |
| 8 | `ischeckused` | 是否检查用户禁用状态 | `char` | 1 | 是 | 1:检查，0:不检查 |
| 9 | `orgfilter` | 组织架构同步条件 | `varchar2` | 1000 | 是 | 组织架构同步条件 |
| 10 | `userfilter` | 人员同步条件 | `varchar2` | 1000 | 是 | 人员同步条件 |
| 11 | `synctype` | 同步类型 | `char` | 1 | 是 | 1:正向同步，0:反向同步 |

# 泛微OA 数据表: `contract_shareinfo`

- **中文名称**: 合同共享信息表
- **所属模块**: `客户管理`
- **数据库表名**: `contract_shareinfo`
- **主键**: `id`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | id |
| 2 | `relateditemid` | 相关项目id | `integer` | - | 是 | 否 | 否 | - | - | 相关项目id |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 否 | 否 | - | - | 1、人力资源；2、部门+安全级别；3、角色+安全级别；4、所有人 |
| 4 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别 |
| 5 | `rolelevel` | 角色等级 | `integer` | - | 是 | 否 | 否 | - | - | 0、部门；1、分部；2、总部 |
| 6 | `sharelevel` | 共享等级 | `integer` | - | 是 | 否 | 否 | - | - | 1、查看；2、编辑 |
| 7 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | 用户id |
| 8 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | 部门id |
| 9 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | 角色id |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | 否 | 否 | - | - | 所有人 |
| 11 | `crmid` | 客户id | `integer` | - | 是 | 否 | 否 | - | - | 客户id |
| 12 | `seclevelmax` | 最大级别 | `integer` | - | 是 | 否 | 否 | - | 100 | 最大级别 |
| 13 | `isdefault` | 是否默认 | `char` | 1 | 是 | 否 | 否 | - | - | 是否默认 |
| 14 | `subcompanyid` | 分部ID | `integer` | - | 是 | 否 | 否 | - | - | 分部ID |

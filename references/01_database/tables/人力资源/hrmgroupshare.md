# 泛微OA 数据表: `hrmgroupshare`

- **中文名称**: 自定义组共享表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmgroupshare`
- **主键**: `id`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `groupid` | 组id | `integer` | - | 是 | 否 | 否 | - | - | 组id |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 否 | 否 | - | - | 共享类型 |
| 4 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别 |
| 5 | `rolelevel` | 角色等级 | `integer` | - | 是 | 否 | 否 | - | - | 角色等级 |
| 6 | `sharelevel` | 共享等级 | `integer` | - | 是 | 否 | 否 | - | - | 共享等级 |
| 7 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | 用户id |
| 8 | `subcompanyid` | 分公司id | `integer` | - | 是 | 否 | 否 | - | - | 分公司id |
| 9 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | 部门id |
| 10 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | 角色id |
| 11 | `foralluser` | 所有用户 | `integer` | - | 是 | 否 | 否 | - | - | 所有用户 |
| 12 | `crmid` | 客户id | `integer` | - | 是 | 否 | 否 | - | - | 客户id |
| 13 | `jobtitleid` | 岗位id | `integer` | - | 是 | 否 | 否 | - | - | 岗位id |
| 14 | `jobtitlelevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | - | 岗位级别 |
| 15 | `scopeid` | 共享范围id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 共享范围id |
| 16 | `seclevelto` | seclevelto | `integer` | - | 是 | 否 | 否 | - | - | seclevelto |
| 17 | `alllevel` | alllevel | `integer` | - | 是 | 否 | 否 | - | - | alllevel |

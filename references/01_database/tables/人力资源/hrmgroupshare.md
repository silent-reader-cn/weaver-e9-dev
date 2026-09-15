# 泛微OA 数据表: `hrmgroupshare`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmgroupshare`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `groupid` | 组id | `integer` | - | 是 | 组id |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 共享类型 |
| 4 | `seclevel` | 安全级别 | `integer` | - | 是 | 安全级别 |
| 5 | `rolelevel` | 角色等级 | `integer` | - | 是 | 角色等级 |
| 6 | `sharelevel` | 共享等级 | `integer` | - | 是 | 共享等级 |
| 7 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 8 | `subcompanyid` | 分公司id | `integer` | - | 是 | 分公司id |
| 9 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 10 | `roleid` | 角色id | `integer` | - | 是 | 角色id |
| 11 | `foralluser` | 所有用户 | `integer` | - | 是 | 所有用户 |
| 12 | `crmid` | 客户id | `integer` | - | 是 | 客户id |
| 13 | `jobtitleid` | 岗位id | `integer` | - | 是 | 岗位id |
| 14 | `jobtitlelevel` | 岗位级别 | `integer` | - | 是 | 岗位级别 |
| 15 | `scopeid` | 共享范围id | `varchar2` | 4000 | 是 | 共享范围id |
| 16 | `seclevelto` | seclevelto | `integer` | - | 是 | seclevelto |
| 17 | `alllevel` | alllevel | `integer` | - | 是 | alllevel |

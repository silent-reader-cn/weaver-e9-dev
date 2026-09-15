# 泛微OA 数据表: `prj_shareinfo`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_shareinfo`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `relateditemid` | 项目id | `integer` | - | 是 | 项目id |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 共享类型 |
| 4 | `seclevel` | 安全级别(下限) | `integer` | - | 是 | 安全级别(下限) |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | 角色级别 |
| 6 | `sharelevel` | 权限 | `integer` | - | 是 | 权限 |
| 7 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 8 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 9 | `roleid` | 角色id | `integer` | - | 是 | 角色id |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | 所有人 |
| 11 | `crmid` | 客户id | `integer` | - | 是 | 客户id |
| 12 | `subcompanyid` | 分部 | `integer` | - | 是 | 分部 |
| 13 | `isdefault` | 是否默认 | `integer` | - | 是 | 是否默认 |
| 14 | `seclevelmax` | 安全级别(上限) | `integer` | - | 是 | 安全级别(上限) |
| 15 | `jobtitleid` | 岗位对象id | `integer` | - | 是 | - |
| 16 | `joblevel` | 岗位级别 | `integer` | - | 是 | - |
| 17 | `scopeid` | 0 | `varchar2` | 800 | 是 | - |

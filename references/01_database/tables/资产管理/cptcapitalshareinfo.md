# 泛微OA 数据表: `cptcapitalshareinfo`

- **所属模块**: `资产管理`
- **数据库表名**: `cptcapitalshareinfo`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `relateditemid` | 资产id | `integer` | - | 是 | 资产id |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 共享类型 |
| 4 | `seclevel` | 安全级别 | `integer` | - | 是 | 安全级别 |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | 角色级别 |
| 6 | `sharelevel` | 权限 | `integer` | - | 是 | 权限 |
| 7 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 8 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 9 | `roleid` | 角色id | `integer` | - | 是 | 角色id |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | 所有人 |
| 11 | `crmid` | 客户id | `integer` | - | 是 | 客户id |
| 12 | `sharefrom` | 来自于 | `integer` | - | 是 | 从资产组同步共享来的,此字段是一级资产组id |
| 13 | `subcompanyid` | 分部 | `integer` | - | 是 | 分部 |
| 14 | `isdefault` | 是否默认 | `integer` | - | 是 | 是否默认 |
| 15 | `seclevelmax` | 最大安全级别 | `integer` | - | 是 | - |
| 16 | `jobtitleid` | 岗位id | `integer` | - | 是 | - |
| 17 | `joblevel` | 岗位级别 | `integer` | - | 是 | - |
| 18 | `scopeid` | 0 | `varchar2` | 800 | 是 | - |

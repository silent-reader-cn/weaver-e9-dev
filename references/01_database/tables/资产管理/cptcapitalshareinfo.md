# 泛微OA 数据表: `cptcapitalshareinfo`

- **中文名称**: 资产共享
- **所属模块**: `资产管理`
- **数据库表名**: `cptcapitalshareinfo`
- **主键**: `id`
- **字段数**: `18`

> 说明：资产权限表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 否 | 否 | - | - | 标识列 |
| 2 | `relateditemid` | 资产id | `integer` | - | 是 | 否 | 否 | - | - | 资产id |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 否 | 否 | - | - | 共享类型 |
| 4 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别 |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | 角色级别 |
| 6 | `sharelevel` | 权限 | `integer` | - | 是 | 否 | 否 | - | - | 权限 |
| 7 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | 用户id |
| 8 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | 部门id |
| 9 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | 角色id |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | 否 | 否 | - | - | 所有人 |
| 11 | `crmid` | 客户id | `integer` | - | 是 | 否 | 否 | - | 0 | 客户id |
| 12 | `sharefrom` | 来自于 | `integer` | - | 是 | 否 | 否 | - | - | 从资产组同步共享来的,此字段是一级资产组id |
| 13 | `subcompanyid` | 分部 | `integer` | - | 是 | 否 | 否 | - | - | 分部 |
| 14 | `isdefault` | 是否默认 | `integer` | - | 是 | 否 | 否 | - | - | 是否默认 |
| 15 | `seclevelmax` | 最大安全级别 | `integer` | - | 是 | 否 | 否 | - | 100 | - |
| 16 | `jobtitleid` | 岗位id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 17 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 18 | `scopeid` | 0 | `varchar2` | 800 | 是 | 否 | 否 | - | 0 | - |

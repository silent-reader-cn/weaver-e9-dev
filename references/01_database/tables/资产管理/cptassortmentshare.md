# 泛微OA 数据表: `cptassortmentshare`

- **中文名称**: 资产组共享
- **所属模块**: `资产管理`
- **数据库表名**: `cptassortmentshare`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 否 | 否 | - | - | 标识列 |
| 2 | `assortmentid` | 资产组id | `integer` | - | 是 | 否 | 否 | - | - | 资产组id |
| 3 | `sharetype` | 对象类型 | `integer` | - | 是 | 否 | 否 | - | - | 对象类型 |
| 4 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别 |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | 角色级别 |
| 6 | `sharelevel` | 权限 | `integer` | - | 是 | 否 | 否 | - | - | 权限 |
| 7 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | 用户id |
| 8 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | 部门id |
| 9 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | 角色id |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | 否 | 否 | - | - | 所有人 |
| 11 | `crmid` | 客户id | `integer` | - | 是 | 否 | 否 | - | 0 | 客户id |
| 12 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | 分部id |
| 13 | `seclevelmax` | 最大安全级别 | `integer` | - | 是 | 否 | 否 | - | 100 | - |
| 14 | `jobtitleid` | 岗位id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 15 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 16 | `scopeid` | 0 | `varchar2` | 800 | 是 | 否 | 否 | - | 0 | - |

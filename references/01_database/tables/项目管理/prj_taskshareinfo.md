# 泛微OA 数据表: `prj_taskshareinfo`

- **中文名称**: 项目任务共享
- **所属模块**: `项目管理`
- **数据库表名**: `prj_taskshareinfo`
- **主键**: `id`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 否 | 否 | - | - | 标识列 |
| 2 | `relateditemid` | 任务id | `integer` | - | 是 | 否 | 否 | - | - | 任务id |
| 3 | `sharetype` | 对象类型 | `integer` | - | 是 | 否 | 否 | - | - | 对象类型 |
| 4 | `seclevel` | 安全级别(下限) | `integer` | - | 是 | 否 | 否 | - | - | 安全级别(下限) |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | 角色级别 |
| 6 | `sharelevel` | 权限 | `integer` | - | 是 | 否 | 否 | - | - | 权限 |
| 7 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | 用户id |
| 8 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | 部门id |
| 9 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | 角色id |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | 否 | 否 | - | - | 所有人 |
| 11 | `crmid` | 客户id | `integer` | - | 是 | 否 | 否 | - | - | 客户id |
| 12 | `sharefrom` | 备用字段 | `integer` | - | 是 | 否 | 否 | - | - | 备用字段 |
| 13 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | 分部id |
| 14 | `seclevelmax` | 安全级别(上限) | `integer` | - | 是 | 否 | 否 | - | 100 | 安全级别(上限) |
| 15 | `jobtitleid` | 岗位对象id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 16 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 17 | `scopeid` | 0 | `varchar2` | 800 | 是 | 否 | 否 | - | 0 | - |

# 泛微OA 数据表: `workplancreateshareset`

- **中文名称**: 日程创建人共享
- **所属模块**: `日程管理`
- **数据库表名**: `workplancreateshareset`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `companyvirtual` | 维度 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 维度 |
| 2 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | id |
| 3 | `planid` | 共享日程类型 | `integer` | - | 是 | 否 | 否 | - | - | 共享日程类型 |
| 4 | `sharetype` | 共享对象类型 | `integer` | - | 是 | 否 | 否 | - | - | 2：分部，3：部门，4：角色，5：所有人，6：所有上级 |
| 5 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别 |
| 6 | `seclevelmax` | 最大安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 最大安全级别 |
| 7 | `rolelevel` | 角色等级 | `integer` | - | 是 | 否 | 否 | - | - | 角色等级 |
| 8 | `sharelevel` | 共享级别 | `integer` | - | 是 | 否 | 否 | - | - | 共享级别 |
| 9 | `userid` | 人力资源id | `integer` | - | 是 | 否 | 否 | - | - | 人力资源id |
| 10 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | 分部id |
| 11 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | 部门id |
| 12 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | 角色id |
| 13 | `suserid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | 用户id |
| 14 | `jobtitleid` | 共享岗位id | `integer` | - | 是 | 否 | 否 | - | - | 共享岗位id |
| 15 | `joblevel` | 共享岗位级别 | `integer` | - | 是 | 否 | 否 | - | - | 0:总部 1:分部 2:部门 |
| 16 | `joblevelvalue` | 共享岗位对象 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 共享岗位对象 |

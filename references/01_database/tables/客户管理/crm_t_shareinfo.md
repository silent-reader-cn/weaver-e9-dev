# 泛微OA 数据表: `crm_t_shareinfo`

- **中文名称**: 客户交易共享信息表
- **所属模块**: `客户管理`
- **数据库表名**: `crm_t_shareinfo`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | id |
| 2 | `relateditemid` | 相关联对象ID | `integer` | - | 是 | 否 | 否 | - | - | 相关联对象ID |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 否 | 否 | - | - | 共享类型 |
| 4 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别 |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | 角色级别 |
| 6 | `sharelevel` | 共享级别 | `integer` | - | 是 | 否 | 否 | - | - | 共享级别 |
| 7 | `userid` | 人员id | `integer` | - | 是 | 否 | 否 | - | - | 人员ID |
| 8 | `departmentid` | 部门ID | `integer` | - | 是 | 否 | 否 | - | - | 部门ID |
| 9 | `roleid` | 角色ID | `integer` | - | 是 | 否 | 否 | - | - | 角色ID |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | 否 | 否 | - | - | 所有人 |
| 11 | `crmid` | 客户id | `integer` | - | 是 | 否 | 否 | - | - | 客户id |
| 12 | `subcompanyid` | 分部ID | `integer` | - | 是 | 否 | 否 | - | - | 分部id |
| 13 | `seclevelmax` | 最大级别 | `integer` | - | 是 | 否 | 否 | - | 100 | 最大级别 |
| 14 | `jobtitleid` | 岗位ID | `integer` | - | 是 | 否 | 否 | - | 0 | 岗位id |
| 15 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | 0 | 岗位级别 |
| 16 | `scopeid` | 所包含的下级 | `varchar2` | 800 | 是 | 否 | 否 | - | 0 | 所包含的下级 |

# 泛微OA 数据表: `crm_t_shareinfo`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_t_shareinfo`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `relateditemid` | 相关联对象ID | `integer` | - | 是 | 相关联对象ID |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 共享类型 |
| 4 | `seclevel` | 安全级别 | `integer` | - | 是 | 安全级别 |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | 角色级别 |
| 6 | `sharelevel` | 共享级别 | `integer` | - | 是 | 共享级别 |
| 7 | `userid` | 人员id | `integer` | - | 是 | 人员ID |
| 8 | `departmentid` | 部门ID | `integer` | - | 是 | 部门ID |
| 9 | `roleid` | 角色ID | `integer` | - | 是 | 角色ID |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | 所有人 |
| 11 | `crmid` | 客户id | `integer` | - | 是 | 客户id |
| 12 | `subcompanyid` | 分部ID | `integer` | - | 是 | 分部id |
| 13 | `seclevelmax` | 最大级别 | `integer` | - | 是 | 最大级别 |
| 14 | `jobtitleid` | 岗位ID | `integer` | - | 是 | 岗位id |
| 15 | `joblevel` | 岗位级别 | `integer` | - | 是 | 岗位级别 |
| 16 | `scopeid` | 所包含的下级 | `varchar2` | 800 | 是 | 所包含的下级 |

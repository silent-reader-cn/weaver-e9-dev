# 泛微OA 数据表: `crm_shareinfo`

- **中文名称**: 客户共享信息表
- **所属模块**: `客户管理`
- **数据库表名**: `crm_shareinfo`
- **主键**: `id`
- **字段数**: `20`

> 说明：客户卡片查看权限

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | 0 | 否 | 否 | 否 | - | - | 主键 |
| 2 | `relateditemid` | 相关客户id | `integer` | 0 | 是 | 否 | 否 | - | - | CRM_customerinfo的id |
| 3 | `sharetype` | 共享类型 | `integer` | 0 | 是 | 否 | 否 | - | - | 1：人力资源；2：部门；3：角色；4：所有人；5：分部；6：岗位； |
| 4 | `seclevel` | 最低安全级别 | `integer` | 0 | 是 | 否 | 否 | - | - | 最低安全级别 |
| 5 | `rolelevel` | 角色级别 | `integer` | 0 | 是 | 否 | 否 | - | - | 角色级别 |
| 6 | `sharelevel` | 共享级别 | `integer` | 0 | 是 | 否 | 否 | - | - | 2：编辑；1：查看 |
| 7 | `userid` | 用户id | `integer` | 0 | 是 | 否 | 否 | - | - | 用户id |
| 8 | `departmentid` | 部门id | `integer` | 0 | 是 | 否 | 否 | - | - | 部门id |
| 9 | `roleid` | 角色id | `integer` | 0 | 是 | 否 | 否 | - | - | 角色id |
| 10 | `foralluser` | 0 | `integer` | 0 | 是 | 否 | 否 | - | - | 0 |
| 11 | `crmid` | 客户id | `integer` | 0 | 是 | 否 | 否 | - | 0 | 客户id |
| 12 | `isdefault` | 默认共享 | `char` | 0 | 是 | 否 | 否 | - | - | 1：默认 |
| 13 | `deptorcomid` | 0 | `integer` | 0 | 是 | 否 | 否 | - | - | 0 |
| 14 | `contents` | 对象id | `integer` | 0 | 是 | 否 | 否 | - | - | 对象id（人力、部门、分部、角色、岗位、所有人） |
| 15 | `subcompanyid` | 分部id | `integer` | 0 | 是 | 否 | 否 | - | - | 分部id |
| 16 | `deleted` | 是否删除 | `integer` | 0 | 是 | 否 | 否 | - | 0 | 1：删除；0：未删除 |
| 17 | `seclevelmax` | 最大安全级别 | `integer` | 0 | 是 | 否 | 否 | - | 100 | 最大安全级别 |
| 18 | `jobtitleid` | 岗位id | `integer` | 0 | 是 | 否 | 否 | - | 0 | 岗位id |
| 19 | `joblevel` | 岗位级别 | `integer` | 0 | 是 | 否 | 否 | - | 0 | 1：指定部门；2：指定分部；0：总部 |
| 20 | `scopeid` | 0 | `varchar2` | 100 | 是 | 否 | 否 | - | 0 | 部门、分部id |

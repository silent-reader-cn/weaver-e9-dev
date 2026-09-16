# 泛微OA 数据表: `hrmcontractshare`

- **中文名称**: 人力资源合同提醒表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmcontractshare`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `sharetype` | 提醒类型 | `integer` | - | 是 | 否 | 否 | - | - | 人力资源、分部、部门、角色、岗位所有人 |
| 3 | `seclevel` | 安全级别从 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `sharelevel` | 提醒级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `userid` | 人员id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `seclevelto` | 安全级别到 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `jobtitleid` | 岗位id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `jobtitlelevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `jobdepartment` | 岗位指定部门 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `jobsubcompany` | 岗位指定分部 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `lowerlevel` | 是否含下级 | `integer` | - | 是 | 否 | 否 | - | - | - |

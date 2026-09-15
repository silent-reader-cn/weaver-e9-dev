# 泛微OA 数据表: `hrmcontractshare`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcontractshare`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `sharetype` | 提醒类型 | `integer` | - | 是 | 人力资源、分部、部门、角色、岗位所有人 |
| 3 | `seclevel` | 安全级别从 | `integer` | - | 是 | - |
| 4 | `rolelevel` | 角色级别 | `integer` | - | 是 | - |
| 5 | `sharelevel` | 提醒级别 | `integer` | - | 是 | - |
| 6 | `userid` | 人员id | `integer` | - | 是 | - |
| 7 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 8 | `departmentid` | 部门id | `integer` | - | 是 | - |
| 9 | `roleid` | 角色id | `integer` | - | 是 | - |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | - |
| 11 | `seclevelto` | 安全级别到 | `integer` | - | 是 | - |
| 12 | `jobtitleid` | 岗位id | `integer` | - | 是 | - |
| 13 | `jobtitlelevel` | 岗位级别 | `integer` | - | 是 | - |
| 14 | `jobdepartment` | 岗位指定部门 | `integer` | - | 是 | - |
| 15 | `jobsubcompany` | 岗位指定分部 | `integer` | - | 是 | - |
| 16 | `lowerlevel` | 是否含下级 | `integer` | - | 是 | - |

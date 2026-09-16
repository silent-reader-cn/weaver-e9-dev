# 泛微OA 数据表: `meetingtype_share`

- **中文名称**: 会议类型共享权限控制
- **所属模块**: `会议管理`
- **数据库表名**: `meetingtype_share`
- **主键**: `id`
- **字段数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `mtid` | 会议类型id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `permissiontype` | 权限类型 | `integer` | - | 是 | 否 | 否 | - | - | 1:部门安全级别<br>3:所有人安全级别<br>5:人力资源<br>6:分部 安全级别 |
| 4 | `seclevel` | 所有人安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `deptlevel` | 部门安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `sublevel` | 分部 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `userid` | 人力资源用户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `describ` | 说明 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `seclevelmax` | 所有人最高安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `deptlevelmax` | 部门最高安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `sublevelmax` | 分部最高安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `rolelevel` | 角色等级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `roleseclevel` | 角色安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `roleseclevelmax` | 角色最高安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `jobtitleid` | 岗位id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | - | 0:总部 1:分部 2:部门 |
| 20 | `joblevelvalue` | 岗位对象 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `meetingcaller`

- **中文名称**: 会议类型默认召集人
- **所属模块**: `会议管理`
- **数据库表名**: `meetingcaller`
- **主键**: `id`
- **字段数**: `14`

> 说明：会议类型关联默认召集人

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `meetingtype` | 会议类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `callertype` | 召集人类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `rolelevel` | 角色等级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `userid` | 召集人id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `foralluser` | 所有人 | `integer` | - | 是 | 否 | 否 | - | - | 已废弃 |
| 10 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `seclevelmax` | 最高安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `jobtitleid` | 岗位id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | - | 0:总部 1:分部 2:部门 |
| 14 | `joblevelvalue` | 岗位对象 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

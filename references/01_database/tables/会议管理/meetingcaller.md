# 泛微OA 数据表: `meetingcaller`

- **所属模块**: `会议管理`
- **数据库表名**: `meetingcaller`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `meetingtype` | 会议类型 | `integer` | - | 是 | - |
| 3 | `callertype` | 召集人类型 | `integer` | - | 是 | - |
| 4 | `seclevel` | 安全级别 | `integer` | - | 是 | - |
| 5 | `rolelevel` | 角色等级 | `integer` | - | 是 | - |
| 6 | `userid` | 召集人id | `integer` | - | 是 | - |
| 7 | `departmentid` | 部门id | `integer` | - | 是 | - |
| 8 | `roleid` | 角色id | `integer` | - | 是 | - |
| 9 | `foralluser` | 所有人 | `integer` | - | 是 | 已废弃 |
| 10 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 11 | `seclevelmax` | 最高安全级别 | `integer` | - | 是 | - |
| 12 | `jobtitleid` | 岗位id | `integer` | - | 是 | - |
| 13 | `joblevel` | 岗位级别 | `integer` | - | 是 | 0:总部 1:分部 2:部门 |
| 14 | `joblevelvalue` | 岗位对象 | `varchar2` | 1000 | 是 | - |

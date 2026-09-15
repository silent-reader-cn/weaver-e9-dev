# 泛微OA 数据表: `meetingshareset`

- **所属模块**: `会议管理`
- **数据库表名**: `meetingshareset`
- **字段总数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `meetingtype` | 会议类型id | `varchar2` | 1000 | 是 | 会议类型id |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 1：指定人 2：分部 3：部门 4：角色 5：所有人 8: 岗位 10:会议信息字段 11:会议服务字段 12:会议议程字段 |
| 4 | `seclevel` | 所有人安全级别 | `integer` | - | 是 | 所有人安全级别 |
| 5 | `seclevelmax` | 所有人最高安全级别 | `integer` | - | 是 | 所有人最高安全级别 |
| 6 | `departmentid` | 部门id | `varchar2` | 1000 | 是 | 部门id |
| 7 | `deptlevel` | 部门安全级别 | `integer` | - | 是 | 部门安全级别 |
| 8 | `deptlevelmax` | 部门最高安全级别 | `integer` | - | 是 | 部门最高安全级别 |
| 9 | `subcompanyid` | 分部id | `varchar2` | 1000 | 是 | 分部id |
| 10 | `sublevel` | 分部 安全级别 | `integer` | - | 是 | 分部 安全级别 |
| 11 | `sublevelmax` | 分部最高安全级别 | `integer` | - | 是 | 分部最高安全级别 |
| 12 | `has_child` | 是否含下级 | `integer` | - | 是 | 0:不含 1:包含 |
| 13 | `userid` | 人力资源 | `varchar2` | 1000 | 是 | 人力资源 |
| 14 | `fieldids` | 自定义字段ID | `varchar2` | 1000 | 是 | 针对shareType=10/11/12的时候记录对应自定义字段 |
| 15 | `roleid` | 角色id | `varchar2` | 1000 | 是 | 角色id |
| 16 | `rolelevel` | 角色等级 | `integer` | - | 是 | 角色等级 |
| 17 | `roleseclevel` | 角色安全级别 | `integer` | - | 是 | 角色安全级别 |
| 18 | `roleseclevelmax` | 角色最高安全级别 | `integer` | - | 是 | 角色最高安全级别 |
| 19 | `jobtitleid` | 岗位id | `varchar2` | 1000 | 是 | 岗位id |
| 20 | `joblevel` | 岗位级别 | `integer` | - | 是 | 0:总部 1:分部 2:部门 |
| 21 | `joblevelvalue` | 岗位对象 | `varchar2` | 1000 | 是 | 针对岗位级别的指定部门和指定分部 |
| 22 | `createrid` | 设置人员ID | `integer` | - | 是 | 设置人员ID |

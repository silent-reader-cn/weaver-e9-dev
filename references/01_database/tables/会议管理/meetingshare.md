# 泛微OA 数据表: `meetingshare`

- **所属模块**: `会议管理`
- **数据库表名**: `meetingshare`
- **字段总数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `meetingid` | 会议id | `integer` | - | 是 | 会议id |
| 3 | `userid` | 人力资源 | `varchar2` | 1000 | 是 | shareType:5人力资源 shareType:10/11/12 时转换后的人力资源 |
| 4 | `usertype` | 共享人员类型 | `integer` | - | 是 | 1：人员 2：客户 |
| 5 | `sharelevel` | 共享级别 | `integer` | - | 是 | 共享级别 |
| 6 | `departmentid` | 部门id | `varchar2` | 1600 | 是 | 部门id |
| 7 | `sharetype` | 共享类型 | `integer` | - | 是 | 1：部门 2：角色 3：所有人 5：指定人力资源 6:分部 8: 岗位 10:会议信息字段 11:会议服务字段 12:会议议程字段 |
| 8 | `seclevel` | 所有人安全级别 | `integer` | - | 是 | 所有人安全级别 |
| 9 | `seclevelmax` | 所有人最高安全级别 | `integer` | - | 是 | 所有人最高安全级别 |
| 10 | `deptlevel` | 部门安全级别 | `integer` | - | 是 | 部门安全级别 |
| 11 | `deptlevelmax` | 部门最高安全级别 | `integer` | - | 是 | 部门最高安全级别 |
| 12 | `subcompanyid` | 分部id | `varchar2` | 1000 | 是 | 分部id |
| 13 | `sublevel` | 分部 安全级别 | `integer` | - | 是 | 分部 安全级别 |
| 14 | `sublevelmax` | 分部最高安全级别 | `integer` | - | 是 | 分部最高安全级别 |
| 15 | `has_child` | 是否含下级 | `integer` | - | 是 | 0:不包含 1:包含 |
| 16 | `fieldids` | 选择的自定义字段 | `varchar2` | 1000 | 是 | shareType:10/11/12时选择的自定义字段 |
| 17 | `roleid` | 角色id | `varchar2` | 1000 | 是 | 角色id |
| 18 | `rolelevel` | 角色等级 | `integer` | - | 是 | 角色等级 |
| 19 | `roleseclevel` | 角色安全级别 | `integer` | - | 是 | 角色安全级别 |
| 20 | `roleseclevelmax` | 角色最高安全级别 | `integer` | - | 是 | 角色最高安全级别 |
| 21 | `jobtitleid` | 岗位id | `varchar2` | 1000 | 是 | 岗位id |
| 22 | `joblevel` | 岗位级别 | `integer` | - | 是 | 岗位级别 |
| 23 | `joblevelvalue` | 岗位对象 | `varchar2` | 1000 | 是 | 岗位对象 |
| 24 | `type` | 共享设置类型 | `integer` | - | 是 | 0:默认会议相关人员 1：后台设置（创建人不可编辑），2：前台设置 |
| 25 | `fromuser` | 当前设置人员 | `integer` | - | 是 | 当前设置人员 |

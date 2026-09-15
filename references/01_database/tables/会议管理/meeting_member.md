# 泛微OA 数据表: `meeting_member`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_member`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `rolelevel` | 角色等级 | `integer` | - | 是 | - |
| 2 | `seclevel` | 安全级别 | `integer` | - | 是 | - |
| 3 | `seclevelmax` | 最高安全级别 | `integer` | - | 是 | - |
| 4 | `departmentid` | 部门id | `integer` | - | 是 | - |
| 5 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 6 | `jobtitleid` | 岗位id | `integer` | - | 是 | - |
| 7 | `joblevel` | 岗位级别 | `integer` | - | 是 | 0:总部 1:分部 2:部门 |
| 8 | `joblevelvalue` | 岗位对象 | `varchar2` | 1000 | 是 | - |
| 9 | `id` | 主键 | `integer` | - | 否 | - |
| 10 | `meetingtype` | 会议类型 | `integer` | - | 是 | - |
| 11 | `membertype` | 人员类型 | `integer` | - | 是 | 1：人力资源，2：客户，3：所有人，5：部门，6：分部，7：角色 |
| 12 | `memberid` | 参会人员id | `integer` | - | 是 | - |
| 13 | `desc_n` | 说明 | `varchar2` | 1000 | 是 | - |
| 14 | `roleid` | 角色id | `integer` | - | 是 | - |

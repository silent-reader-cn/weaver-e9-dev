# 泛微OA 数据表: `kq_format_total`

- **中文名称**: 考勤报表主表
- **所属模块**: `人力资源`
- **数据库表名**: `kq_format_total`
- **主键**: `resourceid，kqdate`
- **字段数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `resourceid` | 人员ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `kqdate` | 考勤日期 | `varchar2` | 10 | 否 | 否 | 否 | - | - | - |
| 3 | `subcompanyid` | 分部ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `departmentid` | 部门ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `jobtitle` | 岗位ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 6 | `groupid` | 考勤组ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 7 | `serialid` | 班次ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 8 | `workdays` | 应出勤天数 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 9 | `workmins` | 应出勤时长 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 10 | `attendancedays` | 实际出勤天 | `number` | - | 否 | 否 | 否 | - | - | - |
| 11 | `attendancemins` | 实际出勤时长 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 12 | `belate` | 迟到次数 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 13 | `belatemins` | 迟到时长 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 14 | `gravebelate` | 严重迟到次数 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 15 | `gravebelatemins` | 严重迟到时长 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 16 | `leaveeearly` | 早退次数 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 17 | `leaveearlymins` | 早退时长 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 18 | `graveleaveearly` | 严重早退次数 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 19 | `graveleaveearlymins` | 严重早退时长 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 20 | `absenteeism` | 旷工次数 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 21 | `absenteeismmins` | 旷工时长 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 22 | `forgotcheck` | 漏签次数 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 23 | `forgotcheckMins` | 漏签时长 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 24 | `leaveMins` | 请假时长 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 25 | `evectionMins` | 出差时长 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 26 | `outMins` | 公出时长 | `integer` | - | 否 | 否 | 否 | - | - | - |

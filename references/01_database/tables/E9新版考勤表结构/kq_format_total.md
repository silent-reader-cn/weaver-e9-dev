# 泛微OA 数据表: `kq_format_total`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_format_total`
- **字段总数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `resourceid` | 人员ID | `integer` | - | 否 | - |
| 2 | `kqdate` | 考勤日期 | `varchar2` | 10 | 否 | - |
| 3 | `subcompanyid` | 分部ID | `integer` | - | 否 | - |
| 4 | `departmentid` | 部门ID | `integer` | - | 否 | - |
| 5 | `jobtitle` | 岗位ID | `integer` | - | 否 | - |
| 6 | `groupid` | 考勤组ID | `integer` | - | 否 | - |
| 7 | `serialid` | 班次ID | `integer` | - | 否 | - |
| 8 | `workdays` | 应出勤天数 | `integer` | - | 否 | - |
| 9 | `workmins` | 应出勤时长 | `integer` | - | 否 | - |
| 10 | `attendancedays` | 实际出勤天 | `number` | - | 否 | - |
| 11 | `attendancemins` | 实际出勤时长 | `integer` | - | 否 | - |
| 12 | `belate` | 迟到次数 | `integer` | - | 否 | - |
| 13 | `belatemins` | 迟到时长 | `integer` | - | 否 | - |
| 14 | `gravebelate` | 严重迟到次数 | `integer` | - | 否 | - |
| 15 | `gravebelatemins` | 严重迟到时长 | `integer` | - | 否 | - |
| 16 | `leaveeearly` | 早退次数 | `integer` | - | 否 | - |
| 17 | `leaveearlymins` | 早退时长 | `integer` | - | 否 | - |
| 18 | `graveleaveearly` | 严重早退次数 | `integer` | - | 否 | - |
| 19 | `graveleaveearlymins` | 严重早退时长 | `integer` | - | 否 | - |
| 20 | `absenteeism` | 旷工次数 | `integer` | - | 否 | - |
| 21 | `absenteeismmins` | 旷工时长 | `integer` | - | 否 | - |
| 22 | `forgotcheck` | 漏签次数 | `integer` | - | 否 | - |
| 23 | `forgotcheckMins` | 漏签时长 | `integer` | - | 否 | - |
| 24 | `leaveMins` | 请假时长 | `integer` | - | 否 | - |
| 25 | `evectionMins` | 出差时长 | `integer` | - | 否 | - |
| 26 | `outMins` | 公出时长 | `integer` | - | 否 | - |

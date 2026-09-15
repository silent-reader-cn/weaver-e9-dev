# 泛微OA 数据表: `kq_format_detail`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_format_detail`
- **字段总数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `resourceid` | 人员ID | `integer` | - | 否 | - |
| 2 | `kqdate` | 考勤日期 | `char` | 10 | 否 | - |
| 3 | `groupid` | 考勤组ID | `integer` | - | 否 | - |
| 4 | `serialid` | 班次ID | `integer` | - | 否 | - |
| 5 | `serialnumber` | 班次序号 | `integer` | - | 否 | - |
| 6 | `workbegindate` | 工作开始日期 | `char` | 10 | 否 | - |
| 7 | `workbegintime` | 工作开始时间 | `char` | 8 | 否 | - |
| 8 | `workenddate` | 工作结束日期 | `char` | 10 | 否 | - |
| 9 | `workendtime` | 工作结束时间 | `char` | 8 | 否 | - |
| 10 | `workmins` | 工作时长 | `integer` | - | 否 | - |
| 11 | `signindate` | 签到日期 | `char` | 10 | 否 | - |
| 12 | `signintime` | 签到时间 | `char` | 8 | 否 | - |
| 13 | `signinid` | 签到ID | `integer` | - | 否 | - |
| 14 | `signoutdate` | 签退日期 | `char` | 10 | 否 | - |
| 15 | `signouttime` | 签退时间 | `char` | 8 | 否 | - |
| 16 | `signoutid` | 签退ID | `integer` | - | 否 | - |
| 17 | `attendanceMins` | 出勤时长 | `integer` | - | 否 | - |
| 18 | `belatemins` | 迟到时长 | `integer` | - | 否 | - |
| 19 | `graveBeLateMins` | 严重迟到时长 | `integer` | - | 否 | - |
| 20 | `leaveearlymins` | 早退时长 | `integer` | - | 否 | - |
| 21 | `graveLeaveEarlyMins` | 严重早退时长 | `integer` | - | 否 | - |
| 22 | `absenteeismmins` | 旷工时长 | `integer` | - | 否 | - |
| 23 | `leaveMins` | 请假时长 | `integer` | - | 否 | - |
| 24 | `evectionMins` | 出差时长 | `integer` | - | 否 | - |
| 25 | `outMins` | 公出时长 | `integer` | - | 否 | - |
| 26 | `forgotcheckMins` | 漏签时长 | `integer` | - | 否 | - |

# 泛微OA 数据表: `kq_format_total`

- **所属模块**: `人力资源`
- **数据库表名**: `kq_format_total`
- **字段总数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `resourceid` | 人员ID | `integer` | - | - | - |
| 2 | `kqdate` | 考勤日期 | `varchar2` | 10 | - | - |
| 3 | `subcompanyid` | 分部ID | `integer` | - | - | - |
| 4 | `departmentid` | 部门ID | `integer` | - | - | - |
| 5 | `jobtitle` | 岗位ID | `integer` | - | - | - |
| 6 | `groupid` | 考勤组ID | `integer` | - | - | - |
| 7 | `serialid` | 班次ID | `integer` | - | - | - |
| 8 | `workdays` | 应出勤天数 | `integer` | - | - | - |
| 9 | `workmins` | 应出勤时长 | `integer` | - | - | - |
| 10 | `attendancedays` | 实际出勤天 | `number` | - | - | - |
| 11 | `attendancemins` | 实际出勤时长 | `integer` | - | - | - |
| 12 | `belate` | 迟到次数 | `integer` | - | - | - |
| 13 | `belatemins` | 迟到时长 | `integer` | - | - | - |
| 14 | `gravebelate` | 严重迟到次数 | `integer` | - | - | - |
| 15 | `gravebelatemins` | 严重迟到时长 | `integer` | - | - | - |
| 16 | `leaveeearly` | 早退次数 | `integer` | - | - | - |
| 17 | `leaveearlymins` | 早退时长 | `integer` | - | - | - |
| 18 | `graveleaveearly` | 严重早退次数 | `integer` | - | - | - |
| 19 | `graveleaveearlymins` | 严重早退时长 | `integer` | - | - | - |
| 20 | `absenteeism` | 旷工次数 | `integer` | - | - | - |
| 21 | `absenteeismmins` | 旷工时长 | `integer` | - | - | - |
| 22 | `forgotcheck` | 漏签次数 | `integer` | - | - | - |
| 23 | `forgotcheckMins` | 漏签时长 | `integer` | - | - | - |
| 24 | `leaveMins` | 请假时长 | `integer` | - | - | - |
| 25 | `evectionMins` | 出差时长 | `integer` | - | - | - |
| 26 | `outMins` | 公出时长 | `integer` | - | - | - |

# 泛微OA 数据表: `kq_overtime_signtask`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_overtime_signtask`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `resourceid` | 人员id | `integer` | - | 否 | - |
| 3 | `signdate` | 打卡所属日期 | `varchar2` | - | 否 | - |
| 4 | `signtime` | 工作时间的，最后签退时间 | `varchar2` | - | 否 | - |
| 5 | `lastworktime` | 最后下班时间 | `varchar2` | - | 否 | - |
| 6 | `signintime4out` | 非工作时间记录的签到时间 | `varchar2` | - | 否 | - |
| 7 | `workmins` | 工作时间的工作时长 | `varchar2` | - | 否 | - |

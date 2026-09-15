# 泛微OA 数据表: `hrmworktimewarp`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmworktimewarp`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `diffid` | 人力资源考勤id | `integer` | - | 是 | HrmScheduleMaintance的id |
| 3 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 4 | `diffdate` | 日期 | `char` | 10 | 是 | 日期 |
| 5 | `difftype` | 类型 | `char` | 1 | 是 | 类型 |
| 6 | `intime` | 入公司时间 | `char` | 5 | 是 | 入公司时间 |
| 7 | `outtime` | 出公司时间 | `char` | 5 | 是 | 出公司时间 |
| 8 | `theintime` | 正常上班时间 | `char` | 5 | 是 | 正常上班时间 |
| 9 | `theouttime` | 正常下班时间 | `char` | 5 | 是 | 正常下班时间 |
| 10 | `counttime` | 打卡时间 | `integer` | - | 是 | 打卡时间 |
| 11 | `diffcounttime` | 考勤计算时间 | `integer` | - | 是 | 考勤计算时间 |

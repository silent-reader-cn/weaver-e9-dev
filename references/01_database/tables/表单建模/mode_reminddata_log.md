# 泛微OA 数据表: `mode_reminddata_log`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_reminddata_log`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `remindjobid` | 提醒基本信息id | `integer` | - | 是 | 对应mode_remindjob表的id |
| 3 | `lastreminddate` | 上次提醒日期 | `varchar2` | 80 | 是 | 上次提醒的日期 |
| 4 | `lastremindtime` | 上次提醒时间 | `varchar2` | 80 | 是 | 上次提醒的时间 |

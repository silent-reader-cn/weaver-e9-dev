# 泛微OA 数据表: `bill_hrmscheduledetail`

- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmscheduledetail`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `scheduleid` | 请假主表id | `integer` | - | 是 | 请假主表id |
| 3 | `diffid` | 请假类型id | `integer` | - | 是 | 请假类型id |
| 4 | `startdate` | 开始日期 | `char` | 10 | 是 | 开始日期 |
| 5 | `starttime` | 开始时间 | `char` | 8 | 是 | 开始时间 |
| 6 | `enddate` | 结束日期 | `char` | 10 | 是 | 结束日期 |
| 7 | `endtime` | 结束时间 | `char` | 8 | 是 | 结束时间 |
| 8 | `sumday` | 总天数 | `integer` | - | 是 | 总天数 |

# 泛微OA 数据表: `hrmperformanceplancheck`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformanceplancheck`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `planmodulid` | 计划模板id | `integer` | - | 是 | 计划模板id |
| 3 | `cycle` | 周期 | `char` | 1 | 是 | 周期 |
| 4 | `plandate` | 计划日期 | `varchar2` | 1000 | 是 | 计划日期 |
| 5 | `planday` | 计划天数 | `varchar2` | 1000 | 是 | 计划天数 |
| 6 | `workplanid` | 日程id | `varchar2` | 1000 | 是 | 日程id |

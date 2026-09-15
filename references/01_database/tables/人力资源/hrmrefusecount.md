# 泛微OA 数据表: `hrmrefusecount`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmrefusecount`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `refuse_date` | 拒绝日期 | `varchar2` | 10 | 是 | 拒绝日期 |
| 3 | `refuse_year` | 年份 | `integer` | - | 是 | 年份 |
| 4 | `refuse_month` | 月份 | `integer` | - | 是 | 月份 |
| 5 | `refuse_hour` | 小时 | `integer` | - | 是 | 小时 |
| 6 | `refuse_loginid` | 人员登录id | `varchar2` | 1000 | 是 | 人员登录id |

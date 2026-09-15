# 泛微OA 数据表: `crm_contacterlog_remind`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_contacterlog_remind`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `customerid` | 客户id | `integer` | - | 是 | 客户id |
| 3 | `daytype` | 提醒日期类型 | `integer` | - | 是 | 提醒日期类型 |
| 4 | `before` | 提前多少天 | `integer` | - | 是 | 提前多少天 |
| 5 | `isremind` | 是否已提醒 | `integer` | - | 是 | 是否已提醒 |
| 6 | `lastestcontactdate` | 最后联系时间 | `char` | 20 | 是 | 最后联系时间 |

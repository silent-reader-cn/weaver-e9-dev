# 泛微OA 数据表: `hrmcareerplan`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcareerplan`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `topic` | 招聘主题 | `varchar2` | 1000 | 是 | 招聘主题 |
| 3 | `principalid` | 负责人id | `integer` | - | 是 | 负责人id |
| 4 | `informmanid` | 通知人id | `integer` | - | 是 | 通知人id |
| 5 | `emailmould` | 邮件通知模板 | `integer` | - | 是 | 邮件通知模板 |
| 6 | `startdate` | 开始日期 | `char` | 10 | 是 | 开始日期 |
| 7 | `budget` | 预算 | `float` | 53 | 是 | 预算 |
| 8 | `budgettype` | 预算类型 | `integer` | - | 是 | 预算类型 |
| 9 | `memo` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 10 | `enddate` | 结束日期 | `char` | 10 | 是 | 结束日期 |
| 11 | `fare` | 费用 | `float` | 53 | 是 | 费用 |
| 12 | `faretype` | 费用类型 | `integer` | - | 是 | 费用类型 |
| 13 | `advice` | 总结建议 | `varchar2` | 4000 | 是 | 总结建议 |

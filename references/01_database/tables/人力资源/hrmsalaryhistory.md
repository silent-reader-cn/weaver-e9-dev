# 泛微OA 数据表: `hrmsalaryhistory`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalaryhistory`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `hrmid` | 人员id | `integer` | - | 是 | 人员id |
| 3 | `currentdate` | 当前时间 | `char` | 10 | 是 | 当前时间 |
| 4 | `itemid` | 工资单规则id | `integer` | - | 是 | 工资单规则id |
| 5 | `salary` | 工资 | `number` | (12,2) | 是 | 工资 |

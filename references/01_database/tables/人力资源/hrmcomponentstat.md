# 泛微OA 数据表: `hrmcomponentstat`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcomponentstat`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `salarystat` | 总金额 | `number` | (10,3) | 是 | 总金额 |
| 4 | `periodyear` | 年 | `char` | 4 | 是 | 年 |
| 5 | `periodmonth` | 月 | `char` | 2 | 是 | 月 |

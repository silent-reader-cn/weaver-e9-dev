# 泛微OA 数据表: `hrmsalarywelfarerate`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalarywelfarerate`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `itemid` | 薪酬id | `integer` | - | 是 | 薪酬id |
| 3 | `cityid` | 城市id | `integer` | - | 是 | 城市id |
| 4 | `personwelfarerate` | 个人费率 | `number` | (10,2) | 是 | 个人费率 |
| 5 | `companywelfarerate` | 公司费率 | `number` | (10,2) | 是 | 公司费率 |

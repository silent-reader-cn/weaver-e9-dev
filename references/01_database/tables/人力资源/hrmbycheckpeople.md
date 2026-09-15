# 泛微OA 数据表: `hrmbycheckpeople`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmbycheckpeople`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `checkid` | 考核id | `integer` | - | 是 | 考核id |
| 3 | `resourceid` | 被考核人的id | `integer` | - | 是 | 被考核人的id |
| 4 | `checkercount` | 考核人的id | `integer` | - | 是 | 考核人的id |
| 5 | `proportion` | 考核人的权重 | `integer` | - | 是 | 考核人的权重 |
| 6 | `checkresourcetype` | 考核人的类型 | `integer` | - | 是 | 考核人的类型 |
| 7 | `result` | 被考核人的成绩 | `number` | (10,2) | 是 | 被考核人的成绩 |
| 8 | `lastmodifydate` | 考核人的最后打分时间 | `char` | 10 | 是 | 考核人的最后打分时间 |

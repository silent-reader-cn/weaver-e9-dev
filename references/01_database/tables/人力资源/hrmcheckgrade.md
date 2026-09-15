# 泛微OA 数据表: `hrmcheckgrade`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcheckgrade`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `checkpeopleid` | 被考核人信息表的id | `integer` | - | 是 | 被考核人信息表的id |
| 3 | `checkitemid` | 考核项目id | `integer` | - | 是 | 考核项目id |
| 4 | `result` | 考核人对被考核人打的某一项的成绩 | `number` | (10,1) | 是 | 考核人对被考核人打的某一项的成绩 |
| 5 | `checkitemproportion` | 每一项成绩的权重 | `integer` | - | 是 | 每一项成绩的权重 |

# 泛微OA 数据表: `mode_custombrowserdspfield`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_custombrowserdspfield`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `customid` | 浏览框id | `integer` | - | 是 | 对应mode_custombrowser表的id |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | 对应workflow_billfield表的id |
| 4 | `isquery` | 是否查询条件 | `char` | 1 | 是 | - |

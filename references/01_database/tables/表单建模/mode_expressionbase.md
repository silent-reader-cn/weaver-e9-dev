# 泛微OA 数据表: `mode_expressionbase`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_expressionbase`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `searchtransmethodid` | 查询id | `integer` | - | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | 对应workflow_billfield表中的id |
| 4 | `fieldname` | 数据库字段名 | `varchar2` | 800 | 是 | - |

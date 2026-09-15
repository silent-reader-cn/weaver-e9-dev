# 泛微OA 数据表: `mode_excelfielddetail`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_excelfielddetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `mainid` | 条件设置表id | `integer` | - | 是 | 对应条件设置表的id |
| 3 | `selectids` | 选择框id | `varchar2` | 1000 | 是 | - |
| 4 | `selectvalue` | 选择框的值 | `integer` | - | 是 | - |
| 5 | `fieldid` | 字段id | `clob` | 4000 | 是 | - |

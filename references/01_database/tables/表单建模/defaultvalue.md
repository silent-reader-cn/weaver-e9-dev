# 泛微OA 数据表: `defaultvalue`

- **所属模块**: `表单建模`
- **数据库表名**: `defaultvalue`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `modeid` | 模块id | `integer` | - | 是 | 对应modeinfo表的id |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | 对应workflow_billfield表的id |
| 4 | `customervalue` | 默认值 | `varchar2` | 1000 | 是 | 默认值，一个字段只能设置一个默认值 |
| 5 | `formid` | 表单id | `integer` | - | 是 | 对应workflow_bill表的id |

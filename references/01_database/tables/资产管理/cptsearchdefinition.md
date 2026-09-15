# 泛微OA 数据表: `cptsearchdefinition`

- **所属模块**: `资产管理`
- **数据库表名**: `cptsearchdefinition`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `fieldname` | 字段名 | `varchar2` | 400 | 是 | 字段名 |
| 3 | `isconditionstitle` | 是否作为字段列或查询条件 | `integer` | - | 是 | 是否作为字段列或查询条件 |
| 4 | `istitle` | 是否作为显示列 | `integer` | - | 是 | 是否作为显示列 |
| 5 | `isconditions` | 是否 作为条件 | `integer` | - | 是 | 是否 作为条件 |
| 6 | `isseniorconditions` | 是否高级条件 | `integer` | - | 是 | 是否高级条件 |
| 7 | `mouldid` | 模板id | `integer` | - | 是 | 模板id |
| 8 | `displayorder` | 显示顺序 | `float` | 22 | 是 | 显示顺序 |

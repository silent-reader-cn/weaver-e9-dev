# 泛微OA 数据表: `esbreturnrule_variablebase`

- **所属模块**: `集成模块`
- **数据库表名**: `esbreturnrule_variablebase`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 主键ID |
| 2 | `name` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 3 | `ruleid` | 规则ID | `integer` | - | 是 | 规则ID |
| 4 | `fieldtype` | 字段类型 | `varchar2` | 80 | 是 | 字段类型 |
| 5 | `htmltype` | HTML类型 | `integer` | - | 是 | HTML类型 |

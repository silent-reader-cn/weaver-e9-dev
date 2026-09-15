# 泛微OA 数据表: `esbreturnrule_expressions`

- **所属模块**: `集成模块`
- **数据库表名**: `esbreturnrule_expressions`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 主键ID |
| 2 | `ruleid` | 规则主键 | `integer` | - | 是 | 规则主键 |
| 3 | `relation` | 规则之间的关系 | `integer` | - | 是 | 规则之间的关系：与关系、或关系 |
| 4 | `expids` | 表达式ID | `varchar2` | 1000 | 是 | 表达式ID |
| 5 | `expbaseid` | 表达式基本ID | `integer` | - | 是 | 表达式基本ID |

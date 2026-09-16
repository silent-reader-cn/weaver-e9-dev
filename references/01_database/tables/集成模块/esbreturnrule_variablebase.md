# 泛微OA 数据表: `esbreturnrule_variablebase`

- **中文名称**: ESB接口配置返回规则变量配置
- **所属模块**: `集成模块`
- **数据库表名**: `esbreturnrule_variablebase`
- **主键**: `id`
- **字段数**: `5`

> 说明：ESB接口配置返回规则变量配置，该表仿照rule_variablebase表设计开发

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 否 | 否 | - | - | 主键ID |
| 2 | `name` | 名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 名称 |
| 3 | `ruleid` | 规则ID | `integer` | - | 是 | 是 | 否 | - | - | 规则ID |
| 4 | `fieldtype` | 字段类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 字段类型 |
| 5 | `htmltype` | HTML类型 | `integer` | - | 是 | 否 | 否 | - | - | HTML类型 |

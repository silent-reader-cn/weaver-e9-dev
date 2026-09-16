# 泛微OA 数据表: `esbreturnrule_mapitem`

- **中文名称**: ESB接口配置返回规则映射项
- **所属模块**: `集成模块`
- **数据库表名**: `esbreturnrule_mapitem`
- **主键**: `id`
- **字段数**: `9`

> 说明：ESB接口配置返回规则映射项，该表仿照rule_mapitem表设计开发

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 否 | 否 | - | - | 主键ID |
| 2 | `ruleid` | 规则ID | `integer` | - | 是 | 否 | 否 | - | - | 规则ID |
| 3 | `rulesrc` | 源规则 | `integer` | - | 是 | 否 | 否 | - | - | 源规则 |
| 4 | `linkid` | 链接ID | `integer` | - | 是 | 否 | 否 | - | - | 链接ID |
| 5 | `rulevarid` | 规则变量ID | `integer` | - | 是 | 否 | 否 | - | - | 规则变量ID |
| 6 | `formfieldid` | 表单字段ID | `integer` | - | 是 | 否 | 否 | - | - | 表单字段ID |
| 7 | `rowidenty` | 行标识 | `integer` | - | 是 | 否 | 否 | - | - | 行标识 |
| 8 | `nodeid` | 节点ID | `integer` | - | 是 | 否 | 否 | - | - | 节点ID |
| 9 | `meetcondition` | 会合条件 | `integer` | - | 是 | 否 | 否 | - | - | 会合条件 |

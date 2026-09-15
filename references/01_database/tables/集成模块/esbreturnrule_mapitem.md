# 泛微OA 数据表: `esbreturnrule_mapitem`

- **所属模块**: `集成模块`
- **数据库表名**: `esbreturnrule_mapitem`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 主键ID |
| 2 | `ruleid` | 规则ID | `integer` | - | 是 | 规则ID |
| 3 | `rulesrc` | 源规则 | `integer` | - | 是 | 源规则 |
| 4 | `linkid` | 链接ID | `integer` | - | 是 | 链接ID |
| 5 | `rulevarid` | 规则变量ID | `integer` | - | 是 | 规则变量ID |
| 6 | `formfieldid` | 表单字段ID | `integer` | - | 是 | 表单字段ID |
| 7 | `rowidenty` | 行标识 | `integer` | - | 是 | 行标识 |
| 8 | `nodeid` | 节点ID | `integer` | - | 是 | 节点ID |
| 9 | `meetcondition` | 会合条件 | `integer` | - | 是 | 会合条件 |

# 泛微OA 数据表: `esbreturnrule_expressionbase`

- **所属模块**: `集成模块`
- **数据库表名**: `esbreturnrule_expressionbase`
- **字段总数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 主键ID |
| 2 | `ruleid` | 规则ID | `integer` | - | 是 | 规则ID |
| 3 | `datafield` | 数据字段 | `integer` | - | 是 | 数据字段 |
| 4 | `datafieldtext` | 数据字段文本信息 | `varchar2` | 1000 | 是 | 数据字段文本信息 |
| 5 | `compareoption1` | 比较操作符1 | `integer` | - | 是 | 比较操作符1 |
| 6 | `compareoption2` | 比较操作符2 | `integer` | - | 是 | 比较操作符2 |
| 7 | `htmltype` | HTML类型 | `integer` | - | 是 | HTML类型 |
| 8 | `typehrm` | HR类型 | `integer` | - | 是 | HR类型 |
| 9 | `fieldtype` | 字段类型 | `varchar2` | 80 | 是 | 字段类型 |
| 10 | `valuetype` | 值类型 | `integer` | - | 是 | 值类型 |
| 11 | `paramtype` | 参数类型 | `integer` | - | 是 | 参数类型 |
| 12 | `elementvalue1` | 元素值1 | `varchar2` | 1000 | 是 | 元素值1 |
| 13 | `elementlabel1` | 元素标签1 | `varchar2` | 1000 | 是 | 元素标签1 |
| 14 | `elementvalue2` | 元素值2 | `varchar2` | 1000 | 是 | 元素值2 |
| 15 | `dbtype` | 数据库类型 | `varchar2` | 400 | 是 | 数据库类型 |
| 16 | `redius` | 半径 | `integer` | - | 是 | 半径 |
| 17 | `meetcondition` | 会合条件 | `integer` | - | 是 | 会合条件 |
| 18 | `nodeid` | 节点ID | `integer` | - | 是 | 节点ID |
| 19 | `jingdu` | 经度 | `varchar2` | 800 | 是 | 经度 |
| 20 | `weidu` | 纬度 | `varchar2` | 800 | 是 | 纬度 |

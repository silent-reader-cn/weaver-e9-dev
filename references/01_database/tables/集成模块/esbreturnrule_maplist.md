# 泛微OA 数据表: `esbreturnrule_maplist`

- **中文名称**: ESB接口配置返回规则映射列表
- **所属模块**: `集成模块`
- **数据库表名**: `esbreturnrule_maplist`
- **主键**: `id`
- **字段数**: `9`

> 说明：ESB接口配置返回规则映射列表，该表仿照rule_maplist表设计开发

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 否 | 否 | - | - | 主键ID |
| 2 | `wfid` | 流程ID | `integer` | - | 是 | 否 | 否 | - | - | 流程ID |
| 3 | `linkid` | 链接ID | `integer` | - | 是 | 否 | 否 | - | - | 链接ID |
| 4 | `ruleid` | 规则ID | `integer` | - | 是 | 是 | 否 | esbreturnrule.id | - | 规则ID |
| 5 | `isused` | 是否使用 | `integer` | - | 是 | 否 | 否 | - | - | 是否使用 |
| 6 | `rulesrc` | 源规则 | `integer` | - | 是 | 否 | 否 | - | - | 源规则 |
| 7 | `nm` | nm | `integer` | - | 是 | 否 | 否 | - | - | nm |
| 8 | `rowidenty` | 行标识 | `integer` | - | 是 | 否 | 否 | - | - | 行标识 |
| 9 | `detailid` | 明细号 | `integer` | - | 是 | 否 | 否 | - | - | 明细号 |

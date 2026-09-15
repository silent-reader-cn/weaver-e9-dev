# 泛微OA 数据表: `workflow_tridiffwfdifffield`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_tridiffwfdifffield`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `issplitdetail` | 明细拆分触发 | `char` | 1 | 是 | - |
| 2 | `triggertype` | 触发类型 | `char` | 1 | 是 | 1：自动触发，2：手动触发 |
| 3 | `triggeroperation` | 触发操作 | `char` | 1 | 是 | 1：批准，2：退回，""或其他：任何操作都触发 |
| 4 | `enable` | 使能操作 | `char` | 1 | 是 | - |
| 5 | `triggersourcetype` | 触发源类型 | `varchar2` | 80 | 是 | - |
| 6 | `triggersourceorder` | 触发源顺序 | `integer` | - | 是 | - |
| 7 | `triggercondition` | 触发条件 | `varchar2` | 1000 | 是 | - |
| 8 | `triggersource` | 触发源 | `integer` | - | 是 | - |
| 9 | `condition` | 条件ID | `varchar2` | 4000 | 是 | - |
| 10 | `conditioncn` | 条件详情 | `clob` | 4000 | 是 | - |
| 11 | `rulerelationship` | 条件关系 | `char` | 1 | 是 | - |
| 12 | `id` | ID | `integer` | - | 否 | - |
| 13 | `mainworkflowid` | 主流程id | `integer` | - | 是 | - |
| 14 | `triggernodeid` | 触发节点 | `integer` | - | 是 | - |
| 15 | `triggertime` | 触发时间 | `char` | 1 | 是 | 1:到达节点,2:离开节点 |
| 16 | `fieldid` | 主流程的可区分字段id | `integer` | - | 是 | - |

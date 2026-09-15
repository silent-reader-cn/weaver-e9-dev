# 泛微OA 数据表: `workflow_requestoperatelog`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestoperatelog`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `detailinfo` | 明细JSON数据 | `clob` | 4000 | 是 | - |
| 2 | `retype` | 操作类型 | `char` | 1 | 是 | - |
| 3 | `reoperatorid` | 被代理人ID | `varchar2` | 20 | 是 | - |
| 4 | `id` | ID | `integer` | - | 否 | - |
| 5 | `requestid` | 请求id | `integer` | - | 是 | - |
| 6 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 7 | `isremark` | 操作状态 | `integer` | - | 是 | 与workflow_currentoperator表中的isremark是不同的 |
| 8 | `operatorid` | 操作人id | `integer` | - | 是 | - |
| 9 | `operatortype` | 操作人类型 | `integer` | - | 是 | - |
| 10 | `operatedate` | 操作日期 | `varchar2` | 80 | 是 | - |
| 11 | `operatetime` | 操作时间 | `varchar2` | 64 | 是 | - |
| 12 | `operatetype` | 操作类型 | `varchar2` | 200 | 是 | - |

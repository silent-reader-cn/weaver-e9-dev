# 泛微OA 数据表: `workflow_requestexception`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestexception`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `keyid` | 自增ID | `integer` | - | 否 | - |
| 2 | `requestid` | 请求ID | `integer` | - | 是 | - |
| 3 | `nodeid` | 节点ID | `integer` | - | 是 | - |
| 4 | `destnodeid` | 目标节点ID | `integer` | - | 是 | - |
| 5 | `exceptiontype` | 异常类型 | `char` | 1 | 是 | - |
| 6 | `signtype` | 会签关系 | `char` | 1 | 是 | - |
| 7 | `flowoperator` | 接收人 | `varchar2` | 1000 | 是 | - |

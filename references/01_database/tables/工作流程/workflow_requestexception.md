# 泛微OA 数据表: `workflow_requestexception`

- **中文名称**: 流程提交异常处理信息表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestexception`
- **主键**: `keyid`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `keyid` | 自增ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `requestid` | 请求ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `nodeid` | 节点ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `destnodeid` | 目标节点ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `exceptiontype` | 异常类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 6 | `signtype` | 会签关系 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `flowoperator` | 接收人 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

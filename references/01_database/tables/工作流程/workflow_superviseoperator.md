# 泛微OA 数据表: `workflow_superviseoperator`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_superviseoperator`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | - |
| 2 | `requestid` | 流程 | `integer` | - | 是 | - |
| 3 | `workflowid` | 路径 | `integer` | - | 是 | - |
| 4 | `workflowtype` | 路径类型 | `integer` | - | 是 | - |
| 5 | `userid` | 用户 | `integer` | - | 是 | - |
| 6 | `usertype` | 用户类型 | `integer` | - | 是 | - |
| 7 | `nodeid` | 节点 | `integer` | - | 是 | - |
| 8 | `nodetype` | 节点名称 | `integer` | - | 是 | - |
| 9 | `groupdetailid` | 操作组id | `integer` | - | 是 | - |
| 10 | `receivedate` | 接收日期 | `char` | 10 | 是 | - |
| 11 | `receivetime` | 接收时间 | `char` | 8 | 是 | - |
| 12 | `logtype` | 签字意见类型 | `char` | 1 | 是 | - |

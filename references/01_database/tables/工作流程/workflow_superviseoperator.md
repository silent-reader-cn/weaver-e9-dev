# 泛微OA 数据表: `workflow_superviseoperator`

- **中文名称**: 流程督办数据表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_superviseoperator`
- **主键**: `id`
- **字段数**: `12`

> 说明：计算之后督办数据存储表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `requestid` | 流程 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `workflowid` | 路径 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `workflowtype` | 路径类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `userid` | 用户 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `usertype` | 用户类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `nodeid` | 节点 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `nodetype` | 节点名称 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `groupdetailid` | 操作组id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `receivedate` | 接收日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 11 | `receivetime` | 接收时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 12 | `logtype` | 签字意见类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `workflow_node_flowtime`

- **中文名称**: 未归档流程节点耗时
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_node_flowtime`
- **主键**: `无`
- **字段数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `groupid` | 操作人组ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `overflowtime` | 超时时间 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `isremark` | 操作类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 4 | `islasttimes` | 最后一次操作 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `viewtype` | 查看标志 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `usertype` | 用户类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `nodeoperator` | 操作人 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 8 | `receivedate` | 接受日期 | `varchar2` | 10 | 否 | 否 | 否 | - | - | - |
| 9 | `flowtime` | 耗时 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `status` | 记录状态 | `char` | 1 | 是 | 否 | 否 | - | - | 0：待办 1：已办 |
| 11 | `isovertime` | 是否超时 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 12 | `departmentid` | 操作人部门ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `subcompanyid1` | 操作人分部ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `userstatus` | 用户状态 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `createdate` | 创建日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 16 | `workflowtype` | 流程类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `receivetime` | 接受时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 18 | `requestid` | 请求ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 19 | `workflowid` | 流程ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 20 | `nodeid` | 节点ID | `integer` | - | 否 | 否 | 否 | - | - | - |

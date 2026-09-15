# 泛微OA 数据表: `workflow_request_flowtime`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_request_flowtime`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `onlysave` | 只是新建保存 | `char` | 1 | 是 | - |
| 2 | `requestid` | 请求ID | `integer` | - | 否 | - |
| 3 | `workflowid` | 流程ID | `integer` | - | 否 | - |
| 4 | `workflowtype` | 流程类型 | `integer` | - | 否 | - |
| 5 | `createdate` | 创建日期 | `varchar2` | 10 | 否 | - |
| 6 | `createtime` | 创建时间 | `varchar2` | 64 | 否 | - |
| 7 | `lastoperatedate` | 最后操作日期 | `varchar2` | 80 | 是 | - |
| 8 | `currentnodeid` | 当前节点 | `integer` | - | 是 | - |
| 9 | `creator` | 创建人ID | `integer` | - | 否 | - |
| 10 | `flowtime` | 流转耗时 | `integer` | - | 是 | - |
| 11 | `status` | 当前状态 | `char` | 1 | 是 | - |
| 12 | `departmentid` | 部门ID | `integer` | - | 是 | - |
| 13 | `subcompanyid1` | 分部ID | `integer` | - | 是 | - |
| 14 | `userstatus` | 用户状态 | `integer` | - | 是 | - |

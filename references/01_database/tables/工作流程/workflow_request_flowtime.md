# 泛微OA 数据表: `workflow_request_flowtime`

- **中文名称**: 未归档流程耗时记录
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_request_flowtime`
- **主键**: `requestid`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `onlysave` | 只是新建保存 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 2 | `requestid` | 请求ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `workflowid` | 流程ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `workflowtype` | 流程类型 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `createdate` | 创建日期 | `varchar2` | 10 | 否 | 否 | 否 | - | - | - |
| 6 | `createtime` | 创建时间 | `varchar2` | 64 | 否 | 否 | 否 | - | - | - |
| 7 | `lastoperatedate` | 最后操作日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 8 | `currentnodeid` | 当前节点 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `creator` | 创建人ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 10 | `flowtime` | 流转耗时 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `status` | 当前状态 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 12 | `departmentid` | 部门ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `subcompanyid1` | 分部ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `userstatus` | 用户状态 | `integer` | - | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `workflow_request_fix_flowtime`

- **中文名称**: 归档流程耗时记录
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_request_fix_flowtime`
- **主键**: `requestid`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `requestid` | 请求ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `workflowid` | 流程ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `workflowtype` | 流程类型 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `createdate` | 创建日期 | `varchar2` | 10 | 否 | 否 | 否 | - | - | - |
| 5 | `createtime` | 创建时间 | `varchar2` | 64 | 否 | 否 | 否 | - | - | - |
| 6 | `lastoperatedate` | 最后操作日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 7 | `currentnodeid` | 当前节点ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `creator` | 创建人 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 9 | `flowtime` | 流程耗时 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `status` | 流程状态 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 11 | `departmentid` | 创建人部门ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `subcompanyid1` | 创建人分部ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `userstatus` | 创建人状态 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `onlysave` | 只是保存数据 | `char` | 1 | 是 | 否 | 否 | - | - | - |

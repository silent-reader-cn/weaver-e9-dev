# 泛微OA 数据表: `workflow_viewlog`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_viewlog`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `varchar2` | 1000 | 否 | - |
| 2 | `p_nodeid` | 节点id | `varchar2` | 250 | 是 | - |
| 3 | `p_opteruid` | 操作用户id | `varchar2` | 250 | 是 | - |
| 4 | `p_date` | 日期 | `varchar2` | 1000 | 是 | - |
| 5 | `p_addip` | 添加ip | `varchar2` | 1000 | 是 | - |
| 6 | `p_number` | 编号 | `varchar2` | 1000 | 是 | - |
| 7 | `requestid` | 请求id | `varchar2` | 250 | 是 | - |
| 8 | `p_nodename` | 节点名称 | `varchar2` | 1000 | 是 | - |
| 9 | `requestname` | 请求名称 | `varchar2` | 1000 | 是 | - |
| 10 | `workflowtype` | 流程类型 | `varchar2` | 1000 | 是 | - |
| 11 | `workflowtypeid` | 流程类型id | `varchar2` | 1000 | 是 | - |
| 12 | `workflowid` | 流程id | `varchar2` | 1000 | 是 | - |

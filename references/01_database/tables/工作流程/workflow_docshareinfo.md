# 泛微OA 数据表: `workflow_docshareinfo`

- **中文名称**: 流程文档共享信息表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_docshareinfo`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `docid` | 文档id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `nodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `beagentid` | 被代理人id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `sharelevel` | 分享级别 | `integer` | - | 是 | 否 | 否 | - | - | - |

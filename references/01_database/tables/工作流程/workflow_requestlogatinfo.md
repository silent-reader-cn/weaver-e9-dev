# 泛微OA 数据表: `workflow_requestlogatinfo`

- **中文名称**: 流程请求日期信息表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestlogatinfo`
- **主键**: `id`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `nodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `logtype` | 日志类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 6 | `operatedate` | 操作日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 7 | `operatetime` | 操作时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |
| 8 | `operator` | 操作者 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `atuserid` | @人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `forwardresource_temp` | 转发资源_temp | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `forwardresource` | 转发资源 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |

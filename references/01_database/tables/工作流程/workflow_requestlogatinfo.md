# 泛微OA 数据表: `workflow_requestlogatinfo`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestlogatinfo`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `requestid` | 请求id | `integer` | - | 是 | - |
| 3 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 4 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 5 | `logtype` | 日志类型 | `char` | 1 | 是 | - |
| 6 | `operatedate` | 操作日期 | `varchar2` | 80 | 是 | - |
| 7 | `operatetime` | 操作时间 | `varchar2` | 64 | 是 | - |
| 8 | `operator` | 操作者 | `integer` | - | 是 | - |
| 9 | `atuserid` | @人 | `integer` | - | 是 | - |
| 10 | `forwardresource_temp` | 转发资源_temp | `varchar2` | 4000 | 是 | - |
| 11 | `forwardresource` | 转发资源 | `clob` | 4000 | 是 | - |

# 泛微OA 数据表: `workflow_function_manage`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_function_manage`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `workflowid` | 工作流id | `integer` | - | 是 | - |
| 2 | `typeview` | 流程状态查看 | `char` | 1 | 是 | - |
| 3 | `dataview` | 流程数据查看 | `char` | 1 | 是 | - |
| 4 | `automatism` | 自动催办 | `char` | 1 | 是 | - |
| 5 | `manual` | 人工催办 | `char` | 1 | 是 | - |
| 6 | `transmit` | 转发 | `char` | 1 | 是 | - |
| 7 | `retract` | 强制收回 | `char` | 1 | 是 | - |
| 8 | `pigeonhole` | 强制归档 | `char` | 1 | 是 | - |
| 9 | `operatortype` | 流程节点id | `integer` | - | 是 | 监控人为-1 |
| 10 | `isdelesubwf` | 是否 删除子流程 | `char` | 1 | 是 | - |

# 泛微OA 数据表: `workflow_process_relative`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_process_relative`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `workflowid` | 流程id | `integer` | - | 否 | - |
| 3 | `nodeids` | 节点ids | `varchar2` | 800 | 是 | - |
| 4 | `officaltype` | 设置发文类型：发文/收文/签报 | `integer` | - | 是 | - |
| 5 | `pdid` | 环节id | `integer` | - | 否 | - |

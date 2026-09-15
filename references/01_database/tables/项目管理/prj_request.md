# 泛微OA 数据表: `prj_request`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_request`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `prjid` | 项目id | `integer` | - | 是 | 项目id |
| 3 | `taskid` | 任务id | `integer` | - | 是 | 任务id |
| 4 | `isactived` | 是否活动任务 | `integer` | - | 是 | 是否活动任务 |
| 5 | `version` | 版本 | `integer` | - | 是 | 版本 |
| 6 | `requestid` | 流程id | `integer` | - | 是 | 流程id |
| 7 | `type` | 类型 | `integer` | - | 是 | 类型 |
| 8 | `workflowid` | 流程类型 | `integer` | - | 是 | 流程类型 |

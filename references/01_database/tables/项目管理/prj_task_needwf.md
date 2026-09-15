# 泛微OA 数据表: `prj_task_needwf`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_task_needwf`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `taskid` | 任务id | `integer` | - | 是 | 任务id |
| 3 | `templettaskid` | 模板任务id | `integer` | - | 是 | 模板任务id |
| 4 | `workflowid` | 流程id | `integer` | - | 是 | 流程id |
| 5 | `isnecessary` | 是否必须 | `char` | 1 | 是 | 是否必须 |
| 6 | `istemplettask` | 是否模板任务 | `char` | 1 | 是 | 是否模板任务 |

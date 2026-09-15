# 泛微OA 数据表: `workflow_createtask`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_createtask`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `wfid` | 流程id | `integer` | - | 是 | - |
| 3 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 4 | `changetime` | 转化时间 | `integer` | - | 是 | - |
| 5 | `taskid` | 任务id | `integer` | - | 是 | - |
| 6 | `creatertype` | 创建者类型 | `integer` | - | 是 | - |
| 7 | `wffieldid` | 流程字段id | `integer` | - | 是 | - |
| 8 | `changemode` | 转化模式 | `integer` | - | 是 | - |

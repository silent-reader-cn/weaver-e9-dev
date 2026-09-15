# 泛微OA 数据表: `workflow_createtaskdetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_createtaskdetail`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `createtaskid` | 创建任务id | `integer` | - | 是 | - |
| 3 | `wffieldid` | 流程字段id | `integer` | - | 是 | - |
| 4 | `isdetail` | 是否为明细字段 | `integer` | - | 是 | - |
| 5 | `wtfieldid` | 流程任务字段id | `integer` | - | 是 | - |
| 6 | `groupid` | 组id | `integer` | - | 是 | - |
| 7 | `wffieldtype` | 流程字段类型 | `integer` | - | 是 | - |

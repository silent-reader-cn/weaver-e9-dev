# 泛微OA 数据表: `workflow_createtaskdetail`

- **中文名称**: 流程创建任务明细表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_createtaskdetail`
- **主键**: `id`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `createtaskid` | 创建任务id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `wffieldid` | 流程字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `isdetail` | 是否为明细字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `wtfieldid` | 流程任务字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `groupid` | 组id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `wffieldtype` | 流程字段类型 | `integer` | - | 是 | 否 | 否 | - | - | - |

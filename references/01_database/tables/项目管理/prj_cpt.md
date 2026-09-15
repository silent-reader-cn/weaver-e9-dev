# 泛微OA 数据表: `prj_cpt`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_cpt`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `prjid` | 项目id | `integer` | - | 是 | 项目id |
| 3 | `taskid` | 任务id | `integer` | - | 是 | 任务id |
| 4 | `isactived` | 是否为活动任务 | `integer` | - | 是 | 是否为活动任务(执行状态的项目,isactive=2) |
| 5 | `version` | 任务版本 | `integer` | - | 是 | 任务版本 |
| 6 | `requestid` | 流程id | `integer` | - | 是 | 流程id |
| 7 | `type` | 类型 | `integer` | - | 是 | 类型 |

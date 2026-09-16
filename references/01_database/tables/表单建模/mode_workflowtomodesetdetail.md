# 泛微OA 数据表: `mode_workflowtomodesetdetail`

- **中文名称**: 流程转数据详细表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_workflowtomodesetdetail`
- **主键**: `id`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `mainid` | 流程转数据主id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_workflowtomodeset表的id |
| 3 | `modefieldid` | 模块字段名称 | `integer` | - | 是 | 否 | 否 | - | - | 模块字段id，对应workflow_billfield表的id |
| 4 | `wffieldid` | 流程字段名称 | `integer` | - | 是 | 否 | 否 | - | - | 流程字段id，对应workflow_billfield表的id |
| 5 | `defaultvalue` | 错误信息字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |

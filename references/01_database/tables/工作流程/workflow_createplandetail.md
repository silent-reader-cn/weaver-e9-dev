# 泛微OA 数据表: `workflow_createplandetail`

- **中文名称**: 留存
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_createplandetail`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `createplanid` | workflow_createplan表主键 | `integer` | - | 是 | 否 | 否 | - | - | workflow_createplan表主键 |
| 3 | `wffieldid` | 流程字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `isdetail` | 是否明细字段 | `integer` | - | 是 | 否 | 否 | - | - | 1、是，2、不是 |
| 5 | `planfieldname` | 日程字段名 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 6 | `groupid` | 组id | `integer` | - | 是 | 否 | 否 | - | - | workflow_createplangroup表主键 |

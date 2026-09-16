# 泛微OA 数据表: `workflow_createplangroup`

- **中文名称**: 流程转日程分组表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_createplangroup`
- **主键**: `id`
- **字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `createplanid` | workflow_createplan表主键 | `integer` | - | 是 | 否 | 否 | - | - | workflow_createplan表主键 |
| 3 | `groupid` | 分组id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `isused` | 是否开启转换 | `integer` | - | 是 | 否 | 否 | - | - | 1、是，2、否 |

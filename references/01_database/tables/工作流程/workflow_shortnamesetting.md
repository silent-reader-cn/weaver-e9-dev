# 泛微OA 数据表: `workflow_shortnamesetting`

- **中文名称**: 流程编号简称设置表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_shortnamesetting`
- **主键**: `id`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `formid` | 表单或单据id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `isbill` | 是否单据 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是，0：否 |
| 5 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `fieldvalue` | 字段值 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `shortnamesetting` | 简称设置 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |

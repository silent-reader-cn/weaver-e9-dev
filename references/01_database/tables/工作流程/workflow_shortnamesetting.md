# 泛微OA 数据表: `workflow_shortnamesetting`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_shortnamesetting`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 3 | `formid` | 表单或单据id | `integer` | - | 是 | - |
| 4 | `isbill` | 是否单据 | `char` | 1 | 是 | 1：是，0：否 |
| 5 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 6 | `fieldvalue` | 字段值 | `integer` | - | 是 | - |
| 7 | `shortnamesetting` | 简称设置 | `varchar2` | 800 | 是 | - |

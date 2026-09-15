# 泛微OA 数据表: `workflow_docprop`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_docprop`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 3 | `selectitemid` | 选择框可选项id | `integer` | - | 是 | - |
| 4 | `seccategoryid` | 文档子目录id | `integer` | - | 是 | - |
| 5 | `objid` | 对象id | `integer` | - | 是 | - |
| 6 | `objtype` | 对象类型 | `char` | 1 | 是 | - |

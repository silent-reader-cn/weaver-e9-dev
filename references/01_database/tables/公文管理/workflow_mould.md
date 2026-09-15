# 泛微OA 数据表: `workflow_mould`

- **所属模块**: `公文管理`
- **数据库表名**: `workflow_mould`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `selectvalue` | 选择框值 | `integer` | - | 是 | - |
| 2 | `isdefault` | 是否默认 | `char` | 1 | 是 | - |
| 3 | `id` | ID | `integer` | - | 否 | - |
| 4 | `workflowid` | 流程id | `integer` | - | 否 | - |
| 5 | `mouldid` | 模板id | `integer` | - | 否 | - |
| 6 | `mouldtype` | 模板类型 | `integer` | - | 是 | - |
| 7 | `visible` | 是否可见 | `integer` | - | 是 | - |
| 8 | `seccategory` | 文档子目录 | `integer` | - | 是 | - |

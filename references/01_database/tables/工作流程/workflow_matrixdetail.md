# 泛微OA 数据表: `workflow_matrixdetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_matrixdetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `groupdetailid` | 组明细id | `integer` | - | 否 | - |
| 2 | `condition_field` | 条件字段 | `integer` | - | 否 | - |
| 3 | `workflow_field` | 流转字段 | `integer` | - | 否 | - |
| 4 | `workflow_objid` | 字段值 | `varchar2` | 4000 | 是 | - |
| 5 | `workflow_bhxj` | 包含下级 | `char` | 1 | 是 | - |

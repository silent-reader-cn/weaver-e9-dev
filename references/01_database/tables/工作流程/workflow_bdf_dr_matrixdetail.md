# 泛微OA 数据表: `workflow_bdf_dr_matrixdetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_bdf_dr_matrixdetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `dataranageid` | 主表id | `integer` | - | 否 | workflow_bdf_dataranage的id |
| 2 | `condition_field` | 条件字段id | `integer` | - | 否 | - |
| 3 | `workflow_field` | 字段id | `integer` | - | 否 | - |
| 4 | `workflow_objid` | objid | `varchar2` | 4000 | 是 | - |
| 5 | `workflow_bhxj` | 是否包含下级 | `char` | 1 | 是 | - |

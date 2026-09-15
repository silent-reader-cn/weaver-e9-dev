# 泛微OA 数据表: `workflow_urger_matrix_detail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_urger_matrix_detail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `groupdetailid` | groupid | `integer` | - | 是 | - |
| 2 | `condition_field` | 条件字段 | `integer` | - | 是 | - |
| 3 | `workflow_field` | 流程字段 | `integer` | - | 是 | - |
| 4 | `workflow_objid` | objid | `varchar2` | 4000 | 是 | 分部 部门 |
| 5 | `workflow_bhxj` | 上下级关系 | `char` | 1 | 是 | - |

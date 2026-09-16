# 泛微OA 数据表: `workflow_matrixdetail`

- **中文名称**: 流程矩阵明细表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_matrixdetail`
- **主键**: `无`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `groupdetailid` | 组明细id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `condition_field` | 条件字段 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `workflow_field` | 流转字段 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `workflow_objid` | 字段值 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `workflow_bhxj` | 包含下级 | `char` | 1 | 是 | 否 | 否 | - | - | - |

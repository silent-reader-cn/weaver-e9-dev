# 泛微OA 数据表: `workflow_bdf_dr_matrixdetail`

- **中文名称**: 浏览数据定义数据范围矩阵明细表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_bdf_dr_matrixdetail`
- **主键**: `无`
- **字段数**: `5`

> 说明：浏览数据定义数据范围矩阵明细

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `dataranageid` | 主表id | `integer` | - | 否 | 是 | 否 | - | - | workflow_bdf_dataranage的id |
| 2 | `condition_field` | 条件字段id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `workflow_field` | 字段id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `workflow_objid` | objid | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `workflow_bhxj` | 是否包含下级 | `char` | 1 | 是 | 否 | 否 | - | - | - |

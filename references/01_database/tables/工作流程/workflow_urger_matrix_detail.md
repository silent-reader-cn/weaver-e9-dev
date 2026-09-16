# 泛微OA 数据表: `workflow_urger_matrix_detail`

- **中文名称**: 督办矩阵操作设置明细表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_urger_matrix_detail`
- **主键**: `无`
- **字段数**: `5`

> 说明：督办矩阵操作设置表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `groupdetailid` | groupid | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `condition_field` | 条件字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `workflow_field` | 流程字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `workflow_objid` | objid | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 分部 部门 |
| 5 | `workflow_bhxj` | 上下级关系 | `char` | 1 | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `exp_fieldmap_cs`

- **中文名称**: 流程字段映射关系表
- **所属模块**: `集成模块`
- **数据库表名**: `exp_fieldmap_cs`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `rgworkflowid` | 注册流程列表里的id | `integer` | - | 是 | 否 | 否 | - | - | exp_workflowDetail表里的id |
| 3 | `fieldmapid` | 转换规则id | `integer` | - | 是 | 否 | 否 | - | - | 根据protype对应不同的表里的id protype=0,表示xml映射(exp_workflowFieldXMLMap);protype=1,表示数据库映射(exp_workflowFieldDBMap) |
| 4 | `fieldvalue` | 值 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `convertvalue` | 转换值 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `protype` | 转换映射类型 | `char` | 1 | 是 | 否 | 否 | - | - | protype=0,表示xml映射(exp_workflowFieldXMLMap); protype=1,表示数据库映射(exp_workflowFieldDBMap) |

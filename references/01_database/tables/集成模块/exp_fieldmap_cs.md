# 泛微OA 数据表: `exp_fieldmap_cs`

- **所属模块**: `集成模块`
- **数据库表名**: `exp_fieldmap_cs`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `rgworkflowid` | 注册流程列表里的id | `integer` | - | 是 | exp_workflowDetail表里的id |
| 3 | `fieldmapid` | 转换规则id | `integer` | - | 是 | 根据protype对应不同的表里的id protype=0,表示xml映射(exp_workflowFieldXMLMap);protype=1,表示数据库映射(exp_workflowFieldDBMap) |
| 4 | `fieldvalue` | 值 | `varchar2` | 1000 | 是 | - |
| 5 | `convertvalue` | 转换值 | `varchar2` | 1000 | 是 | - |
| 6 | `protype` | 转换映射类型 | `char` | 1 | 是 | protype=0,表示xml映射(exp_workflowFieldXMLMap); protype=1,表示数据库映射(exp_workflowFieldDBMap) |

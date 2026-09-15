# 泛微OA 数据表: `exp_workflowfielddbmap`

- **所属模块**: `集成模块`
- **数据库表名**: `exp_workflowfielddbmap`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `rgworkflowid` | 注册流程列表里的id | `integer` | - | 是 | exp_workflowDetail表里的id |
| 3 | `fieldid` | 流程表单字段id | `integer` | - | 是 | - |
| 4 | `fieldhtmltype` | 表单字段html类型 | `integer` | - | 是 | - |
| 5 | `fieldtype` | 表单字段类型 | `integer` | - | 是 | - |
| 6 | `fieldname` | 字段名称 | `varchar2` | 1000 | 是 | - |
| 7 | `valuetype` | 取值类型 | `char` | 1 | 是 | 根据字段类型加取值类型值来决定取值 |
| 8 | `expfieldname` | 导出字段名称 | `varchar2` | 1000 | 是 | - |
| 9 | `expfieldtype` | 导出字段类型 | `varchar2` | 800 | 是 | - |
| 10 | `fileddbname` | 字段数据库类型 | `varchar2` | 1000 | 是 | - |

# 泛微OA 数据表: `exp_workflowfielddbmap`

- **中文名称**: 数据库方案流程导出字段转换关系表
- **所属模块**: `集成模块`
- **数据库表名**: `exp_workflowfielddbmap`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `rgworkflowid` | 注册流程列表里的id | `integer` | - | 是 | 否 | 否 | - | - | exp_workflowDetail表里的id |
| 3 | `fieldid` | 流程表单字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `fieldhtmltype` | 表单字段html类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `fieldtype` | 表单字段类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `fieldname` | 字段名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `valuetype` | 取值类型 | `char` | 1 | 是 | 否 | 否 | - | - | 根据字段类型加取值类型值来决定取值 |
| 8 | `expfieldname` | 导出字段名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `expfieldtype` | 导出字段类型 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 10 | `fileddbname` | 字段数据库类型 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

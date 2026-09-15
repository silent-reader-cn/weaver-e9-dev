# 泛微OA 数据表: `workflow_billfield`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_billfield`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldshowtypes` | 显示类型 | `integer` | - | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `billid` | 单据id | `integer` | - | 是 | - |
| 4 | `fieldname` | 数据库表字段名称 | `varchar2` | 480 | 是 | - |
| 5 | `fieldlabel` | 字段显示名称 | `integer` | - | 是 | - |
| 6 | `fielddbtype` | 单据字段数据库类型 | `varchar2` | 320 | 是 | - |
| 7 | `fieldhtmltype` | 单据字段页面类型 | `char` | 1 | 是 | - |

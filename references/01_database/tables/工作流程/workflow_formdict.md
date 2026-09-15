# 泛微OA 数据表: `workflow_formdict`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formdict`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldshowtypes` | 下拉开显示类型 | `integer` | - | 是 | - |
| 2 | `istemplate` | 是否模板 | `char` | 1 | 是 | - |
| 3 | `id` | ID | `integer` | - | 否 | - |
| 4 | `fieldname` | 字段名称 | `varchar2` | 320 | 是 | 数据库字段名 |
| 5 | `fielddbtype` | 字段数据库类型 | `varchar2` | 320 | 是 | - |
| 6 | `fieldhtmltype` | 字段页面类型 | `char` | 1 | 是 | - |

# 泛微OA 数据表: `hrm_formfield`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_formfield`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldid` | 字段id | `integer` | - | 否 | 字段id |
| 2 | `fielddbtype` | 字段数据库类型 | `varchar2` | 320 | 是 | &nbsp;integer、varchar |
| 3 | `fieldname` | 字段名称 | `varchar2` | 240 | 是 | 数据库保存字段名 |
| 4 | `fieldlabel` | 字段显示名labelid | `varchar2` | 800 | 是 | 字段显示名labelid |
| 5 | `fieldhtmltype` | 字段页面类型 | `char` | 1 | 是 | - |

# 泛微OA 数据表: `departmentdefinefield`

- **所属模块**: `人力资源`
- **数据库表名**: `departmentdefinefield`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `billid` | 单据id | `integer` | - | 是 | 单据id |
| 3 | `fieldname` | 数据库表字段名称 | `varchar2` | 480 | 是 | 数据库表字段名称 |
| 4 | `fieldlabel` | 字段显示名称 | `integer` | - | 是 | 字段显示名称 |
| 5 | `fielddbtype` | 单据字段数据库类型 | `varchar2` | 320 | 是 | 单据字段数据库类型 |
| 6 | `fieldhtmltype` | 单据字段页面类型 | `char` | 1 | 是 | - |

# 泛微OA 数据表: `hrmprivacysetting`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmprivacysetting`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `fieldid` | 字段ID | `varchar2` | 1000 | 是 | 字段ID   关联hrm_formfield |
| 3 | `fieldname` | 字段名 | `varchar2` | 1000 | 是 | 字段名 |
| 4 | `fieldlabel` | 字段显示名 | `varchar2` | 1000 | 是 | 字段显示名 |
| 5 | `showtypedefault` | 默认显示类型 | `varchar2` | 800 | 是 | 默认显示类型 |
| 6 | `showset` | 显示设置 | `varchar2` | 800 | 是 | 显示设置 |
| 7 | `showtype` | 显示类型 | `varchar2` | 800 | 是 | 显示类型 |

# 泛微OA 数据表: `crm_customizeoption`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_customizeoption`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `tabledesc` | 信息表类型 | `integer` | - | 是 | 1-客户信息表,2-联系人信息表 |
| 3 | `fieldname` | 相应表中的字段名 | `varchar2` | 1000 | 是 | 相应表中的字段名 |
| 4 | `labelid` | 字段显示名的Label的ID | `integer` | - | 是 | 字段显示名的Label的ID |
| 5 | `labelname` | 字段显示名,以后会不用 | `varchar2` | 1000 | 是 | 字段显示名,以后会不用 |

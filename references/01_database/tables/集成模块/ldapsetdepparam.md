# 泛微OA 数据表: `ldapsetdepparam`

- **所属模块**: `集成模块`
- **数据库表名**: `ldapsetdepparam`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `depattr` | 部门字段名称 | `varchar2` | 800 | 是 | 部门字段名称 |
| 3 | `ldapdepattr` | ldap属性名称 | `varchar2` | 800 | 是 | ldap属性名称 |

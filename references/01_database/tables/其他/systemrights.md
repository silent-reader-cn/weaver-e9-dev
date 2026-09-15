# 泛微OA 数据表: `systemrights`

- **所属模块**: `其他`
- **数据库表名**: `systemrights`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | ID |
| 2 | `rightdesc` | 权限描述 | `varchar2` | 1000 | 是 | 权限描述 |
| 3 | `righttype` | 权限类型 | `char` | 1 | 是 | 权限类型 |
| 4 | `detachable` | 可分权权限 | `integer` | - | 是 | 可分权权限 |

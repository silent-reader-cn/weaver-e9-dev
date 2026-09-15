# 泛微OA 数据表: `hrm_transfer_set`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_transfer_set`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `type` | 所属类型 | `integer` | - | 否 | 所属类型 |
| 3 | `name` | 权限名称 | `varchar2` | 400 | 是 | 权限名称 |
| 4 | `code_name` | 权限代码 | `varchar2` | 400 | 是 | 权限代码 |
| 5 | `link_address` | 链接地址 | `varchar2` | 1000 | 是 | 链接地址 |
| 6 | `class_name` | 关联类src 路径 | `varchar2` | 1000 | 是 | 关联类src 路径 |
| 7 | `link_class_name` | 链接类别名称 | `varchar2` | 1000 | 是 | 链接类别名称 |

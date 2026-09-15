# 泛微OA 数据表: `cus_treeform`

- **所属模块**: `知识管理`
- **数据库表名**: `cus_treeform`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `scope` | 范围 | `varchar2` | 50 | 否 | - |
| 2 | `formlabel` | 显示名称 | `varchar2` | 400 | 否 | - |
| 3 | `id` | 显示标识 | `integer` | - | 否 | - |
| 4 | `parentid` | 父节点id | `integer` | - | 否 | - |
| 5 | `viewtype` | 显示类型 | `char` | 1 | 是 | - |
| 6 | `scopeorder` | 显示顺序 | `integer` | - | 是 | - |

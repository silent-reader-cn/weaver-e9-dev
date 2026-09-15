# 泛微OA 数据表: `cus_formdict`

- **所属模块**: `知识管理`
- **数据库表名**: `cus_formdict`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `qfws` | ？ | `varchar2` | 1000 | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `fielddbtype` | 字段数据库类型 | `varchar2` | 320 | 是 | - |
| 4 | `fieldhtmltype` | 字段页面类型 | `char` | 1 | 是 | - |
| 5 | `type` | 字段详细类型 | `integer` | - | 是 | - |
| 6 | `fieldname` | 数据库表字段名称 | `varchar2` | 240 | 是 | - |
| 7 | `fieldlabel` | 字段显示名称 | `varchar2` | 1000 | 是 | - |
| 8 | `scope` | 范围 | `varchar2` | 200 | 是 | 文档对应：doccustomfieldbyseccategory |

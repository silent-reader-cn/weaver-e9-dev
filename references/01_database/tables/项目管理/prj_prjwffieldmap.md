# 泛微OA 数据表: `prj_prjwffieldmap`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_prjwffieldmap`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `mainid` | 流程配置主表id | `integer` | - | 是 | 流程配置主表id |
| 3 | `fieldtype` | 字段类型 | `integer` | - | 是 | 字段类型 |
| 4 | `fieldid` | 字段id | `integer` | - | 是 | 字段id |
| 5 | `fieldname` | 字段名 | `varchar2` | 400 | 是 | 字段名 |

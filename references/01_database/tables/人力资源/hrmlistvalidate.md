# 泛微OA 数据表: `hrmlistvalidate`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmlistvalidate`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `tab_label` | 标签值 | `varchar2` | 400 | 是 | 标签值 |
| 2 | `id` | ID | `integer` | - | 否 | ID |
| 3 | `name` | 人力资源功能项目名称 | `varchar2` | 400 | 是 | 人力资源功能项目名称 |
| 4 | `validate_n` | 是否启用 | `integer` | - | 是 | 0：不启用，1：启用 |
| 5 | `parentid` | 父ID | `integer` | - | 是 | 父ID |
| 6 | `tab_url` | 标签地址 | `varchar2` | 1000 | 是 | 标签地址 |
| 7 | `tab_type` | 标签类型 | `integer` | - | 是 | 标签类型 |
| 8 | `tab_index` | 标签索引 | `integer` | - | 是 | 标签索引 |

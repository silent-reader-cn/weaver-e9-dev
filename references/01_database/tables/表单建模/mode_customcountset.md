# 泛微OA 数据表: `mode_customcountset`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_customcountset`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `orderid` | 排序id | `integer` | - | 是 | - |
| 2 | `id` | id | `integer` | - | 否 | - |
| 3 | `customid` | 查询id | `integer` | - | 是 | - |
| 4 | `name` | 名称 | `varchar2` | 1000 | 是 | - |
| 5 | `formtype` | 表单类型 | `char` | 1 | 是 | - |
| 6 | `formname` | 表单名称 | `varchar2` | 1000 | 是 | - |
| 7 | `countfield` | 统计字段 | `varchar2` | 1000 | 是 | - |
| 8 | `defaultsql` | 过滤sql | `varchar2` | 1000 | 是 | - |
| 9 | `icon` | 图标 | `varchar2` | 1000 | 是 | - |
| 10 | `setdesc` | 描述 | `varchar2` | 1000 | 是 | - |

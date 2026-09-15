# 泛微OA 数据表: `formmodeelement`

- **所属模块**: `表单建模`
- **数据库表名**: `formmodeelement`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isautoomit` | 超出宽度自动省略 | `varchar2` | 8 | 是 | - |
| 2 | `morehref` | 多连接 | `varchar2` | 2000 | 是 | - |
| 3 | `id` | ID | `integer` | - | 否 | - |
| 4 | `eid` | 门户页面id | `integer` | - | 是 | - |
| 5 | `reportid` | 查询id | `integer` | - | 是 | - |
| 6 | `isshowunread` | 4 | `integer` | - | 是 | - |
| 7 | `fields` | 字段 | `varchar2` | 1000 | 是 | - |
| 8 | `fieldswidth` | 字段宽度 | `varchar2` | 1000 | 是 | - |
| 9 | `disorder` | 顺序 | `float` | 22 | 是 | - |
| 10 | `searchtitle` | 查询标题 | `varchar2` | 1000 | 是 | - |

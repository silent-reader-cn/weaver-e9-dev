# 泛微OA 数据表: `formmodeelementtemplate`

- **所属模块**: `表单建模`
- **数据库表名**: `formmodeelementtemplate`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `eid` | eid | `integer` | - | 是 | - |
| 3 | `reportid` | 查询id | `integer` | - | 是 | - |
| 4 | `isshowunread` | 是否显示已读 | `integer` | - | 是 | - |
| 5 | `fields` | 字段 | `varchar2` | 400 | 是 | - |
| 6 | `fieldswidth` | 字段宽度度 | `varchar2` | 400 | 是 | - |
| 7 | `disorder` | 排序 | `float` | 22 | 是 | - |
| 8 | `searchtitle` | 查询名称 | `varchar2` | 400 | 是 | - |
| 9 | `isautoomit` | 是否自动下滑 | `varchar2` | 1 | 是 | - |

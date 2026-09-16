# 泛微OA 数据表: `formmodeelementtemplate`

- **中文名称**: 表单建模门户元素表
- **所属模块**: `表单建模`
- **数据库表名**: `formmodeelementtemplate`
- **主键**: `id`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `eid` | eid | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `reportid` | 查询id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `isshowunread` | 是否显示已读 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `fields` | 字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 6 | `fieldswidth` | 字段宽度度 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 7 | `disorder` | 排序 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 8 | `searchtitle` | 查询名称 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 9 | `isautoomit` | 是否自动下滑 | `varchar2` | 1 | 是 | 否 | 否 | - | - | - |

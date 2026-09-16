# 泛微OA 数据表: `mode_exportexcelfield`

- **中文名称**: 查询列表导出excel自定义字段
- **所属模块**: `表单建模`
- **数据库表名**: `mode_exportexcelfield`
- **主键**: `customid`
- **字段数**: `7`

> 说明：查询列表导出excel自定义字段详细说明表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `customid` | 查询列表id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `fieldid` | 字段id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `isexport` | 是否导出 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 4 | `exportorder` | 导出顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `lastoperator` | 操作者id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `operatedate` | 操作日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 7 | `operatetime` | 操作时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |

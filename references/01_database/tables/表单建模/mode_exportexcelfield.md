# 泛微OA 数据表: `mode_exportexcelfield`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_exportexcelfield`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `customid` | 查询列表id | `integer` | - | 否 | - |
| 2 | `fieldid` | 字段id | `integer` | - | 否 | - |
| 3 | `isexport` | 是否导出 | `char` | 1 | 是 | - |
| 4 | `exportorder` | 导出顺序 | `integer` | - | 是 | - |
| 5 | `lastoperator` | 操作者id | `integer` | - | 是 | - |
| 6 | `operatedate` | 操作日期 | `varchar2` | 10 | 是 | - |
| 7 | `operatetime` | 操作时间 | `varchar2` | 8 | 是 | - |

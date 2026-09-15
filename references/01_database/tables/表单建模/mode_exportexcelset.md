# 泛微OA 数据表: `mode_exportexcelset`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_exportexcelset`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `customid` | 查询列表id | `integer` | - | 否 | - |
| 2 | `iscustomstyle` | 是否自定义导出样式 | `char` | 1 | 是 | - |
| 3 | `isgroupexport` | 是否分组导出 | `char` | 1 | 是 | - |
| 4 | `isexportfield` | 是否自定义导出字段 | `char` | 1 | 是 | - |
| 5 | `lastoperator` | 操作者id | `integer` | - | 是 | - |
| 6 | `operatedate` | 操作日期 | `varchar2` | 10 | 是 | - |
| 7 | `operatetime` | 操作时间 | `varchar2` | 8 | 是 | - |

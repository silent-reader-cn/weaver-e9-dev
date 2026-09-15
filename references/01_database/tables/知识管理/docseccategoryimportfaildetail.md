# 泛微OA 数据表: `docseccategoryimportfaildetail`

- **所属模块**: `知识管理`
- **数据库表名**: `docseccategoryimportfaildetail`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 目录id | `integer` | - | 否 | - |
| 2 | `historyid` | 历史目录id | `integer` | - | 是 | - |
| 3 | `failrow` | 失败的行 | `integer` | - | 是 | - |
| 4 | `failcol` | 失败的列 | `varchar2` | 800 | 是 | - |
| 5 | `seccategoryname` | 目录名称 | `varchar2` | 1000 | 是 | - |
| 6 | `failreason` | 失败原因 | `varchar2` | 800 | 是 | - |

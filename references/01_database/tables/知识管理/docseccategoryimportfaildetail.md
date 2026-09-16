# 泛微OA 数据表: `docseccategoryimportfaildetail`

- **中文名称**: 目录导入失败明细表
- **所属模块**: `知识管理`
- **数据库表名**: `docseccategoryimportfaildetail`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 目录id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `historyid` | 历史目录id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `failrow` | 失败的行 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `failcol` | 失败的列 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 5 | `seccategoryname` | 目录名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `failreason` | 失败原因 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |

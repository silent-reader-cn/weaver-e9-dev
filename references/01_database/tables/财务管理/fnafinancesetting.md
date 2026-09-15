# 泛微OA 数据表: `fnafinancesetting`

- **所属模块**: `财务管理`
- **数据库表名**: `fnafinancesetting`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `guid1` | 主键 | `char` | 32 | 否 | - |
| 2 | `fnavoucherxmlid` | fnavoucherxml.id | `integer` | - | 是 | - |
| 3 | `fieldname` | 字段名称 | `varchar2` | 800 | 是 | - |
| 4 | `fieldvaluetype1` | 字段值类型1 | `char` | 20 | 是 | - |
| 5 | `fieldvaluetype2` | 字段值类型2 | `char` | 20 | 是 | - |
| 6 | `fielddbtbname` | 字段数据库表名 | `char` | 100 | 是 | - |
| 7 | `detailtable` | 明细表序号 | `integer` | - | 是 | - |
| 8 | `fielddbname` | 字段数据类型名称 | `char` | 100 | 是 | - |
| 9 | `fielddbtype` | 字段数据类型 | `char` | 20 | 是 | - |
| 10 | `datasourceid` | oa外部数据源id | `varchar2` | 1000 | 是 | - |
| 11 | `fieldvalue` | 字段值 | `clob` | 4000 | 是 | - |

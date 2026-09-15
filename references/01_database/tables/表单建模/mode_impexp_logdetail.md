# 泛微OA 数据表: `mode_impexp_logdetail`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_impexp_logdetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `logid` | 日志id | `integer` | - | 否 | - |
| 3 | `tablename` | 表名称 | `varchar2` | 400 | 是 | - |
| 4 | `logtype` | 日志类型 | `integer` | - | 否 | - |
| 5 | `message` | 详细信息 | `varchar2` | 1000 | 是 | - |

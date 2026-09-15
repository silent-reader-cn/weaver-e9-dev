# 泛微OA 数据表: `mode_impfailurelog`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_impfailurelog`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `modeid` | 模块id | `integer` | - | 否 | 对应的是模块的id，即modeinfo的id |
| 3 | `errormsg` | 错误信息 | `varchar2` | 2000 | 否 | 记录行列错误信息 |
| 4 | `tablename` | 表名称 | `varchar2` | 2000 | 否 | 表名称 |
| 5 | `tablefield` | 表字段名称 | `varchar2` | 2000 | 否 | 表字段名称，字段类型，字段名 |
| 6 | `detailmation` | 详细信息 | `varchar2` | 2000 | 否 | 记录日志报错的详细信息 |
| 7 | `searchid` | uuid | `varchar2` | 2000 | 否 | 用于查询页面信息，等于表mode_batchimp_log的failurerow |

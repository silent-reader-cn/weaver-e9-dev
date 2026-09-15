# 泛微OA 数据表: `mode_impexp_recorddetail`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_impexp_recorddetail`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `tablename` | 表名称 | `varchar2` | 400 | 否 | - |
| 3 | `columnname` | 字段名称 | `varchar2` | 400 | 否 | - |
| 4 | `columnvalue` | 字段值 | `varchar2` | 800 | 是 | - |
| 5 | `requestid` | 请求id | `varchar2` | 256 | 否 | - |
| 6 | `rollbackid` | 版本id | `varchar2` | 256 | 是 | - |
| 7 | `ptype` | 类型 | `integer` | - | 否 | - |

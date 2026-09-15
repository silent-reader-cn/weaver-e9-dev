# 泛微OA 数据表: `mailerrorhint`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailerrorhint`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `errorname` | 错误异常名称 | `varchar2` | 1000 | 是 | - |
| 3 | `errorhint` | 错误提示 | `varchar2` | 1000 | 是 | - |
| 4 | `solution` | 解决方案 | `varchar2` | 1000 | 是 | - |
| 5 | `keyword` | 错误关键字 | `varchar2` | 1000 | 是 | - |
| 6 | `isvariable` | 是否存在替换字符 | `integer` | - | 是 | - |

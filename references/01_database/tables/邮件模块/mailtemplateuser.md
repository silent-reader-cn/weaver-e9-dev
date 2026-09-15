# 泛微OA 数据表: `mailtemplateuser`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailtemplateuser`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 2 | `templateid` | 模板id | `integer` | - | 是 | 模板id |
| 3 | `templatetype` | 模板类型 | `char` | 1 | 是 | 是否为系统模板。1：系统模板。非1：用户模板 |

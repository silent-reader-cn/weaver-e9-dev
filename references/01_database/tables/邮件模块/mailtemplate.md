# 泛微OA 数据表: `mailtemplate`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailtemplate`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `userid` | 用户id | `integer` | - | 是 | - |
| 3 | `templatename` | 模板名称 | `varchar2` | 400 | 是 | - |
| 4 | `templatedescription` | 模板描述 | `varchar2` | 800 | 是 | - |
| 5 | `templatesubject` | 邮件主题 | `varchar2` | 800 | 是 | - |
| 6 | `templatecontent` | 邮件内容 | `clob` | 4000 | 是 | - |
| 7 | `isdefault` | 是否默认模板 | `char` | 1 | 是 | - |

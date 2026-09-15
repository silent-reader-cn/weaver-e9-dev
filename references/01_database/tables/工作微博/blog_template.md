# 泛微OA 数据表: `blog_template`

- **所属模块**: `工作微博`
- **数据库表名**: `blog_template`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `tempname` | 模板名称 | `varchar2` | 800 | 是 | - |
| 3 | `isused` | 是否启用 | `integer` | - | 是 | - |
| 4 | `tempcontent` | 模板内容 | `clob` | 4000 | 是 | - |
| 5 | `description` | 描述 | `clob` | 4000 | 是 | - |
| 6 | `tempdesc` | 模板描述 | `varchar2` | 1000 | 是 | - |
| 7 | `issystem` | 是否系统模板 | `char` | 1 | 是 | - |
| 8 | `userid` | 人员id | `integer` | - | 是 | - |

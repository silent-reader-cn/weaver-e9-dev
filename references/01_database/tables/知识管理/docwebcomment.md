# 泛微OA 数据表: `docwebcomment`

- **所属模块**: `知识管理`
- **数据库表名**: `docwebcomment`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `docid` | 文档id | `integer` | - | 是 | - |
| 3 | `name` | 名称 | `varchar2` | 800 | 是 | - |
| 4 | `mail_1` | 邮件 | `varchar2` | 240 | 是 | - |
| 5 | `comment_1` | 内容 | `varchar2` | 2000 | 是 | - |
| 6 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 7 | `createtime` | 创建时间 | `char` | 8 | 是 | - |

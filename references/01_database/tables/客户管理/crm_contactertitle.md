# 泛微OA 数据表: `crm_contactertitle`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_contactertitle`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `fullname` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 3 | `description` | 描述 | `varchar2` | 1000 | 是 | 描述 |
| 4 | `usetype` | 使用方法 | `char` | 1 | 是 | "p"表示前缀，"s"表示后缀 |
| 5 | `language` | 使用该称呼底语言种类ID | `integer` | - | 是 | 同时也是相关信息的使用语言 |
| 6 | `abbrev` | 称呼的缩写 | `varchar2` | 1000 | 是 | 在MailMerge模板中可以选择使用全称还是缩写 |
| 7 | `orderkey` | 排序字段 | `integer` | - | 是 | 排序字段 |

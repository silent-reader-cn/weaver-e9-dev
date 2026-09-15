# 泛微OA 数据表: `email_label_detail`

- **所属模块**: `邮件模块`
- **数据库表名**: `email_label_detail`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 主键 |
| 2 | `labelid` | 标签id | `integer` | - | 是 | 标签值id。email_label表id |
| 3 | `mailid` | 邮件id | `integer` | - | 是 | 邮件id。mailresource表id |

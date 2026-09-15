# 泛微OA 数据表: `mailsendrecord`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailsendrecord`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 表mailsendmain id | `integer` | - | 是 | - |
| 2 | `sendto` | 收件人地址 | `varchar2` | 1000 | 是 | - |
| 3 | `subject` | 邮件标题 | `varchar2` | 1000 | 是 | - |
| 4 | `body` | 邮件内容 | `varchar2` | 4000 | 是 | - |
| 5 | `sendcount` | 发送次数 | `integer` | - | 是 | - |
| 6 | `sendtoid` | 收件人员id | `integer` | - | 是 | - |

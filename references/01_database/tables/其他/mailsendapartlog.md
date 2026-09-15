# 泛微OA 数据表: `mailsendapartlog`

- **所属模块**: `其他`
- **数据库表名**: `mailsendapartlog`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `mailid` | 邮件id | `integer` | - | 否 | - |
| 2 | `sendfrom` | 发件人 | `varchar2` | 2100 | 是 | - |
| 3 | `sendto` | 收件人 | `varchar2` | 100 | 是 | - |
| 4 | `sendstatus` | 发送结果，1成功，0失败 | `integer` | - | 是 | - |
| 5 | `senddate` | 发送时间 | `char` | 19 | 是 | - |
| 6 | `errormsg` | 错误详情 | `varchar2` | 4000 | 是 | - |

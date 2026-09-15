# 泛微OA 数据表: `mailsendmain`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailsendmain`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `sendfrom` | 发件人地址 | `varchar2` | 1000 | 是 | - |
| 3 | `sendcc` | 抄送地址 | `varchar2` | 1000 | 是 | - |
| 4 | `sendbcc` | 密送地址 | `varchar2` | 1000 | 是 | - |
| 5 | `charset` | 编码类型 | `char` | 1 | 是 | - |
| 6 | `priority` | 重要级别 | `char` | 1 | 是 | - |
| 7 | `senddate` | 发送日期 | `char` | 10 | 是 | - |
| 8 | `sendtime` | 发送时间 | `char` | 8 | 是 | - |
| 9 | `isfinished` | 无文档可查 | `char` | 1 | 是 | - |
| 10 | `sendtotype` | 无文档可查 | `char` | 1 | 是 | - |
| 11 | `sender` | 无文档可查 | `integer` | - | 是 | - |

# 泛微OA 数据表: `mailaccount`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailaccount`
- **字段总数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isstarttls` | 是否使用TLS方式 | `char` | 1 | 是 | 1：启用 |
| 2 | `id` | ID | `integer` | - | 是 | - |
| 3 | `userid` | 用户id | `integer` | - | 是 | - |
| 4 | `accountname` | 帐户名称 | `varchar2` | 50 | 是 | - |
| 5 | `accountid` | 登录名 | `varchar2` | 400 | 是 | - |
| 6 | `accountpassword` | 密码 | `varchar2` | 400 | 是 | - |
| 7 | `servertype` | 服务器类型 | `integer` | - | 是 | - |
| 8 | `popserver` | pop3服务器 | `varchar2` | 800 | 是 | - |
| 9 | `popserverport` | pop3服务器端口 | `integer` | - | 是 | - |
| 10 | `smtpserver` | smtp服务器 | `varchar2` | 800 | 是 | - |
| 11 | `smtpserverport` | smtp服务器端口 | `integer` | - | 是 | - |
| 12 | `needcheck` | 是否需要发件认证 | `char` | 1 | 是 | - |
| 13 | `needsave` | 是否保留服务器上的邮件 | `char` | 1 | 是 | - |
| 14 | `isdefault` | 是否默认帐户 | `char` | 1 | 是 | - |
| 15 | `accountmailaddress` | 邮件地址 | `varchar2` | 50 | 是 | - |
| 16 | `autoreceive` | 自动收取邮件时是否包含此帐户 | `integer` | - | 是 | - |
| 17 | `encryption` | 邮箱密码是否启用加密 | `integer` | - | 是 | 1为启用 |
| 18 | `sendneedssl` | 是否以ssl方式发送 | `char` | 1 | 是 | - |
| 19 | `getneedssl` | 是否以ssl方式接收 | `char` | 1 | 是 | - |
| 20 | `receivescope` | 接收时间范围 | `integer` | - | 是 | - |
| 21 | `receivedatescope` | 接收时间 | `varchar2` | 400 | 是 | - |
| 22 | `sendstatus` | 发送状态 | `char` | 1 | 是 | - |
| 23 | `receivestatus` | 接收状态 | `char` | 1 | 是 | - |
| 24 | `lasttime` | 上次接收的邮件最后时间 | `varchar2` | 400 | 是 | 存储上一波接收的优先最大的senddate值 |

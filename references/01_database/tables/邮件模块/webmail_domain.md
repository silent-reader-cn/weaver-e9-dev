# 泛微OA 数据表: `webmail_domain`

- **所属模块**: `邮件模块`
- **数据库表名**: `webmail_domain`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `domain_id` | 邮件服务器id | `integer` | - | 是 | - |
| 2 | `domain` | 邮件服务器域名 | `varchar2` | 800 | 是 | - |
| 3 | `pop_server` | 收信服务器地址 | `varchar2` | 800 | 是 | - |
| 4 | `smtp_server` | 发信服务器地址 | `varchar2` | 800 | 是 | - |
| 5 | `is_smtp_auth` | 发件认证 | `varchar2` | 800 | 是 | - |
| 6 | `pop_port` | 收信服务器端口 | `varchar2` | 800 | 是 | - |
| 7 | `smtp_port` | 发信服务器端口 | `varchar2` | 800 | 是 | - |
| 8 | `is_pop` | 是否使用pop协议 | `varchar2` | 800 | 是 | - |
| 9 | `is_ssl_pop` | 是否使用ssl下pop协议 | `varchar2` | 800 | 是 | - |
| 10 | `is_ssl_smtp` | 是否使用ssl下smtp协议 | `varchar2` | 800 | 是 | - |
| 11 | `need_save` | 保留服务器上邮件 | `integer` | - | 是 | - |
| 12 | `auto_receive` | 自动接收 | `integer` | - | 是 | - |
| 13 | `receive_scopt` | 收件范围 | `integer` | - | 是 | - |
| 14 | `is_start_tls` | 是否启用TLS方式 | `char` | 1 | 是 | 1：是 |

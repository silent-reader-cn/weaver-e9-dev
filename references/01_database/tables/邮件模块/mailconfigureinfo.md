# 泛微OA 数据表: `mailconfigureinfo`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailconfigureinfo`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `innermail` | 是否使用内部邮件 | `integer` | - | 是 | - |
| 2 | `outtermail` | 是否使用外部邮件 | `integer` | - | 是 | - |
| 3 | `filepath` | 邮件附件上传目录 | `varchar2` | 1000 | 是 | - |
| 4 | `totalattachmentsize` | 邮件附件上传大小 | `integer` | - | 是 | - |
| 5 | `perattachmentsize` | 单个附件大小 | `integer` | - | 是 | - |
| 6 | `attachmentcount` | 附件上传数量 | `integer` | - | 是 | - |
| 7 | `isall` | 是否开启所有人 | `integer` | - | 是 | - |
| 8 | `iseml` | 是否开启eml导出 | `integer` | - | 是 | - |
| 9 | `emlpath` | eml存放目录 | `varchar2` | 400 | 是 | - |
| 10 | `emlperiod` | eml保存天数 | `integer` | - | 是 | - |
| 11 | `cleartime` | 垃圾邮件自动清理时间 | `integer` | - | 是 | - |
| 12 | `dimissionemptime` | 离职人员邮件清理时间 | `integer` | - | 是 | - |
| 13 | `isclear` | 是否开启自动清理 | `integer` | - | 是 | - |
| 14 | `autoreceive` | 是否开启自动接收 | `integer` | - | 是 | 1：开启 |
| 15 | `timecount` | 自动接收频率 | `integer` | - | 是 | 频率毫秒数 |
| 16 | `isrecordsuccessmailremindlog` | 是否记录发送成功日志 | `integer` | - | 是 | 1：开启 |
| 17 | `clearmailremindlogtimelimit` | 群发日志保留时间(天) | `integer` | - | 是 | 天数值 |

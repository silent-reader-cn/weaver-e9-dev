# 泛微OA 数据表: `sms_message`

- **所属模块**: `短信模块`
- **数据库表名**: `sms_message`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | 0 | 否 | 主键 |
| 2 | `message` | 短信内容 | `varchar2` | 4000 | 是 | 短信内容 |
| 3 | `recievenumber` | 接收短信号码 | `varchar2` | 120 | 是 | 短信接收号码 |
| 4 | `sendnumber` | 发送短信号码 | `varchar2` | 120 | 是 | 短信发送号码 |
| 5 | `messagestatus` | 短信状态 | `char` | 1 | 是 | 0待发 1发送成功 2已收到 3发送失败 |
| 6 | `requestid` | 流程id | `integer` | 0 | 是 | 流程id |
| 7 | `userid` | 发送人id | `integer` | 0 | 是 | 发送人id |
| 8 | `usertype` | 发送人类型 | `char` | 1 | 是 | 发送人类型 |
| 9 | `messagetype` | 短信类型 | `char` | 1 | 是 | 1:回复  2:发送 |
| 10 | `finishtime` | 发送时间 | `char` | 19 | 是 | 发送时间 2018-12-20 14:00:00 |
| 11 | `smsyear` | 发送年 | `char` | 4 | 是 | 发送年 |
| 12 | `smsmonth` | 发送月 | `char` | 2 | 是 | 发送月 |
| 13 | `smsday` | 发送日 | `char` | 2 | 是 | 发送日 |
| 14 | `isdelete` | 是否逻辑删除 | `char` | 1 | 是 | 0 未删除 1已删除 |
| 15 | `touserid` | 接收人id | `integer` | 0 | 是 | &nbsp; |
| 16 | `tousertype` | 接收人类型 | `char` | 1 | 是 | &nbsp; |

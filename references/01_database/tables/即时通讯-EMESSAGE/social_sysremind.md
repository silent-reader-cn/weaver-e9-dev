# 泛微OA 数据表: `social_sysremind`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_sysremind`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `remindtype` | 提醒类型 | `integer` | - | 是 | 提醒类型 |
| 3 | `requestid` | 提醒id | `integer` | - | 是 | 提醒id |
| 4 | `requesttitle` | 提醒标题 | `varchar2` | 800 | 是 | 提醒标题 |
| 5 | `requestdetails` | 提醒细节 | `varchar2` | 2000 | 是 | 提醒细节 |
| 6 | `sendtime` | 发送时间 | `char` | 20 | 是 | 发送时间 |
| 7 | `extra` | 额外信息 | `varchar2` | 1000 | 是 | 额外信息 |

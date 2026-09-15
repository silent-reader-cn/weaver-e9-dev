# 泛微OA 数据表: `social_immsgread`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_immsgread`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `msgid` | 消息id | `varchar2` | 100 | 否 | 消息id |
| 3 | `receiverid` | 接受者id | `integer` | - | 否 | 接受者id |
| 4 | `status` | 消息状态 | `integer` | - | 否 | 消息状态 |
| 5 | `sendtime` | 消息发送时间 | `char` | 23 | 否 | 消息发送时间 |
| 6 | `userid` | 发送者id | `integer` | - | 否 | 发送者id |

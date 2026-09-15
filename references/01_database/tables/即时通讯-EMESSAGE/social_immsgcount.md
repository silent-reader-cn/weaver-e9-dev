# 泛微OA 数据表: `social_immsgcount`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_immsgcount`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | 0 | 是 | 主键id |
| 2 | `msgid` | 消息id | `varchar2` | 800 | 是 | 消息id |
| 3 | `receiverid` | 接收人id | `integer` | - | 是 | 接收人id |
| 4 | `status` | 消息状态 | `integer` | - | 是 | 1：未读；0：已读 |
| 5 | `sendtime` | 发送时间 | `char` | 23 | 是 | 发送时间 |
| 6 | `userid` | 发送人id | `integer` | - | 是 | 发送人id |

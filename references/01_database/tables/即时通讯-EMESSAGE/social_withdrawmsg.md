# 泛微OA 数据表: `social_withdrawmsg`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_withdrawmsg`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `msgid` | 消息id | `varchar2` | 50 | 是 | 消息id |
| 3 | `userid` | 发送人id | `integer` | - | 是 | 发送人id |
| 4 | `targetid` | 接收人id | `varchar2` | 400 | 是 | 接收人id |

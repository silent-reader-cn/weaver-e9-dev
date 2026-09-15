# 泛微OA 数据表: `social_broadcastreceiver`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_broadcastreceiver`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `msgid` | 广播的id | `varchar2` | 400 | 是 | 广播的id（和social_broadcast对应） |
| 3 | `receiverid` | 接收人id | `integer` | - | 是 | 接收人id |

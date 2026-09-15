# 泛微OA 数据表: `social_broadcast`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_broadcast`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 序列 | `integer` | - | 否 | 广播序列号。不同数据库有不同的生成策略 |
| 2 | `plaintext` | 广播内容 | `clob` | 4000 | 否 | 广播内容（文本消息） |
| 3 | `msgid` | 消息id | `varchar2` | 400 | 否 | 消息id |
| 4 | `fromuserid` | 发起人 | `integer` | - | 否 | 发起人的id |
| 5 | `sendtime` | 发起时间 | `varchar2` | 160 | 否 | 发起广播的时间 |
| 6 | `requestobjs` | 附件JSON串 | `varchar2` | 1000 | 否 | 记录发起广播时的附件，图片等信息。 |
| 7 | `extra` | 附属信息 | `varchar2` | 1000 | 是 | extra附属消息 |

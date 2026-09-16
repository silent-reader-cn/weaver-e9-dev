# 泛微OA 数据表: `social_imconversation`

- **中文名称**: emessage用户所有会话列表
- **所属模块**: `即时通讯/EMESSAGE`
- **数据库表名**: `social_imconversation`
- **主键**: `id`
- **字段数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 否 | 否 | - | - | 主键id |
| 2 | `userid` | 最后发言的用户id | `integer` | - | 否 | 否 | 否 | - | - | 最后发言的用户id |
| 3 | `targetid` | 会话id | `varchar2` | 800 | 否 | 否 | 否 | - | - | 会话id |
| 4 | `targettype` | 会话类型 | `varchar2` | 160 | 否 | 否 | 否 | - | - | 会话类型 |
| 5 | `targetportrait` | 会话描述（暂未使用） | `varchar2` | 800 | 是 | 否 | 否 | - | - | 用来保存对会话进行备注的信息，没有用到 |
| 6 | `targetname` | 会话名称 | `varchar2` | 800 | 否 | 否 | 否 | - | - | 会话名称 |
| 7 | `msgid` | 最近一条消息的id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 最近一条消息的id |
| 8 | `unreadcnt` | 未读数（暂未使用） | `integer` | - | 是 | 否 | 否 | - | - | 未读数 |
| 9 | `istop` | Deprecated废弃字段 | `char` | 1 | 是 | 否 | 否 | - | - | Deprecated废弃字段 |
| 10 | `lasttime` | 最后时间 | `varchar2` | 800 | 否 | 否 | 否 | - | - | 最后时间 |
| 11 | `senderid` | 发送者id(必达,广播等) | `integer` | - | 是 | 否 | 否 | - | - | 发送者id(必达,广播等) |
| 12 | `isopenfire` | 是否基于openfire | `integer` | - | 是 | 否 | 否 | - | - | 是否基于openfire |
| 13 | `msgcontent` | 会话最近一条消息的内容 | `nvarchar2` | 4000 | 否 | 否 | 否 | - | - | 会话最近一条消息的内容 |

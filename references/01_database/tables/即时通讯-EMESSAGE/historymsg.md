# 泛微OA 数据表: `historymsg`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `historymsg`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fullamount` | 客户端发的完整消息体 | `clob` | 4000 | 是 | 客户端发的完整消息体 |
| 2 | `msgid` | 消息id | `varchar2` | 100 | 是 | 消息id |
| 3 | `id` | 自增id | `integer` | - | 是 | 自增id |
| 4 | `fromuserid` | 消息发送方 | `varchar2` | 100 | 是 | 消息发送方 |
| 5 | `targetid` | 会话id | `varchar2` | 100 | 是 | 会话id |
| 6 | `targettype` | 会话类型 | `varchar2` | 800 | 是 | ( * 0:单聊   * 1:群聊   * 2:历史问题不用   * 3:必达   * 4:系统广播   * 5:系统提醒   * 6:小e工作台     * 7:最近的密聊   * 8:密聊中最近会话     * 100:次账号  (很少用)) |
| 7 | `groupid` | 会话范围 | `varchar2` | 100 | 是 | 会话范围 |
| 8 | `classname` | 消息类型 | `varchar2` | 800 | 是 | 消息类型 |
| 9 | `extra` | 消息扩展字段 | `clob` | 4000 | 是 | 消息扩展字段 |
| 10 | `type` | 无用 | `varchar2` | 800 | 是 | 废弃 |
| 11 | `imageuri` | 图片消息 fileid | `varchar2` | 800 | 是 | 图片消息 fileid |
| 12 | `datetime` | 消息入库时间 | `varchar2` | 100 | 是 | 消息入库时间 |
| 13 | `msgcontent` | 消息文本内容 | `clob` | 4000 | 是 | 消息文本内容 |

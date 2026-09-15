# 泛微OA 数据表: `historymsgrecently`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `historymsgrecently`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 自增 | `integer` | - | 是 | 自增 |
| 2 | `fromuserid` | 消息发送方 | `varchar2` | 100 | 是 | 消息发送方 |
| 3 | `targetid` | 会话id | `varchar2` | 100 | 是 | 会话id |
| 4 | `targettype` | 会话类型 | `varchar2` | 800 | 是 | ( * 0:单聊   * 1:群聊   * 2:历史问题不用   * 3:必达   * 4:系统广播   * 5:系统提醒   * 6:小e工作台     * 7:最近的密聊   * 8:密聊中最近会话     * 100:次账号  (很少用)) |
| 5 | `groupid` | 会话范围 | `varchar2` | 100 | 是 | 会话范围 |
| 6 | `classname` | 消息类型 | `varchar2` | 800 | 是 | 消息类型 |
| 7 | `msgcontent` | 消息文本内容 | `clob` | 4000 | 是 | 消息文本内容 |
| 8 | `extra` | 消息扩展字段 | `clob` | 4000 | 是 | 消息扩展字段 |
| 9 | `type` | 无用 | `varchar2` | 800 | 是 | 无用 |
| 10 | `imageuri` | 图片消息 fileid | `varchar2` | 800 | 是 | 图片消息 fileid |
| 11 | `datetime` | 消息入库时间 | `varchar2` | 100 | 是 | 消息入库时间 |
| 12 | `msgid` | 消息id | `varchar2` | 100 | 是 | 消息id |
| 13 | `fullamount` | 客户端发的完整消息体 | `clob` | 4000 | 是 | 客户端发的完整消息体 |

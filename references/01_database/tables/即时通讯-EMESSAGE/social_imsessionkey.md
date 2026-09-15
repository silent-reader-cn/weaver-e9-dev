# 泛微OA 数据表: `social_imsessionkey`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imsessionkey`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 是 | 主键id |
| 2 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 3 | `sessionkey` | session值 | `varchar2` | 1000 | 是 | session值 |
| 4 | `logindate` | 登录时间戳 | `varchar2` | 160 | 是 | 登录时间戳 |
| 5 | `loginstatus` | 目前状态 | `integer` | - | 是 | 目前状态  0 离线，1 pc在线， 2 WEB在线 |
| 6 | `updatetime` | 最后更新时间 | `varchar2` | 160 | 是 | 最后更新时间 |
| 7 | `socketstatus` | 客户端与消息服务器的连接状态 | `integer` | - | 是 | 客户端与消息服务器的连接状态 |

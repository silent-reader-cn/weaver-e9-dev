# 泛微OA 数据表: `social_imsessionkey`

- **中文名称**: emessage用户session表
- **所属模块**: `即时通讯/EMESSAGE`
- **数据库表名**: `social_imsessionkey`
- **主键**: `id`
- **字段数**: `7`

> 说明：emessage中用来记录用户登录后session值的表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键id | `integer` | - | 是 | 否 | 否 | - | - | 主键id |
| 2 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | 用户id |
| 3 | `sessionkey` | session值 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | session值 |
| 4 | `logindate` | 登录时间戳 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 登录时间戳 |
| 5 | `loginstatus` | 目前状态 | `integer` | - | 是 | 否 | 否 | - | - | 目前状态 0 离线，1 pc在线， 2 WEB在线 |
| 6 | `updatetime` | 最后更新时间 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 最后更新时间 |
| 7 | `socketstatus` | 客户端与消息服务器的连接状态 | `integer` | - | 是 | 否 | 否 | - | - | 客户端与消息服务器的连接状态 |

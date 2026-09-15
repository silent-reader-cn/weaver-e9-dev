# 泛微OA 数据表: `social_imsetting`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imsetting`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | 0 | 是 | 主键自增 |
| 2 | `userid` | 登陆用户id | `integer` | 0 | 是 | 登陆用户id |
| 3 | `targetid` | 接收用户id | `varchar2` | 1000 | 是 | 接收用户id |
| 4 | `remindtype` | 是否开启新消息通知 | `integer` | 0 | 是 | 1：开启新消息通知；0：关闭新消息通知 |
| 5 | `targettype` | 目标类型 | `integer` | 0 | 是 | 该字段值始终是1 |

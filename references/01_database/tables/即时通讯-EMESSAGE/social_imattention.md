# 泛微OA 数据表: `social_imattention`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imattention`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | 0 | 是 | 主键id |
| 2 | `userid` | 用户id | `integer` | 0 | 是 | 用户id |
| 3 | `targetid` | 聊天对象 | `varchar2` | 800 | 是 | 聊天对象 |
| 4 | `targettype` | 聊天类型 | `varchar2` | 160 | 是 | 聊天类型 |

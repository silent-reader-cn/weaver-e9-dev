# 泛微OA 数据表: `social_immsgtag`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_immsgtag`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `msgid` | 消息id | `varchar2` | 100 | 是 | 消息id |
| 3 | `tag` | 消息标记 | `char` | 1 | 是 | 消息标记 |
| 4 | `shareid` | 必达id | `number` | (11,0) | 是 | 必达id |

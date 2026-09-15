# 泛微OA 数据表: `social_translog`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_translog`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `roomname` | 群组名 | `varchar2` | 800 | 是 | 群组名 |
| 3 | `transfer` | 迁移目的地 | `char` | 1 | 是 | 迁移目的地 |
| 4 | `status` | 迁移状态 | `char` | 1 | 是 | 迁移状态 |
| 5 | `membercnt` | 群组人员 | `integer` | - | 是 | 群组人员 |
| 6 | `operatedate` | 操作时间 | `char` | 20 | 是 | 操作时间 |
| 7 | `operatorid` | 操作人员 | `integer` | - | 是 | 操作人员 |

# 泛微OA 数据表: `cowork_votes`

- **所属模块**: `协作管理`
- **数据库表名**: `cowork_votes`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `itemid` | 协作id | `integer` | - | 是 | - |
| 3 | `discussid` | 协作交流id | `integer` | - | 是 | - |
| 4 | `userid` | 点赞人 | `integer` | - | 是 | - |
| 5 | `createdate` | 点赞日期 | `char` | 10 | 是 | - |
| 6 | `createtime` | 点赞时间 | `char` | 5 | 是 | - |
| 7 | `status` | 是否点赞 | `varchar2` | 16 | 是 | - |

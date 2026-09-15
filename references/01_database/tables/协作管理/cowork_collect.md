# 泛微OA 数据表: `cowork_collect`

- **所属模块**: `协作管理`
- **数据库表名**: `cowork_collect`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `createtime` | 收藏时间 | `char` | 8 | 是 | - |
| 2 | `iscollect` | 是否收藏 | `varchar2` | 16 | 是 | - |
| 3 | `id` | id | `integer` | - | 否 | - |
| 4 | `itemid` | 协作id | `integer` | - | 是 | - |
| 5 | `discussid` | 协作交流id | `integer` | - | 是 | - |
| 6 | `userid` | 点赞人员 | `integer` | - | 是 | - |
| 7 | `createdate` | 收藏日期 | `char` | 10 | 是 | - |

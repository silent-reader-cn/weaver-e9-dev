# 泛微OA 数据表: `social_allgroupinfos`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_allgroupinfos`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | 0 | 否 | 主键id |
| 2 | `groupid` | 群id | `varchar2` | 800 | 是 | 群id |
| 3 | `groupname` | 群名称 | `varchar2` | 1000 | 是 | 群名称 |
| 4 | `createuserid` | 创建人id | `varchar2` | 800 | 是 | 创建人id |
| 5 | `members` | 群成员id | `varchar2` | 4000 | 是 | 群成员id |

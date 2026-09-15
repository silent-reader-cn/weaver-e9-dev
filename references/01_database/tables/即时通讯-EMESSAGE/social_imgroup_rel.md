# 泛微OA 数据表: `social_imgroup_rel`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imgroup_rel`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `rel_id` | 群分组id | `integer` | - | 否 | 对应social_imgroup表的id |
| 3 | `userid` | 用户id | `varchar2` | 800 | 否 | 用户id |
| 4 | `groupid` | 群id | `varchar2` | 800 | 否 | 群聊的id |
| 5 | `groupname` | 群名 | `varchar2` | 1000 | 否 | 群名称 |
| 6 | `grouprowid` | 暂时未使用 | `integer` | - | 是 | 暂时未使用 |
| 7 | `isopenfire` | 是否基于openfire | `integer` | - | 否 | 1代表基于openfire，0代表是公有云的 |

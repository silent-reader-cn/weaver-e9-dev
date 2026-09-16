# 泛微OA 数据表: `social_imgroup_rel`

- **中文名称**: emessage群聊所属群组
- **所属模块**: `即时通讯/EMESSAGE`
- **数据库表名**: `social_imgroup_rel`
- **主键**: `id`
- **字段数**: `7`

> 说明：记录emessage中每个群聊属于其中每个用户的某一个群组

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 否 | 否 | - | - | 主键id |
| 2 | `rel_id` | 群分组id | `integer` | - | 否 | 否 | 否 | - | - | 对应social_imgroup表的id |
| 3 | `userid` | 用户id | `varchar2` | 800 | 否 | 否 | 否 | - | - | 用户id |
| 4 | `groupid` | 群id | `varchar2` | 800 | 否 | 否 | 否 | - | - | 群聊的id |
| 5 | `groupname` | 群名 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | 群名称 |
| 6 | `grouprowid` | 暂时未使用 | `integer` | - | 是 | 否 | 否 | - | - | 暂时未使用 |
| 7 | `isopenfire` | 是否基于openfire | `integer` | - | 否 | 否 | 否 | - | - | 1代表基于openfire，0代表是公有云的 |

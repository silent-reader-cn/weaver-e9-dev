# 泛微OA 数据表: `social_imdelgrouplog`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imdelgrouplog`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `userid` | 用户id | `varchar2` | 800 | 是 | 用户id |
| 3 | `name` | 名称 | `varchar2` | 800 | 是 | 名称 |
| 4 | `delgroupid` | 群组id | `varchar2` | 1000 | 是 | 群组id |
| 5 | `delgroupname` | 解散群名 | `varchar2` | 800 | 是 | 解散群名 |
| 6 | `deldate` | 删除日期 | `varchar2` | 800 | 是 | 删除日期 |
| 7 | `remoteip` | 移除ip | `varchar2` | 800 | 是 | 移除ip |

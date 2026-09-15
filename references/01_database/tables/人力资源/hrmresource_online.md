# 泛微OA 数据表: `hrmresource_online`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmresource_online`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `user_id` | 人员id | `integer` | - | 是 | 人员id |
| 2 | `date_time` | 时间戳 | `varchar2` | 160 | 是 | 时间戳 |
| 3 | `online_flag` | 人员在线标识 | `char` | 1 | 是 | 人员在线标识 |
| 4 | `serverip` | 服务地址IP | `varchar2` | 400 | 是 | 服务地址IP |

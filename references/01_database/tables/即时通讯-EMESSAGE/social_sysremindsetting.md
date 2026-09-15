# 泛微OA 数据表: `social_sysremindsetting`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_sysremindsetting`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `remindtype` | 提醒类型 | `integer` | - | 是 | 提醒类型 |
| 3 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 4 | `ifon` | 是否开启 | `char` | 1 | 是 | 是否开启 |
| 5 | `ifdeskremind` | 是否开启桌面提醒 | `char` | 1 | 是 | 是否开启桌面提醒 |

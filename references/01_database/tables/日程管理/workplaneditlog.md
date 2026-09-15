# 泛微OA 数据表: `workplaneditlog`

- **所属模块**: `日程管理`
- **数据库表名**: `workplaneditlog`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `workplanid` | 日程id | `integer` | - | 是 | 日程id |
| 3 | `fieldname` | 字段名称 | `varchar2` | 240 | 是 | 字段名称 |
| 4 | `oldvalue` | 旧值 | `varchar2` | 800 | 是 | 旧值 |
| 5 | `newvalue` | 新值 | `varchar2` | 800 | 是 | 新值 |
| 6 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 7 | `usertype` | 用户类型 | `char` | 1 | 是 | 用户类型 |
| 8 | `ipaddress` | ip地址 | `char` | 15 | 是 | ip地址 |
| 9 | `logdate` | 日志日期 | `char` | 10 | 是 | 日志日期 |
| 10 | `logtime` | 日志时间 | `char` | 8 | 是 | 日志时间 |

# 泛微OA 数据表: `workplanviewlog`

- **所属模块**: `日程管理`
- **数据库表名**: `workplanviewlog`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 主键 |
| 2 | `workplanid` | 日程id | `integer` | - | 是 | 日程id |
| 3 | `viewtype` | 查看状态 | `char` | 1 | 是 | 1：创建，2：编辑，3：查看，4：删除 |
| 4 | `userid` | 查看用户 | `integer` | - | 是 | 查看用户 |
| 5 | `usertype` | 用户类型 | `char` | 1 | 是 | 用户类型 |
| 6 | `ipaddress` | ip地址 | `char` | 15 | 是 | ip地址 |
| 7 | `logdate` | 日志记录日期 | `char` | 10 | 是 | 日志记录日期 |
| 8 | `logtime` | 日志记录时间 | `char` | 8 | 是 | 日志记录时间 |

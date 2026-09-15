# 泛微OA 数据表: `workplanrevision`

- **所属模块**: `日程管理`
- **数据库表名**: `workplanrevision`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `planid` | 计划id | `integer` | - | 是 | 计划id |
| 3 | `operator` | 操作者 | `integer` | - | 是 | 操作者 |
| 4 | `operatetime` | 操作时间 | `varchar2` | 160 | 是 | 操作时间 |
| 5 | `operatetype` | 操作类型 | `char` | 1 | 是 | 操作类型 |
| 6 | `clientip` | 客户端ip地址 | `varchar2` | 160 | 是 | 客户端ip地址 |

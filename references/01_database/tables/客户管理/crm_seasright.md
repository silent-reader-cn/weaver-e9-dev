# 泛微OA 数据表: `crm_seasright`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_seasright`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `seasid` | 公海id | `integer` | - | 是 | 公海id |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 共享类型 |
| 4 | `sharelevel` | 共享级别 | `integer` | - | 是 | 共享级别 |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | 角色级别 |
| 6 | `contentid` | 共享范围 | `integer` | - | 是 | 共享范围 |
| 7 | `seclevelmin` | 最低安全级别 | `integer` | - | 是 | 最低安全级别 |
| 8 | `seclevelmax` | 最高安全级别 | `integer` | - | 是 | 最高安全级别 |
| 9 | `createdate` | 创建日期 | `varchar2` | 400 | 是 | 创建时间 |
| 10 | `createuser` | 创建者 | `integer` | - | 是 | 创建者 |

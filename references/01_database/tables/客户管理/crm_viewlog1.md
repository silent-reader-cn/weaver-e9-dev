# 泛微OA 数据表: `crm_viewlog1`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_viewlog1`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `viewer` | 浏览者 | `integer` | - | 是 | 浏览者 |
| 3 | `viewdate` | 浏览日期 | `char` | 10 | 是 | 浏览日期 |
| 4 | `viewtime` | 浏览时间 | `char` | 8 | 是 | 浏览时间 |
| 5 | `ipaddress` | IP地址 | `char` | 15 | 是 | ip地址 |
| 6 | `submitertype` | 联系类型 | `integer` | - | 是 | 联系类型 |

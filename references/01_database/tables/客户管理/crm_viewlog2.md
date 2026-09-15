# 泛微OA 数据表: `crm_viewlog2`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_viewlog2`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `customerid` | 客户id | `integer` | - | 是 | 客户id |
| 2 | `oldmanager` | 旧的客户经理 | `integer` | - | 是 | 旧的客户经理 |
| 3 | `newmanager` | 新的客户经理 | `integer` | - | 是 | 新的客户经理 |
| 4 | `movedate` | 转移日期 | `char` | 10 | 是 | 转移日期 |
| 5 | `movetime` | 转移时间 | `char` | 8 | 是 | 转移时间 |

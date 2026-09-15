# 泛微OA 数据表: `workplanexchange`

- **所属模块**: `日程管理`
- **数据库表名**: `workplanexchange`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `workplanid` | 日程id | `integer` | - | 是 | 日程id |
| 3 | `memberid` | 人员id | `integer` | - | 是 | 人员id |
| 4 | `exchangecount` | 未读交流数 | `integer` | - | 是 | 未读交流数 |
| 5 | `membertype` | 人员类型 | `char` | 1 | 是 | 人员类型 |

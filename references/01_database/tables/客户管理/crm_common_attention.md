# 泛微OA 数据表: `crm_common_attention`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_common_attention`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `operatetype` | 关注类型 | `integer` | - | 是 | 1为客户 2为商机 3为联系人 |
| 3 | `objid` | 关注id | `integer` | - | 是 | 关注id |
| 4 | `operator` | 关注人员id | `integer` | - | 是 | 关注人员id |
| 5 | `operatedate` | 关注日期 | `char` | 10 | 是 | 关注日期 |
| 6 | `operatetime` | 关注时间 | `char` | 8 | 是 | 关注时间 |

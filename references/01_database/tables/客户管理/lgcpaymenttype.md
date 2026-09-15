# 泛微OA 数据表: `lgcpaymenttype`

- **所属模块**: `客户管理`
- **数据库表名**: `lgcpaymenttype`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | 0 | 否 | id |
| 2 | `typename` | 类型名称 | `varchar2` | 480 | 是 | 类型名称 |
| 3 | `typedesc` | 类型说明 | `varchar2` | 1000 | 是 | 类型说明 |
| 4 | `paymentid` | 支付方式 | `integer` | 0 | 是 | 支付方式 |

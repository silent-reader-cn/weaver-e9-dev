# 泛微OA 数据表: `crm_contractproduct`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_contractproduct`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `contractid` | 合同id | `integer` | - | 是 | 合同id |
| 3 | `productid` | 产品id | `integer` | - | 是 | 产品id |
| 4 | `unitid` | 单位id | `integer` | - | 是 | 单位id |
| 5 | `price` | 价格 | `number` | (17,2) | 是 | 价格 |
| 6 | `currencyid` | 货币id | `integer` | - | 是 | 货币id |
| 7 | `depreciation` | 折扣 | `integer` | - | 是 | 折扣 |
| 8 | `sumprice` | 总额 | `number` | (17,2) | 是 | 总额 |
| 9 | `plandate` | 交货日期 | `char` | 10 | 是 | 交货日期 |
| 10 | `factnumber_n` | 实际交货数量 | `float` | 53 | 是 | 实际交货数量 |
| 11 | `factdate` | 实际交货日期 | `char` | 10 | 是 | 实际交货日期 |
| 12 | `isfinish` | 是否结束 | `integer` | - | 是 | 是否结束 |
| 13 | `isremind` | 是否提醒 | `integer` | - | 是 | 是否提醒 |
| 14 | `number_n` | 交货数量 | `number` | (17,2) | 是 | 交货数量 |

# 泛微OA 数据表: `crm_producttable`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_producttable`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `sellchanceid` | 销售机会id | `integer` | - | 是 | 销售机会id |
| 2 | `productid` | 产品id | `integer` | - | 是 | 产品id |
| 3 | `assetunitid` | 计量单位 | `integer` | - | 是 | 计量单位 |
| 4 | `currencyid` | 货币id | `integer` | - | 是 | 货币id |
| 5 | `salesprice` | 销售价格 | `number` | (12,2) | 是 | 销售价格 |
| 6 | `salesnum` | 销售数量 | `float` | 53 | 是 | 销售数量 |
| 7 | `totelprice` | 总金额 | `number` | (18,2) | 是 | 总金额 |

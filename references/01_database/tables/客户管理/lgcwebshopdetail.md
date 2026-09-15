# 泛微OA 数据表: `lgcwebshopdetail`

- **所属模块**: `客户管理`
- **数据库表名**: `lgcwebshopdetail`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `webshopid` | 订单id | `integer` | - | 是 | 订单id |
| 3 | `assetid` | 商品id | `integer` | - | 是 | 商品id |
| 4 | `countryid` | 国家id | `integer` | - | 是 | 国家id |
| 5 | `currencyid` | 货币id | `integer` | - | 是 | 货币id |
| 6 | `assetprice` | 单价 | `number` | (18,3) | 是 | 单价 |
| 7 | `taxrate` | 税率 | `integer` | - | 是 | 税率 |
| 8 | `purchasenum` | 数量 | `float` | 22 | 是 | 数量 |

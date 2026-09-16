# 泛微OA 数据表: `lgcwebshopdetail`

- **中文名称**: 网上订单详情表
- **所属模块**: `客户管理`
- **数据库表名**: `lgcwebshopdetail`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | id |
| 2 | `webshopid` | 订单id | `integer` | - | 是 | 否 | 否 | - | - | 订单id |
| 3 | `assetid` | 商品id | `integer` | - | 是 | 否 | 否 | - | - | 商品id |
| 4 | `countryid` | 国家id | `integer` | - | 是 | 否 | 否 | - | - | 国家id |
| 5 | `currencyid` | 货币id | `integer` | - | 是 | 否 | 否 | - | - | 货币id |
| 6 | `assetprice` | 单价 | `number` | (18,3) | 是 | 否 | 否 | - | - | 单价 |
| 7 | `taxrate` | 税率 | `integer` | - | 是 | 否 | 否 | - | - | 税率 |
| 8 | `purchasenum` | 数量 | `float` | 22 | 是 | 否 | 否 | - | - | 数量 |

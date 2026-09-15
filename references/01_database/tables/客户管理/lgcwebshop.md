# 泛微OA 数据表: `lgcwebshop`

- **所属模块**: `客户管理`
- **数据库表名**: `lgcwebshop`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `usertype` | 收货人类型 | `integer` | - | 是 | 收货人类型 |
| 3 | `userid` | 收货人id | `integer` | - | 是 | 收货人id |
| 4 | `username` | 收货人名称 | `varchar2` | 1000 | 是 | 收货人名称 |
| 5 | `usercountry` | 收货人国家 | `integer` | - | 是 | 收货人国家 |
| 6 | `useremail` | 收货人邮箱 | `varchar2` | 1000 | 是 | 收货人邮箱 |
| 7 | `receiveaddress` | 收货人地址 | `varchar2` | 1000 | 是 | 收货人地址 |
| 8 | `receivetype` | 收货类型 | `integer` | - | 是 | 收货类型 |
| 9 | `postcode` | 邮编 | `varchar2` | 1000 | 是 | 邮编 |
| 10 | `telephone1` | 电话1 | `varchar2` | 1000 | 是 | 电话1 |
| 11 | `telephone2` | 电话2 | `varchar2` | 1000 | 是 | 电话2 |
| 12 | `paymentmode` | 支付方式 | `varchar2` | 1000 | 是 | 支付方式 |
| 13 | `currencyid` | 货币id | `integer` | - | 是 | 货币id |
| 14 | `purchasecount` | 订单金额 | `number` | (18,3) | 是 | 订单金额 |
| 15 | `purchaseremark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 16 | `purchasedate` | 订单日期 | `char` | 10 | 是 | 订单日期 |
| 17 | `purchasestatus` | 订单状态 | `char` | 1 | 是 | 订单状态 |
| 18 | `manageid` | 管理员 | `integer` | - | 是 | 管理员 |

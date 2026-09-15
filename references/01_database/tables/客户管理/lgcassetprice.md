# 泛微OA 数据表: `lgcassetprice`

- **所属模块**: `客户管理`
- **数据库表名**: `lgcassetprice`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | 0 | 否 | id |
| 2 | `assetid` | 产品编号 | `integer` | 0 | 是 | 产品编号 |
| 3 | `assetcountyid` | 产品国家id | `integer` | 0 | 是 | 产品国家 |
| 4 | `pricedesc` | 价格描述 | `varchar2` | 1000 | 是 | 价格描述 |
| 5 | `numfrom` | 数量从 | `integer` | 0 | 是 | 数量从 |
| 6 | `numto` | 数量到 | `integer` | 0 | 是 | 数量到 |
| 7 | `currencyid` | 货币种类id | `integer` | 0 | 是 | 货币种类id |
| 8 | `unitprice` | 单位价格 | `number` | (18,3) | 是 | 单位价格 |
| 9 | `taxrate` | 税率 | `integer` | 0 | 是 | 税率 |

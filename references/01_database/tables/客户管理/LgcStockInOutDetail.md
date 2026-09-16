# 泛微OA 数据表: `LgcStockInOutDetail`

- **中文名称**: 产品进出库详情表
- **所属模块**: `客户管理`
- **数据库表名**: `LgcStockInOutDetail`
- **主键**: `id`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | id |
| 2 | `inoutid` | 进出库id | `integer` | - | 是 | 否 | 否 | - | - | 进出库id |
| 3 | `assetid` | 产品id | `integer` | - | 是 | 否 | 否 | - | - | 产品id |
| 4 | `batchmark` | 批量标记 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 批量标记 |
| 5 | `number_n` | 数量 | `float` | 53 | 是 | 否 | 否 | - | - | 数量 |
| 6 | `currencyid` | 货币id | `integer` | - | 是 | 否 | 否 | - | - | 货币id |
| 7 | `defcurrencyid` | 默认货币id | `integer` | - | 是 | 否 | 否 | - | - | 默认货币id |
| 8 | `exchangerate` | 0 | `float` | 18,3 | 是 | 否 | 否 | - | - | 0 |
| 9 | `defunitprice` | 0 | `float` | 18,3 | 是 | 否 | 否 | - | - | 0 |
| 10 | `unitprice` | 0 | `float` | 18,3 | 是 | 否 | 否 | - | - | 0 |
| 11 | `taxrate` | 税率 | `integer` | - | 是 | 否 | 否 | - | - | 税率 |

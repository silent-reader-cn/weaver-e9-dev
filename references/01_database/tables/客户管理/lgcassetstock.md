# 泛微OA 数据表: `lgcassetstock`

- **所属模块**: `客户管理`
- **数据库表名**: `lgcassetstock`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | 0 | 否 | id |
| 2 | `warehouseid` | 仓库id | `integer` | 0 | 是 | 仓库id |
| 3 | `assetid` | 产品id | `integer` | 0 | 是 | 产品id |
| 4 | `stocknum` | 期初数 | `float` | 22 | 是 | 期初数 |
| 5 | `unitprice` | 期初单价 | `number` | (18,3) | 是 | 期初单价 |

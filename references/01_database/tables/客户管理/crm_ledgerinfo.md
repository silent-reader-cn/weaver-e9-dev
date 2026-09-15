# 泛微OA 数据表: `crm_ledgerinfo`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_ledgerinfo`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `customerid` | 客户id | `integer` | 11 | 否 | 客户id |
| 2 | `customercode` | 客户财务代码 | `varchar2` | 80 | 是 | 客户财务代码 |
| 3 | `tradetype` | 交易类型 | `char` | 1 | 是 | 1：买方；2卖方 |
| 4 | `ledger1` | 科目1 id | `integer` | 11 | 是 | 科目1 id |
| 5 | `ledger2` | 科目2 id | `integer` | 11 | 是 | 科目2 id |

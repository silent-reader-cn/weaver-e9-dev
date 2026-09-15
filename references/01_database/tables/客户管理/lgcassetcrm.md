# 泛微OA 数据表: `lgcassetcrm`

- **所属模块**: `客户管理`
- **数据库表名**: `lgcassetcrm`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | 0 | 否 | id |
| 2 | `assetid` | 产品id | `integer` | 0 | 是 | 产品id |
| 3 | `crmid` | 供应商id | `integer` | 0 | 是 | 供应商id |
| 4 | `countryid` | 国家id | `integer` | 0 | 是 | 国家id |
| 5 | `ismain` | 是否是主供应商 | `char` | 1 | 是 | 是否是主供应商 |
| 6 | `assetcode` | 产品在供应商处编码 | `char` | 60 | 是 | 产品在供应商处编码 |
| 7 | `currencyid` | 货币种类id | `integer` | 0 | 是 | 货币种类id |
| 8 | `purchaseprice` | 采购单价 | `number` | (18,3) | 是 | 采购单价 |
| 9 | `taxrate` | 税率 | `integer` | 0 | 是 | 税率 |
| 10 | `unitid` | 单位id | `integer` | 0 | 是 | 单位id |
| 11 | `packageunit` | 包装单位的 | `varchar2` | 800 | 是 | 包装单位的 |
| 12 | `supplyremark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 13 | `docid` | 附件id | `integer` | 0 | 是 | 附件id |
| 14 | `contractid` | 合同id | `integer` | 0 | 是 | 合同id |

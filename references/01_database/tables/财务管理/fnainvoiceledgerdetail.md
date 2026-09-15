# 泛微OA 数据表: `fnainvoiceledgerdetail`

- **所属模块**: `财务管理`
- **数据库表名**: `fnainvoiceledgerdetail`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `unitnumber` | 数量 | `integer` | - | 是 | - |
| 2 | `unitprice` | 单价 | `number` | (18,2) | 是 | - |
| 3 | `id` | 主键 | `integer` | - | 否 | - |
| 4 | `mainid` | 主表id（发票台账表id） | `integer` | - | 是 | - |
| 5 | `invoiceserviceyype` | 货物或应税劳务、服务名称 | `varchar2` | 1500 | 是 | - |
| 6 | `pricewithouttax` | 金额 | `number` | (18,2) | 是 | - |
| 7 | `taxrate` | 税率 | `number` | (6,2) | 是 | - |
| 8 | `tax` | 税额 | `number` | (18,2) | 是 | - |

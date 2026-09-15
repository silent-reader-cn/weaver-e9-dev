# 泛微OA 数据表: `fnainvoiceledger`

- **所属模块**: `财务管理`
- **数据库表名**: `fnainvoiceledger`
- **字段总数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `imageid` | OCR图片id | `integer` | - | 是 | - |
| 2 | `purchasertaxno` | 买方税号 | `varchar2` | 200 | 是 | - |
| 3 | `salestaxno` | 买房税号 | `varchar2` | 200 | 是 | - |
| 4 | `userid_new` | 发票归属人 | `integer` | - | 是 | - |
| 5 | `invoicesource_new` | 发票来源 | `integer` | - | 是 | - |
| 6 | `checkcode` | 发票校验码 | `varchar2` | 1000 | 是 | - |
| 7 | `status` | 发票状态 | `integer` | - | 是 | - |
| 8 | `card_id_new` | 微信电子发票card_id | `varchar2` | 1000 | 是 | - |
| 9 | `encrypt_code_new` | 微信电子发票encrypt_code | `varchar2` | 1000 | 是 | - |
| 10 | `openid_new` | 微信电子发票openid_new | `varchar2` | 1000 | 是 | - |
| 11 | `wechatstatus` | 微信电子发票状态 | `varchar2` | 240 | 是 | - |
| 12 | `id` | 主键 | `integer` | - | 否 | - |
| 13 | `billingdate` | 开票日期 | `char` | 10 | 是 | - |
| 14 | `invoicecode` | 发票代码 | `varchar2` | 60 | 是 | - |
| 15 | `invoicenumber` | 发票号码 | `varchar2` | 60 | 是 | - |
| 16 | `invoicetype` | 发票类型 | `integer` | - | 是 | - |
| 17 | `seller` | 销售方 | `varchar2` | 1500 | 是 | - |
| 18 | `purchaser` | 购买方 | `varchar2` | 1500 | 是 | - |
| 19 | `invoiceserviceyype` | 货物或应税服务类型 | `varchar2` | 1500 | 是 | - |
| 20 | `pricewithouttax` | 金额（不含税价） | `number` | (20,2) | 是 | - |
| 21 | `taxrate` | 税率 | `number` | (8,2) | 是 | - |
| 22 | `tax` | 税额（税价） | `number` | (20,2) | 是 | - |
| 23 | `taxincludedprice` | 价税合计（含税价） | `number` | (20,2) | 是 | - |
| 24 | `authenticity` | 发票真伪 | `integer` | - | 是 | - |
| 25 | `reimbursementdate` | 报销日期 | `char` | 10 | 是 | - |
| 26 | `reimburseperson` | 报销人 | `integer` | - | 是 | - |
| 27 | `requestid` | 流程requestId | `integer` | - | 是 | - |

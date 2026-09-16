# 泛微OA 数据表: `fnainvoiceledger`

- **中文名称**: 发票台账表
- **所属模块**: `财务管理`
- **数据库表名**: `fnainvoiceledger`
- **主键**: `id`
- **字段数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `imageid` | OCR图片id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `purchasertaxno` | 买方税号 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 3 | `salestaxno` | 买房税号 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 4 | `userid_new` | 发票归属人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `invoicesource_new` | 发票来源 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `checkcode` | 发票校验码 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `status` | 发票状态 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `card_id_new` | 微信电子发票card_id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `encrypt_code_new` | 微信电子发票encrypt_code | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 10 | `openid_new` | 微信电子发票openid_new | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `wechatstatus` | 微信电子发票状态 | `varchar2` | 240 | 是 | 否 | 否 | - | - | - |
| 12 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 13 | `billingdate` | 开票日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 14 | `invoicecode` | 发票代码 | `varchar2` | 60 | 是 | 否 | 否 | - | - | - |
| 15 | `invoicenumber` | 发票号码 | `varchar2` | 60 | 是 | 否 | 否 | - | - | - |
| 16 | `invoicetype` | 发票类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `seller` | 销售方 | `varchar2` | 1500 | 是 | 否 | 否 | - | - | - |
| 18 | `purchaser` | 购买方 | `varchar2` | 1500 | 是 | 否 | 否 | - | - | - |
| 19 | `invoiceserviceyype` | 货物或应税服务类型 | `varchar2` | 1500 | 是 | 否 | 否 | - | - | - |
| 20 | `pricewithouttax` | 金额（不含税价） | `number` | (20,2) | 是 | 否 | 否 | - | - | - |
| 21 | `taxrate` | 税率 | `number` | (8,2) | 是 | 否 | 否 | - | - | - |
| 22 | `tax` | 税额（税价） | `number` | (20,2) | 是 | 否 | 否 | - | - | - |
| 23 | `taxincludedprice` | 价税合计（含税价） | `number` | (20,2) | 是 | 否 | 否 | - | - | - |
| 24 | `authenticity` | 发票真伪 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `reimbursementdate` | 报销日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 26 | `reimburseperson` | 报销人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 27 | `requestid` | 流程requestId | `integer` | - | 是 | 否 | 否 | - | - | - |

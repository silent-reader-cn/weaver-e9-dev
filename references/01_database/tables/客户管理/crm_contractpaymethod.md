# 泛微OA 数据表: `crm_contractpaymethod`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_contractpaymethod`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `contractid` | 合同id | `integer` | - | 是 | 合同id |
| 3 | `prjname` | 付款项目名称 | `varchar2` | 800 | 是 | 付款项目名称 |
| 4 | `typeid` | 付款性质 | `integer` | - | 是 | 付款性质 |
| 5 | `payprice` | 付款金额 | `number` | (17,2) | 是 | 付款金额 |
| 6 | `paydate` | 付款日期 | `char` | 10 | 是 | 付款日期 |
| 7 | `factprice` | 实际付款金额 | `number` | (17,2) | 是 | 实际付款金额 |
| 8 | `factdate` | 实际付款日期 | `char` | 10 | 是 | 实际付款日期 |
| 9 | `qualification` | 付款条件 | `varchar2` | 1000 | 是 | 付款条件 |
| 10 | `isfinish` | 是否结束 | `integer` | - | 是 | 是否结束 |
| 11 | `isremind` | 是否提醒 | `integer` | - | 是 | 是否提醒 |
| 12 | `feetypeid` | 费用类型 | `integer` | - | 是 | 费用类型 |
| 13 | `fnalogid` | 财务对应日志id | `integer` | - | 是 | 财务对应日志id |

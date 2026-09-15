# 泛微OA 数据表: `crm_payinfo`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_payinfo`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `payid` | 单据id | `integer` | - | 是 | 单据id |
| 3 | `factprice` | 实际付款金额 | `number` | (15,2) | 是 | 实际付款金额 |
| 4 | `factdate` | 实际付款日期 | `char` | 10 | 是 | 实际付款日期 |
| 5 | `creater` | 创建者 | `integer` | - | 是 | 创建者 |
| 6 | `formnum` | 笔数 | `varchar2` | 1000 | 是 | 笔数 |

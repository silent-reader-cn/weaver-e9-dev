# 泛微OA 数据表: `bill_fnabudgetchgapplydetail`

- **所属模块**: `财务管理`
- **数据库表名**: `bill_fnabudgetchgapplydetail`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | bill_fnabudgetchgapply.id | `integer` | - | 是 | - |
| 2 | `organizationid` | 承担主体 | `integer` | - | 是 | - |
| 3 | `subject` | 科目 | `integer` | - | 是 | - |
| 4 | `budgetperiod` | 费用日期 | `char` | 10 | 是 | - |
| 5 | `relatedprj` | 相关项目 | `integer` | - | 是 | - |
| 6 | `relatedcrm` | 相关客户 | `integer` | - | 是 | - |
| 7 | `description` | 说明 | `varchar2` | 400 | 是 | - |
| 8 | `oldamount` | 原预算 | `number` | (15,3) | 是 | - |
| 9 | `applyamount` | 审批新预算金额 | `number` | (15,3) | 是 | - |
| 10 | `amount` | 新预算金额 | `number` | (15,3) | 是 | - |
| 11 | `changeamount` | 原新预算差额 | `number` | (15,3) | 是 | - |
| 12 | `organizationtype` | 承担主体类型 | `integer` | - | 是 | - |
| 13 | `dsporder` | 显示序号 | `integer` | - | 是 | - |

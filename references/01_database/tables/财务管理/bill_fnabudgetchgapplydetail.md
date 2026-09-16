# 泛微OA 数据表: `bill_fnabudgetchgapplydetail`

- **中文名称**: 预算变更申请单明细表
- **所属模块**: `财务管理`
- **数据库表名**: `bill_fnabudgetchgapplydetail`
- **主键**: `id+dsporder`
- **字段数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | bill_fnabudgetchgapply.id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `organizationid` | 承担主体 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `subject` | 科目 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `budgetperiod` | 费用日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 5 | `relatedprj` | 相关项目 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `relatedcrm` | 相关客户 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `description` | 说明 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 8 | `oldamount` | 原预算 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 9 | `applyamount` | 审批新预算金额 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 10 | `amount` | 新预算金额 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 11 | `changeamount` | 原新预算差额 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 12 | `organizationtype` | 承担主体类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `dsporder` | 显示序号 | `integer` | - | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `bill_fnawipeapplydetail`

- **所属模块**: `财务管理`
- **数据库表名**: `bill_fnawipeapplydetail`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `relatedcrm` | 相关客户 | `integer` | - | 是 | - |
| 2 | `description` | 说明 | `varchar2` | 1000 | 是 | - |
| 3 | `applyamount` | 审批金额 | `number` | (15,3) | 是 | - |
| 4 | `amount` | 申请季节 | `number` | (15,3) | 是 | - |
| 5 | `organizationtype` | 承担主体类型 | `integer` | - | 是 | - |
| 6 | `dsporder` | 明细序号 | `integer` | - | 是 | - |
| 7 | `fccremain` | 作废 | `varchar2` | 4000 | 是 | - |
| 8 | `id` | bill_fnawipeapply.id | `integer` | - | 是 | - |
| 9 | `organizationid` | 承担主体 | `integer` | - | 是 | - |
| 10 | `subject` | 科目 | `integer` | - | 是 | - |
| 11 | `budgetperiod` | 费用日期 | `char` | 10 | 是 | - |
| 12 | `attachcount` | 附件数 | `integer` | - | 是 | - |
| 13 | `hrmremain` | 个人预算信息 | `number` | (15,3) | 是 | - |
| 14 | `deptremain` | 部门预算信息 | `number` | (15,3) | 是 | - |
| 15 | `subcomremain` | 分部预算信息 | `number` | (15,3) | 是 | - |
| 16 | `loanbalance` | 作废 | `number` | (15,3) | 是 | - |
| 17 | `relatedprj` | 相关项目 | `integer` | - | 是 | - |

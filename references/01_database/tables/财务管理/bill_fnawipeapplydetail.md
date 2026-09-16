# 泛微OA 数据表: `bill_fnawipeapplydetail`

- **中文名称**: 报销申请单明细表
- **所属模块**: `财务管理`
- **数据库表名**: `bill_fnawipeapplydetail`
- **主键**: `id+dsporder`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `relatedcrm` | 相关客户 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `description` | 说明 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `applyamount` | 审批金额 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 4 | `amount` | 申请季节 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 5 | `organizationtype` | 承担主体类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `dsporder` | 明细序号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `fccremain` | 作废 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 8 | `id` | bill_fnawipeapply.id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `organizationid` | 承担主体 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `subject` | 科目 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `budgetperiod` | 费用日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 12 | `attachcount` | 附件数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `hrmremain` | 个人预算信息 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 14 | `deptremain` | 部门预算信息 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 15 | `subcomremain` | 分部预算信息 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 16 | `loanbalance` | 作废 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 17 | `relatedprj` | 相关项目 | `integer` | - | 是 | 否 | 否 | - | - | - |

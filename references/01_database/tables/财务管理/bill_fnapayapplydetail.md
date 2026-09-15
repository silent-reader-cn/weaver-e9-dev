# 泛微OA 数据表: `bill_fnapayapplydetail`

- **所属模块**: `财务管理`
- **数据库表名**: `bill_fnapayapplydetail`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 是 | - |
| 2 | `organizationid` | 承担主体 | `integer` | - | 是 | - |
| 3 | `subject` | 科目 | `integer` | - | 是 | - |
| 4 | `budgetperiod` | 费用日期 | `char` | 10 | 是 | - |
| 5 | `hrmremain` | 人员预算信息显示字段 | `number` | (15,3) | 是 | - |
| 6 | `deptremain` | 部门预算信息显示字段 | `number` | (15,3) | 是 | - |
| 7 | `subcomremain` | 分部预算信息显示字段 | `number` | (15,3) | 是 | - |
| 8 | `relatedprj` | 相关项目 | `integer` | - | 是 | - |
| 9 | `relatedcrm` | 相关客户 | `integer` | - | 是 | - |
| 10 | `description` | 说明 | `varchar2` | 800 | 是 | - |
| 11 | `applyamount` | 申请金额 | `number` | (15,3) | 是 | - |
| 12 | `amount` | 审核金额 | `number` | (15,3) | 是 | - |
| 13 | `organizationtype` | 承担主体类型 | `integer` | - | 是 | - |
| 14 | `dsporder` | 主键 | `integer` | - | 是 | - |
| 15 | `fccremain` | 成本中心预算信息显示字段 | `varchar2` | 4000 | 是 | - |

# 泛微OA 数据表: `bill_fnapayapplydetail`

- **中文名称**: 付款申请单
- **所属模块**: `财务管理`
- **数据库表名**: `bill_fnapayapplydetail`
- **主键**: `id+dsporder`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `organizationid` | 承担主体 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `subject` | 科目 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `budgetperiod` | 费用日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 5 | `hrmremain` | 人员预算信息显示字段 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 6 | `deptremain` | 部门预算信息显示字段 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 7 | `subcomremain` | 分部预算信息显示字段 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 8 | `relatedprj` | 相关项目 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `relatedcrm` | 相关客户 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `description` | 说明 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 11 | `applyamount` | 申请金额 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 12 | `amount` | 审核金额 | `number` | (15,3) | 是 | 否 | 否 | - | - | - |
| 13 | `organizationtype` | 承担主体类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `dsporder` | 主键 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `fccremain` | 成本中心预算信息显示字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `fnabudgetinfodetail`

- **所属模块**: `财务管理`
- **数据库表名**: `fnabudgetinfodetail`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `budgetinfoid` | 部门预算信息id | `integer` | - | 是 | - |
| 3 | `budgetperiods` | 年度期间id | `integer` | - | 是 | 预算年度表主键 |
| 4 | `budgettypeid` | 科目id | `integer` | - | 是 | - |
| 5 | `budgetresourceid` | 人员id | `integer` | - | 是 | 预算相关人力资源 |
| 6 | `budgetcrmid` | 客户id | `integer` | - | 是 | 预算相关客户 |
| 7 | `budgetprojectid` | 项目id | `integer` | - | 是 | 预算相关项目 |
| 8 | `budgetaccount` | 金额 | `number` | (18,2) | 是 | - |
| 9 | `budgetremark` | 备注 | `varchar2` | 1000 | 是 | - |
| 10 | `budgetperiodslist` | 期间id | `integer` | - | 是 | 月度科目：1~12；季度科目：1~4；半年度科目：1~2；年度科目：1；如果科目是按月度编制预算的话：1~12月对应写入该字段1~12；如果科目是按季度编制预算的话：第一季度：1；第二季度：2；第三季度：3；第四季度：4； 如果科目是按半年度编制预算的话：上半年：1；下半年：2； 如果科目是按年度编制预算的话：写入固定值：1； |
| 11 | `fnaincrement` | 偏差金额 | `number` | (18,2) | 是 | - |

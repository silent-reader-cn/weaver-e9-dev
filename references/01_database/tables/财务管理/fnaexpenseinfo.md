# 泛微OA 数据表: `fnaexpenseinfo`

- **所属模块**: `财务管理`
- **数据库表名**: `fnaexpenseinfo`
- **字段总数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isbudgetautomovebyminusamt` | 超额结转标识 | `integer` | - | 是 | 1：是；其他：否； 该笔记录是否超额预算结转产生的记录 |
| 2 | `sfbxwc` | 是否报销完成标识 | `integer` | - | 是 | 1：是；其他：否； 该标志位用来在事后报销流程冲抵事前申请流程时，标识是否为了临时占用预算而产生的本条数据。 最终会在事后报销流程实际扣除时释放标识=1的当前流程产生的记录。 |
| 3 | `writeoffflag` | 预申请费用是否冲销完成 | `integer` | - | 是 | 1：是；其他：否； 1、该笔记录是否报销完成，只对预申请流程产生的冻结费用有效。 2、且只有通过事后报销流程冲抵完的，预申请流程的费用才会更新该字段。 3、值=1的时候，不会对该记录进行结转（开启结转审批中费用的时候）。 |
| 4 | `id` | 主键 | `integer` | - | 是 | - |
| 5 | `organizationid` | 承担主体id | `integer` | - | 是 | 分部id；部门id；个人id；成本中心id； |
| 6 | `organizationtype` | 承担主体类型 | `integer` | - | 是 | 1：分部；2：部门；3：个人；18004：成本中心； |
| 7 | `occurdate` | 费用发生日期 | `char` | 10 | 是 | - |
| 8 | `amount` | 金额 | `number` | (15,3) | 是 | - |
| 9 | `subject` | 科目id | `integer` | - | 是 | - |
| 10 | `status` | 状态 | `integer` | - | 是 | 0：审批中；1：生效； |
| 11 | `type` | 来源类型 | `integer` | - | 是 | 1：付款；2：报销；3：冲销； |
| 12 | `relatedprj` | 项目id | `integer` | - | 是 | 相关项目 |
| 13 | `relatedcrm` | 客户id | `integer` | - | 是 | 相关客户 |
| 14 | `debitremark` | 凭证号 | `varchar2` | 400 | 是 | 手工做账时才会录入 |
| 15 | `description` | 描述 | `varchar2` | 1000 | 是 | - |
| 16 | `requestid` | 流程requestid | `integer` | - | 是 | 统计用流程requestid |
| 17 | `sharerequestid` | 作废 | `varchar2` | 1000 | 是 | 作废 |
| 18 | `guid` | 作废 | `char` | 32 | 是 | 作废 |
| 19 | `requestiddtlid` | 流程明细表id | `integer` | - | 是 | 统计用流程明细表id |
| 20 | `sourcedtlnumber` | 流程明细表序号 | `integer` | - | 是 | 记录来源明细表序号 |
| 21 | `sourcerequestid` | 流程requestid | `integer` | - | 是 | 来源流程requestid |
| 22 | `sourcerequestiddtlid` | 流程明细表id | `integer` | - | 是 | 记录来源流程明细表id |
| 23 | `budgetperiods` | 年度期间id | `integer` | - | 是 | 费用发生日期所属：预算年度表主键 |
| 24 | `budgetperiodslist` | 期间id | `integer` | - | 是 | 月度科目：1~12；季度科目：1~4；半年度科目：1~2；年度科目：1；  如果科目是按月度编制预算的话：1~12月对应写入该字段1~12  如果科目是按季度编制预算的话：第一季度：1；第二季度：2；第三季度：3；第四季度：4；  如果科目是按半年度编制预算的话：上半年：1；下半年：2；  如果科目是按年度编制预算的话：写入固定值：1； |
| 25 | `occurdateold` | 结转前日期 | `char` | 10 | 是 | 费用发生过审批中结转是会将结转前的日期写入该字段 |
| 26 | `isbudgetautomove` | 是否结转标识 | `integer` | - | 是 | 费用发生过审批中结转该字段会被更新成：1 |

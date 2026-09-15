# 泛微OA 数据表: `fnabudgetinfo`

- **所属模块**: `财务管理`
- **数据库表名**: `fnabudgetinfo`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `description1` | 备注信息 | `varchar2` | 1000 | 是 | - |
| 2 | `id` | 主键 | `integer` | - | 否 | - |
| 3 | `budgetstatus` | 预算状态 | `integer` | - | 是 | 0：未审批； 1：已审批； |
| 4 | `createrid` | 创建人id | `integer` | - | 是 | - |
| 5 | `approverid` | 审批人id | `integer` | - | 是 | 通过审批流程生效的预算才有数据 |
| 6 | `approverdate` | 审批日期 | `char` | 10 | 是 | 通过审批流程生效的预算才有数据 |
| 7 | `budgetorganizationid` | 组织id | `integer` | - | 是 | 分部：分部id； 部门：部门id； 人员：人员id； 成本中心：成本中心id； |
| 8 | `organizationtype` | 组织id类型 | `integer` | - | 是 | 0：总部； 1：分部； 2：部门； 18004：成本中心； |
| 9 | `budgetperiods` | 年度期间id | `integer` | - | 是 | 预算年度表主键 |
| 10 | `revision` | 版本 | `integer` | - | 是 | - |
| 11 | `status` | 状态 | `integer` | - | 是 | 0 ：草稿；1 ：生效；2 ：历史；3 ：待审批； |
| 12 | `remark` | 备注 | `varchar2` | 1000 | 是 | - |
| 13 | `createdate` | 创建日期 | `char` | 20 | 是 | - |
| 14 | `orgorder` | 批量编制排序字段 | `integer` | - | 是 | 按：总部、分部、部门、个人，成本中心的级别关系从小到大进行赋值 |
| 15 | `optype` | 生成方式 | `char` | 1 | 是 | j：结转；空：编制； |

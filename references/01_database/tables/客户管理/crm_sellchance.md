# 泛微OA 数据表: `crm_sellchance`

- **中文名称**: 客户销售机会信息表
- **所属模块**: `客户管理`
- **数据库表名**: `crm_sellchance`
- **主键**: `id`
- **字段数**: `24`

> 说明：商机（销售机会）信息表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `creater` | 创建者 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `subject` | 标题 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 4 | `customerid` | 相关客户 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `comefromid` | 来源id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `sellstatusid` | 销售状态id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `endtatusid` | 最后状态id | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `predate` | 销售预期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 9 | `preyield` | 预期收益 | `number` | (18,2) | 是 | 否 | 否 | - | - | - |
| 10 | `currencyid` | 币种id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `probability` | 可能性 | `number` | (8,2) | 是 | 否 | 否 | - | - | 最大1 |
| 12 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 13 | `createtime` | 创建时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 14 | `content` | 主题 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 15 | `approver` | 审批 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 16 | `approvedate` | 审批日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 17 | `approvetime` | 审批时间 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 18 | `approvestatus` | 审批状态 | `char` | 1 | 是 | 否 | 否 | - | 0 | - |
| 19 | `sufactor` | 实际收益性 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `defactor` | 可能性 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `departmentid` | 部门ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `subcompanyid` | 销售经理分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `selltype` | 销售类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `selltypesid` | 销售机会 | `integer` | - | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `crm_sellchance`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_sellchance`
- **字段总数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `creater` | 创建者 | `integer` | - | 是 | - |
| 3 | `subject` | 标题 | `varchar2` | 400 | 是 | - |
| 4 | `customerid` | 相关客户 | `integer` | - | 是 | - |
| 5 | `comefromid` | 来源id | `integer` | - | 是 | - |
| 6 | `sellstatusid` | 销售状态id | `integer` | - | 是 | - |
| 7 | `endtatusid` | 最后状态id | `char` | 1 | 是 | - |
| 8 | `predate` | 销售预期 | `char` | 10 | 是 | - |
| 9 | `preyield` | 预期收益 | `number` | (18,2) | 是 | - |
| 10 | `currencyid` | 币种id | `integer` | - | 是 | - |
| 11 | `probability` | 可能性 | `number` | (8,2) | 是 | 最大1 |
| 12 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 13 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 14 | `content` | 主题 | `varchar2` | 4000 | 是 | - |
| 15 | `approver` | 审批 | `integer` | - | 是 | - |
| 16 | `approvedate` | 审批日期 | `char` | 10 | 是 | - |
| 17 | `approvetime` | 审批时间 | `char` | 10 | 是 | - |
| 18 | `approvestatus` | 审批状态 | `char` | 1 | 是 | - |
| 19 | `sufactor` | 实际收益性 | `integer` | - | 是 | - |
| 20 | `defactor` | 可能性 | `integer` | - | 是 | - |
| 21 | `departmentid` | 部门ID | `integer` | - | 是 | - |
| 22 | `subcompanyid` | 销售经理分部id | `integer` | - | 是 | - |
| 23 | `selltype` | 销售类型 | `integer` | - | 是 | - |
| 24 | `selltypesid` | 销售机会 | `integer` | - | 是 | - |

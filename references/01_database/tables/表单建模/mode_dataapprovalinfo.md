# 泛微OA 数据表: `mode_dataapprovalinfo`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_dataapprovalinfo`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `billid` | 数据id | `integer` | - | 是 | 对应模块的uf表的id |
| 2 | `modeid` | 模块id | `integer` | - | 是 | 模块id |
| 3 | `formid` | 表单id | `integer` | - | 是 | 对应workflow_billfield表的id |
| 4 | `requestid` | 流程requestid | `integer` | - | 是 | 流程requestid |
| 5 | `operator` | 操作人id | `integer` | - | 是 | 对应hrmresource的id |
| 6 | `operatedate` | 操作日期 | `varchar2` | 80 | 是 | 日期 |
| 7 | `operatetime` | 操作时间 | `varchar2` | 64 | 是 | 时间 |
| 8 | `approvalstatus` | 审批状态 | `integer` | - | 是 | - |
| 9 | `approvaldate` | 审批日期 | `varchar2` | 80 | 是 | - |
| 10 | `approvaltime` | 审批时间 | `varchar2` | 64 | 是 | - |
| 11 | `id` | ID | `integer` | - | 否 | - |

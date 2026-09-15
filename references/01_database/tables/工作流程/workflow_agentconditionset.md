# 泛微OA 数据表: `workflow_agentconditionset`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_agentconditionset`
- **字段总数**: `29`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `agentid` | 代理id主键 | `integer` | - | 是 | - |
| 2 | `bagentuid` | 被代理人 | `integer` | - | 是 | - |
| 3 | `agentuid` | 代理人 | `integer` | - | 是 | - |
| 4 | `id` | ID | `varchar2` | 500 | 否 | - |
| 5 | `agentid_bak` | 未使用 | `varchar2` | 1000 | 是 | - |
| 6 | `bagentuid_bak` | 未使用 | `varchar2` | 1000 | 是 | - |
| 7 | `agentuid_bak` | 未使用 | `varchar2` | 1000 | 是 | - |
| 8 | `conditionss` | 条件值 | `varchar2` | 4000 | 是 | - |
| 9 | `conditioncn` | 条件名称 | `varchar2` | 4000 | 是 | - |
| 10 | `conditionkeyid` | 条件唯一值 | `varchar2` | 4000 | 是 | 关联关系 |
| 11 | `begindate` | 开始日期 | `varchar2` | 450 | 是 | - |
| 12 | `begintime` | 开始时间 | `varchar2` | 450 | 是 | - |
| 13 | `enddate` | 结束日期 | `varchar2` | 450 | 是 | - |
| 14 | `endtime` | 结束时间 | `varchar2` | 450 | 是 | - |
| 15 | `workflowid` | 工作流id | `varchar2` | 4000 | 是 | - |
| 16 | `recoverstate` | 是否重新代理 | `varchar2` | 4000 | 是 | 状态1 标示为需要重新代理 |
| 17 | `iscreateagenter` | 创建代理 | `varchar2` | 1000 | 是 | - |
| 18 | `agenttype` | 代理状态 | `varchar2` | 1000 | 是 | 状态1有效、否则无效 |
| 19 | `isproxydeal` | 流转中的是否代理 | `varchar2` | 1000 | 是 | - |
| 20 | `ispendthing` | 流转中的待办事宜 | `varchar2` | 1000 | 是 | - |
| 21 | `operatorid` | 操作人 | `varchar2` | 1000 | 是 | - |
| 22 | `operatordate` | 操作日期 | `varchar2` | 1000 | 是 | - |
| 23 | `operatortime` | 操作时间 | `varchar2` | 1000 | 是 | - |
| 24 | `isset` | 是否已经把待办事宜转给代理人 | `varchar2` | 1000 | 是 | - |
| 25 | `backdate` | 收回日期 | `varchar2` | 1000 | 是 | - |
| 26 | `backtime` | 收回时间 | `varchar2` | 1000 | 是 | - |
| 27 | `agentconditionid` | 后续使用 | `varchar2` | 1000 | 是 | - |
| 28 | `agentbatch` | 批次 | `varchar2` | 1000 | 是 | - |
| 29 | `rulerelationship` | 关联规则 | `varchar2` | 400 | 是 | - |

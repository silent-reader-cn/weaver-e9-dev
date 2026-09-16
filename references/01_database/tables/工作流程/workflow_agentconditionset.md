# 泛微OA 数据表: `workflow_agentconditionset`

- **中文名称**: 代理设置信息明细表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_agentconditionset`
- **主键**: `id`
- **字段数**: `29`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `agentid` | 代理id主键 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `bagentuid` | 被代理人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `agentuid` | 代理人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `id` | ID | `varchar2` | 500 | 否 | 否 | 否 | - | - | - |
| 5 | `agentid_bak` | 未使用 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `bagentuid_bak` | 未使用 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `agentuid_bak` | 未使用 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `conditionss` | 条件值 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `conditioncn` | 条件名称 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `conditionkeyid` | 条件唯一值 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 关联关系 |
| 11 | `begindate` | 开始日期 | `varchar2` | 450 | 是 | 否 | 否 | - | - | - |
| 12 | `begintime` | 开始时间 | `varchar2` | 450 | 是 | 否 | 否 | - | - | - |
| 13 | `enddate` | 结束日期 | `varchar2` | 450 | 是 | 否 | 否 | - | - | - |
| 14 | `endtime` | 结束时间 | `varchar2` | 450 | 是 | 否 | 否 | - | - | - |
| 15 | `workflowid` | 工作流id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 16 | `recoverstate` | 是否重新代理 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 状态1 标示为需要重新代理 |
| 17 | `iscreateagenter` | 创建代理 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 18 | `agenttype` | 代理状态 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 状态1有效、否则无效 |
| 19 | `isproxydeal` | 流转中的是否代理 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 20 | `ispendthing` | 流转中的待办事宜 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 21 | `operatorid` | 操作人 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 22 | `operatordate` | 操作日期 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 23 | `operatortime` | 操作时间 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 24 | `isset` | 是否已经把待办事宜转给代理人 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 25 | `backdate` | 收回日期 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 26 | `backtime` | 收回时间 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 27 | `agentconditionid` | 后续使用 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 28 | `agentbatch` | 批次 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 29 | `rulerelationship` | 关联规则 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |

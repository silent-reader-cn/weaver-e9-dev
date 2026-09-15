# 泛微OA 数据表: `workflow_agent`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_agent`
- **字段总数**: `23`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `agentid` | 代理id | `integer` | - | 否 | - |
| 2 | `workflowid` | 工作流id | `integer` | - | 是 | - |
| 3 | `beagenterid` | 被代理人 | `integer` | - | 是 | - |
| 4 | `agenterid` | 代理人 | `integer` | - | 是 | - |
| 5 | `begindate` | 代理开始日期 | `char` | 10 | 是 | - |
| 6 | `begintime` | 代理开始时间 | `char` | 8 | 是 | - |
| 7 | `enddate` | 代理结束日期 | `char` | 10 | 是 | - |
| 8 | `endtime` | 代理结束时间 | `char` | 8 | 是 | - |
| 9 | `iscreateagenter` | 是否代理创建权限 | `integer` | - | 是 | - |
| 10 | `agenttype` | 状态 | `char` | 1 | 是 | 1：有效 0：无效 |
| 11 | `operatorid` | 设置人id | `integer` | - | 是 | - |
| 12 | `operatordate` | 设置日期 | `char` | 10 | 是 | - |
| 13 | `operatortime` | 设置时间 | `char` | 8 | 是 | - |
| 14 | `isset` | 是否已经把待办事宜转给代理人 | `char` | 1 | 是 | - |
| 15 | `ispending` | 是否要把待办事宜转给代理人 | `char` | 1 | 是 | - |
| 16 | `backdate` | 收回代理日期 | `char` | 10 | 是 | - |
| 17 | `backtime` | 收回代理时间 | `char` | 8 | 是 | - |
| 18 | `isproxydeal` | 流转中的待办事宜 | `varchar2` | 160 | 是 | - |
| 19 | `iseditstartdate` | 是否是初始化数据 | `varchar2` | 800 | 是 | 1标示是 其他否 |
| 20 | `iseditstarttime` | 是否是初始化数据 | `varchar2` | 800 | 是 | 1标示是 其他否 |
| 21 | `iseditenddate` | 是否是初始化数据 | `varchar2` | 800 | 是 | 1标示是 其他否 |
| 22 | `iseditendtime` | 是否是初始化数据 | `varchar2` | 800 | 是 | 1标示是 其他否 |
| 23 | `agentstate` | 代理状态 | `varchar2` | 80 | 是 | - |

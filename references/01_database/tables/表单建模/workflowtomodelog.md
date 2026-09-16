# 泛微OA 数据表: `workflowtomodelog`

- **中文名称**: 流程转数据日志信息表
- **所属模块**: `表单建模`
- **数据库表名**: `workflowtomodelog`
- **主键**: `id`
- **字段数**: `24`

> 说明：流程转数据日志表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `modeuuid` | uuid | `varchar2` | 100 | 是 | 否 | 否 | - | - | - |
| 2 | `check_dt_sql_msg` | 校验sql信息 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 3 | `successfullog` | 成功sql信息 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `actionid` | 接口id | `integer` | - | 是 | 否 | 否 | - | - | 更改转数据配置这个id会变更的 |
| 5 | `errorlog` | 错误日志信息 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `workflowtomodesetid` | 流程转数据配置项id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `requestname` | 流程名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 0：流程流转 1：历史数据写入 |
| 8 | `logsources` | 日志来源 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `requestid` | 流程请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `triggertype` | 触发时间 | `integer` | - | 是 | 否 | 否 | - | - | 离开节点，到达节点 或者出口时候为空 |
| 11 | `triggernodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `workflowexport` | 出口 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `triggermethod` | 节点or出口 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `ip` | 触发转数据操作者ip | `varchar2` | 100 | 是 | 否 | 否 | - | - | - |
| 15 | `operator` | 操作者 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `circulationdate` | 流转日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 17 | `circulationtime` | 流转时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 18 | `logtype` | 日志类型(0成功，1失败) | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 20 | `typename` | 类型名称 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 21 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `billid` | 数据id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 23 | `mainid` | 主id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |

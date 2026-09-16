# 泛微OA 数据表: `workflow_penetratelog`

- **中文名称**: 流程详细日志表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_penetratelog`
- **主键**: `id`
- **字段数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `nodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `logtype` | 日志类型 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 6 | `operatedate` | 操作日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 7 | `operatetime` | 操作时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |
| 8 | `operator` | 操作者 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `remark` | 操作类型 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `clientip` | 客户端ip | `varchar2` | 120 | 是 | 否 | 否 | - | - | - |
| 11 | `operatortype` | 操作类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `destnodeid` | 目标节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `receivedpersons_temp` | temp | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 14 | `showorder` | 操作人的显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `agentorbyagentid` | 当前记录为被代理人记录时，显示代理人的id | `integer` | - | 是 | 否 | 否 | - | - | 没有代理为-1 |
| 16 | `agenttype` | 代理类型 | `varchar2` | 8 | 是 | 否 | 否 | - | - | 0：没有代理 1：当前记录是被代理人记录(isremak=2或=4)； 2：当前记录是代理人记录（isremak 值取决于代理人是否已经操作） |
| 17 | `logid` | 日志id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `annexdocids` | 相关附件id | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 19 | `requestlogid` | 请求日志id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `operatordept` | 操作者部门 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `signdocids` | 相关文档id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 22 | `signworkflowids` | 签字意见相关流程 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 23 | `ismobile` | 是否为手机版 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 24 | `handwrittensign` | 手写签批 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `speechattachment` | 语音附件 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `receivedpersons` | 接收者名称 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 27 | `remarklocation` | 签字意见位置 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

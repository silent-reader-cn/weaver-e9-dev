# 泛微OA 数据表: `workflow_penetratelog`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_penetratelog`
- **字段总数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `requestid` | 请求id | `integer` | - | 是 | - |
| 3 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 4 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 5 | `logtype` | 日志类型 | `varchar2` | 8 | 是 | - |
| 6 | `operatedate` | 操作日期 | `varchar2` | 80 | 是 | - |
| 7 | `operatetime` | 操作时间 | `varchar2` | 64 | 是 | - |
| 8 | `operator` | 操作者 | `integer` | - | 是 | - |
| 9 | `remark` | 操作类型 | `varchar2` | 4000 | 是 | - |
| 10 | `clientip` | 客户端ip | `varchar2` | 120 | 是 | - |
| 11 | `operatortype` | 操作类型 | `integer` | - | 是 | - |
| 12 | `destnodeid` | 目标节点id | `integer` | - | 是 | - |
| 13 | `receivedpersons_temp` | temp | `varchar2` | 4000 | 是 | - |
| 14 | `showorder` | 操作人的显示顺序 | `integer` | - | 是 | - |
| 15 | `agentorbyagentid` | 当前记录为被代理人记录时，显示代理人的id | `integer` | - | 是 | 没有代理为-1 |
| 16 | `agenttype` | 代理类型 | `varchar2` | 8 | 是 | 0：没有代理      1：当前记录是被代理人记录(isremak=2或=4)；      2：当前记录是代理人记录（isremak      值取决于代理人是否已经操作） |
| 17 | `logid` | 日志id | `integer` | - | 是 | - |
| 18 | `annexdocids` | 相关附件id | `varchar2` | 2000 | 是 | - |
| 19 | `requestlogid` | 请求日志id | `integer` | - | 是 | - |
| 20 | `operatordept` | 操作者部门 | `integer` | - | 是 | - |
| 21 | `signdocids` | 相关文档id | `varchar2` | 1000 | 是 | - |
| 22 | `signworkflowids` | 签字意见相关流程 | `varchar2` | 1000 | 是 | - |
| 23 | `ismobile` | 是否为手机版 | `varchar2` | 8 | 是 | - |
| 24 | `handwrittensign` | 手写签批 | `integer` | - | 是 | - |
| 25 | `speechattachment` | 语音附件 | `integer` | - | 是 | - |
| 26 | `receivedpersons` | 接收者名称 | `clob` | 4000 | 是 | - |
| 27 | `remarklocation` | 签字意见位置 | `varchar2` | 1000 | 是 | - |

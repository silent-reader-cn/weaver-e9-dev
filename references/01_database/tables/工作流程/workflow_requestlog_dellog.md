# 泛微OA 数据表: `workflow_requestlog_dellog`

- **中文名称**: 流程签字意见删除记录表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestlog_dellog`
- **主键**: `logid`
- **字段数**: `33`

> 说明：流程签字意见记录删除表 用来记录被删除流程的签字意见

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `isvalid` | 是否有效 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 2 | `issubmitdirect` | 是否启用提交至退回节点 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 3 | `remarkquote` | 签字意见引用 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `fulltextannotation` | 全文批注 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `speechattachmente9` | e9语音附件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `logid` | 签字意见id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `nodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `logtype` | 签字意见类型 | `char` | 1 | 是 | 否 | 否 | - | - | 0：批准 1：保存 2：提交 3：退回 4：重新打开 5：删除 6：激活 7：转发 9：批注 a：意见征询 b：意见征询回复 e：强制归档 h：转办 i：干预 j：转办反馈 s：督办 t：抄送 |
| 11 | `operatedate` | 操作日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 12 | `operatetime` | 操作时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 13 | `operator` | 操作人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `remark1` | 签字意见 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 15 | `clientip` | 客户端地址 | `char` | 15 | 是 | 否 | 否 | - | - | - |
| 16 | `operatortype` | 操作人类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：人力资源，2：客户 |
| 17 | `destnodeid` | 目标节点 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `receivedpersons_1` | 接收人 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 19 | `showorder` | 显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `agentorbyagentid` | 代理人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `agenttype` | 代理类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 22 | `annexdocids` | 相关附件 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 23 | `requestlogid` | 日志id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 24 | `operatordept` | 操作者部门 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `signdocids` | 相关文档 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 26 | `signworkflowids` | 相关流程 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 27 | `receivedpersons` | 接收者名称 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 28 | `ismobile` | 是否为手机版本 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 29 | `handwrittensign` | 手写签批 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 30 | `speechattachment` | 语音附件 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 31 | `receivedpersonids` | 接收人id | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 32 | `remarklocation` | 意见位置 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 33 | `remark` | 签字意见 | `long` | 0 | 是 | 否 | 否 | - | - | - |

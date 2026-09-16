# 泛微OA 数据表: `workflow_requestlog`

- **中文名称**: 工作流请求签字日志表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestlog`
- **主键**: `logid`
- **字段数**: `32`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `issubmitdirect` | 退回后再提交直达本节点 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是<br>其他：否 |
| 2 | `remarkquote` | 流程保存时记录意见及引用-废弃 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 3 | `fulltextannotation` | 全文批注 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `speechattachmente9` | e9语音字段多语音 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `workflowid` | 工作流id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `nodeid` | 操作节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `logtype` | 签字类型 | `char` | 1 | 是 | 否 | 否 | - | - | 0：批准<br>1：保存<br>2：提交<br>3：退回<br>4：重新打开<br>5：删除<br>6：激活<br>7：转发<br>9：批注<br>a：意见征询<br>b：意见征询回复<br>e：强制归档<br>h：转办<br>i：干预<br>j：转办反馈<br>s：督办<br>t：抄送 |
| 9 | `operatedate` | 操作日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 10 | `operatetime` | 操作时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 11 | `operator` | 操作者 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `remark1` | 意见 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 13 | `clientip` | 客户端ip | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 14 | `operatortype` | 操作者类型 | `integer` | - | 是 | 否 | 否 | - | 0 | 1：人力资源，2：客户 |
| 15 | `destnodeid` | 下一节点id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 16 | `receivedpersons_1` | 接收人 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 17 | `showorder` | 显示顺序呢 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `agentorbyagentid` | 代理人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `agenttype` | 代理类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 20 | `logid` | 日志id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `remark` | 签字信息 | `long` | 0 | 是 | 否 | 否 | - | - | - |
| 22 | `annexdocids` | 相关附件 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 23 | `requestlogid` | 日志id | `integer` | - | 否 | 否 | 否 | - | 0 | - |
| 24 | `operatordept` | 操作者部门 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `signdocids` | 相关文档 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 26 | `signworkflowids` | 相关流程 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 27 | `receivedpersons` | 接收者名称 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 28 | `ismobile` | 是否为手机版本 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 29 | `handwrittensign` | 手写签批 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 30 | `speechattachment` | 语音附件 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 31 | `receivedpersonids` | 接收人id | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 32 | `remarklocation` | 意见位置 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `workflow_requestbase_dellog`

- **中文名称**: 流程删除记录表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestbase_dellog`
- **主键**: `requestid`
- **字段数**: `40`

> 说明：流程删除记录表 用来恢复流程数据

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `isvalid` | 是否有效 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 2 | `requestid` | 请求id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `lastnodeid` | 最后操作节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `lastnodetype` | 最后操作节点类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 6 | `currentnodeid` | 当前节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `currentnodetype` | 当前节点类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `status` | 请求状态 | `varchar2` | 960 | 是 | 否 | 否 | - | - | - |
| 9 | `passedgroups` | 已经通过的操作者组数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `totalgroups` | 总共需要的操作者组数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `requestname` | 请求名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `creater` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 14 | `createtime` | 创建时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 15 | `lastoperator` | 最后操作人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `lastoperatedate` | 最后操作日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 17 | `lastoperatetime` | 最后操作时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 18 | `deleted` | 是否测试状态 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `creatertype` | 创建人类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `lastoperatortype` | 最后操作者类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `nodepasstime` | 节点超时时间 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 22 | `nodelefttime` | 节点处理剩余时间 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 23 | `docids` | 相关文档 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 24 | `crmids` | 相关客户 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 25 | `hrmids_temp` | 相关人力资源 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 26 | `prjids` | 相关项目 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 27 | `cptids` | 相关资产 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 28 | `requestlevel` | 请求级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 29 | `requestmark` | 流程编号 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 30 | `messagetype` | 消息提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 31 | `mainrequestid` | 主流程的请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 32 | `currentstatus` | 保存流程暂停、撤销时流程状态 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 33 | `laststatus` | 用于保存流程暂停、撤销时，流程status的值 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |
| 34 | `ismultiprint` | 是否已批量打印 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 35 | `chatstype` | 微信提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 36 | `ecology_pinyin_search` | ecology_拼音_搜索 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 37 | `hrmids` | 相关人力资源 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 38 | `requestnamenew` | 流程标题 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 带后标题 |
| 39 | `formsignaturemd5` | 格式签名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 40 | `dataaggregated` | 子流程归档汇总标记 | `char` | 1 | 是 | 否 | 否 | - | - | - |

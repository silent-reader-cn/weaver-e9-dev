# 泛微OA 数据表: `workflow_requestbase`

- **中文名称**: 工作流请求基本信息表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestbase`
- **主键**: `requestid`
- **字段数**: `39`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `totalgroups` | 总共需要的操作者组数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `requestname` | 请求名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `creater` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 5 | `createtime` | 创建时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 6 | `lastoperator` | 最后操作者id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `lastoperatedate` | 最后操作日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 8 | `lastoperatetime` | 最后操作时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 9 | `deleted` | 是否删除 | `integer` | - | 是 | 否 | 否 | - | 0 | 0：是 |
| 10 | `creatertype` | 创建人类型 | `integer` | - | 是 | 否 | 否 | - | 0 | 1：人力资源，2：客户 |
| 11 | `lastoperatortype` | 最后操作者类型 | `integer` | - | 是 | 否 | 否 | - | 0 | 1：人力资源，2：客户 |
| 12 | `nodepasstime` | 节点超时时间 | `float` | 22 | 是 | 否 | 否 | - | -1 | 小时 |
| 13 | `nodelefttime` | 节点处理剩余时间 | `float` | 22 | 是 | 否 | 否 | - | -1 | 小时 |
| 14 | `docids` | 相关文档 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 15 | `crmids` | 相关客户 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 16 | `hrmids_temp` | temp | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 17 | `prjids` | 相关项目 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 18 | `cptids` | 相关资产 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 19 | `requestlevel` | 请求级别 | `integer` | - | 是 | 否 | 否 | - | 0 | 0：正常<br>1：重要<br>2：紧急 |
| 20 | `requestmark` | 请求说明 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 21 | `messagetype` | 消息提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `mainrequestid` | 主流程的请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `currentstatus` | 保存流程暂停、撤销时流程状态 | `integer` | - | 是 | 否 | 否 | - | - | 0为暂停，1为撤销 |
| 24 | `laststatus` | 用于保存流程暂停、撤销时，流程status的值 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |
| 25 | `ismultiprint` | 是否已批量打印 | `integer` | - | 是 | 否 | 否 | - | 0 | 1：已经批量打印，0或其他：未批量打印 |
| 26 | `chatstype` | 微信提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 27 | `ecology_pinyin_search` | ecology_拼音_搜索 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 28 | `hrmids` | 相关人力资源 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 29 | `requestnamenew` | 带标题字段的请求标题 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 30 | `formsignaturemd5` | 表单数据串加密字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 31 | `dataaggregated` | 子流程是否归档汇总状态 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 32 | `requestid` | 请求id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 33 | `workflowid` | 工作流id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 34 | `lastnodeid` | 最后操作节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 35 | `lastnodetype` | 最后操作节点类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 36 | `currentnodeid` | 当前节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 37 | `currentnodetype` | 当前节点类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 38 | `status` | 请求状态 | `varchar2` | 500 | 是 | 否 | 否 | - | - | - |
| 39 | `passedgroups` | 已经通过的操作者组数 | `integer` | - | 是 | 否 | 否 | - | - | - |

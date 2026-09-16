# 泛微OA 数据表: `workflow_curroperator_dellog`

- **中文名称**: 流程删除-工作流节点操作人删除记录表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_curroperator_dellog`
- **主键**: `id`
- **字段数**: `40`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `autodate` | 参考workflow_curroperator表 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 2 | `autodatetime` | 参考workflow_curroperator表 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `isbereject` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 4 | `isprocessing` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 5 | `isvalid` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 6 | `processuser` | 参考workflow_curroperator表 | `number` | (22,0) | 是 | 否 | 否 | - | - | - |
| 7 | `id` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `requestid` | 参考workflow_curroperator表 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 9 | `userid` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `groupid` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `workflowid` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `workflowtype` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `isremark` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 14 | `usertype` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `nodeid` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `agentorbyagentid` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `agenttype` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 18 | `showorder` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `receivedate` | 参考workflow_curroperator表 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 20 | `receivetime` | 参考workflow_curroperator表 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 21 | `viewtype` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `iscomplete` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `islasttimes` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `operatedate` | 参考workflow_curroperator表 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 25 | `operatetime` | 参考workflow_curroperator表 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 26 | `groupdetailid` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 27 | `isreminded` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 28 | `isprocessed` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 29 | `wfreminduser` | 参考workflow_curroperator表 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 30 | `wfusertypes` | 参考workflow_curroperator表 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 31 | `preisremark` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 32 | `isreject` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 33 | `needwfback` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 34 | `lastisremark` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 35 | `isreminded_csh` | 参考workflow_curroperator表 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 36 | `wfreminduser_csh` | 参考workflow_curroperator表 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 37 | `wfusertypes_csh` | 参考workflow_curroperator表 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 38 | `handleforwardid` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 39 | `takisremark` | 参考workflow_curroperator表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 40 | `lastreminddatetime` | 参考workflow_curroperator表 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

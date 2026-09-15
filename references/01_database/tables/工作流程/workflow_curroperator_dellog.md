# 泛微OA 数据表: `workflow_curroperator_dellog`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_curroperator_dellog`
- **字段总数**: `40`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `autodate` | 参考workflow_curroperator表 | `varchar2` | 1000 | 是 | - |
| 2 | `autodatetime` | 参考workflow_curroperator表 | `varchar2` | 1000 | 是 | - |
| 3 | `isbereject` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 4 | `isprocessing` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 5 | `isvalid` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 6 | `processuser` | 参考workflow_curroperator表 | `number` | (22,0) | 是 | - |
| 7 | `id` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 8 | `requestid` | 参考workflow_curroperator表 | `integer` | - | 否 | - |
| 9 | `userid` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 10 | `groupid` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 11 | `workflowid` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 12 | `workflowtype` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 13 | `isremark` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 14 | `usertype` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 15 | `nodeid` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 16 | `agentorbyagentid` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 17 | `agenttype` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 18 | `showorder` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 19 | `receivedate` | 参考workflow_curroperator表 | `char` | 10 | 是 | - |
| 20 | `receivetime` | 参考workflow_curroperator表 | `char` | 8 | 是 | - |
| 21 | `viewtype` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 22 | `iscomplete` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 23 | `islasttimes` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 24 | `operatedate` | 参考workflow_curroperator表 | `char` | 10 | 是 | - |
| 25 | `operatetime` | 参考workflow_curroperator表 | `char` | 8 | 是 | - |
| 26 | `groupdetailid` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 27 | `isreminded` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 28 | `isprocessed` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 29 | `wfreminduser` | 参考workflow_curroperator表 | `varchar2` | 1000 | 是 | - |
| 30 | `wfusertypes` | 参考workflow_curroperator表 | `varchar2` | 800 | 是 | - |
| 31 | `preisremark` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 32 | `isreject` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 33 | `needwfback` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 34 | `lastisremark` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 35 | `isreminded_csh` | 参考workflow_curroperator表 | `char` | 1 | 是 | - |
| 36 | `wfreminduser_csh` | 参考workflow_curroperator表 | `varchar2` | 4000 | 是 | - |
| 37 | `wfusertypes_csh` | 参考workflow_curroperator表 | `varchar2` | 4000 | 是 | - |
| 38 | `handleforwardid` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 39 | `takisremark` | 参考workflow_curroperator表 | `integer` | - | 是 | - |
| 40 | `lastreminddatetime` | 参考workflow_curroperator表 | `varchar2` | 4000 | 是 | - |

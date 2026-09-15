# 泛微OA 数据表: `wf_fna_wnlink_imp`

- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_wnlink_imp`
- **字段总数**: `72`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `impguid1` | workflow_nodelink表对应字段 | `varchar2` | 400 | 是 | - |
| 2 | `id` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 3 | `workflowid` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 4 | `nodeid` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 5 | `isreject` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 6 | `linkname` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 7 | `destnodeid` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 8 | `directionfrom` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 9 | `directionto` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 10 | `x1` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 11 | `y1` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 12 | `x2` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 13 | `y2` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 14 | `x3` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 15 | `y3` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 16 | `x4` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 17 | `y4` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 18 | `x5` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 19 | `y5` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 20 | `nodepasstime` | workflow_nodelink表对应字段 | `number` | (20,5) | 是 | - |
| 21 | `nodepasshour` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 22 | `nodepassminute` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 23 | `isremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 24 | `remindhour` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 25 | `remindminute` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 26 | `flowremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 27 | `msgremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 28 | `mailremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 29 | `isnodeoperator` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 30 | `iscreater` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 31 | `ismanager` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 32 | `isother` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 33 | `remindobjectids` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 34 | `isautoflow` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 35 | `flownextoperator` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 36 | `flowobjectids` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 37 | `isbulidcode` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 38 | `ismustpass` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 39 | `tipsinfo` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 40 | `processoropinion` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 41 | `wfrequestid` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 42 | `condition` | workflow_nodelink表对应字段 | `clob` | 4000 | 是 | - |
| 43 | `conditioncn` | workflow_nodelink表对应字段 | `clob` | 4000 | 是 | - |
| 44 | `startdirection` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 45 | `enddirection` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 46 | `points` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 47 | `datefield` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 48 | `timefield` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 49 | `customworkflowid` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 50 | `flowobjectreject` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 51 | `flowobjectsubmit` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 52 | `isremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 53 | `remindhour_csh` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 54 | `remindminute_csh` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 55 | `flowremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 56 | `msgremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 57 | `mailremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 58 | `isnodeoperator_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 59 | `iscreater_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 60 | `ismanager_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 61 | `isother_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 62 | `remindobjectids_csh` | workflow_nodelink表对应字段 | `clob` | 4000 | 是 | - |
| 63 | `selectnodepass` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 64 | `customworkflowid_csh` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 65 | `infocentreremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 66 | `infocentreremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 67 | `chatsremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 68 | `linkorder` | workflow_nodelink表对应字段 | `integer` | - | 是 | - |
| 69 | `newrule` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 70 | `ecology_pinyin_search` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 71 | `chatsremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |
| 72 | `rulerelationship` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | - |

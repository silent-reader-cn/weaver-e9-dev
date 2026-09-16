# 泛微OA 数据表: `wf_fna_wnlink_imp`

- **中文名称**: 预算流程初始化定义表-workflow_nodelink
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_wnlink_imp`
- **主键**: `workflow_nodelink表对应字段`
- **字段数**: `72`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `impguid1` | workflow_nodelink表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 2 | `id` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `workflowid` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `nodeid` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `isreject` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `linkname` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `destnodeid` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `directionfrom` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `directionto` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `x1` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `y1` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `x2` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `y2` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `x3` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `y3` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `x4` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `y4` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `x5` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `y5` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `nodepasstime` | workflow_nodelink表对应字段 | `number` | (20,5) | 是 | 否 | 否 | - | - | - |
| 21 | `nodepasshour` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `nodepassminute` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `isremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 24 | `remindhour` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `remindminute` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `flowremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 27 | `msgremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 28 | `mailremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 29 | `isnodeoperator` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 30 | `iscreater` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 31 | `ismanager` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 32 | `isother` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 33 | `remindobjectids` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 34 | `isautoflow` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 35 | `flownextoperator` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 36 | `flowobjectids` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 37 | `isbulidcode` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 38 | `ismustpass` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 39 | `tipsinfo` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 40 | `processoropinion` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 41 | `wfrequestid` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 42 | `condition` | workflow_nodelink表对应字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 43 | `conditioncn` | workflow_nodelink表对应字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 44 | `startdirection` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 45 | `enddirection` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 46 | `points` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 47 | `datefield` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 48 | `timefield` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 49 | `customworkflowid` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 50 | `flowobjectreject` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 51 | `flowobjectsubmit` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 52 | `isremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 53 | `remindhour_csh` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 54 | `remindminute_csh` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 55 | `flowremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 56 | `msgremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 57 | `mailremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 58 | `isnodeoperator_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 59 | `iscreater_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 60 | `ismanager_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 61 | `isother_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 62 | `remindobjectids_csh` | workflow_nodelink表对应字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 63 | `selectnodepass` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 64 | `customworkflowid_csh` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 65 | `infocentreremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 66 | `infocentreremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 67 | `chatsremind` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 68 | `linkorder` | workflow_nodelink表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 69 | `newrule` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 70 | `ecology_pinyin_search` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 71 | `chatsremind_csh` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 72 | `rulerelationship` | workflow_nodelink表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

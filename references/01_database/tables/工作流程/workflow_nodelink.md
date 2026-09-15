# 泛微OA 数据表: `workflow_nodelink`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodelink`
- **字段总数**: `73`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `drawstyle` | 新版流程图的样式 | `varchar2` | 1000 | 是 | - |
| 2 | `e9points` | e9出口方向 | `varchar2` | 1000 | 是 | - |
| 3 | `id` | ID | `integer` | - | 否 | - |
| 4 | `workflowid` | 工作流id | `integer` | - | 是 | - |
| 5 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 6 | `isreject` | 节点是否可退回 | `char` | 1 | 是 | 0：否，1：是 |
| 7 | `linkname` | 出口名称 | `varchar2` | 480 | 是 | - |
| 8 | `destnodeid` | 目标节点id | `integer` | - | 是 | - |
| 9 | `directionfrom` | 节点连线图形显示起点 | `integer` | - | 是 | - |
| 10 | `directionto` | 节点连线图形显示终点 | `integer` | - | 是 | - |
| 11 | `x1` | 节点连线图形显示横坐标1 | `integer` | - | 是 | - |
| 12 | `y1` | 节点连线图形显示纵坐标1 | `integer` | - | 是 | - |
| 13 | `x2` | 节点连线图形显示横坐标2 | `integer` | - | 是 | - |
| 14 | `y2` | 节点连线图形显示纵坐标2 | `integer` | - | 是 | - |
| 15 | `x3` | 节点连线图形显示横坐标3 | `integer` | - | 是 | - |
| 16 | `y3` | 节点连线图形显示纵坐标3 | `integer` | - | 是 | - |
| 17 | `x4` | 节点连线图形显示横坐标4 | `integer` | - | 是 | - |
| 18 | `y4` | 节点连线图形显示纵坐标4 | `integer` | - | 是 | - |
| 19 | `x5` | 节点连线图形显示横坐标5 | `integer` | - | 是 | - |
| 20 | `y5` | 节点连线图形显示纵坐标5 | `integer` | - | 是 | - |
| 21 | `nodepasstime` | 节点超时时间（小时） | `float` | 22 | 是 | - |
| 22 | `nodepasshour` | 节点超时小时 | `integer` | - | 是 | - |
| 23 | `nodepassminute` | 节点超时分钟 | `integer` | - | 是 | - |
| 24 | `isremind` | 是否超时提醒 | `char` | 1 | 是 | - |
| 25 | `remindhour` | 提前提醒小时 | `integer` | - | 是 | - |
| 26 | `remindminute` | 提前提醒分钟 | `integer` | - | 是 | - |
| 27 | `flowremind` | 工作流提醒 | `char` | 1 | 是 | - |
| 28 | `msgremind` | 短信提醒 | `char` | 1 | 是 | - |
| 29 | `mailremind` | 邮件提醒 | `char` | 1 | 是 | - |
| 30 | `isnodeoperator` | 提醒本节点操作人 | `char` | 1 | 是 | - |
| 31 | `iscreater` | 提醒创建人 | `char` | 1 | 是 | - |
| 32 | `ismanager` | 提醒本节点操作人经理 | `char` | 1 | 是 | - |
| 33 | `isother` | 提醒指定对象 | `char` | 1 | 是 | - |
| 34 | `remindobjectids` | 提醒的指定对象 | `varchar2` | 800 | 是 | - |
| 35 | `isautoflow` | 是否超时处理 | `char` | 1 | 是 | - |
| 36 | `flownextoperator` | 自动流转至下一操作人 | `char` | 1 | 是 | - |
| 37 | `flowobjectids` | 指定干预对象 | `varchar2` | 800 | 是 | - |
| 38 | `isbulidcode` | 是否生成编号 | `char` | 1 | 是 | 1：是，0或其它：否 |
| 39 | `ismustpass` | 是否必须通过 | `char` | 1 | 是 | 1：是，0或其它：否 |
| 40 | `tipsinfo` | 出口提示信息 | `varchar2` | 1000 | 是 | - |
| 41 | `processoropinion` | 处理意见 | `varchar2` | 1000 | 是 | 流程超时显示的签字意见 |
| 42 | `wfrequestid` | 请求id | `integer` | - | 是 | 用户前端设置超时时使用 |
| 43 | `condition` | 出口条件 | `clob` | 4000 | 是 | - |
| 44 | `conditioncn` | 出口条件，显示用 | `clob` | 4000 | 是 | - |
| 45 | `startdirection` | 出口起点方向 | `integer` | - | 是 | - |
| 46 | `enddirection` | 出口结束方向 | `integer` | - | 是 | - |
| 47 | `points` | 出口结束方向 | `varchar2` | 1000 | 是 | - |
| 48 | `datefield` | 日期字段 | `varchar2` | 1000 | 是 | - |
| 49 | `timefield` | 时间字段 | `varchar2` | 1000 | 是 | - |
| 50 | `customworkflowid` | 消息提醒中心 | `integer` | - | 是 | - |
| 51 | `flowobjectreject` | 退回至目标节点 | `varchar2` | 800 | 是 | - |
| 52 | `flowobjectsubmit` | 提交至目标节点 | `varchar2` | 800 | 是 | - |
| 53 | `isremind_csh` | 超时后提醒 | `char` | 1 | 是 | - |
| 54 | `remindhour_csh` | 超时后提交小时 | `integer` | - | 是 | - |
| 55 | `remindminute_csh` | 超时后提醒分钟 | `integer` | - | 是 | - |
| 56 | `flowremind_csh` | 超时后流程提醒 | `char` | 1 | 是 | - |
| 57 | `msgremind_csh` | 超时后短信提醒 | `char` | 1 | 是 | - |
| 58 | `mailremind_csh` | 超时后邮件提醒 | `char` | 1 | 是 | - |
| 59 | `isnodeoperator_csh` | 超时后提醒节点操作者 | `char` | 1 | 是 | - |
| 60 | `iscreater_csh` | 超时后提交创建人 | `char` | 1 | 是 | - |
| 61 | `ismanager_csh` | 超时后提醒节点操作者经理 | `char` | 1 | 是 | - |
| 62 | `isother_csh` | 提醒指定对象 | `char` | 1 | 是 | - |
| 63 | `remindobjectids_csh` | 提醒的指定对象 | `varchar2` | 4000 | 是 | - |
| 64 | `selectnodepass` | 选择经过的节点 | `integer` | - | 是 | - |
| 65 | `customworkflowid_csh` | 触发工作流 | `integer` | - | 是 | - |
| 66 | `infocentreremind` | 消息中心提醒 | `char` | 1 | 是 | - |
| 67 | `infocentreremind_csh` | 消息中心提醒 | `char` | 1 | 是 | - |
| 68 | `chatsremind` | 微信提醒 | `char` | 1 | 是 | - |
| 69 | `linkorder` | 连接顺序 | `integer` | - | 是 | - |
| 70 | `newrule` | 新规则 | `varchar2` | 1000 | 是 | - |
| 71 | `ecology_pinyin_search` | ecology_拼音_搜索 | `varchar2` | 1000 | 是 | - |
| 72 | `chatsremind_csh` | 微信提醒 | `char` | 1 | 是 | - |
| 73 | `rulerelationship` | 规则间关系 | `char` | 1 | 是 | 1：and,2：or |

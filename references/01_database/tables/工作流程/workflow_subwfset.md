# 泛微OA 数据表: `workflow_subwfset`

- **中文名称**: 子流程设置表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_subwfset`
- **主键**: `id`
- **字段数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `issplitdetail` | 明细拆分触发 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 2 | `id` | 子流程设置表id | `integer` | - | 否 | 否 | 否 | - | - | 由sequenceindex表得到，对应的indexdesc为workflow_subwfsetid |
| 3 | `mainworkflowid` | 主流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `subworkflowid` | 子流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `triggernodeid` | 触发节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `triggertime` | 触发时间 | `char` | 1 | 是 | 否 | 否 | - | - | 1:到达节点,2:离开节点 |
| 7 | `subwfcreatortype` | 子流程创建人类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:主流程当前操作人,2:主流程创建人,3:主流程单人力资源字段 |
| 8 | `subwfcreatorfieldid` | 主流程单人力资源字段id或多人力资源字段id或收文单位字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `isread` | 流程之间的意见是否可相互查看 | `integer` | - | 是 | 否 | 否 | - | 0 | 0否，1是 |
| 10 | `triggertype` | 触发类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1：自动触发，2：手动触发 |
| 11 | `triggeroperation` | 触发操作 | `char` | 1 | 是 | 否 | 否 | - | - | 1：批准<br>2：退回<br>""或其他：任何操作都触发 |
| 12 | `triggersource` | 触发源 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `triggersourcetype` | 触发源类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 14 | `triggersourceorder` | 触发源顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `triggercondition` | 触发条件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 16 | `isreadnodes` | 是否为已查看节点 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `isreadmainwf` | 是否为已看出主流程 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 18 | `isreadmainwfnodes` | 是否为已看出主流程节点 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 19 | `isreadparallelwf` | 是否是已查看并行流程 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 20 | `isreadparallelwfnodes` | 是否是已查看并行流程节点 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 21 | `enable` | 是否使能 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 22 | `isstopcreaternode` | 是否允许创建节点 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 23 | `condition` | 触发条件ID | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 24 | `conditioncn` | 触发条件详细 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 25 | `rulerelationship` | 条件关系 | `char` | 1 | 是 | 否 | 否 | - | - | and or |

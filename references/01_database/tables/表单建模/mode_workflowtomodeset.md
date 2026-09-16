# 泛微OA 数据表: `mode_workflowtomodeset`

- **中文名称**: 流程转数据基本信息
- **所属模块**: `表单建模`
- **数据库表名**: `mode_workflowtomodeset`
- **主键**: `id`
- **字段数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `conditionsql` | 触发sql | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 2 | `conditiontext` | 触发内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 3 | `uuid` | uuid | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 4 | `remark` | 备注 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 6 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表的id |
| 7 | `workflowid` | 流程类型 | `integer` | - | 是 | 否 | 否 | - | - | 工作流程id，对应workflow_base表的id |
| 8 | `modecreater` | 模块创建人 | `integer` | - | 是 | 否 | 否 | - | - | 1：流程当前操作人<br>2：流程创建人<br>3：流程人力资源相关字段 |
| 9 | `modecreaterfieldid` | 流程人力资源相关字段 | `integer` | - | 是 | 否 | 否 | - | - | 当使用流程中的字段的值作为模块的创建人时字段的id，对应workflow_billfield表的id |
| 10 | `triggernodeid` | 触发节点 | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_nodebase表的id |
| 11 | `triggertype` | 触发时间 | `integer` | - | 是 | 否 | 否 | - | - | 0：离开节点<br>1：到达节点 |
| 12 | `isenable` | 是否启用 | `char` | 1 | 是 | 否 | 否 | - | - | 1：启用<br>0：不启用<br>只有启用时，流程转数据才能生效 |
| 13 | `formtype` | 触发表单 | `varchar2` | 240 | 是 | 否 | 否 | - | - | maintable：主表<br>detail1：明细1，依此类推 |
| 14 | `actionid` | 接口id | `integer` | - | 是 | 否 | 否 | - | - | 对应在流程中设置的节点预处理和后处理的接口id,对应workflowactionset表的id |
| 15 | `maintableopttype` | 主表操作类型 | `varchar2` | 8 | 是 | 否 | 否 | - | - | 1：插入<br>2：更新 |
| 16 | `maintableupdatecondition` | 主表更新条件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `basedfield` | 基础字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 18 | `triggermethod` | 触发方法 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `workflowexport` | 流程出口 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `maintablewherecondition` | 主表触发条件 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 21 | `resetdataid` | 重置数据id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `ishistoricaluser` | 是否计算 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `workflowtomodename` | 流程转数据名称 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 24 | `isold` | 是否老节点 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 25 | `conditiontype` | 触发类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `setdesc` | 描述 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

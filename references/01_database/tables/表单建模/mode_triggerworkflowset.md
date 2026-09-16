# 泛微OA 数据表: `mode_triggerworkflowset`

- **中文名称**: 数据审批基本信息
- **所属模块**: `表单建模`
- **数据库表名**: `mode_triggerworkflowset`
- **主键**: `id`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `triggername` | 名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 2 | `triggeroperation` | 操作类型 | `varchar2` | 8 | 是 | 否 | 否 | - | - | 保存/提交 |
| 3 | `isenable` | 是否开启 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 4 | `conditiontype` | 条件类型 | `integer` | - | 是 | 否 | 否 | - | - | 1.字段类型sql 2.自定义sql类型 |
| 5 | `uuid` | uuid | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 6 | `setdesc` | 描述 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 8 | `modeid` | 模块名称 | `integer` | - | 是 | 否 | 否 | - | - | 模块id，对应modeinfo表的id |
| 9 | `workflowid` | 被触发流程类型 | `integer` | - | 是 | 否 | 否 | - | - | 工作流程id，对应workflow_base中的id，只有自定义的新表单的流程才能作为被触发的流程 |
| 10 | `wfcreater` | 被触发流程创建人 | `integer` | - | 是 | 否 | 否 | - | - | 被触发流程创建人<br>1:模块当前操作人<br>2:模块创建人<br>3:模块人力资源相关字段 |
| 11 | `wfcreaterfieldid` | 模块人力资源相关字段 | `integer` | - | 是 | 否 | 否 | - | - | 被触发流程创建人，从表单建模字段中取值时对应的字段id，对应workflow_billfield表的id |
| 12 | `successwriteback` | 流程触发成功回写 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 触发审批流成功或者失败的时候，可以设置回写值，用来修改当前模块某些主字段的值，比如:a="2"，<br>如果要修改多个字段的值，请用","将多个字段的值隔开，比如a="2",b="3",c="abc"，<br>其中a,b,c是指表单中数据库字段名。 |
| 13 | `failwriteback` | 流程触发失败回写 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 同上 |
| 14 | `showcondition` | 流程触发条件 | `clob` | 4000 | 是 | 否 | 否 | - | - | 流程触发条件sql |
| 15 | `showconditioncn` | 流程触发条件显示名称 | `clob` | 4000 | 是 | 否 | 否 | - | - | 流程触发条件sql对应的中文显示名称 |

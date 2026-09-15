# 泛微OA 数据表: `mode_triggerworkflowset`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_triggerworkflowset`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `triggername` | 名称 | `varchar2` | 1000 | 是 | - |
| 2 | `triggeroperation` | 操作类型 | `varchar2` | 8 | 是 | 保存/提交 |
| 3 | `isenable` | 是否开启 | `varchar2` | 8 | 是 | - |
| 4 | `conditiontype` | 条件类型 | `integer` | - | 是 | 1.字段类型sql 2.自定义sql类型 |
| 5 | `uuid` | uuid | `varchar2` | 800 | 是 | - |
| 6 | `setdesc` | 描述 | `varchar2` | 4000 | 是 | - |
| 7 | `id` | ID | `integer` | - | 否 | - |
| 8 | `modeid` | 模块名称 | `integer` | - | 是 | 模块id，对应modeinfo表的id |
| 9 | `workflowid` | 被触发流程类型 | `integer` | - | 是 | 工作流程id，对应workflow_base中的id，只有自定义的新表单的流程才能作为被触发的流程 |
| 10 | `wfcreater` | 被触发流程创建人 | `integer` | - | 是 | - |

# 泛微OA 数据表: `workflow_printset`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_printset`
- **字段总数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `workflowid` | workflowid | `integer` | - | 是 | - |
| 3 | `nodeid` | nodeid | `integer` | - | 是 | - |
| 4 | `modeid` | 模板id | `integer` | - | 是 | - |
| 5 | `type` | 类型 | `integer` | - | 是 | 1 html模式 2模板模式 3 表单中的html模式 4表单中的模板模式 |
| 6 | `isactive` | 是否活动版本(废弃) | `integer` | - | 是 | - |
| 7 | `orderid` | 顺序id | `integer` | - | 是 | - |
| 8 | `showdesc` | 显示内容 | `varchar2` | 4000 | 是 | - |
| 9 | `showtype` | 显示类型 | `char` | 1 | 是 | - |
| 10 | `stnull` | 是否显示空意见 | `char` | 1 | 是 | - |
| 11 | `printflowcomment` | 节点意见显示默认设置的值 | `char` | 1 | 是 | - |
| 12 | `printenable` | 是否启用 | `integer` | - | 是 | - |
| 13 | `viewtype` | viewtype | `varchar2` | 2000 | 是 | - |
| 14 | `selectformat` | 显示内容类型 | `integer` | - | 是 | - |
| 15 | `signshowdesc` | 有签章的显示类型 | `varchar2` | 4000 | 是 | - |
| 16 | `viewdesc` | viewdesc | `varchar2` | 2000 | 是 | - |
| 17 | `flowsignset` | 流程意见设置 | `integer` | - | 是 | - |
| 18 | `nodesignset` | 节点意见设置 | `integer` | - | 是 | - |
| 19 | `remarkcolumn` | 分栏 | `integer` | - | 是 | - |

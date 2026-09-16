# 泛微OA 数据表: `workflow_flownode`

- **中文名称**: 流程流转节点表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_flownode`
- **主键**: `修改时间`
- **字段数**: `31`

> 说明：主键

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `remarkcolumn` | - | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `isapprovalprocess` | - | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 3 | `showdesc` | - | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `selectformat` | - | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `signshowdesc` | - | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `printselectformat` | - | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `printsignshowdesc` | - | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 8 | `printshowdesc` | - | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `printviewdesc` | - | `varchar2` | 2000 | 是 | 否 | 否 | - | all | - |
| 10 | `printviewtype` | - | `varchar2` | 2000 | 是 | 否 | 否 | - | all | - |
| 11 | `printremarkcolumn` | - | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 12 | `printstnull` | - | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 13 | `printshowtype` | - | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 14 | `rejecttocreater` | - | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `vdaction` | - | `char` | 1 | 是 | 否 | 否 | - | 0 | - |
| 16 | `vdposition` | - | `char` | 1 | 是 | 否 | 否 | - | 0 | - |
| 17 | `batchsubmit` | - | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `forwardback` | - | `char` | 1 | 是 | 否 | 否 | - | 1 | - |
| 19 | `isenableidcheck` | - | `char` | 1 | 是 | 否 | 否 | - | 0 | - |
| 20 | `isenabledtaptn` | - | `char` | 1 | 是 | 否 | 否 | - | 0 | - |
| 21 | `isenablesignatures` | - | `char` | 1 | 是 | 否 | 否 | - | 0 | - |
| 22 | `wf_verified` | - | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 23 | `selectnextflow` | - | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `selectnextflowtype` | - | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `selectnextflownode` | - | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 26 | `useexceptionhandle` | - | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 27 | `exceptionhandleway` | - | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 28 | `flowtoassignnode` | - | `integer` | - | 是 | 否 | 否 | - | - | - |
| 29 | `notseeeachother` | - | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 30 | `subprocesssummary` | - | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 31 | `isremarklocation` | - | `integer` | - | 是 | 否 | 否 | - | 0 | - |

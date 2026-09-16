# 泛微OA 数据表: `workflow_flownode`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_flownode`
- **文档收录字段数**: `31`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `remarkcolumn` | - | `integer` | - | - | - |
| 2 | `isapprovalprocess` | - | `char` | 1 | - | - |
| 3 | `showdesc` | - | `varchar2` | 4000 | - | - |
| 4 | `selectformat` | - | `integer` | - | - | - |
| 5 | `signshowdesc` | - | `varchar2` | 4000 | - | - |
| 6 | `printselectformat` | - | `integer` | - | - | - |
| 7 | `printsignshowdesc` | - | `varchar2` | 4000 | - | - |
| 8 | `printshowdesc` | - | `varchar2` | 4000 | - | - |
| 9 | `printviewdesc` | - | `varchar2` | 2000 | - | - |
| 10 | `printviewtype` | - | `varchar2` | 2000 | - | - |
| 11 | `printremarkcolumn` | - | `char` | 1 | - | - |
| 12 | `printstnull` | - | `char` | 1 | - | - |
| 13 | `printshowtype` | - | `char` | 1 | - | - |
| 14 | `rejecttocreater` | - | `integer` | - | - | - |
| 15 | `vdaction` | - | `char` | 1 | - | - |
| 16 | `vdposition` | - | `char` | 1 | - | - |
| 17 | `batchsubmit` | - | `integer` | - | - | - |
| 18 | `forwardback` | - | `char` | 1 | - | - |
| 19 | `isenableidcheck` | - | `char` | 1 | - | - |
| 20 | `isenabledtaptn` | - | `char` | 1 | - | - |
| 21 | `isenablesignatures` | - | `char` | 1 | - | - |
| 22 | `wf_verified` | - | `clob` | 4000 | - | - |
| 23 | `selectnextflow` | - | `integer` | - | - | - |
| 24 | `selectnextflowtype` | - | `integer` | - | - | - |
| 25 | `selectnextflownode` | - | `varchar2` | 1000 | - | - |
| 26 | `useexceptionhandle` | - | `char` | 1 | - | - |
| 27 | `exceptionhandleway` | - | `char` | 1 | - | - |
| 28 | `flowtoassignnode` | - | `integer` | - | - | - |
| 29 | `notseeeachother` | - | `char` | 1 | - | - |
| 30 | `subprocesssummary` | - | `char` | 1 | - | - |
| 31 | `isremarklocation` | - | `integer` | - | - | - |

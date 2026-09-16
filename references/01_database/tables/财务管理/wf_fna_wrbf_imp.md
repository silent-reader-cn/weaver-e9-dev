# 泛微OA 数据表: `wf_fna_wrbf_imp`

- **中文名称**: 预算流程初始化定义表-workflow_rquestBrowseFunction
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_wrbf_imp`
- **主键**: `workflow_rquestBrowseFunction表对应字段`
- **字段数**: `62`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `requestnameshoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 2 | `workflowtypeshoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `processnumbershoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `createtypeidshoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `departmentshoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `jsqjtype_readonly` | workflow_rquestBrowseFunction表对应字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `gdtype_readonly` | workflow_rquestBrowseFunction表对应字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `xgkhid_readonly` | workflow_rquestBrowseFunction表对应字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 9 | `xgxmid_readonly` | workflow_rquestBrowseFunction表对应字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 10 | `createdate_readonly` | workflow_rquestBrowseFunction表对应字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 11 | `createsubid_readonly` | workflow_rquestBrowseFunction表对应字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 12 | `createdeptid_readonly` | workflow_rquestBrowseFunction表对应字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 13 | `createtypeid_readonly` | workflow_rquestBrowseFunction表对应字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 14 | `processnumber_readonly` | workflow_rquestBrowseFunction表对应字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 15 | `workflowtype_readonly` | workflow_rquestBrowseFunction表对应字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 16 | `requestname_readonly` | workflow_rquestBrowseFunction表对应字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 17 | `xgxmtype` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 18 | `xgkhtype` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 19 | `createdatefieldid` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 20 | `cjrfbshoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 21 | `createsubidshoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 22 | `impguid1` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 23 | `workflowid` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 24 | `fieldid` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 25 | `fieldtype` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 26 | `searchname` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 27 | `showorder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 28 | `showopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 29 | `searchvalue` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 30 | `requestbs` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 31 | `requestname` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 32 | `workflowtype` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 33 | `processnumber` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 34 | `createtype` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 35 | `createtypeid` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 36 | `xgxmidopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 37 | `xgkhidopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 38 | `gdtypeopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 39 | `jsqjtypeopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 40 | `createdepttype` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 41 | `createsubidopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 42 | `createdateopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 43 | `createdatetypeshoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 44 | `xgxmidshoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 45 | `xgkhidshoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 46 | `gdtypeshoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 47 | `jsqjtypeshoworder` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 48 | `department` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 49 | `createsubtype` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 50 | `createsubid` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 51 | `createdatetype` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 52 | `createdatestart` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 53 | `xgxmid` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 54 | `xgkhid` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 55 | `gdtype` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 56 | `jsqjtype` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 57 | `requestnameopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 58 | `workflowtypeopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 59 | `processnumberopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 60 | `createtypeidopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 61 | `createdeptidopen` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 62 | `createdateend` | workflow_rquestBrowseFunction表对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

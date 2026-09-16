# 泛微OA 数据表: `wf_fna_wfbase_imp`

- **中文名称**: 预算流程初始化定义表-workflow_base
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_wfbase_imp`
- **主键**: `workflow_base表对应字段`
- **字段数**: `105`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `impguid1` | workflow_base表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 2 | `candelacc` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 3 | `isforwardrights` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `isimportwf` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `isrejectremind` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `ischangrejectnode` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `wfdocownertype` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `wfdocownerfieldid` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `newdocpath` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `keepsign` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `seccategoryid` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `custompage` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 13 | `issignview` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `isselectrejectnode` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 15 | `forbidattdownload` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `isimportdetail` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 17 | `specialapproval` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 18 | `frequency` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `cycle` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 20 | `nosynfields` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 21 | `isneeddelacc` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 22 | `sapsource` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 23 | `isfnacontrol` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 24 | `fnanodeid` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 25 | `fnadepartmentid` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 26 | `smsalertstype` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 27 | `forwardreceivedef` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 28 | `issavecheckform` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 29 | `archivenomsgalert` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 30 | `archivenomailalert` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 31 | `isfnabudgetwf` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 32 | `chatstype` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 33 | `chatsalerttype` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 34 | `notremindifarchived` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 35 | `isworkflowdoc` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 36 | `officaltype` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 37 | `version` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 38 | `activeversionid` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 39 | `versiondescription` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 40 | `versioncreater` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 41 | `dsporder` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 42 | `fieldnotimport` | workflow_base表对应字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 43 | `isfree` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 44 | `ecology_pinyin_search` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 45 | `custompage4emoble` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 46 | `isupdatetitle` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 47 | `isshared` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 48 | `isoverrb` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 49 | `isoveriv` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 50 | `showcharturl` | workflow_base表对应字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 51 | `isautoapprove` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 52 | `isautocommit` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 53 | `isshowsrc` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 54 | `sendtomessagetype` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 55 | `islockworkflow` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 56 | `limitvalue` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 57 | `id` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 58 | `workflowname` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 59 | `workflowdesc` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 60 | `workflowtype` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 61 | `securelevel` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 62 | `formid` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 63 | `userid` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 64 | `isbill` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 65 | `iscust` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 66 | `helpdocid` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 67 | `isvalid` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 68 | `needmark` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 69 | `messagetype` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 70 | `multisubmit` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 71 | `defaultname` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 72 | `docpath` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 73 | `subcompanyid` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 74 | `mailmessagetype` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 75 | `docrightbyoperator` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 76 | `doccategory` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 77 | `istemplate` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 78 | `templateid` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 79 | `catelogtype` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 80 | `selectedcatelog` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 81 | `docrightbyhrmresource` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 82 | `needaffirmance` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 83 | `isremarks` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 84 | `isannexupload` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 85 | `annexdoccategory` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 86 | `isshowonreportinput` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 87 | `titlefieldid` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 88 | `keywordfieldid` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 89 | `isshowchart` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 90 | `orderbytype` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 91 | `istridiffworkflow` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 92 | `ismodifylog` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 93 | `ifversion` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 94 | `wfdocpath` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 95 | `wfdocowner` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 96 | `isedit` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 97 | `editor` | workflow_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 98 | `editdate` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 99 | `edittime` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 100 | `showdelbuttonbyreject` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 101 | `showuploadtab` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 102 | `issigndoc` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 103 | `showdoctab` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 104 | `issignworkflow` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 105 | `showworkflowtab` | workflow_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

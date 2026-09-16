# 泛微OA 数据表: `wf_fna_wf_imp`

- **中文名称**: 预算流程初始化定义表-workflow_nodebase
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_wf_imp`
- **主键**: `workflow_nodebase表对应字段`
- **字段数**: `104`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `impguid1` | workflow_nodebase表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 2 | `isbeforwardalready` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 3 | `isshowbeforwardalready` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `isalreadyforward` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `isshowalreadyforward` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `isbeforwardsubmitalready` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `isshowbeforwardsubmitalready` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 8 | `isbeforwardsubmitnotaries` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `isshowbeforwardsubmitnotaries` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `freefs` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `nodeorder` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `signfieldids` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 13 | `ishideinput` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `ishidearea` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `issubwfallend` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 16 | `subwfscope` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 17 | `subwfdiffscope` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 18 | `issubwfremind` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 19 | `subwfremindtype` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 20 | `subwfremindoperator` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 21 | `subwfremindobject` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 22 | `subwfremindperson` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 23 | `subwffreeforword` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 24 | `istakingopinions` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 25 | `ishandleforward` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 26 | `vttakingopinions` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 27 | `vthandleforward` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 28 | `vttpostil` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 29 | `vtrpostil` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 30 | `vmobilesource` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 31 | `rulerelationship` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 32 | `pdfprint` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 33 | `useexceptionhandle` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 34 | `exceptionhandleway` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 35 | `flowtoassignnode` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 36 | `notseeeachother` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 37 | `printflowcomment` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 38 | `subprocesssummary` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 39 | `isremarklocation` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 40 | `isrejectremind` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 41 | `ischangrejectnode` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 42 | `isselectrejectnode` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 43 | `rejectablenodes` | workflow_nodebase表对应字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 44 | `issubmitdirectnode` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 45 | `workflowid` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 46 | `nodeid` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 47 | `nodetype` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 48 | `viewnodeids` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 49 | `ismode` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 50 | `showdes` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 51 | `printdes` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 52 | `isformsignature` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 53 | `nodetitle` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 54 | `viewtypeall` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 55 | `viewdescall` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 56 | `showtype` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 57 | `vtapprove` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 58 | `vtrealize` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 59 | `vtforward` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 60 | `vtpostil` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 61 | `vtrecipient` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 62 | `vtreject` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 63 | `vtsuperintend` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 64 | `vtover` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 65 | `vdcomments` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 66 | `vddeptname` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 67 | `vdoperator` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 68 | `vddate` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 69 | `vdtime` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 70 | `stnull` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 71 | `formsignaturewidth` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 72 | `formsignatureheight` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 73 | `drawbackflag` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 74 | `ispendingforward` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 75 | `iswaitforwardopinion` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 76 | `isbeforward` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 77 | `issubmitedopinion` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 78 | `issubmitforward` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 79 | `isfreeworkflow` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 80 | `freewfsetcurnamecn` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 81 | `freewfsetcurnameen` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 82 | `rejectbackflag` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 83 | `issignmustinput` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 84 | `toexcel` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 85 | `vsignupload` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 86 | `vsigndoc` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 87 | `vsignworkflow` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 88 | `freewfsetcurnametw` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 89 | `isbeforwardsubmit` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 90 | `isbeforwardmodify` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 91 | `isbeforwardpending` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 92 | `isshowpendingforward` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 93 | `isshowwaitforwardopinion` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 94 | `isshowbeforward` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 95 | `isshowsubmitedopinion` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 96 | `isshowsubmitforward` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 97 | `isshowbeforwardsubmit` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 98 | `isshowbeforwardmodify` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 99 | `isshowbeforwardpending` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 100 | `isfeedback` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 101 | `isnullnotfeedback` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 102 | `vtintervenor` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 103 | `isbeforwardtodo` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 104 | `isshowbeforwardtodo` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

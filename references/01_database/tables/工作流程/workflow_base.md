# 泛微OA 数据表: `workflow_base`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_base`
- **字段总数**: `135`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isshowsrc` | 显示意见来源 | `varchar2` | 8 | 是 | - |
| 2 | `sendtomessagetype` | 消息类型 | `char` | 1 | 是 | - |
| 3 | `islockworkflow` | 流程锁定 | `char` | 1 | 是 | - |
| 4 | `limitvalue` | 限制附件上传格式 | `varchar2` | 2000 | 是 | - |
| 5 | `locknodes` | 流程编辑锁定 | `varchar2` | 2000 | 是 | - |
| 6 | `tracefieldid` | 痕迹正文字段 | `integer` | - | 是 | - |
| 7 | `tracesavesecid` | 痕迹正文保存目录 | `integer` | - | 是 | - |
| 8 | `tracecategorytype` | 痕迹正文保存目录类型 | `char` | 1 | 是 | - |
| 9 | `tracecategoryfieldid` | 痕迹正文保存目录字段ID | `integer` | - | 是 | - |
| 10 | `tracedocownertype` | 痕迹正文所有者类型 | `integer` | - | 是 | - |
| 11 | `tracedocownerfieldid` | 痕迹正文所有者字段 | `integer` | - | 是 | - |
| 12 | `tracedocowner` | 痕迹正文所有者 | `integer` | - | 是 | - |
| 13 | `titletemplate` | 标题模版 | `clob` | 4000 | 是 | - |
| 14 | `freewftype` | 自由流程的模式 | `char` | 1 | 是 | 1：简易模式，2：高级模式 |
| 15 | `titleset` | 自定义模式 | `char` | 1 | 是 | 0或空为默认模式 |
| 16 | `isautoremark` | 自动填写户最后一次手动操作的意见 | `char` | 1 | 是 | - |
| 17 | `importreadonlyfield` | 允许导入数据到只读字段 | `char` | 1 | 是 | 1：是　其他：否 |
| 18 | `enablesignature` | test | `char` | 1 | 是 | - |
| 19 | `issmsremind` | 是否开启短信提醒 | `char` | 1 | 是 | - |
| 20 | `iswechatremind` | 是否开启微信提醒 | `char` | 1 | 是 | - |
| 21 | `isemailremind` | 是否开启邮件提醒 | `char` | 1 | 是 | - |
| 22 | `isdefaultsmsremind` | 短信默认提醒 | `char` | 1 | 是 | - |
| 23 | `isdefaultwechatremind` | 微信默认提醒 | `char` | 1 | 是 | - |
| 24 | `isdefaultemailremind` | 邮件默认提醒 | `char` | 1 | 是 | - |
| 25 | `isarchivenoremind` | 归档节点不需提醒 | `char` | 1 | 是 | - |
| 26 | `isccnoremind` | 抄送人不需提醒 | `char` | 1 | 是 | - |
| 27 | `ischosereminder` | 由操作者选择提醒接收人 | `char` | 1 | 是 | - |
| 28 | `alterremindnodestype` | 允许修改提醒的节点类型 | `char` | 1 | 是 | 0：全部，1：选择 |
| 29 | `alterremindnodes` | 选择提醒的节点id，用“,”间隔 | `varchar2` | 1000 | 是 | - |
| 30 | `submittype` | 批量提交启用节点 | `integer` | - | 是 | 0:全部,1:选择 2：排除 |
| 31 | `hrmconditionshowtype` | 人力资源条件显示设置 | `char` | 1 | 是 | - |
| 32 | `defaultnameruletype` | 标题设置规则 | `char` | 1 | 是 | - |
| 33 | `isreaffirm` | test | `char` | 1 | 是 | - |
| 34 | `isonlyoneautoapprove` | 仅当后续节点操作者为本人一人时自动处理 | `char` | 1 | 是 | - |
| 35 | `isopencommunication` | 是否启用相关交流 | `integer` | - | 是 | - |
| 36 | `isselectrejectnode` | 退回时是否可选择退回节点 | `char` | 1 | 是 | - |
| 37 | `forbidattdownload` | 禁止附件批量下载 | `integer` | - | 是 | - |
| 38 | `isimportdetail` | 是否导入明细 | `char` | 1 | 是 | - |
| 39 | `specialapproval` | 是否特批件 | `char` | 1 | 是 | 1:是,0或其他:否 |
| 40 | `frequency` | 次数 | `integer` | - | 是 | - |
| 41 | `cycle` | 周期 | `char` | 1 | 是 | - |
| 42 | `nosynfields` | 不需同步字段 | `varchar2` | 2000 | 是 | - |
| 43 | `isneeddelacc` | 设置是否流程删除时相关的附件 | `varchar2` | 8 | 是 | - |
| 44 | `sapsource` | sap数据源 | `varchar2` | 160 | 是 | - |
| 45 | `isfnacontrol` | 是否需要预算控制 | `char` | 1 | 是 | - |
| 46 | `fnanodeid` | 预算节点id | `varchar2` | 4000 | 是 | - |
| 47 | `fnadepartmentid` | 预算部门id | `varchar2` | 4000 | 是 | - |
| 48 | `smsalertstype` | 设置短信提醒方式 | `char` | 1 | 是 | - |
| 49 | `forwardreceivedef` | 转发接收定义 | `char` | 1 | 是 | - |
| 50 | `issavecheckform` | 流程保存是否验证必填 | `char` | 1 | 是 | 0：否 1：是 |
| 51 | `archivenomsgalert` | 归档节点不需短信提醒 | `char` | 1 | 是 | 0：否 1：是 |
| 52 | `archivenomailalert` | 归档节点不需邮件提醒 | `char` | 1 | 是 | 0：否 1：是 |
| 53 | `isfnabudgetwf` | 是否是费控流程 | `char` | 1 | 是 | - |
| 54 | `chatstype` | 是否微信提醒 | `integer` | - | 是 | - |
| 55 | `chatsalerttype` | 微信提醒类型 | `integer` | - | 是 | - |
| 56 | `notremindifarchived` | 归档路程不在提醒 | `integer` | - | 是 | - |
| 57 | `isworkflowdoc` | 是否是公文流程 | `integer` | - | 是 | - |
| 58 | `version` | 版本号 | `integer` | - | 是 | - |
| 59 | `activeversionid` | 当前流程所属活动版本id | `integer` | - | 是 | - |
| 60 | `versiondescription` | 版本介绍 | `varchar2` | 1000 | 是 | - |
| 61 | `versioncreater` | 版本创建人 | `integer` | - | 是 | - |
| 62 | `dsporder` | 显示顺序 | `integer` | - | 是 | - |
| 63 | `fieldnotimport` | 无需导入字段 | `varchar2` | 4000 | 是 | - |
| 64 | `isfree` | 是否是自由流程 | `char` | 1 | 是 | - |
| 65 | `ecology_pinyin_search` | 流程名称拼音缩写-用于快速搜索 | `varchar2` | 1000 | 是 | - |
| 66 | `officaltype` | 公文类型 | `integer` | - | 是 | - |
| 67 | `custompage4emoble` | 手机版用自定义页面 | `varchar2` | 2000 | 是 | - |
| 68 | `isupdatetitle` | 是否修改过流程标题字段 | `integer` | - | 是 | 0或者空：未修改过流程标题字段 1：修改了流程标题字段 |
| 69 | `isshared` | 是否允许共享 | `char` | 1 | 是 | - |
| 70 | `isoverrb` | 归档收回 | `char` | 1 | 是 | - |
| 71 | `isoveriv` | 归档干预 | `char` | 1 | 是 | - |
| 72 | `showcharturl` | 显示流程图 | `varchar2` | 4000 | 是 | - |
| 73 | `isautoapprove` | 自动批准 | `char` | 1 | 是 | - |
| 74 | `isautocommit` | 自动提交 | `char` | 1 | 是 | - |
| 75 | `id` | ID | `integer` | - | 否 | - |
| 76 | `workflowname` | 工作流名称 | `varchar2` | 1000 | 是 | - |
| 77 | `workflowdesc` | 工作流描述 | `varchar2` | 1000 | 是 | - |
| 78 | `workflowtype` | 所属工作流种类 | `integer` | - | 是 | - |
| 79 | `securelevel` | 安全级别 | `varchar2` | 24 | 是 | - |
| 80 | `formid` | 表单或单据id | `integer` | - | 是 | - |
| 81 | `userid` | 创建人id | `integer` | - | 是 | - |
| 82 | `isbill` | 单据还是表单 | `char` | 1 | 是 | 0：表单1：单据 |
| 83 | `iscust` | 是否为门户工作流 | `integer` | - | 是 | 0：否 1：是 |
| 84 | `helpdocid` | 工作流帮助文档id | `integer` | - | 是 | - |
| 85 | `isvalid` | 是否有效 | `char` | 1 | 是 | 0：否 1：是 |
| 86 | `needmark` | 是否需要编号 | `char` | 1 | 是 | 0：否 1：是 |
| 87 | `messagetype` | 否短信提醒 | `integer` | - | 是 | 0：否 1：是 |
| 88 | `multisubmit` | 是否批量提交 | `integer` | - | 是 | 0：否 1：是 |
| 89 | `defaultname` | 是否默认说明 | `integer` | - | 是 | 0：否 1：是 |
| 90 | `docpath` | 附件上传目录名称 | `varchar2` | 2000 | 是 | - |
| 91 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 92 | `mailmessagetype` | 是否邮件提醒 | `integer` | - | 是 | 0：否 1：是 |
| 93 | `docrightbyoperator` | 是否跟随文档关联 | `integer` | - | 是 | 0：否 1：是 |
| 94 | `doccategory` | 附件上传目录id | `varchar2` | 1000 | 是 | - |
| 95 | `istemplate` | 是否为流程模板 | `char` | 1 | 是 | 0：否 1：是 |
| 96 | `templateid` | 流程引用模板id | `integer` | - | 是 | - |
| 97 | `catelogtype` | 附件上传目录类型 | `integer` | - | 是 | 0：固定目录 1：选择目录 |
| 98 | `selectedcatelog` | 所选择目录的对应的id | `integer` | - | 是 | - |
| 99 | `docrightbyhrmresource` | 是否按人力资源字段附权 | `integer` | - | 是 | 默认为不启用 |
| 100 | `needaffirmance` | 是否需要提交确认 | `char` | 1 | 是 | 0：否 1：是 |
| 101 | `isremarks` | 是否允许已办及办结事宜转发 | `char` | 1 | 是 | - |
| 102 | `isannexupload` | 是否允许签字意见上传附件 | `char` | 1 | 是 | - |
| 103 | `annexdoccategory` | 流程签字意见附件文档目录 | `varchar2` | 1000 | 是 | - |
| 104 | `isshowonreportinput` | 是否数据中心输入表 | `char` | 1 | 是 | 0：否 1：是 |
| 105 | `titlefieldid` | 标题字段id | `integer` | - | 是 | - |
| 106 | `keywordfieldid` | 主题词字段id | `integer` | - | 是 | - |
| 107 | `isshowchart` | 提交流程后是否显示流程图 | `char` | 1 | 是 | 0：否 1：是 |
| 108 | `orderbytype` | 流程审批意见显示顺序 | `char` | 1 | 是 | 1：倒序；2：正序 |
| 109 | `istridiffworkflow` | 是否触发不同流程 | `char` | 1 | 是 | 0：否 1：是 |
| 110 | `ismodifylog` | 是否记录表单修改日志 | `char` | 1 | 是 | 0：否 1：是 |
| 111 | `ifversion` | 是否保留正文版本 | `char` | 1 | 是 | 0：否 1：是 |
| 112 | `wfdocpath` | 流程保存为文档的路径 | `varchar2` | 800 | 是 | - |
| 113 | `wfdocowner` | 流程保存?槲?n的所有者 | `varchar2` | 800 | 是 | - |
| 114 | `isedit` | 是否正在图形化编辑 | `char` | 1 | 是 | - |
| 115 | `editor` | 当前编辑人 | `integer` | - | 是 | - |
| 116 | `editdate` | 编辑日期 | `char` | 10 | 是 | - |
| 117 | `edittime` | 编辑时间 | `char` | 8 | 是 | - |
| 118 | `showdelbuttonbyreject` | 退回创建节点是否可删除 | `char` | 1 | 是 | 0：否 1：是 |
| 119 | `showuploadtab` | 是否显示上传附件tab | `char` | 1 | 是 | 0：否 1：是 |
| 120 | `issigndoc` | 是否允许签字意见关联文档 | `char` | 1 | 是 | 0：否 1：是 |
| 121 | `showdoctab` | 是否显示相关文档tab | `char` | 1 | 是 | 0：否 1：是 |
| 122 | `issignworkflow` | 是否允许签字意见关联流程 | `char` | 1 | 是 | 0：否 1：是 |
| 123 | `showworkflowtab` | 是否显示相关流程tab | `char` | 1 | 是 | 0：否 1：是 |
| 124 | `candelacc` | 是否允许删除附件 | `char` | 1 | 是 | 0：否 1：是 |
| 125 | `isforwardrights` | 是否允许转发人设置被转发人权限 | `char` | 1 | 是 | 0：否 1：是 |
| 126 | `isimportwf` | 新建时是否可导入流程 | `char` | 1 | 是 | 0：否 1：是 |
| 127 | `isrejectremind` | 退回是否提醒的 | `char` | 1 | 是 | 0：否 1：是 |
| 128 | `ischangrejectnode` | 退回人是否可设置提醒节点 | `char` | 1 | 是 | 0：否 1：是 |
| 129 | `wfdocownertype` | 流程存为文档的文档所有者取值类型 | `integer` | - | 是 | 1、指定人 2、取流程表单字段的值 |
| 130 | `wfdocownerfieldid` | 流程存为文档的文档所有者 | `integer` | - | 是 | 如果取值与流程表单字段的值，指定字段id |
| 131 | `newdocpath` | 流程中多文档字段 | `varchar2` | 1000 | 是 | 直接新建文档是可根据该属性指定的目录，直接到文档创建目录（格式主目录id/分目录id/子目录id） |
| 132 | `keepsign` | 保持签字意见 | `integer` | - | 是 | - |
| 133 | `seccategoryid` | 子目录id | `integer` | - | 是 | - |
| 134 | `custompage` | 自定义页面 | `varchar2` | 2000 | 是 | - |
| 135 | `issignview` | 是否允许查看先关流程签字意见 | `integer` | - | 是 | - |

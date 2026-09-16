# 泛微OA 数据表: `docdetail`

- **中文名称**: 文档信息表
- **所属模块**: `知识管理`
- **数据库表名**: `docdetail`
- **主键**: `id`
- **字段数**: `105`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `sumdownload` | 下载量 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 2 | `accessorycount` | 附件个数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `replaydoccount` | 回复文档的数量 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `usertype` | 用户类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1：人力资源，2：客户 |
| 5 | `docno` | 文档归档号 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 6 | `cancopy` | 是否可以拷贝 | `char` | 1 | 是 | 否 | 否 | - | - | 1、是；0、否 |
| 7 | `canremind` | 回复是否提醒 | `char` | 1 | 是 | 否 | 否 | - | - | 1、是；0、否 |
| 8 | `countmark` | 打分次数 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 9 | `summark` | 总分数 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 10 | `sumreadcount` | 浏览量 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 11 | `orderable` | 是否可以订阅 | `char` | 1 | 是 | 否 | 否 | - | 0 | 1、是；0、否 |
| 12 | `docextendname` | 扩展名 | `char` | 10 | 是 | 否 | 否 | - | - | 可选项：doc 、html、xls |
| 13 | `doccode` | 文档编号 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 14 | `docedition` | 文档版本 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `doceditionid` | 文档版本id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `ishistory` | 是否历史 | `integer` | - | 是 | 否 | 否 | - | - | 1:是，0：否 |
| 17 | `maindoc` | 主文档 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `approvetype` | 审批类型 | `integer` | - | 是 | 否 | 否 | - | - | 1:生效审批,2:失效审批 |
| 19 | `readoptercanprint` | 允许只读操作人打印 | `integer` | - | 是 | 否 | 否 | - | - | 0:不允许，1:允许 |
| 20 | `docvaliduserid` | 生效操作人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `docvaliddate` | 生效日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 22 | `docvalidtime` | 生效时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 23 | `docpubuserid` | 发布操作人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `docpubdate` | 发布日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 25 | `docpubtime` | 发布时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 26 | `docreopenuserid` | 重新打开操作人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 27 | `docreopendate` | 重新打开日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 28 | `docreopentime` | 重新打开时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 29 | `docinvaluserid` | 失效操作人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 30 | `docinvaldate` | 失效日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 31 | `docinvaltime` | 失效时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 32 | `doccanceluserid` | 作废操作人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 33 | `doccanceldate` | 作废日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 34 | `doccanceltime` | 作废时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 35 | `selectedpubmouldid` | 选择的发布模板 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 36 | `checkoutstatus` | 签出状态 | `char` | 1 | 是 | 否 | 否 | - | - | 1：自动签出，2：强制签出，0或其它：未签出 |
| 37 | `checkoutuserid` | 签出用户 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 38 | `checkoutusertype` | 签出用户类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 39 | `checkoutdate` | 签出日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 40 | `checkouttime` | 签出时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 41 | `hasusedtemplet` | 是否套红，即是否已经套用显示模板 | `char` | 1 | 是 | 否 | 否 | - | - | 1：已经套红，0或null：尚未套红。针对已经套红的文档将不能调用显示模板或编辑模板。 |
| 42 | `invalidationdate` | 失效日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 43 | `doccreatertype` | 文档创建者类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 44 | `doclastmodusertype` | 文档最后修改者类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 45 | `docapproveusertype` | 文档审批者类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 46 | `docvalidusertype` | 生效操作人类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 47 | `docinvalusertype` | 失效操作人类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 48 | `docarchiveusertype` | 文档归档者类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 49 | `doccancelusertype` | 作废操作人类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 50 | `docpubusertype` | 发布操作人类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 51 | `docreopenusertype` | 重新打开操作人类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 52 | `ownertype` | 文档拥有者类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1:内部用户，2：外部用户 |
| 53 | `docstatus` | 文档状态 | `integer` | - | 是 | 否 | 否 | - | - | 0:草稿<br>1:生效/正常(不需要审批，归档重新打开)<br>2: 生效/正常(审批后,发布后)<br>3:审批<br>4:退回(草稿)<br>5:归档<br>6:待发布<br>7:失效<br>8:作废<br>9:流程草稿 |
| 54 | `canprintednum` | 可打印份数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 55 | `hasprintednum` | 已打印份数 | `integer` | - | 否 | 否 | 否 | - | 0 | 默认为0 |
| 56 | `approverequestid` | 文档生效审批请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 57 | `fromworkflow` | 是否来自流程 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 58 | `istop` | 是否置顶 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 59 | `topdate` | 置顶日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 60 | `toptime` | 置顶时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |
| 61 | `topstartdate` | 置顶有效开始日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 62 | `topenddate` | 置顶有效结束日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 63 | `invalidrequestid` | 文档失效审批请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 64 | `editmouldid` | 编辑模版id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 65 | `ecology_pinyin_search` | 查询用拼音首字母 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 66 | `docvestin` | 不知道 | `integer` | - | 否 | 否 | 否 | - | 0 | - |
| 67 | `id` | 文档id | `integer` | - | 否 | 否 | 否 | - | - | 由sequenceindex表得到，对应“docid” |
| 68 | `maincategory` | 文档主目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 69 | `subcategory` | 文档分目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 70 | `seccategory` | 文档子目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 71 | `doctype` | 文档种类 | `integer` | - | 是 | 否 | 否 | - | - | 1：html文档；2：office文档 |
| 72 | `doclangurage` | 文档语言 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 73 | `docapprovable` | 是否需要审批 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 74 | `docreplyable` | 可否回复 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 75 | `isreply` | 是否回复文档 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 76 | `replydocid` | 回复文件id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 77 | `docsubject` | 文档标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 78 | `docsharetype` | 文档共享种类 | `char` | 1 | 是 | 否 | 否 | - | - | 0:不共享，1:所有人，2:本部门员工，3:角色 |
| 79 | `shareroleid` | 共享角色id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 80 | `docpublishtype` | 新闻类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1: 文档，2：主页，3：标题 |
| 81 | `itemid` | 文档中选择的物品id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 82 | `itemmaincategoryid` | 文档中选择的物品种类id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 83 | `hrmresid` | 文档中选择的人资源id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 84 | `crmid` | 文档中选择的crmid | `integer` | - | 是 | 否 | 否 | - | - | - |
| 85 | `projectid` | 文档中选择的项目id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 86 | `financeid` | 文档中选择的财务-交易id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 87 | `financerefenceid1` | 文档中选择的财务-参考id1 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 88 | `financerefenceid2` | 文档中选择的财务-参考id2 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 89 | `doccreaterid` | 文档创建者id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 90 | `docdepartmentid` | 文档创建者所在部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 91 | `doccreatedate` | 文档创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 92 | `doccreatetime` | 文档创建时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 93 | `doclastmoduserid` | 文档最后修改者id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 94 | `doclastmoddate` | 文档最后修改时间 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 95 | `doclastmodtime` | 文档最后修改日期 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 96 | `docapproveuserid` | 文档审批者id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 97 | `docapprovedate` | 文档审批日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 98 | `docapprovetime` | 文档审批时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 99 | `docarchiveuserid` | 文档归档者id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 100 | `docarchivedate` | 文档归档日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 101 | `docarchivetime` | 文档归档时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 102 | `parentids` | 文档父节点字符串 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 103 | `assetid` | 资产id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 104 | `ownerid` | 文档拥有者id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 105 | `keyword` | 关键字 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

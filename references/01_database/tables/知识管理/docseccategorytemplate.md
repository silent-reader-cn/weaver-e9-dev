# 泛微OA 数据表: `docseccategorytemplate`

- **中文名称**: 目录模版表
- **所属模块**: `知识管理`
- **数据库表名**: `docseccategorytemplate`
- **主键**: `无`
- **字段数**: `74`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `uploadext` | 附件上传控制格式 | `varchar2` | 4000 | 是 | 否 | 否 | - | *.* | - |
| 2 | `pushoperation` | 推送设置 | `number` | (2,0) | 是 | 否 | 否 | - | 0 | - |
| 3 | `pushways` | 推送方式 | `varchar2` | 1000 | 是 | 否 | 否 | - | 0,0,0,0 | - |
| 4 | `id` | 子目录id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `name` | 目录模版名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `subcategoryid` | 分目录id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `categoryname` | 子目录名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `docmouldid` | 文档模板id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `publishable` | 是否可以发布 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 10 | `replyable` | 是否可以回复 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 11 | `shareable` | 是否可以选择共享 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 12 | `cusertype` | 具有创建权限的用户种类 | `char` | 1 | 是 | 否 | 否 | - | - | 申请人: a<br>承包商: f<br>职员: h<br>代理商: r<br>供应商: s<br>客户: c<br>学生: d<br>临时:t |
| 13 | `cuserseclevel` | 用户的安全级别 &gt;= | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `cdepartmentid1` | 可创建文档的部门1 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `cdepseclevel1` | 部门1中人员的安全级别 &gt;= | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `cdepartmentid2` | 可创建文档的部门2 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `cdepseclevel2` | 部门2中人员的安全级别 &gt;= | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `croleid1` | 可创建文档的角色1 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `crolelevel1` | 角色1中人员的级别 &gt;= | `char` | 1 | 是 | 否 | 否 | - | - | 0:部门<br>1:分部<br>2:总部 |
| 20 | `croleid2` | 可创建文档的角色2 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `crolelevel2` | 角色2中人员的级别 &gt;= | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 22 | `croleid3` | 可创建文档的角色3 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `crolelevel3` | 角色3中人员的级别 &gt;= | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 24 | `hasaccessory` | 是否允许上传附件 | `char` | 1 | 是 | 否 | 否 | - | - | 现已经不使用 |
| 25 | `accessorynum` | 最大允许附件数 | `integer` | - | 是 | 否 | 否 | - | - | 现已经不使用 |
| 26 | `hasasset` | 是否需要相关资产 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要,1：需要 |
| 27 | `assetlabel` | 相关资产标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 28 | `hasitems` | 是否需要相关物品 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要,1：需要 |
| 29 | `itemlabel` | 相关物品标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 30 | `hashrmres` | 是否需要相关人力资源信息 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要，1：需要 |
| 31 | `hrmreslabel` | 相关人力资源标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 32 | `hascrm` | 是否需要相关客户信息 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要，1：需要 |
| 33 | `crmlabel` | 相关客户标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 34 | `hasproject` | 是否需要相关项目信息 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要，1：需要 |
| 35 | `projectlabel` | 相关项目标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 36 | `hasfinance` | 是否需要相关财务信息 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要，1：需要 |
| 37 | `financelabel` | 相关财务标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 38 | `approveworkflowid` | 审批工作流 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 39 | `markable` | 是否可以打分 | `char` | 1 | 是 | 否 | 否 | - | - | 1、是；0、否 |
| 40 | `markanonymity` | 是否匿名打分 | `char` | 1 | 是 | 否 | 否 | - | - | 1、是；0、否 |
| 41 | `orderable` | 是否可以订阅 | `char` | 1 | 是 | 否 | 否 | - | (0) | 1、是；0、否 |
| 42 | `defaultlockeddoc` | 锁定查看文档 | `integer` | - | 是 | 否 | 否 | - | (0) | - |
| 43 | `allownmodimsharel` | 允许修改默认共享 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 44 | `allownmodimsharew` | （该字段暂未启用） | `integer` | - | 是 | 否 | 否 | - | - | - |
| 45 | `maxuploadfilesize` | 此目录下最大允许上传的附件的大小 | `integer` | - | 是 | 否 | 否 | - | (5) | - |
| 46 | `wordmouldid` | word模板id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 47 | `coder` | 子目录编码 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 48 | `issetshare` | 提交文档时是否弹出共享设置窗口 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 49 | `nodownload` | 禁止文档下载 | `integer` | - | 是 | 否 | 否 | - | - | 禁止对word、excel、wps、ppt类型文档的下载(存为本地文件)，对html类型文档无效，对html类型文档的附件不限制。(1、禁止,0、否) |
| 50 | `norepeatedname` | 是否允许重复 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 51 | `iscontroledbydir` | 是否受控目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 52 | `puboperation` | 发布操作 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 53 | `childdocreadremind` | 子文档阅读提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 54 | `readoptercanprint` | 允许只读操作人打印 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 55 | `editionisopen` | 启用版本管理 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 56 | `editionprefix` | 显示前缀 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 57 | `readercanviewhistoryedition` | 只读权限操作人可查看历史版本 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 58 | `isopenapprovewf` | 是否启用审批流 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 59 | `validityapprovewf` | 生效审批流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 60 | `invalidityapprovewf` | 失效效审批流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 61 | `fromdir` | 源目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 62 | `usecustomsearch` | 是否启用自定义列表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 63 | `appointedworkflowid` | 新建工作流指定流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 64 | `defaultdummycata` | 虚拟目录 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 65 | `isprintcontrol` | 是否打印控制 | `char` | 1 | 是 | 否 | 否 | - | - | 1为是，0或其他为否 |
| 66 | `printapplyworkflowid` | 打印申请流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 67 | `relationable` | 是否显示相关资源 | `char` | 1 | 是 | 否 | 否 | - | 0 | 1：显示，0或其他：不显示 |
| 68 | `maxofficedocfilesize` | office文档最大大小 | `integer` | - | 是 | 否 | 否 | - | 8 | - |
| 69 | `isopenattachment` | 单附件直接打开 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 70 | `isautoextendinfo` | 有附件时展开文档附件属性 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 71 | `isnotdelhisatt` | 删除文档时是否删除历史版本文档的附件 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 72 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 73 | `islogcontrol` | 文档阅读日志控制 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 74 | `logviewtype` | 文档日志查看类型 | `integer` | - | 是 | 否 | 否 | - | - | 0 按文档权限查看，1 按文档日志权限查看 |

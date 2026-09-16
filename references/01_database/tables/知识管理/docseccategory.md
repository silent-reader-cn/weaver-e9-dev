# 泛微OA 数据表: `docseccategory`

- **中文名称**: 文档子目录表
- **所属模块**: `知识管理`
- **数据库表名**: `docseccategory`
- **主键**: `无`
- **字段数**: `82`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `seccategorytype` | 目录类型 | `integer` | - | 否 | 否 | 否 | - | 0 | - |
| 2 | `uploadext` | 附件上传限制格式 | `varchar2` | 4000 | 是 | 否 | 否 | - | *.* | - |
| 3 | `pushoperation` | 推送操作 | `number` | (2,0) | 是 | 否 | 否 | - | 0 | - |
| 4 | `pushways` | 推送方式 | `varchar2` | 1000 | 是 | 否 | 否 | - | 0,0,0,0 | - |
| 5 | `wordmouldid` | word模板id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `coder` | 子目录编码 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 7 | `issetshare` | 提交文档时是否弹出共享设置窗口 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `nodownload` | 禁止文档下载 | `integer` | - | 是 | 否 | 否 | - | - | 禁止对word、excel、wps、ppt类型文档的下载(存为本地文件)，对html类型文档无效，对html类型文档的附件不限制。(1、禁止,0、否) |
| 9 | `norepeatedname` | 禁止文档重名 | `integer` | - | 是 | 否 | 否 | - | - | 该子目录下禁止新建和修改出重名的文档(1、禁止,0、否) |
| 10 | `iscontroledbydir` | 是否受控目录 | `integer` | - | 是 | 否 | 否 | - | - | 选中时正常状态的文档1、“生效”， 0、“正常”； |
| 11 | `puboperation` | 发布操作 | `integer` | - | 是 | 否 | 否 | - | - | 该目录下文档是否需要发布操作才能变为“生效、正常“（1、是；0、否） |
| 12 | `childdocreadremind` | 子文档阅读提醒 | `integer` | - | 是 | 否 | 否 | - | - | 当打开主文档时，是否需要弹出消息，提示查看子文档（1、是；0、否） |
| 13 | `readoptercanprint` | 允许只读操作人打印 | `integer` | - | 是 | 否 | 否 | - | - | 1、允许，0、不允许，2、由文档设置<br>允许：设置该目录下只读操作人可以打印文档；<br>不允许：设置该目录下只读操作人不可以打印文档；<br>由文档设置：该目录下只读操作人是否可以打印，由文档编辑人设置； |
| 14 | `editionisopen` | 启用版本管理 | `integer` | - | 是 | 否 | 否 | - | - | 1：启用，0：未启用 |
| 15 | `editionprefix` | 显示前缀 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 文档属性页版本字段的显示前缀 |
| 16 | `readercanviewhistoryedition` | 只读权限操作人可查看历史版本 | `integer` | - | 是 | 否 | 否 | - | - | 文档的普通查看者是否能查看文档的历史版本 |
| 17 | `isopenapprovewf` | 是否启用审批流 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 18 | `validityapprovewf` | 生效审批流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `invalidityapprovewf` | 失效效审批流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `usecustomsearch` | 是否启用自定义列表 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `appliedtemplateid` | 应用模版id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `defaultdummycata` | 此目录下的默认文档发布 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 23 | `logviewtype` | 文档日志查看类型 | `integer` | - | 是 | 否 | 否 | - | - | 0：按文档权限查看，1：仅管理员能查看 |
| 24 | `secorder` | 目录排序 | `float` | 22 | 是 | 否 | 否 | - | 0 | - |
| 25 | `appointedworkflowid` | 新建工作流指定流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `isprintcontrol` | 是否打印控制 | `char` | 1 | 是 | 否 | 否 | - | - | 1为是，0或其他为否 |
| 27 | `printapplyworkflowid` | 打印申请流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 28 | `islogcontrol` | 文档阅读日志控制 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 29 | `relationable` | 相关资源 | `char` | 1 | 是 | 否 | 否 | - | 0 | - |
| 30 | `isopenattachment` | 单附件直接打开 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 31 | `maxofficedocfilesize` | office文档最大大小 | `integer` | - | 是 | 否 | 否 | - | 8 | - |
| 32 | `isautoextendinfo` | 展开文档属性 | `integer` | - | 是 | 否 | 否 | - | 0 | 0:否，1:是 |
| 33 | `isnotdelhisatt` | 不删除历史版本附件 | `integer` | - | 是 | 否 | 否 | - | 0 | 0:删除，1:不删除 |
| 34 | `bacthdownload` | 是否禁止附件批量下载 | `integer` | - | 是 | 否 | 否 | - | 0 | 1：禁止，0或非1-允许（默认为允许） |
| 35 | `isuser` | 签发人字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 36 | `e8number` | 文号字段id | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 37 | `ecology_pinyin_search` | 查询用拼音首字母 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 38 | `parentid` | 父节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 39 | `dirid` | 目录id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 40 | `dirtype` | 目录类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 41 | `subcompanyid` | 分部 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 42 | `id` | 子目录id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 43 | `subcategoryid` | 分目录id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 44 | `categoryname` | 子目录名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 45 | `docmouldid` | 文档模板id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 46 | `publishable` | 是否可以发布 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 47 | `replyable` | 是否可以回复 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 48 | `shareable` | 是否可以选择共享 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 49 | `cusertype` | 具有创建权限的用户种类 | `char` | 1 | 是 | 否 | 否 | - | - | 申请人: a<br>承包商: f<br>职员: h<br>代理商: r<br>供应商: s<br>客户: c<br>学生: d<br>临时:t |
| 50 | `cuserseclevel` | 用户的安全级别 &gt;= | `integer` | - | 是 | 否 | 否 | - | - | - |
| 51 | `cdepartmentid1` | 可创建文档的部门1 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 52 | `cdepseclevel1` | 部门1中人员的安全级别 &gt;= | `integer` | - | 是 | 否 | 否 | - | - | - |
| 53 | `cdepartmentid2` | 可创建文档的部门2 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 54 | `cdepseclevel2` | 部门2中人员的安全级别 &gt;= | `integer` | - | 是 | 否 | 否 | - | - | - |
| 55 | `croleid1` | 可创建文档的角色1 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 56 | `crolelevel1` | 角色1中人员的级别&gt;= | `char` | 1 | 是 | 否 | 否 | - | - | 0:部门<br>1:分部<br>2:总部 |
| 57 | `croleid2` | 可创建文档的角色2 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 58 | `crolelevel2` | 角色2中人员的级别&gt;= | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 59 | `croleid3` | 可创建文档的角色3 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 60 | `crolelevel3` | 角色3中人员的级别 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 61 | `hasaccessory` | 是否允许上传附件 | `char` | 1 | 是 | 否 | 否 | - | - | 现已经不使用 |
| 62 | `accessorynum` | 最大允许附件数 | `integer` | - | 是 | 否 | 否 | - | - | 现已经不使用 |
| 63 | `hasasset` | 是否需要相关资产 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要,1：需要 |
| 64 | `assetlabel` | 相关资产标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 65 | `hasitems` | 是否需要相关物品 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要,1：需要 |
| 66 | `itemlabel` | 相关物品标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 67 | `hashrmres` | 是否需要相关人力资源信息 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要,1：需要 |
| 68 | `hrmreslabel` | 相关人力资源标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 69 | `hascrm` | 是否需要相关客户信息 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要,1：需要 |
| 70 | `crmlabel` | 相关客户标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 71 | `hasproject` | 是否需要相关项目信息 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要,1：需要 |
| 72 | `projectlabel` | 相关项目标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 73 | `hasfinance` | 是否需要相关财务信息 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不需要,1：需要 |
| 74 | `financelabel` | 相关财务标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 75 | `approveworkflowid` | 审批工作流 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 76 | `markable` | 是否可以打分 | `char` | 1 | 是 | 否 | 否 | - | - | 1、是；0、否 |
| 77 | `markanonymity` | 是否匿名打分 | `char` | 1 | 是 | 否 | 否 | - | - | 1、是；0、否 |
| 78 | `orderable` | 是否可以订阅 | `char` | 1 | 是 | 否 | 否 | - | 0 | 1、是；0、否 |
| 79 | `defaultlockeddoc` | 锁定查看文档 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 80 | `allownmodimsharel` | 允许修改默认共享 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 81 | `allownmodimsharew` | （该字段未启用） | `integer` | - | 是 | 否 | 否 | - | - | （该字段未启用） |
| 82 | `maxuploadfilesize` | 此目录下最大允许上传的附件的大小 | `integer` | - | 是 | 否 | 否 | - | 5 | - |

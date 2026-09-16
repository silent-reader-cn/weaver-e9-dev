# 核心系统表全景字典

> 泛微 OA 二次开发中最常用的核心表速查：表名、中文说明、关键字段与关联关系。
> 完整 1,699 张表见 [`tables/`](./tables/) 与 [`_INDEX.md`](./_INDEX.md)。

在泛微 OA 二次开发、报表统计及数据对接中，直接查询数据库是最常见的高性能方案。

---

## 1. 工作流引擎核心表
| 表名 | 中文说明 | 关键字段 | 关联关系 |
| :--- | :--- | :--- | :--- |
| `workflow_base` | 流程定义主表 | `id`, `workflowname`, `formid`, `isbill` | `formid` 对应单据表定义 |
| `workflow_requestbase` | 流程实例主表 | `requestid`, `workflowid`, `requestname`, `status`, `creater`, `createdate`, `currentnodetype` | 流程总入口，`currentnodetype` 0-创建,1-审批,2-实现,3-归档 |
| `workflow_currentoperator` | 流程待办/操作人表 | `requestid`, `userid`, `isremark`, `isprocessed`, `nodeid`, `viewtype` | `isremark` 0-待办, 2-已办, 4-抄送 |
| `workflow_requestLog` | 流程流转签字意见日志表 | `requestid`, `nodeid`, `operator`, `operatedate`, `operatetime`, `remark`, `logtype` | `logtype` s-提交, r-退回, j-转发, e-强制归档 |
| `workflow_bill` | 单据表定义表 | `id`, `tablename`, `namelabel` | `tablename` 即业务表表名（如 `formtable_main_10`） |
| `workflow_billfield` | 单据字段定义表 | `id`, `billid`, `fieldname`, `fieldlabel`, `fieldhtmltype`, `fielddbtype` | 字段名与中文标签定义 |

## 2. 人力资源与组织架构表
| 表名 | 中文说明 | 关键字段 | 说明 |
| :--- | :--- | :--- | :--- |
| `HrmResource` | 员工主表 | `id`, `workcode`, `lastname`, `loginid`, `departmentid`, `subcompanyid1`, `mobile`, `email`, `status`, `managerid` | `status`: 0-试用, 1-正式, 2-临时, 5-离职, 7-无效 |
| `HrmDepartment` | 部门表 | `id`, `departmentname`, `departmentcode`, `supdepid`, `subcompanyid1`, `canceled` | `supdepid` 上级部门, `canceled` 0-正常, 1-封存 |
| `HrmSubCompany` | 分部/公司表 | `id`, `subcompanyname`, `subcompanycode`, `supsubcomid`, `canceled` | 多分部/子公司架构 |
| `HrmJobTitles` | 岗位表 | `id`, `jobtitlename`, `jobtitlecode`, `jobactivityid` | 员工职务岗位 |

## 3. 知识文档与附件表
| 表名 | 中文说明 | 关键字段 | 说明 |
| :--- | :--- | :--- | :--- |
| `DocDetail` | 文档主信息表 | `id`, `docsubject`, `seccategory`, `doccreaterid`, `doccreatedate`, `docstatus` | 知识库文档 |
| `DocSecCategory` | 文档二级子目录表 | `id`, `categoryname`, `subcategoryid` | 存放文档的实际目录分类 |
| `DocImageFile` | 文档与附件关联表 | `docid`, `imagefileid`, `imagefilename` | 建立文档与物理附件的多对多映射 |
| `ImageFile` | 物理附件元数据表 | `imagefileid`, `imagefilename`, `filerealpath`, `filesize`, `imagefile` | 物理文件存储路径或 Blob |

---

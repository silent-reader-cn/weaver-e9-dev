# 表结构数据质量报告

> 本文件由 `tools/audit_tables.py` 自动生成，请勿手工编辑。

## 结论：表结构文档是**部分收录**，不是完整表结构

`tables/` 下的表结构文档来自上游数据源，**很多表只记录了升级补丁新增的列**，
缺少 `CREATE TABLE` 的基础列。直接依据这些文档编写 SQL 会出错。

**使用前请务必用以下 SQL 从真实库核对：**

```sql
SELECT column_name, data_type, data_length, nullable
FROM user_tab_columns
WHERE table_name = 'WORKFLOW_REQUESTBASE'   -- 换成你的表名（大写）
ORDER BY column_id;
```

> 另外注意：文档中的 `文档收录字段数` 是**本文件记录了几行**，
> 不等于表的真实列数。

---

## 已确证不完整的表

判定方法：本仓库的 `core_tables.md`（手写关键字段清单）或 `sql_cookbook.md`
（生产 SQL 模板）中引用了某列，但该表文档未收录 —— 说明文档必有遗漏。

| 表名 | 模块 | 文档收录字段数 | 缺失的列（被本仓库其他文档引用） | 判定依据 |
| :--- | :--- | :---: | :--- | :--- |
| [`hrmresource`](./tables/人力资源/hrmresource.md) | 人力资源 | 24 | `departmentid`、`email`、`id`、`lastname`、`loginid`、`managerid`、`mobile`、`subcompanyid1`、`workcode` | core_tables.md / sql_cookbook.md |
| [`workflow_currentoperator`](./tables/工作流程/workflow_currentoperator.md) | 工作流程 | 13 | `isprocessed`、`isremark`、`nodeid`、`receivedate`、`receivetime`、`requestid`、`userid`、`viewtype` | core_tables.md / sql_cookbook.md |
| [`workflow_requestlog`](./tables/工作流程/workflow_requestlog.md) | 工作流程 | 1 | `logid`、`logtype`、`nodeid`、`operatedate`、`operatetime`、`operator`、`remark`、`requestid` | core_tables.md / sql_cookbook.md |
| [`docdetail`](./tables/知识管理/docdetail.md) | 知识管理 | 53 | `doccontent`、`doccreatedate`、`doccreaterid`、`docsubject`、`id`、`seccategory` | core_tables.md |
| [`workflow_requestbase`](./tables/工作流程/workflow_requestbase.md) | 工作流程 | 19 | `currentnodetype`、`requestid`、`status`、`workflowid` | core_tables.md / sql_cookbook.md |
| [`docseccategory`](./tables/知识管理/docseccategory.md) | 知识管理 | 13 | `categoryname`、`id`、`subcategoryid` | core_tables.md |
| [`workflow_billfield`](./tables/工作流程/workflow_billfield.md) | 工作流程 | 7 | `type` | core_tables.md |

---

## 全库字段数分布（辅助判断）

| 文档收录字段数 | 表数量 |
| :---: | :---: |
| 1 | 16 |
| 2-5 | 578 |
| 6-10 | 627 |
| 11-20 | 337 |
| 21-40 | 94 |
| 41-80 | 24 |
| 81+ | 11 |

> 中位数仅 **7 列**。字段数极少的表**未必**都是残缺（字典表、序列表本就很小），
> 但反过来，**字段数多也不代表完整** —— 上表列出的才是已确证有遗漏的。

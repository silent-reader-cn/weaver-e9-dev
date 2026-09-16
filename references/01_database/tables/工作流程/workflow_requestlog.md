# 泛微OA 数据表: `workflow_requestlog`

> ⚠️ 表结构不完整（已确证）
>
> 本文件仅收录 **1** 个字段，缺少本表的基础列：`logid`、`logtype`、`nodeid`、`operatedate`、`operatetime`、`operator`、`remark`、`requestid`
>
> 判定依据：本仓库 `core_tables.md` 与 `sql_cookbook.md` 中明确引用了上述列，但本文档未收录。
> 说明本文档是**部分收录**（很可能只含升级补丁新增的列），**不是完整表结构**。
>
> **请勿直接依据本文档编写 SQL**。获取真实结构：
>
> ```sql
> SELECT column_name, data_type, data_length, nullable FROM user_tab_columns WHERE table_name = 'WORKFLOW_REQUESTLOG' ORDER BY column_id;
> ```
<!-- audit-warning-end -->


- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestlog`
- **文档收录字段数**: `1`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `issubmitdirect` | 退回后再提交直达本节点 | `char` | 1 | 是 | - |

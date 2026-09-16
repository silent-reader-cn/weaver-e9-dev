# 泛微OA 数据表: `workflow_billfield`

> ⚠️ 表结构不完整（已确证）
>
> 本文件仅收录 **7** 个字段，缺少本表的基础列：`type`
>
> 判定依据：本仓库 `core_tables.md` 中明确引用了上述列，但本文档未收录。
> 说明本文档是**部分收录**（很可能只含升级补丁新增的列），**不是完整表结构**。
>
> **请勿直接依据本文档编写 SQL**。获取真实结构：
>
> ```sql
> SELECT column_name, data_type, data_length, nullable FROM user_tab_columns WHERE table_name = 'WORKFLOW_BILLFIELD' ORDER BY column_id;
> ```
<!-- audit-warning-end -->


- **所属模块**: `工作流程`
- **数据库表名**: `workflow_billfield`
- **文档收录字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldshowtypes` | 显示类型 | `integer` | - | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `billid` | 单据id | `integer` | - | 是 | - |
| 4 | `fieldname` | 数据库表字段名称 | `varchar2` | 480 | 是 | - |
| 5 | `fieldlabel` | 字段显示名称 | `integer` | - | 是 | - |
| 6 | `fielddbtype` | 单据字段数据库类型 | `varchar2` | 320 | 是 | - |
| 7 | `fieldhtmltype` | 单据字段页面类型 | `char` | 1 | 是 | - |

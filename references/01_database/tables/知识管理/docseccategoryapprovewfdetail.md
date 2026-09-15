# 泛微OA 数据表: `docseccategoryapprovewfdetail`

- **所属模块**: `知识管理`
- **数据库表名**: `docseccategoryapprovewfdetail`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `seccategoryid` | 文挡子目录id | `integer` | - | 是 | - |
| 3 | `approvetype` | 审批类型 | `char` | 1 | 是 | 1:文档生效审批,2:文档失效审批 |
| 4 | `workflowid` | 审批流程 | `integer` | - | 是 | - |
| 5 | `workflowfieldid` | 审批流程字段id | `integer` | - | 是 | - |
| 6 | `docpropertyfieldid` | 文档属性页字段id | `integer` | - | 是 | - |
| 7 | `docseccategorytemplateid` | 目录模版id | `integer` | - | 是 | - |

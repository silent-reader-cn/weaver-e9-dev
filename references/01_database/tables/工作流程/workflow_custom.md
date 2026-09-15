# 泛微OA 数据表: `workflow_custom`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_custom`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `formid` | 表单/单据id | `integer` | - | 是 | - |
| 3 | `isbill` | 是否单据 | `char` | 1 | 是 | 0、否，1、是 |
| 4 | `querytypeid` | 自定义查询种类 | `integer` | - | 是 | - |
| 5 | `customname` | 自定义查询名称 | `varchar2` | 800 | 是 | - |
| 6 | `customdesc` | 自定义查询说明 | `varchar2` | 4000 | 是 | - |
| 7 | `workflowids` | 工作流程 | `varchar2` | 4000 | 是 | - |
| 8 | `subcompanyid` | 所属分部 | `integer` | - | 是 | - |

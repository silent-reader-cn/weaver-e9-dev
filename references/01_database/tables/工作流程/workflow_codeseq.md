# 泛微OA 数据表: `workflow_codeseq`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_codeseq`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `departmentid` | 部门id | `integer` | - | 是 | - |
| 3 | `yearid` | 年份id | `integer` | - | 是 | - |
| 4 | `sequenceid` | 流水号id | `integer` | - | 是 | - |
| 5 | `formid` | 表单或单据id | `integer` | - | 是 | - |
| 6 | `isbill` | 是否单据 | `char` | 1 | 是 | 1：是，0：否 |
| 7 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 8 | `monthid` | 月份id | `integer` | - | 是 | - |
| 9 | `dateid` | 日期id | `integer` | - | 是 | - |
| 10 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 11 | `fieldvalue` | 字段值 | `integer` | - | 是 | - |
| 12 | `supsubcompanyid` | 上级分部id | `integer` | - | 是 | - |
| 13 | `subcompanyid` | 分部id | `integer` | - | 是 | - |

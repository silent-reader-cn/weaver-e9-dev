# 泛微OA 数据表: `workflow_codeseqrecord`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_codeseqrecord`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `requestid` | 请求id | `integer` | - | 是 | - |
| 3 | `codeseqid` | 流程编号流水号表id | `integer` | - | 是 | - |
| 4 | `sequenceid` | 参数在sql中的位置 | `integer` | - | 是 | - |
| 5 | `codeseqreservedid` | 流程编号预留号表id | `integer` | - | 是 | - |
| 6 | `workflowcode` | 流程code | `varchar2` | 800 | 是 | - |

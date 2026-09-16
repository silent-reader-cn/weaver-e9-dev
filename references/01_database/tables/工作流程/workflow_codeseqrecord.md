# 泛微OA 数据表: `workflow_codeseqrecord`

- **中文名称**: 流程编号记录表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_codeseqrecord`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `codeseqid` | 流程编号流水号表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `sequenceid` | 参数在sql中的位置 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `codeseqreservedid` | 流程编号预留号表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `workflowcode` | 流程code | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |

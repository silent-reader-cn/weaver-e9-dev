# 泛微OA 数据表: `workflowrptcondmould`

- **所属模块**: `工作流程`
- **数据库表名**: `workflowrptcondmould`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `mouldname` | 模板名称 | `varchar2` | 1000 | 是 | - |
| 3 | `userid` | 用户id | `integer` | - | 是 | 这里只能为内部用户 |
| 4 | `reportid` | 报表id | `integer` | - | 是 | 对应workflow_report表的id字段 |

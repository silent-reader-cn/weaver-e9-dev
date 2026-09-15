# 泛微OA 数据表: `workflowplanset`

- **所属模块**: `工作流程`
- **数据库表名**: `workflowplanset`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `status` | 状态 | `char` | 1 | 是 | - |
| 3 | `frequencyt` | 流程频率 | `char` | 1 | 是 | - |
| 4 | `datetype` | 时间类型 | `char` | 1 | 是 | - |
| 5 | `datesum` | 生成日期 | `integer` | - | 是 | - |
| 6 | `timeset` | 生成时间 | `varchar2` | 64 | 是 | - |
| 7 | `alerttype` | 短信 | `char` | 1 | 是 | 1、邮件提醒；2 （2：2者都提醒） |
| 8 | `flowid` | 流程id | `integer` | - | 是 | - |

# 泛微OA 数据表: `workflow_customreport`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_customreport`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | - |
| 2 | `reportname` | 报表名称 | `varchar2` | 800 | 是 | - |
| 3 | `formid` | 表单ID | `integer` | - | 否 | - |
| 4 | `isbill` | 单据还是表单 | `char` | 2 | 否 | - |
| 5 | `workflowid` | 流程ID | `varchar2` | 1000 | 是 | - |
| 6 | `creater` | 报表创建人 | `integer` | - | 是 | - |
| 7 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 8 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 9 | `lastupdatedate` | 最后修改日期 | `char` | 10 | 是 | - |
| 10 | `lastupdatetime` | 最后修改时间 | `char` | 8 | 是 | - |

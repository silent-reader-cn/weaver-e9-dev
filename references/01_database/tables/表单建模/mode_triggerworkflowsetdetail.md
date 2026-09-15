# 泛微OA 数据表: `mode_triggerworkflowsetdetail`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_triggerworkflowsetdetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `defaultvalue` | 失败信息 | `clob` | 4000 | 是 | 记录失败信息 |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `mainid` | 数据审批主id | `integer` | - | 是 | 对应mode_triggerworkflowset表的id |
| 4 | `modefieldid` | 模块字段名称 | `integer` | - | 是 | 模块字段id，对应workflow_billfield表的id |
| 5 | `wffieldid` | 流程字段名称 | `integer` | - | 是 | 流程字段id，对应workflow_billfield表的id |

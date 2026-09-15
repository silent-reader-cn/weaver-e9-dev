# 泛微OA 数据表: `hrmperformancecheckflow`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancecheckflow`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `objid` | 对象id | `integer` | - | 是 | 对象id |
| 3 | `objtype` | 对象类型 | `char` | 1 | 是 | 对象类型 |
| 4 | `goalflowid` | 目标审批流程id | `integer` | - | 是 | 目标审批流程id |
| 5 | `planflowid` | 计划审批流程id | `integer` | - | 是 | 计划审批流程id |

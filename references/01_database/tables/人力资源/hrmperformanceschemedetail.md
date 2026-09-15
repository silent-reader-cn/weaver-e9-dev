# 泛微OA 数据表: `hrmperformanceschemedetail`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformanceschemedetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `contentid` | 考核项 | `integer` | - | 是 | 考核项 |
| 3 | `item` | 工作计划 | `integer` | - | 是 | 工作计划 |
| 4 | `checkflow` | workflow_base的id字段 | `integer` | - | 是 | workflow_base的id字段 |
| 5 | `percent_n` | 占比 | `integer` | - | 是 | 占比 |

# 泛微OA 数据表: `hrmperformanceschemedetail`

- **中文名称**: 人力资源目标考核权重表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformanceschemedetail`
- **主键**: `id`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `contentid` | 考核项 | `integer` | - | 是 | 否 | 否 | - | 0 | 考核项 |
| 3 | `item` | 工作计划 | `integer` | - | 是 | 否 | 否 | - | 0 | 工作计划 |
| 4 | `checkflow` | workflow_base的id字段 | `integer` | - | 是 | 否 | 否 | - | 0 | workflow_base的id字段 |
| 5 | `percent_n` | 占比 | `integer` | - | 是 | 否 | 否 | - | 0 | 占比 |

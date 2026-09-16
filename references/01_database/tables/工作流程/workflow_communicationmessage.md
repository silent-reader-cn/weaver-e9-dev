# 泛微OA 数据表: `workflow_communicationmessage`

- **中文名称**: 相关交流提醒表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_communicationmessage`
- **主键**: `id`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `communicationid` | 相关交流主表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `contentid` | 相关交流内容表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `reminduser` | 被提醒人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `hasread` | 被提醒人是否已读 | `integer` | - | 是 | 否 | 否 | - | - | - |

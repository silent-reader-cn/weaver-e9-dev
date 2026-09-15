# 泛微OA 数据表: `workflow_communicationmessage`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_communicationmessage`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `communicationid` | 相关交流主表id | `integer` | - | 是 | - |
| 3 | `contentid` | 相关交流内容表id | `integer` | - | 是 | - |
| 4 | `reminduser` | 被提醒人 | `integer` | - | 是 | - |
| 5 | `hasread` | 被提醒人是否已读 | `integer` | - | 是 | - |

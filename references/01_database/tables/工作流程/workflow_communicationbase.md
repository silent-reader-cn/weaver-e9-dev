# 泛微OA 数据表: `workflow_communicationbase`

- **中文名称**: 相关交流主表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_communicationbase`
- **主键**: `id`
- **字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `requestid` | requestid | `integer` | - | 是 | 是 | 否 | - | - | - |
| 3 | `workflowid` | workflowid | `integer` | - | 是 | 是 | 否 | - | - | - |
| 4 | `communicationname` | 交流名称(扩展) | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

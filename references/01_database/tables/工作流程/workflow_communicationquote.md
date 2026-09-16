# 泛微OA 数据表: `workflow_communicationquote`

- **中文名称**: 相关交流引用表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_communicationquote`
- **主键**: `id`
- **字段数**: `4`

> 说明：相关交流引用

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `communicationid` | 相关交流ID | `integer` | - | 是 | 是 | 否 | workflow_communicationbase | - | workflow_communicationbase的id |
| 3 | `quotecontent` | 引用内容ID | `integer` | - | 是 | 否 | 否 | workflow_communicationcontent | - | - |
| 4 | `bequotecontent` | 被引用内容ID | `integer` | - | 是 | 否 | 否 | workflow_communicationcontent | - | - |

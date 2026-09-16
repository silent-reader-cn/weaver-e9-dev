# 泛微OA 数据表: `govern_officialsetting`

- **中文名称**: 督查督办成文设置表
- **所属模块**: `政务督办采编`
- **数据库表名**: `govern_officialsetting`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `categoryid` | 类型id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `type` | 动作类型 | `integer` | - | 是 | 否 | 否 | - | - | 0下发、1汇报、2催办 |
| 4 | `triggertype` | 触发方式 | `integer` | - | 是 | 否 | 否 | - | - | 0自动触发 1触发公文流程 |
| 5 | `flowid` | 公文流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `attachid` | 成文模板id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `pathid` | 目录id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `isauto` | 是否自动成文 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `isbring` | 是否带入公文流程 | `integer` | - | 是 | 否 | 否 | - | - | 0否，1是 |
| 10 | `documentFiled` | 文档字段 | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表的id |

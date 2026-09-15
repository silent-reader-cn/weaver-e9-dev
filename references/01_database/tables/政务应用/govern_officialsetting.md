# 泛微OA 数据表: `govern_officialsetting`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_officialsetting`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `categoryid` | 类型id | `integer` | - | 否 | - |
| 3 | `type` | 动作类型 | `integer` | - | 是 | 0下发、1汇报、2催办 |
| 4 | `triggertype` | 触发方式 | `integer` | - | 是 | 0自动触发 1触发公文流程 |
| 5 | `flowid` | 公文流程id | `integer` | - | 是 | - |
| 6 | `attachid` | 成文模板id | `integer` | - | 是 | - |
| 7 | `pathid` | 目录id | `integer` | - | 是 | - |
| 8 | `isauto` | 是否自动成文 | `integer` | - | 是 | - |
| 9 | `isbring` | 是否带入公文流程 | `integer` | - | 是 | 0否，1是 |
| 10 | `documentFiled` | 文档字段 | `integer` | - | 是 | 对应workflow_billfield表的id |

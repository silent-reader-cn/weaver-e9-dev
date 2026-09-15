# 泛微OA 数据表: `govern_actionsetting`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_actionsetting`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `categoryid` | 类型id | `integer` | - | 否 | - |
| 3 | `actiontype` | 动作类型 | `integer` | - | 是 | 0新建、1汇报、2分解、3催办、4变更 |
| 4 | `triggertype` | 触发方式 | `integer` | - | 是 | 0卡片触发、1触发流程 |
| 5 | `flowid` | 触发流程的流程id | `integer` | - | 是 | - |
| 6 | `detailtableid` | 分解动作明细表id | `integer` | - | 是 | - |

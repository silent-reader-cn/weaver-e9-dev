# 泛微OA 数据表: `govern_actionconfig`

- **中文名称**: 督查督办动作设置配置表
- **所属模块**: `政务督办采编`
- **数据库表名**: `govern_actionconfig`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `categoryid` | 类型id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `actiontype` | 动作类型 | `integer` | - | 是 | 否 | 否 | - | - | 0新建、1汇报、2分解、3催办、4变更 |
| 4 | `actionsetid` | action id | `integer` | - | 是 | 否 | 否 | - | - | workflowactionset表id |
| 5 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `istriggerreject` | 退回是否触发 | `integer` | - | 是 | 否 | 否 | - | - | 0不触发，1触发 |
| 7 | `ispreoperator` | 执行方式 | `integer` | - | 是 | 否 | 否 | - | - | 1：节点前 0：节点后 |
| 8 | `nodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `govern_actionconfig`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_actionconfig`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `categoryid` | 类型id | `integer` | - | 否 | - |
| 3 | `actiontype` | 动作类型 | `integer` | - | 是 | 0新建、1汇报、2分解、3催办、4变更 |
| 4 | `actionsetid` | action id | `integer` | - | 是 | workflowactionset表id |
| 5 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 6 | `istriggerreject` | 退回是否触发 | `integer` | - | 是 | 0不触发，1触发 |
| 7 | `ispreoperator` | 执行方式 | `integer` | - | 是 | 1：节点前 0：节点后 |
| 8 | `nodeid` | 节点id | `integer` | - | 是 | - |

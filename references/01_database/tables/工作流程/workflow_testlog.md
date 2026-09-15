# 泛微OA 数据表: `workflow_testlog`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_testlog`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 日志ID | `integer` | - | 否 | - |
| 2 | `requestid` | 请求ID | `integer` | - | 是 | - |
| 3 | `workflowid` | 流程ID | `integer` | - | 是 | - |
| 4 | `testtime` | 测试时间 | `char` | 20 | 是 | - |
| 5 | `fileid` | 字段ID | `integer` | - | 是 | - |
| 6 | `tester` | 测试串 | `integer` | - | 是 | - |

# 泛微OA 数据表: `workflow_approveerrorlog`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_approveerrorlog`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `requestid` | 请求ID | `integer` | - | 否 | - |
| 2 | `nodeid` | 节点ID | `integer` | - | 否 | - |
| 3 | `operator` | 操作人 | `integer` | - | 否 | - |
| 4 | `errorremark` | 提交报错messagecontent内容 | `clob` | 4000 | 是 | - |

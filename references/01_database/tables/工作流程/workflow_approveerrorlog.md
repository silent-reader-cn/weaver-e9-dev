# 泛微OA 数据表: `workflow_approveerrorlog`

- **中文名称**: 流程自动批准异常日志
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_approveerrorlog`
- **主键**: `requestid + nodeid`
- **字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `requestid` | 请求ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `nodeid` | 节点ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `operator` | 操作人 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `errorremark` | 提交报错messagecontent内容 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `workflow_approvelog`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_approvelog`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `requestid` | 请求ID | `integer` | - | 否 | - |
| 2 | `nodeid` | 节点ID | `integer` | - | 否 | - |
| 3 | `operator` | 操作者 | `integer` | - | 否 | - |
| 4 | `remark` | 意见内容 | `clob` | 4000 | 是 | - |
| 5 | `logdate` | 记录日期 | `varchar2` | 80 | 是 | - |
| 6 | `logtime` | 记录时间 | `varchar2` | 64 | 是 | - |

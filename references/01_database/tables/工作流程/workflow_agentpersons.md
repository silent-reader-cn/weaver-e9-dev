# 泛微OA 数据表: `workflow_agentpersons`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_agentpersons`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `requestid` | 请求id | `integer` | - | 是 | - |
| 2 | `receivedpersons` | 依次会签的操作人id | `varchar2` | 1000 | 是 | - |
| 3 | `groupdetailid` | 操作组实际i | `integer` | - | 是 | - |
| 4 | `coadjutants` | 依次会签的协办人id | `varchar2` | 1000 | 是 | - |

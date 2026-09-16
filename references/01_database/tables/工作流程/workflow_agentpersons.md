# 泛微OA 数据表: `workflow_agentpersons`

- **中文名称**: 存放当前节点未操作的，并且是依次会签的操作人
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_agentpersons`
- **主键**: `groupdetailid`
- **字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `receivedpersons` | 依次会签的操作人id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `groupdetailid` | 操作组实际i | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `coadjutants` | 依次会签的协办人id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

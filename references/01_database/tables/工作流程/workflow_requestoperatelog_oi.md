# 泛微OA 数据表: `workflow_requestoperatelog_oi`

- **中文名称**: 流程操作日志详细记录其他信息表)
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestoperatelog_oi`
- **主键**: `无`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `optlogid` | 操作日志主表（workflow_requestoperatelog）id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `entitytype` | 实体表 | `integer` | - | 是 | 否 | 否 | - | - | 本条信息是哪张表<br>1：workflow_currentoperator<br>2：workflow_requestlog<br>3：workflow_agentpersons<br>4：workflow_requestbase |
| 4 | `entityid` | 实体表主键值（id） | `integer` | - | 是 | 否 | 否 | - | - | 记录修改/新增/删除表的主键id |
| 5 | `count` | 数量 | `integer` | - | 是 | 否 | 否 | - | - | - |

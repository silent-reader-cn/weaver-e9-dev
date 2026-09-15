# 泛微OA 数据表: `workflow_nodegroup`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodegroup`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 3 | `groupname` | 节点操作者组名称 | `varchar2` | 480 | 是 | - |
| 4 | `canview` | 是否可跟踪 | `integer` | - | 是 | 0：否，1：是 |

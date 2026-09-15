# 泛微OA 数据表: `workflow_nodebase`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodebase`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `drawstyle` | 流程图样式 | `varchar2` | 1000 | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `nodename` | 节点名称 | `varchar2` | 480 | 是 | - |
| 4 | `isstart` | 当前节点是否为创建节点 | `char` | 1 | 是 | 0：否，1：是 |
| 5 | `isreject` | 当前节点是否可以退回 | `char` | 1 | 是 | 0：否，1：是 |
| 6 | `isreopen` | 是否重新打开 | `char` | 1 | 是 | - |
| 7 | `isend` | 是否为归档节点 | `char` | 1 | 是 | 0：否，1：是 |
| 8 | `drawxpos` | 节点图形显示横坐标 | `integer` | - | 是 | - |
| 9 | `drawypos` | 节点图形显示纵坐标 | `integer` | - | 是 | - |
| 10 | `totalgroups` | 当前节点操作者组总数 | `integer` | - | 是 | - |
| 11 | `nodeattribute` | 节点属性 | `char` | 1 | 是 | - |

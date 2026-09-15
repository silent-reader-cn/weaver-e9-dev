# 泛微OA 数据表: `workflowactionset`

- **所属模块**: `工作流程`
- **数据库表名**: `workflowactionset`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `drawbackflag` | 退回时触发 | `integer` | - | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `actionname` | action名称 | `varchar2` | 2000 | 是 | - |
| 4 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 5 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 6 | `nodelinkid` | 出口id | `integer` | - | 是 | - |
| 7 | `ispreoperator` | 节点前后判断 | `integer` | - | 是 | 0：节点后；1：节点前 |
| 8 | `actionorder` | action顺序 | `integer` | - | 是 | - |
| 9 | `interfacetype` | 接口类型 | `integer` | - | 是 | - |
| 10 | `typename` | 类型名称 | `varchar2` | 800 | 是 | - |
| 11 | `interfaceid` | 接口id | `varchar2` | 2000 | 是 | - |
| 12 | `isused` | 是否启用 | `integer` | - | 是 | - |

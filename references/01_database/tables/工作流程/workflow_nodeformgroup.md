# 泛微OA 数据表: `workflow_nodeformgroup`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodeformgroup`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 2 | `groupid` | 组id | `integer` | - | 是 | - |
| 3 | `isadd` | 是否允许新增明细 | `char` | 1 | 是 | - |
| 4 | `isedit` | 是否允许修改已有明细 | `char` | 1 | 是 | - |
| 5 | `isdelete` | 是否允许删除已有明细 | `char` | 1 | 是 | - |
| 6 | `ishidenull` | 是否是否打印空明细 | `char` | 1 | 是 | - |
| 7 | `isdefault` | 是否新增默认空明细 | `char` | 1 | 是 | - |
| 8 | `isneed` | 必须新增明细 | `char` | 1 | 是 | - |
| 9 | `isopensapmul` | 是否开启sap集成多选浏览按钮 | `char` | 1 | 是 | - |
| 10 | `defaultrows` | 默认行数 | `integer` | - | 是 | - |
| 11 | `isprintserial` | 是否连续打印 | `char` | 1 | 是 | - |
| 12 | `allowscroll` | 是否允许滚动 | `char` | 1 | 是 | - |

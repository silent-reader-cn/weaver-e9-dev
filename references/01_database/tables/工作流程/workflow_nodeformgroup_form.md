# 泛微OA 数据表: `workflow_nodeformgroup_form`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodeformgroup_form`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `formid` | 表单id | `integer` | - | 是 | - |
| 2 | `isbill` | 是否是单据 | `integer` | - | 是 | - |
| 3 | `groupid` | 组id | `integer` | - | 是 | - |
| 4 | `isadd` | 是否允许新增已有明细 | `char` | 1 | 是 | - |
| 5 | `isedit` | 是否允许修改已有明细 | `char` | 1 | 是 | - |
| 6 | `isdelete` | 是否允许删除已有明细 | `char` | 1 | 是 | - |
| 7 | `ishidenull` | 是否打印空明细 | `char` | 1 | 是 | - |
| 8 | `isdefault` | 是否新增默认空明细 | `char` | 1 | 是 | - |
| 9 | `isneed` | 必须新增明细 | `char` | 1 | 是 | - |
| 10 | `isopensapmul` | 是否开启sap集成多选按钮 | `char` | 1 | 是 | - |
| 11 | `defaultrows` | 默认行数 | `integer` | - | 是 | - |
| 12 | `isprintserial` | 是否连续打印 | `char` | 1 | 是 | - |
| 13 | `allowscroll` | 是否允许滚动 | `char` | 1 | 是 | - |

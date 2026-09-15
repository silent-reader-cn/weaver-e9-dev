# 泛微OA 数据表: `workflow_groupinfo`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_groupinfo`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 3 | `groupname` | 组名称 | `varchar2` | 1000 | 是 | - |
| 4 | `direction` | 发生额方向 | `integer` | - | 是 | &nbsp; |
| 5 | `x` | x方向 | `number` | (15,2) | 是 | - |
| 6 | `y` | y方向 | `number` | (15,2) | 是 | - |
| 7 | `width` | 宽度 | `number` | (15,2) | 是 | - |
| 8 | `height` | 高度 | `number` | (15,2) | 是 | - |

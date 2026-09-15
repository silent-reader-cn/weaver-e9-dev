# 泛微OA 数据表: `workflow_createflowset`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_createflowset`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 3 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 4 | `fieldid` | 字段id | `varchar2` | 800 | 是 | - |
| 5 | `targetfieldid` | 目标字段id | `varchar2` | 800 | 是 | - |
| 6 | `nodecustomid` | 菜单id | `integer` | - | 是 | - |

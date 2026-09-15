# 泛微OA 数据表: `workflow_nodemode`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodemode`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 3 | `formid` | 表单id | `integer` | - | 是 | - |
| 4 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 5 | `isprint` | 是否打印模板 | `varchar2` | 8 | 是 | - |
| 6 | `modename` | 模块名称 | `varchar2` | 1000 | 是 | - |
| 7 | `modedesc` | 模块描述 | `clob` | 4000 | 是 | - |

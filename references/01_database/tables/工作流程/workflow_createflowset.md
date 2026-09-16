# 泛微OA 数据表: `workflow_createflowset`

- **中文名称**: 自定义创建流程设置表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_createflowset`
- **主键**: `id`
- **字段数**: `6`

> 说明：创建流程设置

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `nodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `fieldid` | 字段id | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 5 | `targetfieldid` | 目标字段id | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 6 | `nodecustomid` | 菜单id | `integer` | - | 是 | 否 | 否 | - | - | - |

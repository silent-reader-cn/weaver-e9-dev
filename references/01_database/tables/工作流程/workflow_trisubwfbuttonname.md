# 泛微OA 数据表: `workflow_trisubwfbuttonname`

- **中文名称**: 手动触发子流程自定义按钮表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_trisubwfbuttonname`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | 是 | 否 | workflow_base | - | - |
| 3 | `nodeid` | 节点id | `integer` | - | 是 | 是 | 否 | workflow_nodebase | - | - |
| 4 | `subwfsettablename` | 设置表名称 | `varchar2` | 30 | 是 | 否 | 否 | - | - | - |
| 5 | `subwfsetid` | 设置表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `trisubwfname7` | 中文名称 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 7 | `trisubwfname8` | 英文名称 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 8 | `trisubwfname9` | 繁体名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

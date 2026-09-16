# 泛微OA 数据表: `workflow_monitor_dt_wfid`

- **中文名称**: 流程前台监控数据表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_monitor_dt_wfid`
- **主键**: `id`
- **字段数**: `7`

> 说明：* 处理 workflow_monitor_info、workflow_monitor_detail、Workflow_VersionInfo数据 * 将三个表的数据进行整合到新表 WORKFLOW_MONITOR_DT_WFID 中。

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `infoid` | 主表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `objtype` | 监控类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `objvalue` | 监控类型值 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `scopetype` | 监控范围类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `scopevalue` | 监控范围数据 | `integer` | - | 是 | 否 | 否 | - | - | - |

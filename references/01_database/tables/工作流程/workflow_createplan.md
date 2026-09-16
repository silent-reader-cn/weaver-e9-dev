# 泛微OA 数据表: `workflow_createplan`

- **中文名称**: 流程转日程主表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_createplan`
- **主键**: `id`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `wfid` | 工作流id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `nodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `changetime` | 转换时间 | `integer` | - | 是 | 否 | 否 | - | - | 1：到达节点，2：离开节点 |
| 5 | `plantypeid` | 日程类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `creatertype` | 日程提交人类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：流程创建人，2：流程人力资源字段 |
| 7 | `wffieldid` | 所选择的流程人力资源字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `remindbeforestart` | 是否开始前提醒 | `integer` | - | 是 | 否 | 否 | - | - | 1、是 |
| 9 | `reminddatebeforestart` | 开始前提醒提前小时数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `remindtimebeforestart` | 开始前提醒提前分钟数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `remindbeforeend` | 是否结束前提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `reminddatebeforeend` | 结束前提醒提前小时数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `remindtimebeforeend` | 开始前提醒提前分钟数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `changemode` | 转化模式 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `remindtype` | 日程默认提醒类型 | `char` | 10 | 是 | 否 | 否 | - | - | 1：不提醒<br>2：短信提醒<br>3：邮件提醒 |

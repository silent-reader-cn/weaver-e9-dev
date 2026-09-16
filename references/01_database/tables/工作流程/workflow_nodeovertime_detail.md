# 泛微OA 数据表: `workflow_nodeovertime_detail`

- **中文名称**: 新超时提醒表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodeovertime_detail`
- **主键**: `id`
- **字段数**: `21`

> 说明：新超时逻辑，存储提醒的表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | 主键 | - | - |
| 2 | `workflowid` | 流程id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `nodeid` | 节点id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `remindName` | 提醒名称 | `varchar2` | - | 否 | 否 | 否 | - | - | - |
| 5 | `remindType` | 提醒类型 | `integer` | - | 否 | 否 | 否 | - | - | 0：超时前提醒 1：超时后提醒 |
| 6 | `remindHour` | 多少小时提醒 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 7 | `remindMinute` | 多少分钟提醒 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 8 | `repeatremind` | 是否重复提醒 | `integer` | - | 否 | 否 | 否 | - | - | 1：开启 |
| 9 | `repeatHour` | 多少小时再次提醒 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 10 | `repeatMinute` | 多少分钟再次提醒 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 11 | `flowremind` | 自定义流程提醒 | `char` | - | 否 | 否 | 否 | - | - | 1：开启 |
| 12 | `msgremind` | 短信提醒 | `char` | - | 否 | 否 | 否 | - | - | 1：开启 |
| 13 | `mailremind` | 邮件提醒 | `char` | - | 否 | 否 | 否 | - | - | 1：开启 |
| 14 | `infocenterremind` | 信息中心提醒 | `char` | - | 否 | 否 | 否 | - | - | 1：开启 |
| 15 | `chatsremind` | 微信提醒 | `char` | - | 否 | 否 | 否 | - | - | e9-新超时已屏蔽此提醒 1：开启 |
| 16 | `customWorkflowid` | 自定义提醒流程id | `integer` | - | 否 | 否 | 否 | - | - | 1：开启 |
| 17 | `iscreater` | 提醒人是否为流程创建者 | `char` | - | 否 | 否 | 否 | - | - | 1：是 |
| 18 | `isnodeoperator` | 提醒人是否为节点操作者 | `char` | - | 否 | 否 | 否 | - | - | 1：是 |
| 19 | `ismanager` | 提醒人是否为节点操作者经理 | `char` | - | 否 | 否 | 否 | - | - | 1：是 |
| 20 | `isother` | 提醒人是否指定其他人 | `char` | - | 否 | 否 | 否 | - | - | 1：是 |
| 21 | `REMINDOBJECTIDS` | 提醒人指定的其他人id | `varchar2` | - | 否 | 否 | 否 | - | - | 多个人，用，分开 |

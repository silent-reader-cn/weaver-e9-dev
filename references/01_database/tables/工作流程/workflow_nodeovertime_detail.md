# 泛微OA 数据表: `workflow_nodeovertime_detail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodeovertime_detail`
- **文档收录字段数**: `21`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | - | - |
| 2 | `workflowid` | 流程id | `integer` | - | - | - |
| 3 | `nodeid` | 节点id | `integer` | - | - | - |
| 4 | `remindName` | 提醒名称 | `varchar2` | - | - | - |
| 5 | `remindType` | 提醒类型 | `integer` | - | - | 0：超时前提醒   1：超时后提醒 |
| 6 | `remindHour` | 多少小时提醒 | `integer` | - | - | - |
| 7 | `remindMinute` | 多少分钟提醒 | `integer` | - | - | - |
| 8 | `repeatremind` | 是否重复提醒 | `integer` | - | - | 1：开启 |
| 9 | `repeatHour` | 多少小时再次提醒 | `integer` | - | - | - |
| 10 | `repeatMinute` | 多少分钟再次提醒 | `integer` | - | - | - |
| 11 | `flowremind` | 自定义流程提醒 | `char` | - | - | 1：开启 |
| 12 | `msgremind` | 短信提醒 | `char` | - | - | 1：开启 |
| 13 | `mailremind` | 邮件提醒 | `char` | - | - | 1：开启 |
| 14 | `infocenterremind` | 信息中心提醒 | `char` | - | - | 1：开启 |
| 15 | `chatsremind` | 微信提醒 | `char` | - | - | e9-新超时已屏蔽此提醒  1：开启 |
| 16 | `customWorkflowid` | 自定义提醒流程id | `integer` | - | - | 1：开启 |
| 17 | `iscreater` | 提醒人是否为流程创建者 | `char` | - | - | 1：是 |
| 18 | `isnodeoperator` | 提醒人是否为节点操作者 | `char` | - | - | 1：是 |
| 19 | `ismanager` | 提醒人是否为节点操作者经理 | `char` | - | - | 1：是 |
| 20 | `isother` | 提醒人是否指定其他人 | `char` | - | - | 1：是 |
| 21 | `REMINDOBJECTIDS` | 提醒人指定的其他人id | `varchar2` | - | - | 多个人，用，分开 |

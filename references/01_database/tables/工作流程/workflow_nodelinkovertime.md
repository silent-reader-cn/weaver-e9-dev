# 泛微OA 数据表: `workflow_nodelinkovertime`

- **中文名称**: 工作流节点出口超时提醒信息表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodelinkovertime`
- **主键**: `id`
- **字段数**: `21`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `linkid` | 出口id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `workflowid` | 工作流id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `remindname` | 提醒名称 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `remindtype` | 提醒类型 | `integer` | - | 是 | 否 | 否 | - | - | 0：超时前提醒，1：超时后提醒 |
| 6 | `remindhour` | 提醒小时 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `remindminute` | 提醒分钟 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `repeatremind` | 重复提醒 | `integer` | - | 是 | 否 | 否 | - | - | 1：是，其他：不是 |
| 9 | `repeathour` | 重复提醒小时 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `repeatminute` | 重复提醒分钟 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `flowremind` | 信息中心提醒 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 12 | `msgremind` | 短信提醒 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 13 | `mailremind` | 邮件提醒 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 14 | `chatsremind` | 微信提醒 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 15 | `infocentreremind` | 自定义流程提醒 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 16 | `customworkflowid` | 自定义提醒流程 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `isnodeoperator` | 提醒本节点操作人 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 18 | `iscreater` | 提醒创建人 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 19 | `ismanager` | 提醒本节点操作人经理 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 20 | `isother` | 提醒指定对象 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 21 | `remindobjectids` | 提醒的指定对象 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

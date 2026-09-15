# 泛微OA 数据表: `workflow_nodelinkovertime`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodelinkovertime`
- **字段总数**: `21`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `linkid` | 出口id | `integer` | - | 是 | - |
| 3 | `workflowid` | 工作流id | `integer` | - | 是 | - |
| 4 | `remindname` | 提醒名称 | `varchar2` | 4000 | 是 | - |
| 5 | `remindtype` | 提醒类型 | `integer` | - | 是 | 0：超时前提醒，1：超时后提醒 |
| 6 | `remindhour` | 提醒小时 | `integer` | - | 是 | - |
| 7 | `remindminute` | 提醒分钟 | `integer` | - | 是 | - |
| 8 | `repeatremind` | 重复提醒 | `integer` | - | 是 | 1：是，其他：不是 |
| 9 | `repeathour` | 重复提醒小时 | `integer` | - | 是 | - |
| 10 | `repeatminute` | 重复提醒分钟 | `integer` | - | 是 | - |
| 11 | `flowremind` | 信息中心提醒 | `char` | 1 | 是 | - |
| 12 | `msgremind` | 短信提醒 | `char` | 1 | 是 | - |
| 13 | `mailremind` | 邮件提醒 | `char` | 1 | 是 | - |
| 14 | `chatsremind` | 微信提醒 | `char` | 1 | 是 | - |
| 15 | `infocentreremind` | 自定义流程提醒 | `char` | 1 | 是 | - |
| 16 | `customworkflowid` | 自定义提醒流程 | `integer` | - | 是 | - |
| 17 | `isnodeoperator` | 提醒本节点操作人 | `char` | 1 | 是 | - |
| 18 | `iscreater` | 提醒创建人 | `char` | 1 | 是 | - |
| 19 | `ismanager` | 提醒本节点操作人经理 | `char` | 1 | 是 | - |
| 20 | `isother` | 提醒指定对象 | `char` | 1 | 是 | - |
| 21 | `remindobjectids` | 提醒的指定对象 | `varchar2` | 4000 | 是 | - |

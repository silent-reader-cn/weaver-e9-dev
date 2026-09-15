# 泛微OA 数据表: `workflow_nodecustomnewmenu`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodecustomnewmenu`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `newcustommessage` | 自定义消息 | `varchar2` | 4000 | 是 | - |
| 2 | `orderid` | 排序 | `integer` | - | 是 | - |
| 3 | `id` | ID | `integer` | - | 否 | - |
| 4 | `wfid` | 工作流id | `integer` | - | 否 | - |
| 5 | `nodeid` | 节点id | `integer` | - | 否 | - |
| 6 | `menutype` | 菜单类型 | `integer` | - | 是 | 0，新建流程；1，新建短信；2，新建微信 |
| 7 | `enable` | 是否启用 | `integer` | - | 是 | 1，启用；其他，不启用 |
| 8 | `newname7` | 自定义菜单中文名称 | `varchar2` | 4000 | 是 | - |
| 9 | `newname8` | 自定义菜单英文名称 | `varchar2` | 4000 | 是 | - |
| 10 | `newname9` | 自定义菜单繁体名称 | `varchar2` | 4000 | 是 | - |
| 11 | `workflowid` | 新建流程的工作流id | `integer` | - | 是 | - |
| 12 | `custommessage` | 新建短信/新建微信的用户自定义内容 | `varchar2` | 4000 | 是 | - |
| 13 | `fieldid` | 新建短信/新建微信的内容字段 | `integer` | - | 是 | - |
| 14 | `usecustomsender` | 新建短信启用自定义落款 | `char` | 1 | 是 | 1，启用 |

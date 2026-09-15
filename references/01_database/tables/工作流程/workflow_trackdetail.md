# 泛微OA 数据表: `workflow_trackdetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_trackdetail`
- **字段总数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `sn` | sn | `integer` | - | 是 | - |
| 3 | `optkind` | 日志操作类型 | `varchar2` | 160 | 是 | - |
| 4 | `opttype` | 日志操作类型 | `integer` | - | 是 | 1:新增;2:修改;3:删除 |
| 5 | `requestid` | 请求对应的id | `integer` | - | 是 | - |
| 6 | `nodeid` | 节点名称 | `integer` | - | 是 | - |
| 7 | `isbill` | 是否是单据 | `integer` | - | 是 | 0:表单,1:单据 |
| 8 | `fieldlableid` | 单据用的leable | `integer` | - | 是 | - |
| 9 | `fieldgroupid` | 明细组id | `integer` | - | 是 | - |
| 10 | `fieldid` | 修改字段对应的id | `integer` | - | 是 | - |
| 11 | `fieldhtmltype` | 修改字段的浏览类型 | `char` | 1 | 是 | - |
| 12 | `fieldtype` | 修改字段的类型 | `varchar2` | 320 | 是 | - |
| 13 | `fieldnamecn` | 修改字段的中文名称 | `varchar2` | 800 | 是 | - |
| 14 | `fieldnameen` | 修改字段的英文名称 | `varchar2` | 800 | 是 | - |
| 15 | `fieldoldtext` | 修改字段的原内容 | `varchar2` | 4000 | 是 | - |
| 16 | `fieldnewtext` | 修改字段的新内容 | `varchar2` | 4000 | 是 | - |
| 17 | `modifiertype` | 修改人类型 | `integer` | - | 是 | - |
| 18 | `agentid` | 代理人 | `integer` | - | 是 | -1：表示流程无代理 |
| 19 | `modifierid` | 修改人对应的id | `integer` | - | 是 | - |
| 20 | `modifierip` | 修改人的ip地址 | `varchar2` | 160 | 是 | - |
| 21 | `modifytime` | 修改人时间 | `varchar2` | 160 | 是 | - |
| 22 | `fieldnametw` | 修改字段的繁体名称 | `varchar2` | 800 | 是 | - |

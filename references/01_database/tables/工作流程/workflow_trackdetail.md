# 泛微OA 数据表: `workflow_trackdetail`

- **中文名称**: 工作流表单明细字段修改日志表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_trackdetail`
- **主键**: `id`
- **字段数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `sn` | sn | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `optkind` | 日志操作类型 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 4 | `opttype` | 日志操作类型 | `integer` | - | 是 | 否 | 否 | - | - | 1:新增;2:修改;3:删除 |
| 5 | `requestid` | 请求对应的id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `nodeid` | 节点名称 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `isbill` | 是否是单据 | `integer` | - | 是 | 否 | 否 | - | - | 0:表单,1:单据 |
| 8 | `fieldlableid` | 单据用的leable | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `fieldgroupid` | 明细组id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `fieldid` | 修改字段对应的id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `fieldhtmltype` | 修改字段的浏览类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 12 | `fieldtype` | 修改字段的类型 | `varchar2` | 320 | 是 | 否 | 否 | - | - | - |
| 13 | `fieldnamecn` | 修改字段的中文名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 14 | `fieldnameen` | 修改字段的英文名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 15 | `fieldoldtext` | 修改字段的原内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 16 | `fieldnewtext` | 修改字段的新内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 17 | `modifiertype` | 修改人类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `agentid` | 代理人 | `integer` | - | 是 | 否 | 否 | - | -1 | -1：表示流程无代理 |
| 19 | `modifierid` | 修改人对应的id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `modifierip` | 修改人的ip地址 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 21 | `modifytime` | 修改人时间 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 22 | `fieldnametw` | 修改字段的繁体名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `workflow_track`

- **中文名称**: 工作流表单主字段修改日志表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_track`
- **主键**: `id`
- **字段数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `optkind` | 日志操作类型 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 3 | `requestid` | 请求对应的id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `nodeid` | 节点名称 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `isbill` | 是否是单据 | `integer` | - | 是 | 否 | 否 | - | - | 0:表单，1:单据 |
| 6 | `fieldlableid` | 单据用的leable | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `fieldid` | 修改字段对应的id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `fieldhtmltype` | 修改字段的浏览类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 9 | `fieldtype` | 修改字段的类型 | `varchar2` | 320 | 是 | 否 | 否 | - | - | - |
| 10 | `fieldnamecn` | 修改字段的中文名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 11 | `fieldnameen` | 修改字段的英文名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 12 | `fieldoldtext` | 修改字段的原内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 13 | `fieldnewtext` | 修改字段的新内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 14 | `modifiertype` | 修改人类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `agentid` | 代理人 | `integer` | - | 是 | 否 | 否 | - | -1 | -1：表示流程无代理 |
| 16 | `modifierid` | 修改人对应的id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `modifierip` | 修改人的ip地址 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 18 | `modifytime` | 修改人时间 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 19 | `fieldnametw` | 修改字段的繁体名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |

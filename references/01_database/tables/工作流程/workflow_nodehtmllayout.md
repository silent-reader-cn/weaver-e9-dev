# 泛微OA 数据表: `workflow_nodehtmllayout`

- **中文名称**: 工作流Html模式模板信息表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodehtmllayout`
- **主键**: `id`
- **字段数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `scriptstr` | e9代码块 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 2 | `stylestr` | e9样式块 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 3 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `formid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `isbill` | 是否单据 | `integer` | - | 是 | 否 | 否 | - | - | 1、是，0、否 |
| 7 | `nodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `type` | 模板类型 | `integer` | - | 是 | 否 | 否 | - | - | 0：编辑模板，1：打印模板 |
| 9 | `layoutname` | 模板名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 10 | `syspath` | 模板在服务器上存储路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `cssfile` | 模板关联的css文件id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `htmlparsescheme` | html解析模板 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `version` | 版本 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 14 | `operuser` | 操作者 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `opertime` | 操作时间 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 16 | `datajson` | 日期json数据 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 17 | `pluginjson` | 插件json数据 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 18 | `scripts` | 脚本 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 19 | `isactive` | 是否活动版本 | `integer` | - | 是 | 否 | 否 | - | - | - |

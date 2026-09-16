# 泛微OA 数据表: `wf_fna_wnhl_imp`

- **中文名称**: 预算流程初始化定义表-workflow_nodehtmllayout
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_wnhl_imp`
- **主键**: `workflow_nodehtmllayout表对应字段`
- **字段数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `impguid1` | workflow_nodehtmllayout表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 2 | `id` | workflow_nodehtmllayout表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `workflowid` | workflow_nodehtmllayout表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `formid` | workflow_nodehtmllayout表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `isbill` | workflow_nodehtmllayout表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `nodeid` | workflow_nodehtmllayout表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `type` | workflow_nodehtmllayout表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `layoutname` | workflow_nodehtmllayout表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `syspath` | workflow_nodehtmllayout表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `cssfile` | workflow_nodehtmllayout表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `htmlparsescheme` | workflow_nodehtmllayout表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `version` | workflow_nodehtmllayout表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `operuser` | workflow_nodehtmllayout表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `opertime` | workflow_nodehtmllayout表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 15 | `datajson` | workflow_nodehtmllayout表对应字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 16 | `pluginjson` | workflow_nodehtmllayout表对应字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 17 | `scripts` | workflow_nodehtmllayout表对应字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 18 | `isactive` | workflow_nodehtmllayout表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |

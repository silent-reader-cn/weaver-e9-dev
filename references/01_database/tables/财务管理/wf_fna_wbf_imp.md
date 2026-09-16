# 泛微OA 数据表: `wf_fna_wbf_imp`

- **中文名称**: 预算流程初始化定义表-workflow_billfield
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_wbf_imp`
- **主键**: `workflow_billfield表对应字段`
- **字段数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `billid` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `fieldname` | workflow_billfield表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `fieldlabel` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `fielddbtype` | workflow_billfield表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `fieldhtmltype` | workflow_billfield表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `type` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `viewtype` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `detailtable` | workflow_billfield表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `fromuser` | workflow_billfield表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `textheight` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `dsporder` | workflow_billfield表对应字段 | `number` | (20,5) | 是 | 否 | 否 | - | - | - |
| 13 | `childfieldid` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `imgheight` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `imgwidth` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `places` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `qfws` | workflow_billfield表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 18 | `textheight_2` | workflow_billfield表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 19 | `selectitem` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `linkfield` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `selectitemtype` | workflow_billfield表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 22 | `pubchoiceid` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `pubchilchoiceid` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `statelev` | workflow_billfield表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `locatetype` | workflow_billfield表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 26 | `impguid1` | workflow_billfield表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |

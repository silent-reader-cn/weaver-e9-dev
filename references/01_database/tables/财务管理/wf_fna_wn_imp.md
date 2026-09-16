# 泛微OA 数据表: `wf_fna_wn_imp`

- **中文名称**: 预算流程初始化定义表-workflow_nodebase
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_wn_imp`
- **主键**: `workflow_nodebase表对应字段`
- **字段数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `impguid1` | workflow_nodebase表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 2 | `operators_1` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 3 | `requestid` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `startnodeid` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `operators` | workflow_nodebase表对应字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `ecology_pinyin_search` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `id` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `nodename` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `isstart` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `isreject` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `isreopen` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 12 | `isend` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 13 | `drawxpos` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `drawypos` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `totalgroups` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `nodeattribute` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 17 | `passnum` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `isfreenode` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 19 | `floworder` | workflow_nodebase表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `signtype` | workflow_nodebase表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

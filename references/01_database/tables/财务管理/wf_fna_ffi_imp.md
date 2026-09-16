# 泛微OA 数据表: `wf_fna_ffi_imp`

- **中文名称**: 预算流程初始化定义表-fnafeewfinfo
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_ffi_imp`
- **主键**: `fnafeewfinfo表对应字段`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | fnafeewfinfo表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `workflowid` | fnafeewfinfo表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `enable` | fnafeewfinfo表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `lastmodifieddate` | fnafeewfinfo表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `templatefile` | fnafeewfinfo表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `templatefilemobile` | fnafeewfinfo表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `fnawftype` | fnafeewfinfo表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 8 | `fnawftypeborrow` | fnafeewfinfo表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `fnawftypecoll` | fnafeewfinfo表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `fnawftypereverse` | fnafeewfinfo表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `fnawftypereim` | fnafeewfinfo表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `overstandardtips` | fnafeewfinfo表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 13 | `isallnodescontrol` | fnafeewfinfo表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `impguid1` | fnafeewfinfo表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 15 | `fnawftypereverseadvance` | fnafeewfinfo表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `wf_fna_waddi_imp`

- **中文名称**: 预算流程初始化定义表-workflow_addinoperate
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_waddi_imp`
- **主键**: `workflow_addinoperate表对应字段`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `impguid1` | workflow_addinoperate表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 2 | `id` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `objid` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `isnode` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `workflowid` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `fieldid` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `fieldop1id` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `fieldop2id` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `operation` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `customervalue` | workflow_addinoperate表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `rules` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `type` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `ispreadd` | workflow_addinoperate表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 14 | `wftomodesetid` | workflow_addinoperate表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 15 | `isnewsap` | workflow_addinoperate表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 16 | `wftofinancesetid` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `istriggerreject` | workflow_addinoperate表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |

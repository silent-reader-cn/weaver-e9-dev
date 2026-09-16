# 泛微OA 数据表: `wf_fna_wval_imp`

- **中文名称**: 预算流程初始化定义表-workflow_viewattrlinkage
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_wval_imp`
- **主键**: `workflow_viewattrlinkage表对应字段`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `impguid1` | workflow_viewattrlinkage表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 2 | `workflowid` | workflow_viewattrlinkage表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `nodeid` | workflow_viewattrlinkage表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `selectfieldid` | workflow_viewattrlinkage表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `selectfieldvalue` | workflow_viewattrlinkage表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `changefieldids` | workflow_viewattrlinkage表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `viewattr` | workflow_viewattrlinkage表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

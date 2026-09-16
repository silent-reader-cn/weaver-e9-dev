# 泛微OA 数据表: `wf_fna_waction_imp`

- **中文名称**: 预算流程初始化定义表-workflowactionset
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_waction_imp`
- **主键**: `workflowactionset表对应字段`
- **字段数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `impguid1` | workflowactionset表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 2 | `id` | workflowactionset表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `actionname` | workflowactionset表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `workflowid` | workflowactionset表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `nodeid` | workflowactionset表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `nodelinkid` | workflowactionset表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `ispreoperator` | workflowactionset表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `actionorder` | workflowactionset表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `interfaceid` | workflowactionset表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `interfacetype` | workflowactionset表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `typename` | workflowactionset表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 12 | `isused` | workflowactionset表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `wf_fna_wnf_imp`

- **中文名称**: 预算流程初始化定义表-workflow_nodeform
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_wnf_imp`
- **主键**: `workflow_nodeform表对应字段`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `impguid1` | workflow_nodeform表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 2 | `nodeid` | workflow_nodeform表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `fieldid` | workflow_nodeform表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `isview` | workflow_nodeform表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `isedit` | workflow_nodeform表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `ismandatory` | workflow_nodeform表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `orderid` | workflow_nodeform表对应字段 | `number` | (20,5) | 是 | 否 | 否 | - | - | - |

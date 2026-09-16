# 泛微OA 数据表: `wf_fna_wb_imp`

- **中文名称**: 预算流程初始化定义表-workflow_bill
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_wb_imp`
- **主键**: `workflow_bill表对应字段`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | workflow_bill表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `namelabel` | workflow_bill表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `tablename` | workflow_bill表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `createpage` | workflow_bill表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `managepage` | workflow_bill表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `viewpage` | workflow_bill表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `detailtablename` | workflow_bill表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 8 | `detailkeyfield` | workflow_bill表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `operationpage` | workflow_bill表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `hasfileup` | workflow_bill表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `invalid` | workflow_bill表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `formdes` | workflow_bill表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 13 | `subcompanyid` | workflow_bill表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `dsporder` | workflow_bill表对应字段 | `number` | (20,5) | 是 | 否 | 否 | - | - | - |
| 15 | `subcompanyid3` | workflow_bill表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `from_module_` | workflow_bill表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 17 | `impguid1` | workflow_bill表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |

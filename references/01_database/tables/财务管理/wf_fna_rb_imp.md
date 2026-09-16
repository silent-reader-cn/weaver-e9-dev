# 泛微OA 数据表: `wf_fna_rb_imp`

- **中文名称**: 预算流程初始化定义表-rule_base
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_rb_imp`
- **主键**: `rule_base表对应字段`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `impguid1` | rule_base表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 2 | `condit_temp` | rule_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 3 | `id` | rule_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `rulesrc` | rule_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `formid` | rule_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `linkid` | rule_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `isbill` | rule_base表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `rulename` | rule_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `ruledesc` | rule_base表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `condit` | rule_base表对应字段 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |

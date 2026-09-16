# 泛微OA 数据表: `wf_fna_fcc_imp`

- **中文名称**: 预算流程初始化定义表-FnaCostCenter
- **所属模块**: `财务管理`
- **数据库表名**: `wf_fna_fcc_imp`
- **主键**: `FnaCostCenter表对应字段`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | FnaCostCenter表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `supfccid` | FnaCostCenter表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `type` | FnaCostCenter表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `name` | FnaCostCenter表对应字段 | `char` | 100 | 是 | 否 | 否 | - | - | - |
| 5 | `code` | FnaCostCenter表对应字段 | `char` | 50 | 是 | 否 | 否 | - | - | - |
| 6 | `archive` | FnaCostCenter表对应字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `description` | FnaCostCenter表对应字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 8 | `impguid1` | FnaCostCenter表对应字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |

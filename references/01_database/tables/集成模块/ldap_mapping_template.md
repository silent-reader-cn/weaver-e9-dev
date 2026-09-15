# 泛微OA 数据表: `ldap_mapping_template`

- **所属模块**: `集成模块`
- **数据库表名**: `ldap_mapping_template`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `templateid` | 标识 | `varchar2` | 100 | 否 | 标识 |
| 2 | `fieldkey` | 字段标识 | `varchar2` | 800 | 是 | 字段标识 |
| 3 | `fieldname` | 字段显示名称 | `varchar2` | 800 | 是 | 字段显示名称 |
| 4 | `datatype` | 数据类型 | `char` | 1 | 是 | :OU对应关系映射，2:分部关系映射，3:部门关系映射，4:人员关系映射 |
| 5 | `ismust` | 是否必填 | `char` | 1 | 是 | 1：必填，0:可选 |
| 6 | `defaulttype` | 默认映射类型 | `char` | 1 | 是 | 0:LDAP字段对应值,1:固定值,2:调用方法 |
| 7 | `defaultvalue` | 默认值 | `varchar2` | 1000 | 是 | 默认值 |
| 8 | `showorder` | 显示顺序 | `integer` | - | 是 | 显示顺序 |

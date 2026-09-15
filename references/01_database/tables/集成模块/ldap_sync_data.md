# 泛微OA 数据表: `ldap_sync_data`

- **所属模块**: `集成模块`
- **数据库表名**: `ldap_sync_data`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `ldapid` | LDAP标识 | `varchar2` | 800 | 是 | LDAP标识 |
| 2 | `uuid` | LDAP数据唯一标识 | `varchar2` | 1000 | 是 | LDAP数据唯一标识 |
| 3 | `rdn` | LDAP域地址 | `varchar2` | 1000 | 是 | LDAP域地址 |
| 4 | `oaid` | OA唯一标识 | `integer` | - | 是 | OA唯一标识 |
| 5 | `datatype` | 数据类型 | `char` | 1 | 是 | 1:分部，2:部门，3:人员 |
| 6 | `synctype` | 同步类型 | `char` | 1 | 是 | 1:LDAP->OA,2:OA->LDAP |

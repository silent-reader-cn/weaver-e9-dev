# 泛微OA 数据表: `ldap_mapping`

- **所属模块**: `集成模块`
- **数据库表名**: `ldap_mapping`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `ldapid` | LDAP标识 | `varchar2` | 800 | 否 | LDAP标识 |
| 3 | `attributename` | 属性名 | `varchar2` | 1000 | 否 | 属性名 |
| 4 | `attributetype` | 类别 | `char` | 1 | 否 | 0:LDAP字段对应值,1:固定值,2:调用方法 |
| 5 | `attributevalue` | 属性值 | `varchar2` | 1000 | 否 | 属性值 |
| 6 | `datatype` | 数据类型 | `char` | 1 | 否 | 1:OU对应关系映射，2:分部关系映射，3:部门关系映射，4:人员关系映射，5:反向同步OU对应关系，6:反向同步分部关系，7:反向同步部门对应关系，8:反向同步人员对应关系 |
| 7 | `showorder` | 显示顺序 | `integer` | - | 是 | 显示顺序 |
| 8 | `attributeOperation` | 操作类别 | `char` | 1 | 是 | 0:无限制 1:仅添加 2:仅修改 |

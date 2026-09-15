# 泛微OA 数据表: `hrmroles_module`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmroles_module`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `rolesmark` | 角色标识 | `varchar2` | 1000 | 是 | 角色标识 |
| 3 | `rolesname` | 角色描述 | `varchar2` | 1000 | 是 | 角色描述 |
| 4 | `docid` | 相关文档id | `integer` | - | 是 | 相关文档id |
| 5 | `isdefault` | 是否默认 | `char` | 1 | 是 | 是否默认，初始值值为0 |
| 6 | `type` | 角色类型 | `integer` | - | 是 | 角色类型，初始值值为0 |
| 7 | `subcompanyid` | 分部id | `integer` | - | 是 | 分部id |

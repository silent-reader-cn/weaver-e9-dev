# 泛微OA 数据表: `info_editrole`

- **所属模块**: `政务应用`
- **数据库表名**: `info_editrole`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 随机id | `varchar2` | 32 | 是 | - |
| 3 | `pathid` | 路径id | `integer` | - | 是 | - |
| 4 | `sharetype` | 权限类型 | `integer` | - | 是 | - |
| 5 | `dataid` | 对应数据id | `integer` | - | 是 | - |
| 6 | `relatedid` | 共享对象id | `clob` | - | 是 | - |
| 7 | `rolelevel` | 共享级别 | `integer` | - | 是 | - |
| 8 | `showlevel` | 安全级别下限 | `integer` | - | 是 | - |
| 9 | `showlevel2` | 安全级别上限 | `integer` | - | 是 | - |
| 10 | `isrolelimited` | 是否受限 | `integer` | - | 是 | 1：是 2；否                                                                        受范围限制时，角色中的部分人员有权限，不受限制时按照角色级别，角色中的所有人用于权限 |
| 11 | `joblevel` | 分类 | `integer` | - | 是 | 0、部门；1、分部；2、总部； |
| 12 | `jobleveltext` | 对象id | `varchar2` | 4000 | 是 | 保存岗位级别对应的对象以逗号分隔的id串 |

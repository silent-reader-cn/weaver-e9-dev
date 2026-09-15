# 泛微OA 数据表: `govern_rightinfo`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_rightinfo`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldid` | 字段id | `integer` | - | 是 | sharetype=7时候生效 显示字段id 对应govern_fieldid |
| 2 | `id` | id | `integer` | - | 否 | - |
| 3 | `categoryid` | 类型id | `integer` | - | 否 | - |
| 4 | `opttype` | 权限级别 | `integer` | - | 是 | 0新建、1查看、2共享、3管理、4监控 |
| 5 | `datatype` | 类型（废弃） | `integer` | - | 是 | 0事项权限   1任务权限 |
| 6 | `sharetype` | 权限类型 | `integer` | - | 是 | 1人员、2部门、3分部、4角色、5所有人、6岗位、7表单字段（人员部门岗位） |
| 7 | `rolelevel` | 角色级别 | `integer` | - | 是 | - |
| 8 | `showlevel` | 安全级别下限 | `integer` | - | 是 | - |
| 9 | `showlevel2` | 安全级别上限 | `integer` | - | 是 | - |
| 10 | `isrolelimited` | 是否收到范围控制 | `integer` | - | 是 | 1：是 2；否                                                                        受范围限制时，角色中的部分人员有权限，不受限制时按照角色级别，角色中的所有人用于权限 |
| 11 | `rolefieldtype` | 字段类型(角色) | `integer` | - | 是 | - |
| 12 | `rolefield` | 字段id(角色) | `integer` | - | 是 | - |
| 13 | `fieldtype` | 显示字段类型 | `integer` | - | 是 | sharetype=7时候生效 显示字段类型（1人员、2分部、3部门、4岗位） |
| 14 | `joblevel` | 岗位级别 | `integer` | - | 是 | 0、部门；1、分部；2、总部； |
| 15 | `jobleveltext` | 岗位对象 | `varchar2` | 4000 | 是 | - |
| 16 | `subtaskview` | 是否有权限查看下级任务 | `integer` | - | 是 | - |
| 17 | `relatedid` | 共享对象id | `varchar2` | 64 | 是 | - |

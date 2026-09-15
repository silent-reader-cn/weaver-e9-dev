# 泛微OA 数据表: `govern_sharerule`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_sharerule`
- **字段总数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `sourceid` | 数据id | `integer` | - | 否 | - |
| 3 | `categoryid` | 类型id | `integer` | - | 否 | - |
| 4 | `datatype` | 类型 | `integer` | - | 是 | 0事项权限   1任务权限 |
| 5 | `opttype` | 权限级别 | `integer` | - | 是 | 1查看2共享3管理4监控 |
| 6 | `sharetype` | 权限类型 | `integer` | - | 是 | 1人员2分部3部门4角色5所有人6岗位7相关字段 |
| 7 | `relatedid` | 对象id | `integer` | - | 是 | - |
| 8 | `rolelevel` | 共享级别（角色） | `integer` | - | 是 | 0部门 1分部 2总部 |
| 9 | `showlevel` | 安全级别下限 | `integer` | - | 是 | - |
| 10 | `showlevel2` | 安全级别上限 | `integer` | - | 是 | - |
| 11 | `isdefault` | 是否共享权限 | `integer` | - | 是 | 0前端用户共享 1设置自动生成 |
| 12 | `isrolelimited` | 是否受范围限制 | `integer` | - | 是 | 1：是 2；否                                                                        受范围限制时，角色中的部分人员有权限，不受限制时按照角色级别，角色中的所有人用于权限 |
| 13 | `rolefieldtype` | 字段类型 | `integer` | - | 是 | - |
| 14 | `rolefield` | 字段id | `integer` | - | 是 | - |
| 15 | `higherlevel` | 上级关系 | `integer` | - | 是 | 暂时不用 |
| 16 | `rightid` | 权限设置id | `integer` | - | 否 | - |
| 17 | `joblevel` | 岗位级别 | `integer` | - | 是 | - |
| 18 | `jobleveltext` | 岗位独享 | `varchar2` | 4000 | 是 | - |
| 19 | `prjruleid` | 对应事项权限id | `integer` | - | 是 | 源任务对应事项权限id关联字段 |

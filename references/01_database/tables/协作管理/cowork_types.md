# 泛微OA 数据表: `cowork_types`

- **所属模块**: `协作管理`
- **数据库表名**: `cowork_types`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `typename` | 协作区类型名称 | `varchar2` | 800 | 是 | - |
| 3 | `departmentid` | 部门 | `integer` | - | 是 | - |
| 4 | `managerid` | 负责人 | `clob` | 4000 | 是 | - |
| 5 | `members` | 协作区成员 | `clob` | 4000 | 是 | - |
| 6 | `isapproval` | 是否需要审批 | `integer` | - | 是 | - |
| 7 | `isanonymous` | 是否允许匿名 | `integer` | - | 是 | - |

# 泛微OA 数据表: `workplanvisitsetdetail`

- **中文名称**: 工作计划访问权限映射明细表（映射两个实体之间的访问权限）
- **所属模块**: `日程管理`
- **数据库表名**: `workplanvisitsetdetail`
- **主键**: `workplanvisitsetdetailid`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `workplanvisitsetdetailid` | 主键 | `integer` | - | 否 | 否 | 是 | - | - | 主键 |
| 2 | `workplanreporttype` | 被查看实体的类型 | `integer` | - | 是 | 否 | 否 | - | - | 人力资源具体类型(部门,职称等) |
| 3 | `workplanreportcontentid` | 被查看实体类型的标识id | `integer` | - | 是 | 否 | 否 | - | - | 人力资源具体类型下的ID |
| 4 | `workplanreportsec` | 被访问者安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 人力资源安全级别 |
| 5 | `workplanvisittype` | 查看实体的类型 | `integer` | - | 是 | 否 | 否 | - | - | 有权限访问人力资源具体类型(部门,职称等) |
| 6 | `workplanvisitcontentid` | 查看实体类型的标识id | `integer` | - | 是 | 否 | 否 | - | - | 有权限访问人力资源具体类型下的ID |
| 7 | `workplanvisitsec` | 访问者安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 有权限访问人力资源安全级别 |
| 8 | `workplanvisitsetid` | 外键，映射workplanvisitset | `integer` | - | 是 | 是 | 否 | workplanvisitset的主键 | - | workPlanVisitSet表标识符 |

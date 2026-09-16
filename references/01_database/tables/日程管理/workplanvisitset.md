# 泛微OA 数据表: `workplanvisitset`

- **中文名称**: 工作计划访问权限映射表（映射两个实体之间的访问权限）
- **所属模块**: `日程管理`
- **数据库表名**: `workplanvisitset`
- **主键**: `workplanvisitsetid`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `workplanvisitsetid` | 主键 | `integer` | - | 否 | 否 | 是 | - | - | 主键 |
| 2 | `workplanreporttype` | 被查看实体的类型 | `integer` | - | 是 | 否 | 否 | - | - | 所有人：1<br>分部：2<br>部门：3<br>角色：4<br>岗位：5<br>人力资源： 6 |
| 3 | `workplanreportcontentid` | 被查看实体类型的标识id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 以“，”分开 |
| 4 | `workplanreportsec` | 被访问者安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 被访问者安全级别 |
| 5 | `workplanvisittype` | 查看实体的类型 | `integer` | - | 是 | 否 | 否 | - | - | 查看实体的类型 |
| 6 | `workplanvisitcontentid` | 查看实体类型的标识id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 以“，”分开 |
| 7 | `workplanvisitsec` | 访问者安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 访问者安全级别 |

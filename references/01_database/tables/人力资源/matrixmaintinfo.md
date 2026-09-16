# 泛微OA 数据表: `matrixmaintinfo`

- **中文名称**: 矩阵维护信息表
- **所属模块**: `人力资源`
- **数据库表名**: `matrixmaintinfo`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | ID |
| 2 | `matrixid` | 矩阵id | `integer` | - | 是 | 否 | 否 | - | - | 矩阵id |
| 3 | `type` | 类型 | `integer` | - | 是 | 否 | 否 | - | - | 类型 |
| 4 | `resourceid` | 人员id | `integer` | - | 是 | 否 | 否 | - | - | 人员id |
| 5 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | 分部id |
| 6 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | 部门id |
| 7 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | 角色id |
| 8 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别 |
| 9 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | 角色级别 |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | 否 | 否 | - | - | 所有人 |

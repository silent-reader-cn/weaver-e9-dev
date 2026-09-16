# 泛微OA 数据表: `hrmresource_trigger`

- **中文名称**: hrmResource同步表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmresource_trigger`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | ID |
| 2 | `managerid` | 经理id | `integer` | - | 是 | 否 | 否 | - | - | 经理id |
| 3 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | 部门id |
| 4 | `subcompanyid1` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | 分部id |
| 5 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别 |
| 6 | `managerstr` | 所有上级 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 所有上级 |

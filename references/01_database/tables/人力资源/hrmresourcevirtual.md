# 泛微OA 数据表: `hrmresourcevirtual`

- **中文名称**: 人力资源虚拟组织人员信息表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourcevirtual`
- **主键**: `id`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | 否 | 否 | - | - | 人员id |
| 3 | `managerid` | 上级id | `integer` | - | 是 | 否 | 否 | - | - | 上级id |
| 4 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | 分部id |
| 5 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | 部门id |
| 6 | `managerstr` | 所有上级id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 所有上级id |
| 7 | `virtualtype` | 虚拟组织类型 | `integer` | - | 是 | 否 | 否 | - | - | 虚拟组织类型 |

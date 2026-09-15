# 泛微OA 数据表: `hrmresourcevirtual`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourcevirtual`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | 人员id |
| 3 | `managerid` | 上级id | `integer` | - | 是 | 上级id |
| 4 | `subcompanyid` | 分部id | `integer` | - | 是 | 分部id |
| 5 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 6 | `managerstr` | 所有上级id | `varchar2` | 1000 | 是 | 所有上级id |
| 7 | `virtualtype` | 虚拟组织类型 | `integer` | - | 是 | 虚拟组织类型 |

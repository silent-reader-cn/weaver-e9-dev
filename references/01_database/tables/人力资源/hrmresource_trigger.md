# 泛微OA 数据表: `hrmresource_trigger`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmresource_trigger`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `managerid` | 经理id | `integer` | - | 是 | 经理id |
| 3 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 4 | `subcompanyid1` | 分部id | `integer` | - | 是 | 分部id |
| 5 | `seclevel` | 安全级别 | `integer` | - | 是 | 安全级别 |
| 6 | `managerstr` | 所有上级 | `varchar2` | 1000 | 是 | 所有上级 |

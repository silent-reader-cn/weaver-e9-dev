# 泛微OA 数据表: `hrmperformancecheckscheme`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancecheckscheme`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `schemename` | 名称 | `varchar2` | 800 | 是 | 名称 |
| 3 | `memo` | 描述 | `varchar2` | 800 | 是 | 描述 |
| 4 | `checkbranchid` | 考核对象分部id | `varchar2` | 1000 | 是 | 考核对象分部id |
| 5 | `checkdeptid` | 考核对象部门id | `varchar2` | 1000 | 是 | 考核对象部门id |
| 6 | `checkpostid` | 考核对象岗位id | `varchar2` | 1000 | 是 | 考核对象岗位id |
| 7 | `checkhrmid` | 考核对象人力资源id | `varchar2` | 1000 | 是 | 考核对象人力资源id |
| 8 | `viewsuperiorid` | 查看对象上级id | `char` | 1 | 是 | 查看对象上级id |
| 9 | `viewsesuperiorid` | 查看对象隔级id | `char` | 1 | 是 | 查看对象隔级id |
| 10 | `viewpostid` | 考核对象岗位id | `varchar2` | 1000 | 是 | 考核对象岗位id |
| 11 | `viewhrmid` | 考核对象人力资源id | `varchar2` | 1000 | 是 | 考核对象人力资源id |
| 12 | `status` | 状态 | `char` | 1 | 是 | 状态 |

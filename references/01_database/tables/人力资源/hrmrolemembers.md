# 泛微OA 数据表: `hrmrolemembers`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmrolemembers`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `resourceidbak` | 人员id副本 | `integer` | - | 是 | 人员id副本 |
| 2 | `resourcetype` | 人员类型 | `integer` | - | 是 | 人员类型 |
| 3 | `alllevel` | 所有级别 | `integer` | - | 是 | 所有级别 |
| 4 | `seclevelfrom` | 级别开始值 | `integer` | - | 是 | 级别开始值 |
| 5 | `seclevelto` | 级别结束值 | `integer` | - | 是 | 级别结束值 |
| 6 | `jobtitlelevel` | 岗位级别 | `integer` | - | 是 | 岗位级别 |
| 7 | `subdepid` | 上级部门id | `integer` | - | 是 | 上级部门id |
| 8 | `resourceid` | 人力资源id | `varchar2` | 1000 | 是 | 人力资源id |
| 9 | `rolelevel` | 角色级别 | `char` | 1 | 是 | 角色级别 |
| 10 | `orderby` | 分组 | `integer` | - | 是 | 分组 |
| 11 | `id` | ID | `integer` | - | 否 | ID |
| 12 | `roleid` | 角色id | `integer` | - | 是 | 角色id |

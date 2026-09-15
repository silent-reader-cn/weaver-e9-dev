# 泛微OA 数据表: `hrmbirthdayshare`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmbirthdayshare`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `seclevelto` | 最高等级 | `integer` | - | 是 | - |
| 2 | `jobtitleid` | 岗位id | `integer` | - | 是 | - |
| 3 | `jobtitlelevel` | 岗位等级 | `integer` | - | 是 | - |
| 4 | `jobdepartment` | 岗位所在部门 | `integer` | - | 是 | - |
| 5 | `jobsubcompany` | 岗位所在分部 | `integer` | - | 是 | - |
| 6 | `lowerlevel` | 最低等级 | `integer` | - | 是 | - |
| 7 | `id` | ID | `integer` | - | 否 | - |
| 8 | `sharetype` | 提醒范围类型 | `integer` | - | 是 | 1.人力资源 2.分部 3.部门 4.角色 5.所有人 |
| 9 | `seclevel` | 提醒类别 | `integer` | - | 是 | - |
| 10 | `rolelevel` | 对象 | `integer` | - | 是 | - |
| 11 | `sharelevel` | 提醒来源范围 | `integer` | - | 是 | 0.本部门 1.本部门及上级部门 2.本部门及下级部门 3.本分部 4.本分部及上级分部 5.本分部及下级分部 |
| 12 | `userid` | 用户id | `integer` | - | 是 | - |
| 13 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 14 | `departmentid` | 部门id | `integer` | - | 是 | - |
| 15 | `roleid` | 角色id | `integer` | - | 是 | - |
| 16 | `foralluser` | 所有人 | `integer` | - | 是 | - |

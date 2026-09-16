# 泛微OA 数据表: `hrmbirthdayshare`

- **中文名称**: 人力资源生日提醒范围设置表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmbirthdayshare`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `seclevelto` | 最高等级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `jobtitleid` | 岗位id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `jobtitlelevel` | 岗位等级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `jobdepartment` | 岗位所在部门 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `jobsubcompany` | 岗位所在分部 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `lowerlevel` | 最低等级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 8 | `sharetype` | 提醒范围类型 | `integer` | - | 是 | 否 | 否 | - | - | 1.人力资源 2.分部 3.部门 4.角色 5.所有人 |
| 9 | `seclevel` | 提醒类别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `rolelevel` | 对象 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `sharelevel` | 提醒来源范围 | `integer` | - | 是 | 否 | 否 | - | - | 0.本部门 1.本部门及上级部门 2.本部门及下级部门 3.本分部 4.本分部及上级分部 5.本分部及下级分部 |
| 12 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `foralluser` | 所有人 | `integer` | - | 是 | 否 | 否 | - | - | - |

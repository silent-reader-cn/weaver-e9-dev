# 泛微OA 数据表: `hrmgroupmembers`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmgroupmembers`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `groupid` | 自定义组id | `integer` | - | 否 | 自定义组id |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 共享类型 |
| 4 | `userid` | 成员id | `integer` | - | 是 | 成员id |
| 5 | `usertype` | 成员类型 | `char` | 1 | 是 | 成员类型 |
| 6 | `seclevel` | 安全等级 | `integer` | - | 是 | 安全等级 |
| 7 | `seclevelto` | 最高安全等级 | `integer` | - | 是 | 最高安全等级 |
| 8 | `rolelevel` | 角色级别 | `integer` | - | 是 | 角色级别 |
| 9 | `sharelevel` | 共享级别 | `integer` | - | 是 | 共享级别 |
| 10 | `subcompanyid` | 分部id | `integer` | - | 是 | 分部id |
| 11 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 12 | `roleid` | 角色id | `integer` | - | 是 | 角色id |
| 13 | `foralluser` | 所有用户 | `integer` | - | 是 | 所有用户 |
| 14 | `jobtitleid` | 岗位id | `integer` | - | 是 | 岗位id |
| 15 | `jobtitlelevel` | 岗位级别 | `integer` | - | 是 | 岗位级别 |
| 16 | `scopeid` | 共享范围id | `varchar2` | 4000 | 是 | 共享范围id |
| 17 | `orggroupid` | 组织结构id | `integer` | - | 是 | 组织结构id |
| 18 | `dsporder` | 显示顺序 | `number` | (18,1) | 是 | 显示顺序 |

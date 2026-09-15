# 泛微OA 数据表: `votingshare`

- **所属模块**: `网上调查`
- **数据库表名**: `votingshare`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `votingid` | 调查id | `integer` | - | 是 | - |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | - |
| 4 | `resourceid` | 用户id | `integer` | - | 是 | - |
| 5 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 6 | `departmentid` | 部门id | `integer` | - | 是 | - |
| 7 | `roleid` | 角色id | `integer` | - | 是 | - |
| 8 | `seclevel` | 安全级别 | `integer` | - | 是 | - |
| 9 | `rolelevel` | 角色级别 | `integer` | - | 是 | - |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | - |
| 11 | `seclevelmax` | 安全级别最大值 | `integer` | - | 是 | - |
| 12 | `joblevel` | 岗位级别 | `char` | 10 | 否 | - |
| 13 | `jobdepartment` | 指定部门 | `char` | 10 | 否 | - |
| 14 | `jobsubcompany` | 指定分部 | `char` | 10 | 否 | - |
| 15 | `jobtitles` | 岗位 | `char` | 10 | 否 | - |

# 泛微OA 数据表: `votingviewer`

- **中文名称**: 调查结果查看范围表
- **所属模块**: `网上调查`
- **数据库表名**: `votingviewer`
- **主键**: `id`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `votingid` | 调查id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `resourceid` | 人员id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `foralluser` | 所有人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `seclevelmax` | 安全级别最大值 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `joblevel` | 岗位级别 | `char` | 10 | 否 | 否 | 否 | - | 0 | - |
| 13 | `jobdepartment` | 指定部门 | `char` | 10 | 否 | 否 | 否 | - | 0 | - |
| 14 | `jobsubcompany` | 指定分部 | `char` | 10 | 否 | 否 | 否 | - | 0 | - |
| 15 | `jobtitles` | 岗位 | `char` | 10 | 否 | 否 | 否 | - | 0 | - |

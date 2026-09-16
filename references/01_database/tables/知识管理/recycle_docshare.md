# 泛微OA 数据表: `recycle_docshare`

- **中文名称**: 回收站-文档共享表
- **所属模块**: `知识管理`
- **数据库表名**: `recycle_docshare`
- **主键**: `id`
- **字段数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `sharelevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `foralluser` | 所有人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `crmid` | 客户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `sharesource` | 共享人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `issecdefaultshare` | 是否是默认共享 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 10 | `orggroupid` | 群组id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `downloadlevel` | 下载级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `allmanagers` | 所有上级 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 13 | `includesub` | 包含下级 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 14 | `orgid` | 组织id | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 15 | `seclevelmax` | 安全级别最大值 | `char` | 10 | 否 | 否 | 否 | - | - | - |
| 16 | `joblevel` | 岗位级别 | `char` | 10 | 否 | 否 | 否 | - | - | - |
| 17 | `jobdepartment` | 指定部门 | `char` | 10 | 否 | 否 | 否 | - | - | - |
| 18 | `jobsubcompany` | 指定分部 | `char` | 10 | 否 | 否 | 否 | - | - | - |
| 19 | `jobids` | 岗位 | `char` | 10 | 否 | 否 | 否 | - | - | - |
| 20 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 21 | `docid` | 文档id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `sharetype` | 共享类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | - |

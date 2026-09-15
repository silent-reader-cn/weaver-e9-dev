# 泛微OA 数据表: `recycle_docshare`

- **所属模块**: `知识管理`
- **数据库表名**: `recycle_docshare`
- **字段总数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `sharelevel` | 安全级别 | `integer` | - | 是 | - |
| 2 | `userid` | 用户id | `integer` | - | 是 | - |
| 3 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 4 | `departmentid` | 部门id | `integer` | - | 是 | - |
| 5 | `roleid` | 角色id | `integer` | - | 是 | - |
| 6 | `foralluser` | 所有人 | `integer` | - | 是 | - |
| 7 | `crmid` | 客户id | `integer` | - | 是 | - |
| 8 | `sharesource` | 共享人 | `integer` | - | 是 | - |
| 9 | `issecdefaultshare` | 是否是默认共享 | `char` | 1 | 是 | - |
| 10 | `orggroupid` | 群组id | `integer` | - | 是 | - |
| 11 | `downloadlevel` | 下载级别 | `integer` | - | 是 | - |
| 12 | `allmanagers` | 所有上级 | `varchar2` | 2000 | 是 | - |
| 13 | `includesub` | 包含下级 | `char` | 10 | 是 | - |
| 14 | `orgid` | 组织id | `char` | 10 | 是 | - |
| 15 | `seclevelmax` | 安全级别最大值 | `char` | 10 | 否 | - |
| 16 | `joblevel` | 岗位级别 | `char` | 10 | 否 | - |
| 17 | `jobdepartment` | 指定部门 | `char` | 10 | 否 | - |
| 18 | `jobsubcompany` | 指定分部 | `char` | 10 | 否 | - |
| 19 | `jobids` | 岗位 | `char` | 10 | 否 | - |
| 20 | `id` | id | `integer` | - | 否 | - |
| 21 | `docid` | 文档id | `integer` | - | 是 | - |
| 22 | `sharetype` | 共享类型 | `integer` | - | 是 | - |
| 23 | `seclevel` | 安全级别 | `integer` | - | 是 | - |
| 24 | `rolelevel` | 角色级别 | `integer` | - | 是 | - |

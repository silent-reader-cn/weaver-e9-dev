# 泛微OA 数据表: `docseccategoryshare`

- **中文名称**: 文档子目录默认共享表
- **所属模块**: `知识管理`
- **数据库表名**: `docseccategoryshare`
- **主键**: `id`
- **字段数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 2 | `jobdepartment` | 岗位指定部门 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 3 | `jobsubcompany` | 岗位指定分部 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 4 | `jobids` | 岗位 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 5 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 6 | `seccategoryid` | 默认共享子目录id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `sharetype` | 共享类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | 0：部门，1：分别，2：总部 |
| 10 | `sharelevel` | 共享级别 | `integer` | - | 是 | 否 | 否 | - | - | 1：查看,2：编辑 |
| 11 | `userid` | 共享人力资源id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `subcompanyid` | 共享分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `departmentid` | 共享部门 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `roleid` | 共享角色 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `foralluser` | 是否共享所有人 | `integer` | - | 是 | 否 | 否 | - | - | 0：否,1：是 |
| 16 | `crmid` | 客户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `docseccategorytemplateid` | 目录模版id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `orggroupid` | 群组id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 19 | `downloadlevel` | 下载权限级别 | `integer` | - | 是 | 否 | 否 | - | - | 0：不可下载,1：可下载 |
| 20 | `operategroup` | 操作组 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 21 | `orgid` | 群组id | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 22 | `seclevelmax` | 安全级别最大值 | `char` | 10 | 否 | 否 | 否 | - | 255 | - |
| 23 | `includesub` | 包含下级 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 24 | `custype` | 客户类型 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 25 | `isolddate` | 历史数据 | `char` | 10 | 是 | 否 | 否 | - | - | 1：历史数据；0：新数据 |

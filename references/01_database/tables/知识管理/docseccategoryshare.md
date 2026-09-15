# 泛微OA 数据表: `docseccategoryshare`

- **所属模块**: `知识管理`
- **数据库表名**: `docseccategoryshare`
- **字段总数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `joblevel` | 岗位级别 | `integer` | - | 是 | - |
| 2 | `jobdepartment` | 岗位指定部门 | `integer` | - | 是 | - |
| 3 | `jobsubcompany` | 岗位指定分部 | `integer` | - | 是 | - |
| 4 | `jobids` | 岗位 | `integer` | - | 是 | - |
| 5 | `id` | ID | `integer` | - | 否 | - |
| 6 | `seccategoryid` | 默认共享子目录id | `integer` | - | 是 | - |
| 7 | `sharetype` | 共享类型 | `integer` | - | 是 | - |
| 8 | `seclevel` | 安全级别 | `integer` | - | 是 | - |
| 9 | `rolelevel` | 角色级别 | `integer` | - | 是 | 0：部门，1：分别，2：总部 |
| 10 | `sharelevel` | 共享级别 | `integer` | - | 是 | 1：查看,2：编辑 |
| 11 | `userid` | 共享人力资源id | `integer` | - | 是 | - |
| 12 | `subcompanyid` | 共享分部id | `integer` | - | 是 | - |
| 13 | `departmentid` | 共享部门 | `integer` | - | 是 | - |
| 14 | `roleid` | 共享角色 | `integer` | - | 是 | - |
| 15 | `foralluser` | 是否共享所有人 | `integer` | - | 是 | 0：否,1：是 |
| 16 | `crmid` | 客户id | `integer` | - | 是 | - |
| 17 | `docseccategorytemplateid` | 目录模版id | `integer` | - | 是 | - |
| 18 | `orggroupid` | 群组id | `integer` | - | 是 | - |
| 19 | `downloadlevel` | 下载权限级别 | `integer` | - | 是 | 0：不可下载,1：可下载 |
| 20 | `operategroup` | 操作组 | `char` | 10 | 是 | - |
| 21 | `orgid` | 群组id | `char` | 10 | 是 | - |
| 22 | `seclevelmax` | 安全级别最大值 | `char` | 10 | 否 | - |
| 23 | `includesub` | 包含下级 | `char` | 10 | 是 | - |
| 24 | `custype` | 客户类型 | `char` | 10 | 是 | - |
| 25 | `isolddate` | 历史数据 | `char` | 10 | 是 | 1：历史数据；0：新数据 |

# 泛微OA 数据表: `diraccesscontrollist`

- **中文名称**: 文档目录访问权限列表
- **所属模块**: `知识管理`
- **数据库表名**: `diraccesscontrollist`
- **主键**: `无`
- **字段数**: `21`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 2 | `jobdepartment` | 指定部门 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 3 | `jobsubcompany` | 指定分部 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 4 | `jobids` | 岗位 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 5 | `mainid` | 主关键字id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 6 | `dirid` | 目录id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 7 | `dirtype` | 目录类型 | `integer` | - | 否 | 否 | 否 | - | - | 0主目录<br>1分目录<br>2子目录 |
| 8 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `usertype` | 用户类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `permissiontype` | 授权类型 | `integer` | - | 否 | 否 | 否 | - | - | 1部门＋安全级别<br>2角色＋级别＋安全级别<br>3安全级别<br>4用户类型＋安全级别 |
| 14 | `operationcode` | 被授权的操作 | `integer` | - | 否 | 否 | 否 | - | - | 0创建文档<br>1创建目录<br>2移动文档 |
| 15 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `docseccategorytemplateid` | 目录模版id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `relatedid` | 相关联id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `seclevelmax` | 安全级别最大值 | `char` | 10 | 否 | 否 | 否 | - | 255 | - |
| 20 | `isolddate` | 是否是历史数据 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 21 | `includesub` | 包含下级 | `char` | 10 | 是 | 否 | 否 | - | - | 是否含有下级 |

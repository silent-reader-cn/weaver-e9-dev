# 泛微OA 数据表: `hp_mobile_ptaccesscontrollist`

- **中文名称**: 移动门户权限控制信息表（待定）
- **所属模块**: `门户管理`
- **数据库表名**: `hp_mobile_ptaccesscontrollist`
- **主键**: `mainid`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `mainid` | 主键 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `dirid` | 目录id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `dirtype` | 目录类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `seclevel` | 安全级别下限 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `usertype` | 用户类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `permissiontype` | 权限类型 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 10 | `operationcode` | 操作code | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `docseccategorytemplateid` | 文档安全类型模板 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `seclevelmax` | 安全级别上限 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `jobtitle` | 岗位名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 16 | `jobtitlelevel` | 岗位级别 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `jobtitlesharevalue` | 岗位id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

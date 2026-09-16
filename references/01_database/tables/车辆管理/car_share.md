# 泛微OA 数据表: `car_share`

- **中文名称**: 车辆共享表
- **所属模块**: `车辆管理`
- **数据库表名**: `car_share`
- **主键**: `id`
- **字段数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 是 | - | - | 主键 |
| 2 | `carid` | 车辆id | `integer` | - | 否 | 是 | 否 | - | - | carinfo表主键 |
| 3 | `userid` | 人力资源 | `varchar2` | 10000 | 是 | 否 | 否 | - | - | 人力资源表主键 |
| 4 | `usertype` | 共享人员类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `sharelevel` | 共享级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `departmentid` | 部门id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `sharetype` | 共享类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `seclevel` | 所有人安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `seclevelmax` | 所有人最高安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `deptlevel` | 部门安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `deptlevelmax` | 部门最高安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `sublevel` | 分部 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `sublevelmax` | 分部最高安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `has_child` | 是否含下级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `fieldids` | 选择的自定义字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `roleid` | 角色id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 18 | `rolelevel` | 角色等级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `roleseclevel` | 角色安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `roleseclevelmax` | 角色最高安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `jobtitleid` | 岗位id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 22 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `joblevelvalue` | 岗位对象 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 24 | `type` | 共享设置类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `fromuser` | 当前设置人员 | `integer` | - | 是 | 否 | 否 | - | - | - |

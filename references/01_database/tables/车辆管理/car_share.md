# 泛微OA 数据表: `car_share`

- **所属模块**: `车辆管理`
- **数据库表名**: `car_share`
- **字段总数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | - | 主键 |
| 2 | `carid` | 车辆id | `integer` | - | - | carinfo表主键 |
| 3 | `userid` | 人力资源 | `varchar2` | 10000 | - | 人力资源表主键 |
| 4 | `usertype` | 共享人员类型 | `integer` | - | - | - |
| 5 | `sharelevel` | 共享级别 | `integer` | - | - | - |
| 6 | `departmentid` | 部门id | `varchar2` | 1000 | - | - |
| 7 | `sharetype` | 共享类型 | `integer` | - | - | - |
| 8 | `seclevel` | 所有人安全级别 | `integer` | - | - | - |
| 9 | `seclevelmax` | 所有人最高安全级别 | `integer` | - | - | - |
| 10 | `deptlevel` | 部门安全级别 | `integer` | - | - | - |
| 11 | `deptlevelmax` | 部门最高安全级别 | `integer` | - | - | - |
| 12 | `subcompanyid` | 分部id | `integer` | - | - | - |
| 13 | `sublevel` | 分部 安全级别 | `integer` | - | - | - |
| 14 | `sublevelmax` | 分部最高安全级别 | `integer` | - | - | - |
| 15 | `has_child` | 是否含下级 | `integer` | - | - | - |
| 16 | `fieldids` | 选择的自定义字段 | `varchar2` | 1000 | - | - |
| 17 | `roleid` | 角色id | `varchar2` | 1000 | - | - |
| 18 | `rolelevel` | 角色等级 | `integer` | - | - | - |
| 19 | `roleseclevel` | 角色安全级别 | `integer` | - | - | - |
| 20 | `roleseclevelmax` | 角色最高安全级别 | `integer` | - | - | - |
| 21 | `jobtitleid` | 岗位id | `varchar2` | 1000 | - | - |
| 22 | `joblevel` | 岗位级别 | `integer` | - | - | - |
| 23 | `joblevelvalue` | 岗位对象 | `varchar2` | 1000 | - | - |
| 24 | `type` | 共享设置类型 | `integer` | - | - | - |
| 25 | `fromuser` | 当前设置人员 | `integer` | - | - | - |

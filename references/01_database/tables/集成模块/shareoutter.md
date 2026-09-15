# 泛微OA 数据表: `shareoutter`

- **所属模块**: `集成模块`
- **数据库表名**: `shareoutter`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 无 |
| 2 | `sysid` | 标识 | `varchar2` | 1000 | 否 | 无 |
| 3 | `type` | 共享类型 | `integer` | - | 否 | 1:人员  2:分部  3：部门  5:所有人 |
| 4 | `content` | 共享内容 | `integer` | - | 否 | 无 |
| 5 | `seclevel` | 安全级别 | `integer` | - | 否 | 无 |
| 6 | `sharelevel` | 共享级别 | `integer` | - | 否 | 无 |
| 7 | `seclevelmax` | 最大共享级别 | `varchar2` | 1000 | 是 | 无 |
| 8 | `jobtitlelevel` | 岗位级别 | `varchar2` | 1000 | 是 | 无 |
| 9 | `jobtitlesharevalue` | 岗位共享值 | `varchar2` | 1000 | 是 | 无 |

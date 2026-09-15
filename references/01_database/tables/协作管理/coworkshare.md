# 泛微OA 数据表: `coworkshare`

- **所属模块**: `协作管理`
- **数据库表名**: `coworkshare`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `sourceid` | 人员ID | `integer` | - | 否 | - |
| 3 | `type` | 类型 | `integer` | - | 否 | 1：人员，2：分部，3：部门，4：角色，5：所有人 |
| 4 | `content` | 协作参与人 | `varchar2` | 4000 | 是 | - |
| 5 | `seclevel` | 最小安全级别 | `integer` | - | 否 | - |
| 6 | `sharelevel` | 分享等级 | `integer` | - | 否 | - |
| 7 | `srcfrom` | 来源 | `integer` | - | 否 | 1：人员，2：创建者，3：负责人 |
| 8 | `seclevelmax` | 最大安全级别 | `integer` | - | 是 | - |
| 9 | `jobtitleid` | 岗位 | `varchar2` | 1000 | 是 | - |
| 10 | `joblevel` | 岗位级别 | `integer` | - | 是 | - |
| 11 | `scopeid` | 岗位值 | `varchar2` | 800 | 是 | - |
| 12 | `has_child` | 是否含下级 | `varchar2` | 16 | 是 | - |
| 13 | `rolelevel` | 角色级别 | `integer` | - | 是 | - |

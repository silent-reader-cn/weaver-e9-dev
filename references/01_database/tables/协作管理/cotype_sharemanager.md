# 泛微OA 数据表: `cotype_sharemanager`

- **所属模块**: `协作管理`
- **数据库表名**: `cotype_sharemanager`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | - |
| 2 | `cotypeid` | 协作区类型id | `integer` | - | 是 | 1：人力资源2：部门3：分部4：角色5：所有人6：岗位 |
| 3 | `sharetype` | 负责人类型 | `integer` | - | 是 | - |
| 4 | `sharevalue` | 负责人 | `varchar2` | 4000 | 是 | - |
| 5 | `seclevel` | 最小安全级别 | `integer` | - | 是 | - |
| 6 | `rolelevel` | 角色等级 | `integer` | - | 是 | - |
| 7 | `seclevelmax` | 最大安全级别 | `integer` | - | 是 | - |
| 8 | `jobtitleid` | 岗位名 | `varchar2` | 1000 | 是 | - |
| 9 | `joblevel` | 岗位级别 | `integer` | - | 是 | - |
| 10 | `scopeid` | 岗位值 | `varchar2` | 800 | 是 | - |
| 11 | `has_child` | 是否含下级 | `varchar2` | 16 | 是 | - |

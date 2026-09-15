# 泛微OA 数据表: `workplanshare`

- **所属模块**: `日程管理`
- **数据库表名**: `workplanshare`
- **字段总数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `companyvirtual` | 维度 | `varchar2` | 1000 | 是 | 维度 |
| 2 | `id` | 主键 | `integer` | - | 否 | id |
| 3 | `workplanid` | 日程id | `integer` | - | 是 | 日程id |
| 4 | `sharetype` | 共享对象类型 | `char` | 1 | 是 | 1：人力资源，2：分部，3：部门，4：角色，5：所有人，6：所有上级 |
| 5 | `forall` | 共享给所有人 | `char` | 1 | 是 | 共享对象类型 |
| 6 | `rolelevel` | 角色等级 | `char` | 1 | 是 | 共享给所有人 |
| 7 | `securitylevel` | 安全级别 | `integer` | - | 是 | 角色等级 |
| 8 | `sharelevel` | 共享级别 | `char` | 1 | 是 | 1：查看，2：编辑 |
| 9 | `userid` | 人力资源id | `varchar2` | 1600 | 是 | 人力资源id |
| 10 | `deptid` | 部门id | `varchar2` | 1600 | 是 | 部门id |
| 11 | `roleid` | 角色id | `varchar2` | 1600 | 是 | 角色id |
| 12 | `subcompanyid` | 分部id | `varchar2` | 1600 | 是 | 分部id |
| 13 | `isdefault` | 是否默认共享 | `char` | 1 | 是 | 1：默认共享 |
| 14 | `securitylevelmax` | 最高安全级别 | `integer` | - | 是 | 最高安全级别 |
| 15 | `type` | 共享设置类型 | `char` | 1 | 是 | 1：创建人自己设置（创建人可编辑），0：后台设置（创建人不可编辑） |
| 16 | `fromuser` | 共享人 | `integer` | - | 是 | 共享人 |
| 17 | `iscreate` | 标识 | `varchar2` | 8 | 是 | 标识 |
| 18 | `jobtitleid` | 共享岗位id | `integer` | - | 是 | 共享岗位id |
| 19 | `joblevel` | 共享岗位级别 | `integer` | - | 是 | 0:总部 1:分部 2:部门 |
| 20 | `joblevelvalue` | 共享岗位对象 | `varchar2` | 1000 | 是 | 共享岗位对象 |

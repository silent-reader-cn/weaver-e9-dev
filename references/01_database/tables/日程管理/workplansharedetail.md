# 泛微OA 数据表: `workplansharedetail`

- **所属模块**: `日程管理`
- **数据库表名**: `workplansharedetail`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `workid` | 日程id | `integer` | - | 是 | 日程id |
| 2 | `userid` | 人力资源共享对象 | `integer` | - | 是 | 当sharetype 为 1, 6 ,7 时有效 |
| 3 | `usertype` | 用户类型 | `integer` | - | 是 | 1,内部用户 |
| 4 | `sharelevel` | 共享等级 | `integer` | - | 是 | 0:客户联系查看权限 1:查看权限 2:编辑权限 |
| 5 | `sharesrc` | 共享类型 | `varchar2` | 8 | 是 | 1:默认共享(后台设置),空:非默认共享 |
| 6 | `sharetype` | 共享对象类型 | `char` | 1 | 否 | 1.人力资源类型2.分部 3.部门 4.角色 5.所有人 6.所有上级 7.直属上级 |
| 7 | `objid` | 对象值 | `integer` | - | 是 | 与sharetype组合使用当sharetype 为 2 ,3 ,4 时表示对象的值 |
| 8 | `rolelevel` | 角色等级 | `integer` | - | 是 | 角色等级 |
| 9 | `securitylevel` | 最小安全级别 | `integer` | - | 是 | 最小安全级别 |
| 10 | `securitylevelmax` | 最大安全级别 | `integer` | - | 是 | 最大安全级别 |
| 11 | `fromuser` | 共享人 | `integer` | - | 是 | 共享人 |
| 12 | `joblevel` | 共享岗位级别 | `integer` | - | 是 | 0:总部 1:分部 2:部门 |
| 13 | `joblevelvalue` | 共享岗位对象 | `integer` | - | 是 | 共享岗位对象 |

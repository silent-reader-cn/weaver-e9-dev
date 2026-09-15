# 泛微OA 数据表: `meeting_sharedetail`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_sharedetail`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `objid` | 共享对象id | `integer` | 0 | 是 | sharetype为1(部门),2（角色）,6（分部）,8（岗位） 才有效。分别为各自表的主键 |
| 2 | `userid` | 共享人员id | `integer` | 0 | 是 | sharetype为5(人力资源),10（会议信息字段）,11（分部）,12（会议议程字段）才有效。为hrmresource表的主键 |
| 3 | `id` | 主键 | `integer` | 0 | 否 | 主键 |
| 4 | `meetingid` | 会议id | `integer` | 0 | 是 | 会议id |
| 5 | `usertype` | 共享人员类型 | `integer` | 0 | 是 | 1：人员 2：客户 |
| 6 | `sharelevel` | 共享级别 | `integer` | 0 | 是 | 共享级别 |
| 7 | `sharetype` | 共享对象类型 | `integer` | 0 | 是 | 1：部门；2：角色；3：所有人；5：人力资源；6：分部；8：岗位；10：会议信息字段；11：会议服务字段；12：会议议程字段 |
| 8 | `seclevel` | 最小安全级别 | `integer` | 0 | 是 | sharetype为1(部门),2(角色),3(所有人),6（分部）才有效。最小安全级别 |
| 9 | `seclevelmax` | 最大安全级别 | `integer` | 0 | 是 | sharetype为1(部门),2(角色),3(所有人),6（分部）才有效。最大安全级别 |
| 10 | `has_child` | 是否含下级 | `integer` | 0 | 是 | 是否含下级，1：是；sharetype为1(部门),6（分部）才有效。 |
| 11 | `rolelevel` | 角色级别 | `integer` | 0 | 是 | 0：部门，1：分部，2：总部 |
| 12 | `joblevel` | 岗位级别 | `integer` | 0 | 是 | 0：总部，1：指定分部，2：指定部门 |
| 13 | `joblevelvalue` | 岗位级别对应的值 | `varchar2` | 1000 | 是 | 当joblevel为1（指定分部）或2（指定部门）才有效 |
| 14 | `type` | 共享来源 | `integer` | 0 | 是 | 0:默认共享 1:后端共享 2:前端共享 |
| 15 | `fromuser` | 共享人 | `integer` | 0 | 是 | 共享操作人 |

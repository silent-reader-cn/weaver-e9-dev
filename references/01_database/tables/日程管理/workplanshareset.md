# 泛微OA 数据表: `workplanshareset`

- **所属模块**: `日程管理`
- **数据库表名**: `workplanshareset`
- **字段总数**: `29`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 主键 |
| 2 | `planid` | 日程类型id | `integer` | - | 是 | 关联workplantype. workplantypeid |
| 3 | `sharetype` | 接收人对象类型 | `integer` | - | 是 | 1：指定人 2：分部3：部门4：角色5：所有人 |
| 4 | `seclevel` | 接收人对象安全级别 | `integer` | - | 是 | 接收人对象安全级别 |
| 5 | `rolelevel` | 接收人角色级别 | `integer` | - | 是 | 1：部门 2 分部3 总部 |
| 6 | `sharelevel` | 共享级别 | `integer` | - | 是 | 1：查看 2：编辑 |
| 7 | `userid` | 被人力资源共享对象 | `varchar2` | 4000 | 是 | 被人力资源共享对象 |
| 8 | `subcompanyid` | 接收人分部 | `varchar2` | 4000 | 是 | 接收人分部 |
| 9 | `departmentid` | 接收人部门 | `varchar2` | 4000 | 是 | 接收人部门 |
| 10 | `roleid` | 接收人角色 | `integer` | - | 是 | 接收人角色 |
| 11 | `foralluser` | 共享给所有人 | `integer` | - | 是 | 共享给所有人 |
| 12 | `ssharetype` | 共享类型 | `integer` | - | 是 | 共享类型 |
| 13 | `sseclevel` | 共享对象安全级别 | `integer` | - | 是 | 共享对象安全级别 |
| 14 | `srolelevel` | 共享角色级别 | `integer` | - | 是 | 1：部门 2 分部3 总部 |
| 15 | `suserid` | 共享用户 | `varchar2` | 4000 | 是 | 共享用户 |
| 16 | `ssubcompanyid` | 共享分部 | `varchar2` | 4000 | 是 | 共享分部 |
| 17 | `sdepartmentid` | 共享部门 | `varchar2` | 4000 | 是 | 共享部门 |
| 18 | `sroleid` | 共享角色 | `integer` | - | 是 | 共享角色 |
| 19 | `sforalluser` | 共享对象为所有人 | `integer` | - | 是 | 共享对象为所有人 |
| 20 | `settype` | 是系统设置还是个人设置 | `integer` | - | 是 | 1 前台设置(个人设置) 0 后台设置(系统设置) |
| 21 | `seclevelmax` | 接收人最高安全级别 | `integer` | - | 是 | 接收人最高安全级别 |
| 22 | `sseclevelmax` | 共享最高安全级别 | `integer` | - | 是 | 共享最高安全级别 |
| 23 | `jobtitleid` | 共享岗位id | `varchar2` | 1000 | 是 | 共享岗位id |
| 24 | `joblevel` | 共享岗位级别 | `integer` | - | 是 | 0:总部 1:分部 2:部门 |
| 25 | `joblevelvalue` | 共享岗位对象 | `varchar2` | 1000 | 是 | 共享岗位对象 |
| 26 | `sjobtitleid` | 接收人岗位id | `varchar2` | 1000 | 是 | 接收人岗位id |
| 27 | `sjoblevel` | 接收人岗位级别 | `integer` | - | 是 | 0:总部 1:分部 2:部门 |
| 28 | `sjoblevelvalue` | 接收人岗位对象 | `varchar2` | 1000 | 是 | 接收人岗位对象 |
| 29 | `companyvirtual` | 维度 | `varchar2` | 1000 | 是 | 维度 |

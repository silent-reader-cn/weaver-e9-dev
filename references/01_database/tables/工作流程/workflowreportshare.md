# 泛微OA 数据表: `workflowreportshare`

- **中文名称**: 工作流报表共享表
- **所属模块**: `工作流程`
- **数据库表名**: `workflowreportshare`
- **主键**: `id`
- **字段数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `reportid` | 报表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `sharetype` | 共享类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `seclevelbak` | 的 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | 0：部门<br>1：分部<br>2：总部 |
| 6 | `sharelevel` | 共享级别 | `integer` | - | 是 | 否 | 否 | - | - | 0：同部门<br>1：同分部<br>2：总部<br>3：同部门下级部门<br>9：多部门 |
| 7 | `useridbak` | 用户id备份 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `subcompanyidbak` | 子公司id备份 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `departmentidbak` | 部门id备份 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `roleidbak` | 规则id备份 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `foralluser` | 是否共享所有用户 | `integer` | - | 是 | 否 | 否 | - | - | 1：是 |
| 12 | `crmid` | 共享客户 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `mutidepartmentid` | 多部门值 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 14 | `userid` | 共享人力资源 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 15 | `departmentid` | 共享部门 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 16 | `subcompanyid` | 共享分部 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `roleid` | 共享角色 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 18 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `allowlook` | 查看权限 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `seclevel2` | 安全级别2 | `integer` | - | 是 | 否 | 否 | - | - | - |

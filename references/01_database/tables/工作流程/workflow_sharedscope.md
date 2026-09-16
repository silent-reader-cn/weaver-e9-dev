# 泛微OA 数据表: `workflow_sharedscope`

- **中文名称**: 流程共享字段字典表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_sharedscope`
- **主键**: `id`
- **字段数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `currentid` | 流程状态表ID | `integer` | - | 是 | 否 | 否 | - | -1 | workflow_currentoperator |
| 2 | `jobobjid` | 岗位 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `id` | id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `wfid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `permissiontype` | 流程共享对象类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `seclevel` | 所有人安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `deptlevel` | 部门安全级别min | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `sublevel` | 分部安全级别min | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `userid` | 人力资源id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `describ` | 描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 14 | `seclevelmax` | 所有人安全级别max | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `deptlevelmax` | 部门安全级别max | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `sublevelmax` | 分部安全级别max | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `roleid` | 角色id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `rolelevel` | 角色级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `roleseclevel` | 角色安全级别min | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `roleseclevelmax` | 角色安全级别max | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `iscanread` | 是否可查看 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `operator` | 共享添加人 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 23 | `currentnodeid` | 当前流程所处节点 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | - | 指定级别为1时，指定级别是指定部门；指定级别为2时，指定级别是指定分部；指定级别为3时，指定级别是总部 |
| 25 | `jobid` | 岗位id | `integer` | - | 是 | 否 | 否 | - | - | 岗位id |
| 26 | `jobobj` | 岗位对应级别指定id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

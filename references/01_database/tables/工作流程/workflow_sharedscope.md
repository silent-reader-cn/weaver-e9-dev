# 泛微OA 数据表: `workflow_sharedscope`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_sharedscope`
- **字段总数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `currentid` | 流程状态表ID | `integer` | - | 是 | workflow_currentoperator |
| 2 | `jobobjid` | 岗位 | `integer` | - | 是 | - |
| 3 | `id` | id | `integer` | - | 是 | - |
| 4 | `wfid` | 流程id | `integer` | - | 是 | - |
| 5 | `requestid` | 请求id | `integer` | - | 是 | - |
| 6 | `permissiontype` | 流程共享对象类型 | `integer` | - | 是 | - |
| 7 | `seclevel` | 所有人安全级别 | `integer` | - | 是 | - |
| 8 | `departmentid` | 部门id | `integer` | - | 是 | - |
| 9 | `deptlevel` | 部门安全级别min | `integer` | - | 是 | - |
| 10 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 11 | `sublevel` | 分部安全级别min | `integer` | - | 是 | - |
| 12 | `userid` | 人力资源id | `integer` | - | 是 | - |
| 13 | `describ` | 描述 | `varchar2` | 1000 | 是 | - |
| 14 | `seclevelmax` | 所有人安全级别max | `integer` | - | 是 | - |
| 15 | `deptlevelmax` | 部门安全级别max | `integer` | - | 是 | - |
| 16 | `sublevelmax` | 分部安全级别max | `integer` | - | 是 | - |
| 17 | `roleid` | 角色id | `integer` | - | 是 | - |
| 18 | `rolelevel` | 角色级别 | `integer` | - | 是 | - |
| 19 | `roleseclevel` | 角色安全级别min | `integer` | - | 是 | - |
| 20 | `roleseclevelmax` | 角色安全级别max | `integer` | - | 是 | - |
| 21 | `iscanread` | 是否可查看 | `integer` | - | 是 | - |
| 22 | `operator` | 共享添加人 | `varchar2` | 80 | 是 | - |
| 23 | `currentnodeid` | 当前流程所处节点 | `integer` | - | 是 | - |
| 24 | `joblevel` | 岗位级别 | `integer` | - | 是 | 指定级别为1时，指定级别是指定部门；指定级别为2时，指定级别是指定分部；指定级别为3时，指定级别是总部 |
| 25 | `jobid` | 岗位id | `integer` | - | 是 | 岗位id |
| 26 | `jobobj` | 岗位对应级别指定id | `varchar2` | 4000 | 是 | - |

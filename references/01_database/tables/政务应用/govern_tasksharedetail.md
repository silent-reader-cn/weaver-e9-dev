# 泛微OA 数据表: `govern_tasksharedetail`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_tasksharedetail`
- **字段总数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `sourceid` | 数据id | `integer` | - | 否 | 对应govern_task表id |
| 3 | `categoryid` | 类型id | `integer` | - | 否 | - |
| 4 | `datatype` | 类型 | `integer` | - | 是 | 0事项权限 1任务权限 |
| 5 | `type` | 权限类型 | `integer` | - | 是 | 1人员2分部3部门4角色5所有人6岗位7相关字段 |
| 6 | `content` | 共享对象id | `integer` | - | 是 | 1查看2共享3管理4监控 |
| 7 | `showlevel` | 安全级别下限 | `integer` | - | 是 | - |
| 8 | `showlevel2` | 安全级别上限 | `integer` | - | 是 | - |
| 9 | `opttype` | 权限级别 | `integer` | - | 是 | - |
| 10 | `isdefault` | 是否共享权限 | `integer` | - | 是 | 0前端用户共享 1设置生成 |
| 11 | `ruleid` | 权限id | `integer` | - | 否 | 对应govern_shareRule_XX表id |
| 12 | `higherlevel` | 上级关系 暂时不用 | `integer` | - | 是 | - |
| 13 | `rightid` | 权限id | `integer` | - | 否 | 对应govern_rightInfo id 仅默认共享有值 |
| 14 | `joblevel` | 岗位级别 | `integer` | - | 是 | 0、部门；1、分部；2、总部； |
| 15 | `jobleveltext` | 岗位对象 | `varchar2` | 4000 | 是 | 保存岗位级别对应的对象以逗号分隔的id串 |
| 16 | `superior` | 上级任务id | `integer` | - | 是 | 如果是督办任务的管理级别权限，除了需要有自身的权限之外还要有对子任务的数据权限  那么要默认生成n+1条权限明细 1代表这条数据自身，n代表n条子任务，当这条权限明细是子任务权限时候该字段代表上级任务的id 而sourceid字段保存对应的子任务id |
| 17 | `projid` | 对应事项id | `integer` | - | 是 | 如果是督办事项的监控权限 那该事项对应的所有子任务都生成一条对应的 监控权限  当这条权限是监控权限时 保存对应的事项id |
| 18 | `supervise1` | 是否有分解权限 | `integer` | - | 是 | 相当于当前任务责任人权限级别，仅当opttype等于3 4时候有效 |
| 19 | `supervise2` | 是否有变更、废弃、完成权限 | `integer` | - | 是 | 相当于上级任务责任人权限级别，仅当opttype等于3 4时候有效 |

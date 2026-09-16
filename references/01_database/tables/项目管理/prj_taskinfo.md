# 泛微OA 数据表: `prj_taskinfo`

- **中文名称**: 项目历史计划任务
- **所属模块**: `项目管理`
- **数据库表名**: `prj_taskinfo`
- **主键**: `id`
- **字段数**: `35`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `stageid` | 阶段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `prefinish` | 前置任务 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 3 | `id` | 标识id | `integer` | - | 否 | 否 | 否 | - | - | 标识列 |
| 4 | `prjid` | 项目id | `integer` | - | 是 | 否 | 否 | - | - | 项目id |
| 5 | `taskid` | 任务id | `integer` | - | 是 | 否 | 否 | - | - | 任务id |
| 6 | `wbscoding` | wbs编码 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | wbs编码 |
| 7 | `subject` | 任务标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 任务标题 |
| 8 | `version` | 版本 | `integer` | - | 是 | 否 | 否 | - | - | 版本 |
| 9 | `isactived` | 是否活动 | `integer` | - | 是 | 否 | 否 | - | 0 | 是否活动(执行状态的项目,isactive=2) |
| 10 | `workday` | 工期 | `number` | (15,2) | 是 | 否 | 否 | - | 0.0 | 工期 |
| 11 | `begindate` | 开始日期 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 开始日期 |
| 12 | `enddate` | 结束日期 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 结束日期 |
| 13 | `content` | 任务说明 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 任务说明 |
| 14 | `fixedcost` | 预算 | `number` | (18,2) | 是 | 否 | 否 | - | 0.00 | 预算 |
| 15 | `parentid` | 上级任务 | `integer` | - | 是 | 否 | 否 | - | 0 | 上级任务 |
| 16 | `parentids` | 上级任务串 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 上级任务串 |
| 17 | `level_n` | 层级 | `integer` | - | 是 | 否 | 否 | - | 1 | 层级 |
| 18 | `hrmid` | 任务负责人 | `varchar2` | 300 | 是 | 否 | 否 | - | - | 任务负责人 |
| 19 | `parenthrmids` | 上级任务负责人串 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 上级任务负责人串 |
| 20 | `isdelete` | 是否删除 | `integer` | - | 是 | 否 | 否 | - | 0 | 是否删除 |
| 21 | `childnum` | 子任务数量 | `integer` | - | 是 | 否 | 否 | - | 0 | 子任务数量 |
| 22 | `realmandays` | 实际工期 | `number` | (15,2) | 是 | 否 | 否 | - | - | 实际工期 |
| 23 | `actualbegindate` | 实际开始日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 实际开始日期 |
| 24 | `actualenddate` | 实际结束日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 实际结束日期 |
| 25 | `finish` | 进度 | `integer` | - | 是 | 否 | 否 | - | - | 进度 |
| 26 | `status` | 状态 | `integer` | - | 是 | 否 | 否 | - | - | 状态 |
| 27 | `islandmark` | 里程碑 | `char` | 1 | 是 | 否 | 否 | - | - | 里程碑 |
| 28 | `creater` | 创建者 | `integer` | - | 是 | 否 | 否 | - | - | 创建者 |
| 29 | `createdate` | 创建日期 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 创建日期 |
| 30 | `createtime` | 创建时间 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 创建时间 |
| 31 | `taskindex` | 任务索引 | `integer` | - | 是 | 否 | 否 | - | - | 任务索引 |
| 32 | `begintime` | 开始时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 开始时间 |
| 33 | `endtime` | 结束时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 结束时间 |
| 34 | `actualbegintime` | 实际开始时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 实际开始时间 |
| 35 | `actualendtime` | 实际结束时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 实际结束时间 |

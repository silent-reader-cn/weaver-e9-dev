# 泛微OA 数据表: `prj_taskprocess`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_taskprocess`
- **字段总数**: `41`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `stageid` | 阶段id | `integer` | - | 是 | - |
| 2 | `stageorder` | 阶段排序 | `integer` | - | 是 | - |
| 3 | `parentids` | 上级任务串 | `varchar2` | 255 | 是 | 上级任务串 |
| 4 | `level_n` | 层级 | `integer` | - | 是 | 层级 |
| 5 | `hrmid` | 任务负责人 | `varchar2` | 300 | 是 | 任务负责人 |
| 6 | `parenthrmids` | 上级任务负责人串 | `varchar2` | 1000 | 是 | 上级任务负责人串 |
| 7 | `isdelete` | 是否删除 | `integer` | - | 是 | 是否删除 |
| 8 | `childnum` | 子任务数 | `integer` | - | 是 | 子任务数 |
| 9 | `prefinish` | 前置任务 | `varchar2` | 4000 | 是 | 前置任务 |
| 10 | `taskconfirm` | 备用字段 | `char` | 1 | 是 | 备用字段 |
| 11 | `islandmark` | 里程碑 | `char` | 1 | 是 | 里程碑 |
| 12 | `dsporder` | 显示顺序 | `integer` | - | 是 | 显示顺序 |
| 13 | `status` | 状态 | `integer` | - | 否 | 状态 |
| 14 | `realmandays` | 实际工期 | `number` | (15,2) | 是 | 实际工期 |
| 15 | `taskindex` | 任务索引 | `integer` | - | 是 | 任务索引 |
| 16 | `actualbegindate` | 实际开始日期 | `char` | 10 | 是 | 实际开始日期 |
| 17 | `actualenddate` | 实际结束日期 | `char` | 10 | 是 | 实际结束日期 |
| 18 | `accessory` | 附件 | `varchar2` | 2000 | 是 | 附件 |
| 19 | `creater` | 创建者 | `integer` | - | 是 | 创建者 |
| 20 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 21 | `createtime` | 创建时间 | `char` | 8 | 是 | 创建时间 |
| 22 | `guid1` | uuid标识 | `char` | 36 | 是 | uuid标识 |
| 23 | `isimp` | 是否是导入的任务 | `char` | 1 | 是 | 是否是导入的任务 |
| 24 | `begintime` | 开始时间 | `varchar2` | 80 | 是 | 开始时间 |
| 25 | `endtime` | 结束赶时间 | `varchar2` | 80 | 是 | 结束赶时间 |
| 26 | `actualbegintime` | 实际开始时间 | `varchar2` | 80 | 是 | 实际开始时间 |
| 27 | `actualendtime` | 实际结束时间 | `varchar2` | 80 | 是 | 实际结束时间 |
| 28 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 29 | `prjid` | 项目id | `integer` | - | 是 | 项目id |
| 30 | `taskid` | 任务id | `integer` | - | 是 | 任务id |
| 31 | `isactived` | 是否活动任务 | `integer` | - | 是 | 是否活动任务 |
| 32 | `version` | 版本 | `integer` | - | 是 | 版本 |
| 33 | `workday` | 工期 | `number` | (10,1) | 是 | 工期 |
| 34 | `begindate` | 开始日期 | `varchar2` | 80 | 是 | 开始日期 |
| 35 | `enddate` | 结束日期 | `varchar2` | 80 | 是 | 结束日期 |
| 36 | `content` | 任务说明 | `varchar2` | 4000 | 是 | 任务说明 |
| 37 | `fixedcost` | 预算 | `number` | (18,2) | 是 | 预算 |
| 38 | `finish` | 进度 | `integer` | - | 是 | 进度 |
| 39 | `wbscoding` | wbs编码 | `varchar2` | 160 | 是 | wbs编码 |
| 40 | `subject` | 标题 | `varchar2` | 640 | 是 | 标题 |
| 41 | `parentid` | 上级任务 | `integer` | - | 是 | 上级任务 |

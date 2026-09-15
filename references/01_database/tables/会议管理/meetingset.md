# 泛微OA 数据表: `meetingset`

- **所属模块**: `会议管理`
- **数据库表名**: `meetingset`
- **字段总数**: `52`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `canchange` | 允许变更 | `char` | 1 | 是 | 0：不开启，1：开启 |
| 2 | `serviceconflictchk` | 服务冲突检验 | `integer` | - | 是 | 0: 关闭 1:开启 |
| 3 | `serviceconflict` | 服务冲突 | `integer` | - | 是 | 1:冲突提醒允许提交 2:禁止提交 |
| 4 | `zqhyzdkd` | 周期最大跨度 | `integer` | - | 是 | 0：默认不开启，>1：开启 |
| 5 | `canquickcreate` | 是否允许快捷新建会议 | `integer` | - | 是 | 0: 关闭 1:开启 |
| 6 | `usemeetingtopic` | 使用议程页签 | `integer` | - | 是 | 0: 关闭 1:开启 |
| 7 | `usemeetingservice` | 使用服务页签 | `integer` | - | 是 | 0: 关闭 1:开启 |
| 8 | `defaultapprover` | 默认审批流 | `integer` | - | 是 | - |
| 9 | `defaultrepeatapprover` | 默认周期会议审批流 | `integer` | - | 是 | - |
| 10 | `usedcolor` | 占用颜色 | `varchar2` | 80 | 是 | - |
| 11 | `agreementcolor` | 审批颜色 | `varchar2` | 80 | 是 | - |
| 12 | `conflictedcolor` | 冲突颜色 | `varchar2` | 80 | 是 | - |
| 13 | `usedcolorfont` | 占用字体颜色 | `varchar2` | 160 | 是 | - |
| 14 | `agreementcolorfont` | 审批字体颜色 | `varchar2` | 160 | 是 | - |
| 15 | `conflictedcolorfont` | 冲突字体颜色 | `varchar2` | 160 | 是 | - |
| 16 | `id` | 会议服务id | `integer` | - | 否 | - |
| 17 | `timerangestart` | 会议室日使用情况 | `integer` | - | 是 | 显示时间段，最小值 |
| 18 | `timerangeend` | 会议室日使用情况 | `integer` | - | 是 | 显示时间段，最大值 |
| 19 | `roomconflictchk` | 会议室冲突提醒 | `integer` | - | 是 | - |
| 20 | `roomconflict` | 会议室冲突时处理方式 | `integer` | - | 是 | 1、仅提醒不做处理,2、禁止提交 |
| 21 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 22 | `dscsdoc` | 相关交流中是否显示相关文档 | `integer` | - | 是 | 0：不显示，1：显示 |
| 23 | `dscswf` | 相关交流中是否显示相关流程 | `integer` | - | 是 | 0：不显示，1：显示 |
| 24 | `dscscrm` | 相关交流中是否显示相关客户 | `integer` | - | 是 | 0：不显示，1：显示 |
| 25 | `dscsprj` | 相关交流中是否显示相关项目 | `integer` | - | 是 | 0：不显示，1：显示 |
| 26 | `dscstsk` | 相关交流中是否显示相关任务 | `integer` | - | 是 | 0：不显示，1：显示 |
| 27 | `dscsattch` | 相关交流中是否显示相关附件 | `integer` | - | 是 | 0：不显示，1：显示 |
| 28 | `dscsattchctgry` | 相关交流中相关附件的上传目录 | `varchar2` | 1000 | 是 | &nbsp; |
| 29 | `tpcdoc` | 会议决议中是否显示相关文档 | `integer` | - | 是 | 0：不显示，1：显示 |
| 30 | `tpcwf` | 会议决议中是否显示相关流程 | `integer` | - | 是 | 0：不显示，1：显示 |
| 31 | `tpccrm` | 会议决议中是否显示相关客户 | `integer` | - | 是 | 0：不显示，1：显示 |
| 32 | `tpcprj` | 会议决议中是否显示相关项目 | `integer` | - | 是 | 0：不显示，1：显示 |
| 33 | `tpctsk` | 会议决议中是否显示相关任务 | `integer` | - | 是 | 0：不显示，1：显示 |
| 34 | `tpcattch` | 会议决议中是否显示相关附件 | `integer` | - | 是 | 0：不显示，1：显示 |
| 35 | `tpcattchctgry` | 会议决议中相关附件的上传目录 | `varchar2` | 1000 | 是 | - |
| 36 | `mtngattchctgry` | 会议默认附件上传目录 | `varchar2` | 1000 | 是 | - |
| 37 | `callerprm` | 召集人权限 | `integer` | - | 是 | 1：默认权限，3：完全控制权限 |
| 38 | `contacterprm` | 联系人权限 | `integer` | - | 是 | 1：默认权限，3：完全控制权限 |
| 39 | `createrprm` | 创建人权限 | `integer` | - | 是 | 1：默认权限，3：完全控制权限 |
| 40 | `memberconflictchk` | 参会人员冲突提醒 | `integer` | - | 是 | - |
| 41 | `memberconflict` | 参会人员冲突时处理方式 | `integer` | - | 是 | 1：仅提醒，2：禁止提交 |
| 42 | `tpcprjflg` | 会议议程相关项目 | `integer` | - | 是 | 废弃 |
| 43 | `tpccrmflg` | 会议议程相关客户 | `integer` | - | 是 | 废弃 |
| 44 | `days` | 周期会议生成的提前天数 | `integer` | - | 是 | 1: 小时  2:半小时 3:20分钟 4:15分钟  6:10分钟  使用 60/值=没格时间 |
| 45 | `recarrive` | 会议回执是否显示到达时间 | `integer` | - | 是 | 0：不显示，1：显示 |
| 46 | `recbook` | 会议回执是否显示订房信息 | `integer` | - | 是 | 0：不显示，1：显示 |
| 47 | `recreturn` | 会议回执是否显示回程信息 | `integer` | - | 是 | 0：不显示，1：显示 |
| 48 | `recremark` | 会议回执是否显示备注信息 | `integer` | - | 是 | 0：不显示，1：显示 |
| 49 | `dspunit` | 占用单位 | `integer` | - | 是 | - |
| 50 | `createmeetingremindchk` | 创建会议提醒开关 | `integer` | - | 是 | 0：不开启，1：开启 |
| 51 | `cancelmeetingremindchk` | 会议取消提醒开关 | `integer` | - | 是 | 0：不开启，1：开启 |
| 52 | `remeetingremindchk` | 会议回执提醒开关 | `integer` | - | 是 | 0：不开启，1：开启 |

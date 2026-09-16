# 泛微OA 数据表: `bill_meeting`

- **中文名称**: 会议审批单
- **所属模块**: `其他`
- **数据库表名**: `bill_meeting`
- **主键**: `id`
- **字段数**: `41`

> 说明：会议流程系统表单

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `remindbeforestart` | 是否开始前提醒 | `integer` | - | 是 | 否 | 否 | - | 0 | 1:开启 0:未开启 |
| 2 | `remindbeforeend` | 是否结束前提醒 | `integer` | - | 是 | 否 | 否 | - | 0 | 1:开启 0:未开启 |
| 3 | `remindtimesbeforestart` | 开始前时间 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 4 | `remindtimesbeforeend` | 结束前时间 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 5 | `repeattype` | 重复模式 | `integer` | - | 是 | 否 | 否 | - | - | 1:日模式 2:周模式 3:月模式 |
| 6 | `repeatdays` | 间隔日 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `repeatweeks` | 间隔周数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `rptweekdays` | 星期几 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 1-7 表示 星期一至星期日 |
| 9 | `repeatmonths` | 间隔月 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `repeatmonthdays` | 每月几号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `crmsnumber` | 客户数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `services` | 服务 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 13 | `remindtypenew` | 新提醒方式 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 14 | `remindimmediately` | 立即提醒 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 15 | `remindhoursbeforestart` | 开始前小时 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `remindhoursbeforeend` | 结束前小时 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `accessorys` | 附件 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 18 | `repeatstrategy` | 重复策略 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `resources` | 参会人 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 20 | `address` | 会议地点 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 21 | `id` | id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `approveid` | 相关会议id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `meetingtype` | 会议类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `meetingname` | 会议名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 25 | `caller` | 召集人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `contacter` | 联系人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 27 | `begindate` | 开始日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 28 | `begintime` | 开始时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |
| 29 | `enddate` | 结束日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 30 | `endtime` | 结束时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |
| 31 | `requestid` | 相关流程 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 32 | `approveby` | 审批人 | `integer` | - | 否 | 否 | 否 | - | 0 | - |
| 33 | `approvedate` | 审批日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 34 | `viewmeetroomusecase` | 会议室占用情况 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 35 | `resourcenum` | 参会人员数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 36 | `crms` | 参会客户 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 37 | `others` | 其他人员 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 38 | `projectid` | 相关项目 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 39 | `customizeaddress` | 自定义地点 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 40 | `description` | 描述 | `varchar2` | 3000 | 是 | 否 | 否 | - | - | - |
| 41 | `remindtype` | 老提醒方式(废弃) | `integer` | - | 是 | 否 | 否 | - | 0 | - |

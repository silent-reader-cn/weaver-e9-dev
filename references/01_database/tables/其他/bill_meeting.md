# 泛微OA 数据表: `bill_meeting`

- **所属模块**: `其他`
- **数据库表名**: `bill_meeting`
- **字段总数**: `41`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `remindbeforestart` | 是否开始前提醒 | `integer` | - | 是 | 1:开启 0:未开启 |
| 2 | `remindbeforeend` | 是否结束前提醒 | `integer` | - | 是 | 1:开启 0:未开启 |
| 3 | `remindtimesbeforestart` | 开始前时间 | `integer` | - | 是 | - |
| 4 | `remindtimesbeforeend` | 结束前时间 | `integer` | - | 是 | - |
| 5 | `repeattype` | 重复模式 | `integer` | - | 是 | 1:日模式  2:周模式 3:月模式 |
| 6 | `repeatdays` | 间隔日 | `integer` | - | 是 | - |
| 7 | `repeatweeks` | 间隔周数 | `integer` | - | 是 | - |
| 8 | `rptweekdays` | 星期几 | `varchar2` | 160 | 是 | 1-7 表示 星期一至星期日 |
| 9 | `repeatmonths` | 间隔月 | `integer` | - | 是 | - |
| 10 | `repeatmonthdays` | 每月几号 | `integer` | - | 是 | - |
| 11 | `crmsnumber` | 客户数 | `integer` | - | 是 | - |
| 12 | `services` | 服务 | `varchar2` | 2000 | 是 | - |
| 13 | `remindtypenew` | 新提醒方式 | `varchar2` | 800 | 是 | - |
| 14 | `remindimmediately` | 立即提醒 | `char` | 1 | 是 | - |
| 15 | `remindhoursbeforestart` | 开始前小时 | `integer` | - | 是 | - |
| 16 | `remindhoursbeforeend` | 结束前小时 | `integer` | - | 是 | - |
| 17 | `accessorys` | 附件 | `varchar2` | 2000 | 是 | - |
| 18 | `repeatstrategy` | 重复策略 | `integer` | - | 是 | - |
| 19 | `resources` | 参会人 | `clob` | 4000 | 是 | - |
| 20 | `address` | 会议地点 | `varchar2` | 4000 | 是 | - |
| 21 | `id` | id | `integer` | - | 是 | - |
| 22 | `approveid` | 相关会议id | `integer` | - | 是 | - |
| 23 | `meetingtype` | 会议类型 | `integer` | - | 是 | - |
| 24 | `meetingname` | 会议名称 | `varchar2` | 1000 | 是 | - |
| 25 | `caller` | 召集人 | `integer` | - | 是 | - |
| 26 | `contacter` | 联系人 | `integer` | - | 是 | - |
| 27 | `begindate` | 开始日期 | `varchar2` | 80 | 是 | - |
| 28 | `begintime` | 开始时间 | `varchar2` | 64 | 是 | - |
| 29 | `enddate` | 结束日期 | `varchar2` | 80 | 是 | - |
| 30 | `endtime` | 结束时间 | `varchar2` | 64 | 是 | - |
| 31 | `requestid` | 相关流程 | `integer` | - | 是 | - |
| 32 | `approveby` | 审批人 | `integer` | - | 否 | - |
| 33 | `approvedate` | 审批日期 | `varchar2` | 80 | 是 | - |
| 34 | `viewmeetroomusecase` | 会议室占用情况 | `varchar2` | 800 | 是 | - |
| 35 | `resourcenum` | 参会人员数 | `integer` | - | 是 | - |
| 36 | `crms` | 参会客户 | `varchar2` | 1000 | 是 | - |
| 37 | `others` | 其他人员 | `varchar2` | 1000 | 是 | - |
| 38 | `projectid` | 相关项目 | `integer` | - | 是 | - |
| 39 | `customizeaddress` | 自定义地点 | `varchar2` | 1000 | 是 | - |
| 40 | `description` | 描述 | `varchar2` | 3000 | 是 | - |
| 41 | `remindtype` | 老提醒方式(废弃) | `integer` | - | 是 | - |

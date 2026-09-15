# 泛微OA 数据表: `meeting`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting`
- **字段总数**: `77`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `qrticket` | 会议二维码 | `varchar2` | 800 | 是 | - |
| 2 | `address` | 会议地点 | `varchar2` | 4000 | 是 | - |
| 3 | `ck_address` | 冲突检测用会议地点 | `varchar2` | 4000 | 是 | 用于自定义会议流程冲突检测 |
| 4 | `ck_services` | 冲突检测用会议服务 | `varchar2` | 1000 | 是 | - |
| 5 | `id` | ID | `integer` | - | 否 | - |
| 6 | `meetingtype` | 会议类型 | `integer` | - | 是 | - |
| 7 | `name` | 会议名称 | `varchar2` | 1000 | 是 | - |
| 8 | `caller` | 召集人 | `integer` | - | 是 | - |
| 9 | `contacter` | 联系人 | `integer` | - | 是 | - |
| 10 | `begindate` | 开始日期 | `varchar2` | 80 | 是 | - |
| 11 | `begintime` | 开始时间 | `varchar2` | 64 | 是 | - |
| 12 | `enddate` | 结束日期 | `varchar2` | 80 | 是 | - |
| 13 | `endtime` | 结束时间 | `varchar2` | 64 | 是 | - |
| 14 | `desc_n` | 备注 | `varchar2` | 4000 | 是 | - |
| 15 | `creater` | 创建人 | `integer` | - | 是 | - |
| 16 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 17 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
| 18 | `approver` | 审批人 | `integer` | - | 是 | - |
| 19 | `approvedate` | 审批日期 | `varchar2` | 80 | 是 | - |
| 20 | `approvetime` | 审批时间 | `varchar2` | 64 | 是 | - |
| 21 | `isapproved` | 会议状态 | `integer` | - | 是 | - |
| 22 | `isdecision` | 是否会议决议 | `integer` | - | 是 | - |
| 23 | `decision` | 决议概述 | `varchar2` | 4000 | 是 | - |
| 24 | `decisiondocid` | 决议相关文档 | `integer` | - | 是 | - |
| 25 | `decisiondate` | 会议日期 | `varchar2` | 80 | 是 | - |
| 26 | `decisiontime` | 会议时间 | `varchar2` | 64 | 是 | - |
| 27 | `decisionhrmid` | 决议人 | `integer` | - | 是 | - |
| 28 | `projectid` | 相关项目 | `integer` | - | 是 | - |
| 29 | `totalmember` | 应到人数 | `integer` | - | 是 | - |
| 30 | `othermembers` | 其他人员 | `varchar2` | 4000 | 是 | - |
| 31 | `othersremark` | 其他说明 | `varchar2` | 4000 | 是 | - |
| 32 | `addressdesc` | 会议地址 | `varchar2` | 1000 | 是 | - |
| 33 | `meetingstatus` | 会议状态 | `integer` | - | 否 | 0：草稿,1：待审批,2:正常,3:退回,4:取消,5:结束 |
| 34 | `requestid` | 会议流程id | `integer` | - | 否 | 与bill_meeting会议流程表中的id对应 |
| 35 | `cancel` | 是否撤消 | `char` | 1 | 是 | 1:已撤消 |
| 36 | `canceldate` | 撤消日期 | `char` | 10 | 是 | - |
| 37 | `canceltime` | 撤消时间 | `char` | 8 | 是 | - |
| 38 | `customizeaddress` | 自定义会议地点 | `varchar2` | 1000 | 是 | - |
| 39 | `description` | 会议内容 | `varchar2` | 3000 | 是 | - |
| 40 | `remindtype` | 提醒类型 | `integer` | - | 是 | - |
| 41 | `remindbeforestart` | 是否开始提醒 | `integer` | - | 是 | - |
| 42 | `remindbeforeend` | 是否结束提醒 | `integer` | - | 是 | - |
| 43 | `remindtimesbeforestart` | 开始提醒时间 | `integer` | - | 是 | - |
| 44 | `remindtimesbeforeend` | 结束提醒时间 | `integer` | - | 是 | - |
| 45 | `accessorys` | 附件id | `varchar2` | 2000 | 是 | - |
| 46 | `roomtype` | 会议室类型 | `integer` | - | 是 | - |
| 47 | `repeattype` | 重复方式 | `integer` | - | 是 | - |
| 48 | `repeatdays` | 周期会议间隔天数 | `integer` | - | 是 | - |
| 49 | `repeatweeks` | 周期会议间隔周数 | `integer` | - | 是 | - |
| 50 | `rptweekdays` | 每周几会议 | `varchar2` | 160 | 是 | - |
| 51 | `repeatmonths` | 周期会议间隔月数 | `integer` | - | 是 | - |
| 52 | `repeatmonthdays` | 每月第几天会议 | `integer` | - | 是 | - |
| 53 | `repeatbegindate` | 重复开始日期 | `varchar2` | 80 | 是 | - |
| 54 | `repeatenddate` | 重复结束日期 | `varchar2` | 80 | 是 | - |
| 55 | `decisionwfids` | 决议相关流程 | `varchar2` | 1000 | 是 | - |
| 56 | `decisioncrmids` | 决议相关客户 | `varchar2` | 1000 | 是 | - |
| 57 | `decisionprjids` | 决议相关项目 | `varchar2` | 1000 | 是 | - |
| 58 | `decisiontskids` | 决议相关任务 | `varchar2` | 1000 | 是 | - |
| 59 | `decisionatchids` | 决议附件 | `varchar2` | 1000 | 是 | - |
| 60 | `repeatstrategy` | 重复会议策略 | `integer` | - | 是 | - |
| 61 | `repeatmeetingid` | 重复会议id | `integer` | - | 是 | - |
| 62 | `remindtypenew` | 提醒方式 | `varchar2` | 800 | 是 | - |
| 63 | `remindimmediately` | 立即提醒 | `char` | 1 | 是 | - |
| 64 | `remindhoursbeforestart` | 开始前小时 | `integer` | - | 是 | - |
| 65 | `remindhoursbeforeend` | 结束前小时 | `integer` | - | 是 | - |
| 66 | `hrmmembersold` | 原参会人(无效) | `varchar2` | 4000 | 是 | - |
| 67 | `crmmembers` | 参会客户 | `varchar2` | 4000 | 是 | - |
| 68 | `crmtotalmember` | 应到客户数 | `integer` | - | 是 | - |
| 69 | `ck_begindate` | 开始日期 | `varchar2` | 80 | 是 | 用于自定义会议流程冲突检测 |
| 70 | `ck_begintime` | 开始时间 | `varchar2` | 64 | 是 | 用于自定义会议流程冲突检测 |
| 71 | `ck_enddate` | 结束日期 | `varchar2` | 80 | 是 | 用于自定义会议流程冲突检测 |
| 72 | `ck_endtime` | 结束时间 | `varchar2` | 64 | 是 | 用于自定义会议流程冲突检测 |
| 73 | `ck_hrmmembersold` | 冲突检测用人员(无效) | `varchar2` | 4000 | 是 | - |
| 74 | `ck_crmmembers` | 参会客户 | `varchar2` | 4000 | 是 | 用于自定义会议流程冲突检测 |
| 75 | `ck_isck` | 是否需要检测冲突 | `varchar2` | 40 | 是 | 000 表示  会议室 参会人员 会议服务都需要检查   每一位表示一种类型的检测 |
| 76 | `hrmmembers` | 参会人员 | `clob` | 4000 | 是 | - |
| 77 | `ck_hrmmembers` | 参会人员 | `clob` | 4000 | 是 | 用于自定义会议流程冲突检测 |
